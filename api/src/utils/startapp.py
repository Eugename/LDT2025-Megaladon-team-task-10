import logging
import warnings
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)


class Model:
    """Класс по инициализации модели на разворачиваемом компьютере
    """
    def __init__(self) -> None:
        try:
            tuned_model_path = "./src/models/ner_model_DeepPavlov_iter2_2126"
            tokenizer = AutoTokenizer.from_pretrained(tuned_model_path)
            tokenizer.model_max_length = 128
            model = AutoModelForTokenClassification.from_pretrained(
                tuned_model_path
            )

            self.ner_pipeline = pipeline(
                "ner",
                model=model,   # путь к сохранённой модели
                tokenizer=tokenizer,
                aggregation_strategy="none"
            )
            self.ner_pipeline("старт")
            logging.info("Модель успешно инициализирована")
        except Exception as e:
            logging.info(f"Модель не инициализировалась, ошибка: {e}")
