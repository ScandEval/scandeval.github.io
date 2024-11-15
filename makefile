leaderboards: download \
	filter_records \
	danish-nlu \
	danish-nlg \
	swedish-nlu \
	swedish-nlg \
	norwegian-nlu \
	norwegian-nlg \
	icelandic-nlu \
	icelandic-nlg \
	faroese-nlu \
	german-nlu \
	german-nlg \
	dutch-nlu \
	dutch-nlg \
	english-nlu \
	english-nlg \
	germanic-nlu \
	germanic-nlg \
	mainland-scandi-nlu \
	mainland-scandi-nlg \
	publish-test-leaderboards

publish:
	@ls | grep -e "-test.md" | sed "s/-test.*//" | xargs -I{} cp {}-test.md {}.md
	@ls | grep -e "-test.csv" | sed "s/-test.*//" | xargs -I{} cp {}-test.csv {}.csv
	@ls | grep -e "-test.md" | sed "s/-test//" | xargs sed -i "" "s/-test//g" || true
	@ls | grep -e "-test.md" | sed "s/-test//" | xargs sed -i "s/-test//g" || true
	@ls | grep -e ".md" | xargs git add
	@ls | grep -e ".csv" | xargs git add
	@git pull --commit
	@git commit -m "feat: Update leaderboards" || true
	@git push
	@echo "Published leaderboards!"

publish-test-leaderboards:
	@ls | grep -e "-test.md" | xargs git add
	@ls | grep -e "-test.csv" | xargs git add
	@git add scandeval_benchmark_results.jsonl
	@git pull --commit
	@git reset scandeval_benchmark_results.jsonl
	@git commit -m "feat: Update test leaderboards" || true
	@git add scandeval_benchmark_results.jsonl
	@git commit -m "feat: Update benchmark results" || true
	@git push
	@echo "Published test leaderboards!"

download:
	# @scp -o ConnectTimeout=5 bk:/home/saattrupdan/scandeval/scandeval_benchmark_results.jsonl blackknight_results.jsonl || true
	# @scp -o ConnectTimeout=5 rabbit:/home/ubuntu/scandeval_benchmark_results.jsonl rabbit_results.jsonl || true
	# @scp -o ConnectTimeout=5 maninpink:/home/ubuntu/scandeval_benchmark_results.jsonl maininpink_results.jsonl || true
	# @scp -o ConnectTimeout=5 hamster:/home/ubuntu/scandeval_benchmark_results.jsonl hamster_results.jsonl || true
	# @scp -o ConnectTimeout=5 creosote:/home/ubuntu/scandeval_benchmark_results.jsonl creosote_results.jsonl || true
	@scp -o ConnectTimeout=5 percival:/home/alex-admin/scandeval/scandeval_benchmark_results.jsonl percival_results.jsonl || true
	@scp -o ConnectTimeout=5 lancelot:/home/alex-admin/scandeval/scandeval_benchmark_results.jsonl lancelot_results.jsonl || true
	# @scp -o ConnectTimeout=5 dfm-a10:/home/ucloud/scandeval_benchmark_results.jsonl dfm-a10_results.jsonl || true
	# @scp -o ConnectTimeout=5 dfm-a40:/home/ucloud/scandeval_benchmark_results.jsonl dfm-a40_results.jsonl || true
	# @scp -o ConnectTimeout=5 dfm-a100:/home/ucloud/scandeval_benchmark_results.jsonl dfm-a100_results.jsonl || true
	@touch scandeval_benchmark_results.jsonl
	@if [ -f blackknight_results.jsonl ]; then \
		cat blackknight_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm blackknight_results.jsonl; \
	fi
	@if [ -f rabbit_results.jsonl ]; then \
		cat rabbit_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm rabbit_results.jsonl; \
	fi
	@if [ -f maininpink_results.jsonl ]; then \
		cat maininpink_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm maininpink_results.jsonl; \
	fi
	@if [ -f hamster_results.jsonl ]; then \
		cat hamster_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm hamster_results.jsonl; \
	fi
	@if [ -f creosote_results.jsonl ]; then \
		cat creosote_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm creosote_results.jsonl; \
	fi
	@if [ -f percival_results.jsonl ]; then \
		cat percival_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm percival_results.jsonl; \
	fi
	@if [ -f lancelot_results.jsonl ]; then \
		cat lancelot_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm lancelot_results.jsonl; \
	fi
	@if [ -f dfm-a10_results.jsonl ]; then \
		cat dfm-a10_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm dfm-a10_results.jsonl; \
	fi
	@if [ -f dfm-a40_results.jsonl ]; then \
		cat dfm-a40_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm dfm-a40_results.jsonl; \
	fi
	@if [ -f dfm-a100_results.jsonl ]; then \
		cat dfm-a100_results.jsonl >> scandeval_benchmark_results.jsonl; \
		rm dfm-a100_results.jsonl; \
	fi

filter_records:
	@. .venv/bin/activate && \
		python python/filter_records.py scandeval_benchmark_results.jsonl

danish-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Danish NLU 🇩🇰" \
			-l da Danish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d DANSK da ner micro_f1_no_misc micro_f1 \
			-d "Angry Tweets" da sent mcc macro_f1 \
			-d ScaLA-da da la mcc macro_f1 \
			-d ScandiQA-da da rc em f1

danish-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Danish NLG 🇩🇰" \
			-l da Danish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d ScandiQA-da da rc em f1 \
			-d Nordjylland-News da summ bertscore rouge_l \
			-d "Danske Talemaader" da know mcc accuracy \
			-d "Danish Citizen Tests" da know mcc accuracy \
			-d HellaSwag-da da reason mcc accuracy

swedish-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Swedish NLU 🇸🇪" \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1

swedish-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Swedish NLG 🇸🇪" \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1 \
			-d SweDN sv summ bertscore rouge_l \
			-d MMLU-sv sv know mcc accuracy \
			-d HellaSwag-sv sv reason mcc accuracy

norwegian-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Norwegian NLU 🇳🇴" \
			-l no Norwegian \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1

norwegian-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Norwegian NLG 🇳🇴" \
			-l no Norwegian \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d "No Sammendrag" no summ bertscore rouge_l \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1 \
			-d MMLU-no no know mcc accuracy \
			-d HellaSwag-no no reason mcc accuracy

icelandic-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Icelandic NLU 🇮🇸" \
			-l is Icelandic \
			-t ner "Named Entity Recognition" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d MIM-GOLD-NER is ner micro_f1_no_misc micro_f1 \
			-d ScaLA-is is la mcc macro_f1 \
			-d NQiI is rc em f1

icelandic-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Icelandic NLG 🇮🇸" \
			-l is Icelandic \
			-t ner "Named Entity Recognition" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d NQiI is rc em f1 \
			-d RRN is summ bertscore rouge_l \
			-d ARC-is is know mcc accuracy \
			-d Winogrande-is is reason mcc accuracy

faroese-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Faroese NLU 🇫🇴" \
			-l fo Faroese \
			-t ner "Named Entity Recognition" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d FoNE fo ner micro_f1_no_misc micro_f1 \
			-d ScaLA-fo fo la mcc macro_f1 \
			-d FoQA fo rc em f1

german-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "German NLU 🇩🇪" \
			-l de German \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d GermEval de ner micro_f1_no_misc micro_f1 \
			-d SB10k de sent mcc macro_f1 \
			-d ScaLA-de de la mcc macro_f1 \
			-d GermanQuAD de rc em f1

german-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "German NLG 🇩🇪" \
			-l de German \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d GermanQuAD de rc em f1 \
			-d MLSum de summ bertscore rouge_l \
			-d MMLU-de de know mcc accuracy \
			-d HellaSwag-de de reason mcc accuracy

dutch-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Dutch NLU 🇳🇱" \
			-l nl Dutch \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d CoNLL-nl nl ner micro_f1_no_misc micro_f1 \
			-d "Dutch Social" nl sent mcc macro_f1 \
			-d ScaLA-nl nl la mcc macro_f1 \
			-d SQuAD-nl nl rc em f1

dutch-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Dutch NLG 🇳🇱" \
			-l nl Dutch \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d SQuAD-nl nl rc em f1 \
			-d Wiki-Lingua-NL nl summ bertscore rouge_l \
			-d MMLU-nl nl know mcc accuracy \
			-d HellaSwag-nl nl reason mcc accuracy

english-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "English NLU 🇬🇧" \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-d CoNLL-en en ner micro_f1_no_misc micro_f1 \
			-d SST5 en sent mcc macro_f1 \
			-d ScaLA-en en la mcc macro_f1 \
			-d SQuAD en rc em f1

english-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "English NLG 🇬🇧" \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d SQuAD en rc em f1 \
			-d CNN-DailyMail en summ bertscore rouge_l \
			-d MMLU en know mcc accuracy \
			-d HellaSwag en reason mcc accuracy

mainland-scandi-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Mainland Scandinavian NLU 🇩🇰🇳🇴🇸🇪" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m accuracy "Accuracy" \
			-d DANSK da ner micro_f1_no_misc micro_f1 \
			-d "Angry Tweets" da sent mcc macro_f1 \
			-d ScaLA-da da la mcc macro_f1 \
			-d ScandiQA-da da rc em f1 \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1 \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1

mainland-scandi-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Mainland Scandinavian NLG 🇩🇰🇳🇴🇸🇪" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d ScandiQA-da da rc em f1 \
			-d Nordjylland-News da summ bertscore rouge_l \
			-d "Danske Talemaader" da know mcc accuracy \
			-d "Danish Citizen Tests" da know mcc accuracy \
			-d HellaSwag-da da reason mcc accuracy \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d "No Sammendrag" no summ bertscore rouge_l \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1 \
			-d MMLU-no no know mcc accuracy \
			-d HellaSwag-no no reason mcc accuracy \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1 \
			-d SweDN sv summ bertscore rouge_l \
			-d MMLU-sv sv know mcc accuracy \
			-d HellaSwag-sv sv reason mcc accuracy

germanic-nlu:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Germanic NLU 🇪🇺" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-l is Icelandic \
			-l de German \
			-l nl Dutch \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
			-m mcc "Matthews Correlation Coefficient" \
			-m macro_f1 "Macro-average F1-score" \
			-m micro_f1_no_misc "Micro-average F1-score without MISC tags" \
			-m micro_f1 "Micro-average F1-score with MISC tags" \
			-m em "Exact Match" \
			-m f1 "F1-score" \
			-m accuracy "Accuracy" \
			-d DANSK da ner micro_f1_no_misc micro_f1 \
			-d "Angry Tweets" da sent mcc macro_f1 \
			-d ScaLA-da da la mcc macro_f1 \
			-d ScandiQA-da da rc em f1 \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1 \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1 \
			-d MIM-GOLD-NER is ner micro_f1_no_misc micro_f1 \
			-d ScaLA-is is la mcc macro_f1 \
			-d NQiI is rc em f1 \
			-d GermEval de ner micro_f1_no_misc micro_f1 \
			-d SB10k de sent mcc macro_f1 \
			-d ScaLA-de de la mcc macro_f1 \
			-d GermanQuAD de rc em f1 \
			-d CoNLL-nl nl ner micro_f1_no_misc micro_f1 \
			-d "Dutch Social" nl sent mcc macro_f1 \
			-d ScaLA-nl nl la mcc macro_f1 \
			-d SQuAD-nl nl rc em f1 \
			-d CoNLL-en en ner micro_f1_no_misc micro_f1 \
			-d SST5 en sent mcc macro_f1 \
			-d ScaLA-en en la mcc macro_f1 \
			-d SQuAD en rc em f1

germanic-nlg:
	@. .venv/bin/activate && \
		python python/generate_leaderboard.py "Germanic NLG 🇪🇺" \
			-l da Danish \
			-l no Norwegian \
			-l sv Swedish \
			-l is Icelandic \
			-l de German \
			-l nl Dutch \
			-l en English \
			-t ner "Named Entity Recognition" \
			-t sent "Sentiment Classification" \
			-t la "Linguistic Acceptability" \
			-t rc "Reading Comprehension" \
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
			-d ScandiQA-da da rc em f1 \
			-d Nordjylland-News da summ bertscore rouge_l \
			-d "Danske Talemaader" da know mcc accuracy \
			-d "Danish Citizen Tests" da know mcc accuracy \
			-d HellaSwag-da da reason mcc accuracy \
			-d NorNE-nb no ner micro_f1_no_misc micro_f1 \
			-d NorNE-nn no ner micro_f1_no_misc micro_f1 \
			-d NoReC no sent mcc macro_f1 \
			-d "No Sammendrag" no summ bertscore rouge_l \
			-d ScaLA-nb no la mcc macro_f1 \
			-d ScaLA-nn no la mcc macro_f1 \
			-d NorQuAD no rc em f1 \
			-d MMLU-no no know mcc accuracy \
			-d HellaSwag-no no reason mcc accuracy \
			-d SUC3 sv ner micro_f1_no_misc micro_f1 \
			-d SweReC sv sent mcc macro_f1 \
			-d ScaLA-sv sv la mcc macro_f1 \
			-d ScandiQA-sv sv rc em f1 \
			-d SweDN sv summ bertscore rouge_l \
			-d MMLU-sv sv know mcc accuracy \
			-d HellaSwag-sv sv reason mcc accuracy \
			-d MIM-GOLD-NER is ner micro_f1_no_misc micro_f1 \
			-d ScaLA-is is la mcc macro_f1 \
			-d NQiI is rc em f1 \
			-d RRN is summ bertscore rouge_l \
			-d ARC-is is know mcc accuracy \
			-d Winogrande-is is reason mcc accuracy \
			-d GermEval de ner micro_f1_no_misc micro_f1 \
			-d SB10k de sent mcc macro_f1 \
			-d ScaLA-de de la mcc macro_f1 \
			-d GermanQuAD de rc em f1 \
			-d MLSum de summ bertscore rouge_l \
			-d MMLU-de de know mcc accuracy \
			-d HellaSwag-de de reason mcc accuracy \
			-d CoNLL-nl nl ner micro_f1_no_misc micro_f1 \
			-d "Dutch Social" nl sent mcc macro_f1 \
			-d ScaLA-nl nl la mcc macro_f1 \
			-d SQuAD-nl nl rc em f1 \
			-d Wiki-Lingua-NL nl summ bertscore rouge_l \
			-d MMLU-nl nl know mcc accuracy \
			-d HellaSwag-nl nl reason mcc accuracy \
			-d CoNLL-en en ner micro_f1_no_misc micro_f1 \
			-d SST5 en sent mcc macro_f1 \
			-d ScaLA-en en la mcc macro_f1 \
			-d SQuAD en rc em f1 \
			-d CNN-DailyMail en summ bertscore rouge_l \
			-d MMLU en know mcc accuracy \
			-d HellaSwag en reason mcc accuracy
