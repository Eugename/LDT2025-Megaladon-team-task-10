"""Модуль с описанием логгера loguru."""

import json

from loguru import logger

logs_path = "/logs"


def serialize(record):
    """Сериализация с включением определенных полей."""
    subset = {
        "time": record["time"].strftime("%Y-%m-%d %H:%M:%S"),
        "function": record["function"],
        "message": record["message"],
        "level": record["level"].name,
    }
    subset.update(json.loads(subset["message"]))
    _ = subset.pop("message", None)
    return json.dumps(subset)


def json_formatter(record):
    """Запись отформатированного лога в поле ["extra"]["serialized"]."""
    record["extra"]["serialized"] = serialize(record)
    return "{extra[serialized]}\n"


def initialize_logger():
    """
    Инициализирует loguru-логгер.

    Returns:
        Логгер типа loguru._logger.Logger.
    """
    logger.remove()
    logger.add(
        f"{logs_path}/backend_bot.log",
        format=json_formatter,
        enqueue=True,
    )
    return logger
