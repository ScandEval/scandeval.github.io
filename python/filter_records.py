"""Removes duplicate entries from a JSONL file."""

import click
import json
from pathlib import Path
import logging
from huggingface_hub import HfApi
from huggingface_hub.hf_api import RepositoryNotFoundError
from tqdm.auto import tqdm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)



def record_is_valid(record: dict) -> bool:
    """Determine if a record is valid.

    Args:
        record:
            The record to validate.

    Returns:
        True if the record is valid, False otherwise.
    """
    BANNED_VERSIONS: list[str] = ["9.3.0", "10.0.0"]
    if record.get("version") in BANNED_VERSIONS:
        return False

    return True


MERGE_CACHE: dict[str, bool] = dict()


@click.command()
@click.argument('filename')
def main(filename: str) -> None:
    """Removes duplicate entries from a JSONL file.

    Args:
        filename:
            The path to the JSONL file.
    """
    records = list()
    with Path(filename).open(mode="r") as f:
        for line_idx, line in enumerate(f):
            if not line.strip():
                continue
            for record in line.replace("}{", "}\n{").split("\n"):
                if not record.strip():
                    continue
                try:
                    records.append(json.loads(record))
                except json.JSONDecodeError:
                    logger.error(f"Invalid JSON on line {line_idx:,}: {record}.")
                    return
    num_raw_records = len(records)

    # Remove models trained with banned versions of ScandEval
    records = [
        record for record in records if record_is_valid(record=record)
    ]
    num_banned_records = num_raw_records - len(records)
    if num_banned_records > 0:
        logger.info(f"Removed {num_banned_records:,} banned records from {filename}.")

    # Filter records
    all_hash_values = [get_hash(dct) for dct in records]
    unique_hash_values = sorted(set(all_hash_values))
    new_records = list()
    for unique_hash_value in tqdm(unique_hash_values, desc="Processing records"):
        matches = [
            record
            for record, hash_value in zip(records, all_hash_values)
            if hash_value == unique_hash_value
        ]
        versions = [
            list(map(int, match.get("scandeval_version", "0.0.0").split(".")))
            for match in matches
        ]
        newest_match = matches[versions.index(max(versions))]
        newest_match = add_missing_entries(record=newest_match)
        new_records.append(newest_match)
    records = new_records
    num_duplicates = num_raw_records - num_banned_records - len(records)
    if num_duplicates:
        logger.info(f"Removed {num_duplicates:,} duplicates from {filename}.")

    # Remove merged models which are not trained on a validation split
    records = [
        record for record in records if not record["merge"] or record["validation_split"]
    ]
    num_merged_records = (
        num_raw_records - num_banned_records - num_duplicates - len(records)
    )
    if num_merged_records:
        logger.info(
            f"Removed {num_merged_records:,} merged records which weren't trained "
            "on a validation split."
        )

    # Write new records to file
    with Path(filename).open(mode="w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

    records_without_merge = list()
    for record in records:
        record.pop("merge")
        records_without_merge.append(record)
    with Path(filename).with_suffix(".no_merge.jsonl").open(mode="w") as f:
        for record in records_without_merge:
            f.write(json.dumps(record) + "\n")


def add_missing_entries(record: dict) -> dict:
    """Adds missing entries to a record.

    Args:
        record:
            A record from the JSONL file.

    Returns:
        The record with missing entries added.
    """
    if "validation_split" not in record:
        record["validation_split"] = False
    if "few_shot" not in record:
        record["few_shot"] = True
    if "generative" not in record:
        record["generative"] = False
    if "merge" not in record:
        record["merge"] = is_merge(model_id=record["model"])
    return record


def get_hash(record: dict) -> str:
    """Returns a hash value for a record.

    Args:
        record:
            A record from the JSONL file.

    Returns:
        A hash value for the record.
    """
    model = record["model"]
    dataset = record["dataset"]
    validation_split = int(record.get("validation_split", False))
    few_shot = int(record.get("few_shot", True))
    generative = int(record.get("generative", False))
    return f"{model}{dataset}{validation_split}{few_shot * generative}"


def is_merge(model_id: str) -> bool:
    """Returns True if the model is a merge model, False otherwise.

    Args:
        model_id:
            The model ID.

    Returns:
        True if the model is a merge model, False otherwise.
    """
    # Remove revisions from model ID
    model_id = model_id.split("@")[0]

    # Return cached value if available
    global MERGE_CACHE
    if model_id in MERGE_CACHE:
        return MERGE_CACHE[model_id]

    # Fresh models do not appear on the model hub, so we assume they are not merge
    # models
    if model_id.startswith("fresh"):
        MERGE_CACHE[model_id] = False
        return False

    # Fetch model info from the model hub, and assume that it is not a merged model if
    # the model is not found
    api = HfApi()
    try:
        model_info = api.model_info(repo_id=model_id)
    except RepositoryNotFoundError:
        MERGE_CACHE[model_id] = False
        return False

    # A model is a merge model if it has merge-related tags
    merge_tags = ["merge", "mergekit"]
    has_merge_tag = any(tag in model_info.tags for tag in merge_tags)
    MERGE_CACHE[model_id] = has_merge_tag
    return has_merge_tag


if __name__ == "__main__":
    main()
