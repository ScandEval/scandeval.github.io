"""Removes duplicate entries from a JSONL file."""

import click
import json
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


BANNED_VERSIONS: list[str] = [
    "9.3.0",
]


@click.command()
@click.argument('filename')
def main(filename: str) -> None:
    """Removes duplicate entries from a JSONL file.

    Args:
        filename:
            The path to the JSONL file.
    """
    with Path(filename).open(mode="r") as f:
        records = [json.loads(line) for line in f if line.strip()]
    num_raw_records = len(records)

    records = [
        record for record in records if record.get("version") not in BANNED_VERSIONS
    ]
    num_banned_records = num_raw_records - len(records)
    if num_banned_records > 0:
        logger.info(f"Removed {num_banned_records:,} banned records from {filename}.")

    all_hash_values = [get_hash(dct) for dct in records]
    unique_hash_values = sorted(set(all_hash_values))

    new_records = list()
    for unique_hash_value in unique_hash_values:
        matches = [
            record
            for record, hash_value in zip(records, all_hash_values)
            if hash_value == unique_hash_value
            and record.get("version") not in BANNED_VERSIONS
        ]
        versions = [
            match.get("scandeval_version", "0.0.0").split(".") for match in matches
        ]
        newest_match = matches[versions.index(max(versions))]
        newest_match = add_missing_entries(record=newest_match)
        new_records.append(newest_match)

    with Path(filename).open(mode="w") as f:
        for record in new_records:
            f.write(json.dumps(record) + "\n")

    num_new_records = len(new_records)
    num_duplicates = num_raw_records - num_new_records - num_banned_records
    logger.info(f"Removed {num_duplicates:,} duplicates from {filename}.")


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


if __name__ == "__main__":
    main()
