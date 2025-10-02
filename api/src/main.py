"""Основной модуль для запуска сервиса."""
from fastapi import FastAPI  # type: ignore

from src.api.v1 import base
from src.utils.startapp import Model
from src.core import config
import warnings
import logging

import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

warnings.filterwarnings("ignore")
logger = logging.getLogger('uvicorn.access')

app = FastAPI(
    # root_path=config.BACKEND_ROOT_PATH,
    openapi_url="/docs/openapi.json",
    title=config.PROJECT_NAME,
    contact=config.PROJECT_CONTACT,
    description=config.PROJECT_DESCRIPTION,
    openapi_tags=config.PROJECT_TAGS,
    version=config.PROJECT_VERSION,
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)
path = "/api"

app.include_router(base.router, prefix=f"{path}")
app.state.ner_pipeline = Model().ner_pipeline
