leaderboards: download \
	mainland-scandi-nlu \
	mainland-scandi-nlg \
	insular-scandi-nlu \
	insular-scandi-nlg \
	german-nlu \
	german-nlg \
	dutch-nlu \
	dutch-nlg \
	english-nlu \
	english-nlg

download:
	@scp rabbit:/home/ubuntu/scandeval_benchmark_results.jsonl rabbit_results.jsonl || (touch rabbit_results.jsonl && echo "Could not download results from rabbit.")
	@scp bk:/home/saattrupdan/scandeval/scandeval_benchmark_results.jsonl blackknight_results.jsonl || (touch blackknight_results.jsonl && echo "Could not download results from blackknight.")
	@cat blackknight_results.jsonl > scandeval_benchmark_results.jsonl
	@cat rabbit_results.jsonl >> scandeval_benchmark_results.jsonl
	@rm rabbit_results.jsonl blackknight_results.jsonl

mainland-scandi-nlu:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Mainland Scandinavian NLU" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d DANSK da ner micro_f1_no_misc micro_f1 \
			-d "Angry Tweets" da sent mcc macro_f1 \
			-d ScaLA-da da la mcc macro_f1 \
			-d ScandiQA-da da qa em f1 \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no qa em f1 \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv qa em f1

mainland-scandi-nlg:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Mainland Scandinavian NLG" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-t summ "Summarization" \
			-t know "Knowledge" \
			-t reason "Common Sense Reasoning" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m bertscore "BERTScore" \
			-m rouge_l "ROUGE-L" \
			-m accuracy "Accuracy" \
			-d DANSK da ner micro_f1_no_misc micro_f1 \
			-d "Angry Tweets" da sent mcc macro_f1 \
			-d ScaLA-da da la mcc macro_f1 \
			-d ScandiQA-da da qa em f1 \
			-d Nordjylland-News da summ bertscore rouge_l \
			-d MMLU-da da know mcc accuracy \
			-d ARC-da da know mcc accuracy \
			-d HellaSwag-da da reason mcc accuracy \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d "No Sammendrag" no summ bertscore rouge_l \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no qa em f1 \
			-d MMLU-no no know mcc accuracy \
			-d ARC-no no know mcc accuracy \
			-d HellaSwag-no no reason mcc accuracy \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv qa em f1 \
			-d SweDN sv summ bertscore rouge_l \
			-d MMLU-sv sv know mcc accuracy \
			-d ARC-sv sv know mcc accuracy \
			-d HellaSwag-sv sv reason mcc accuracy

insular-scandi-nlu:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Insular Scandinavian NLU" \
			-l is Icelandic \
			-l fo Faroese \
			-t ner "Named Entity Recognition" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d MIM-GOLD-NER is ner micro_f1_no_misc micro_f1 \
			-d ScaLA-is is la mcc macro_f1 \
			-d NQiI is qa em f1 \
			-d FoNE fo ner micro_f1_no_misc micro_f1 \
			-d ScaLA-fo fo la mcc macro_f1

insular-scandi-nlg:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Insular Scandinavian NLG" \
			-l is Icelandic \
			-l fo Faroese \
			-t ner "Named Entity Recognition" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-t summ "Summarization" \
			-t know "Knowledge" \
			-t reason "Common Sense Reasoning" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m bertscore "BERTScore" \
			-m rouge_l "ROUGE-L" \
			-m accuracy "Accuracy" \
			-d MIM-GOLD-NER is ner micro_f1_no_misc micro_f1 \
			-d ScaLA-is is la mcc macro_f1 \
			-d NQiI is qa em f1 \
			-d FoNE fo ner micro_f1_no_misc micro_f1 \
			-d ScaLA-fo fo la mcc macro_f1 \
			-d RRN is summ bertscore rouge_l \
			-d MMLU-is is know mcc accuracy \
			-d ARC-is is know mcc accuracy \
			-d HellaSwag-is is reason mcc accuracy

german-nlu:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "German NLU" \
			-l de German \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d GermEval de ner micro_f1_no_misc micro_f1 \
			-d SB10k de sent mcc macro_f1 \
			-d ScaLA-de de la mcc macro_f1 \
			-d GermanQuAD de qa em f1

german-nlg:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "German NLG" \
			-l de German \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-t summ "Summarization" \
			-t know "Knowledge" \
			-t reason "Common Sense Reasoning" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m bertscore "BERTScore" \
			-m rouge_l "ROUGE-L" \
			-m accuracy "Accuracy" \
			-d GermEval de ner micro_f1_no_misc micro_f1 \
			-d SB10k de sent mcc macro_f1 \
			-d ScaLA-de de la mcc macro_f1 \
			-d GermanQuAD de qa em f1 \
			-d MLSum de summ bertscore rouge_l \
			-d MMLU-de de know mcc accuracy \
			-d ARC-de de know mcc accuracy \
			-d HellaSwag-de de reason mcc accuracy

dutch-nlu:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Dutch NLU" \
			-l nl Dutch \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d CoNLL-nl nl ner micro_f1_no_misc micro_f1 \
			-d "Dutch Social" nl sent mcc macro_f1 \
			-d ScaLA-nl nl la mcc macro_f1 \
			-d SQuAD-nl nl qa em f1

dutch-nlg:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "Dutch NLG" \
			-l nl Dutch \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-t summ "Summarization" \
			-t know "Knowledge" \
			-t reason "Common Sense Reasoning" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m bertscore "BERTScore" \
			-m rouge_l "ROUGE-L" \
			-m accuracy "Accuracy" \
			-d CoNLL-nl nl ner micro_f1_no_misc micro_f1 \
			-d "Dutch Social" nl sent mcc macro_f1 \
			-d ScaLA-nl nl la mcc macro_f1 \
			-d SQuAD-nl nl qa em f1 \
			-d Wiki-Lingua-NL nl summ bertscore rouge_l \
			-d MMLU-nl nl know mcc accuracy \
			-d ARC-nl nl know mcc accuracy \
			-d HellaSwag-nl nl reason mcc accuracy

english-nlu:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "English NLU" \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d CoNLL-en en ner micro_f1_no_misc micro_f1 \
			-d SST5 en sent mcc macro_f1 \
			-d ScaLA-en en la mcc macro_f1 \
			-d SQuAD en qa em f1

english-nlg:
	@source .venv/bin/activate && \
		python python/generate_leaderboard.py "English NLG" \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t qa "Question Answering" \
			-t summ "Summarization" \
			-t know "Knowledge" \
			-t reason "Common Sense Reasoning" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m bertscore "BERTScore" \
			-m rouge_l "ROUGE-L" \
			-m accuracy "Accuracy" \
			-d CoNLL-en en ner micro_f1_no_misc micro_f1 \
			-d SST5 en sent mcc macro_f1 \
			-d ScaLA-en en la mcc macro_f1 \
			-d SQuAD en qa em f1 \
			-d CNN-DailyMail en summ bertscore rouge_l \
			-d MMLU en know mcc accuracy \
			-d ARC en know mcc accuracy \
			-d HellaSwag en reason mcc accuracy

radial_plot:
	@source .venv/bin/activate && \
		python python/radial_plot.py \
			-l da \
			-m mhenrichsen/danskgpt-tiny \
			-m mhenrichsen/danskgpt-tiny-chat \
			-m danish-foundation-models/munin-7b-alpha \
			-m mistralai/Mistral-7B-v0.1 \
			-m gpt-3.5-turbo-0613
