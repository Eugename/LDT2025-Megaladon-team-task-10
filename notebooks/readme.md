Model use:
```python
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

model_name = "MegaLDN/rubert-finetune-goods_NER"
tokenizer = AutoTokenizer.from_pretrained(model_name])
model = AutoModelForTokenClassification.from_pretrained(model_name)

ner_pipeline = pipeline(
"ner",
model=model ,
tokenizer=tokenizer ,
aggregation_strategy="none"
)

text = "Сок агуша 2л"
output = ner_pipeline(text)
# >> print(output)
# << [{'entity': 'B-TYPE', 'score': np.float32(0.99929225), 'index': 1, 'word': 'Сок', 'start': 0, 'end': 3}, {'entity': 'B-BRAND', 'score': np.float32(0.8768344), 'index': 2, 'word': 'аг', 'start': 4, 'end': 6}, {'entity': 'B-BRAND', 'score': np.float32(0.85818267), 'index': 3, 'word': '##уша', 'start': 6, 'end': 9}, {'entity': 'B-VOLUME', 'score': np.float32(0.99927515), 'index': 4, 'word': '2', 'start': 10, 'end': 11}, {'entity': 'B-VOLUME', 'score': np.float32(0.9982621), 'index': 5, 'word': '##л', 'start': 11, 'end': 12}]
```
