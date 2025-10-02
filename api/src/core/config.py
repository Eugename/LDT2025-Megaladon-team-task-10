"""Конфигурационные файлы и переменные."""
import os
from sqlalchemy import create_engine  # type:ignore

PROJECT_NAME = "Собери корзину"
PROJECT_DESCRIPTION = """
Это прототипноре решение для интеллектуального поиска в продуктовых онлайн-сервисах.
Сегодня покупатели вводят запросы в произвольной форме: с опечатками, сокращениями и неполными словами.

Цель проекта — разработка системы извлечения именованных сущностей из пользовательских поисковых запросов. Модель автоматически выделяет:

TYPE — категорию товара (молоко, хлеб, вода, чипсы и др.);
BRAND — бренд (Coca-Cola, Простоквашино, Lays и др.);
VOLUME — объём, вес или количество (0.5 л, 1 л, 200 г, 10 шт.);
PERCENT — процент (2.5%, 15%).

Формат аннотации — BIO-разметка, что позволяет корректно обрабатывать как отдельные сущности, так и составные.
Метрика качества: macro-averaged F1-score по BIO-разметке для всех типов сущностей.
"""

PROJECT_CONTACT = {
    "names": ["Miroshnicenko Anton", "Eugine Novikov"],
    "email": ["anton199823@gmail.com", ""]
}
PROJECT_VERSION = "0.1.0"

PROJECT_TAGS = [
    {"name": "Собери корзину",
     "description": "Проект по извлечению сущностей из поисковых запросов в «Пятёрочке». \
Она понимает бренд, категорию, объём и процент,\
повышая точность и скорость поиска товаров", },
]

INPUT_DIR_PATH = os.getenv("INPUT_DIR_PATH")
MODELS_PATH = os.getenv("MODELS_PATH")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")
DB_ECHO_LOG = os.getenv("DB_ECHO_LOG")  # bool логирование SQL запросов

# ENGINE = create_engine(
#     f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:5432/{POSTGRES_DB}"  # noqa
# )

BACKEND_ROOT_PATH = os.getenv("BACKEND_ROOT_PATH")
