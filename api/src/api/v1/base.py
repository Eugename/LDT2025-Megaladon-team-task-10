from fastapi import (  # type: ignore
    APIRouter,
    status,
    HTTPException,
    Request
)
from typing import List
import logging
from src.api.v1.routers.pydentic.classes import QueryInfo, EntityResponse

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
router = APIRouter()


def format(entities_list):
    """
    Форматирует список сущностей из формата (start, end, entity) 
    в формат {"start_index": start, "end_index": end, "entity": entity}
    """
    formatted_list = []
    for entity in entities_list:
        formatted_entity = {
            "start_index": entity[0],
            "end_index": entity[1],
            "entity": entity[2]
        }
        formatted_list.append(formatted_entity)

    return formatted_list


def format_spans(x):
    nums_to_del = []
    for i in range(0, len(x)-1):
        if (x[i]['word'][0] == '#'):
            continue
        if (x[i+1]['word'][0] == '#'):
            nums_to_del.append(i+1)
            x[i]['word'] = x[i]['word'] + x[i+1]['word'].replace('#','')
            x[i]['end'] = x[i+1]['end']
    for i in sorted(nums_to_del, reverse=True):
        x.pop(i)

    # new format
    new = []
    for elem in x:
        new.append((elem['start'], elem['end'], elem['entity']))
    return new


def merge_spans(spans):
    """
    Объединяет соседние интервалы с одинаковым label (B/I одного типа)
    """
    if not spans:
        return []

    merged = []
    current_start, current_end, current_label = spans[0]

    for start, end, label in spans[1:]:
        if label.split("-")[-1] == current_label.split("-")[-1] and start == current_end:
            # расширяем границу, если тип сущности совпадает и интервалы соприкасаются
            current_end = end
        else:
            merged.append((current_start, current_end, current_label))
            current_start, current_end, current_label = start, end, label

    merged.append((current_start, current_end, current_label))
    return merged


@router.get(
    "/healthcheck",
    tags=["Dev"],
    summary="Проверка работоспособности API",
    status_code=status.HTTP_200_OK,
)
async def healthcheck():
    logger.info("Status check request has been received")
    return {"message": "Status: Ok"}


@router.post(
    "/predict",
    tags=["ner"],
    summary="Запрос для получения сущностей",
    response_model=List[EntityResponse],
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Успешный ответ со списком сущностей",
            "content": {
                "application/json": {
                    "example": [
                     {"start_index": 0, "end_index": 4, "entity": "B-BRAND"},
                     {"start_index": 5, "end_index": 7, "entity": "B-VOLUME"},
                     {"start_index": 8, "end_index": 16, "entity": "B-TYPE"}
                    ]
                }
            },
        },
        400: {"description": "Некорректный ввод"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def predict(query: QueryInfo, request: Request):
    """Функция возвращает сущности на основе запроса пользователя
    Args:
        request (QuerryInfo): Реквест с параметрами запроса,
        в данном случае приходит лишь input
        response_model (_type_, optional): Вид возвращения переменных.
        Defaults to List[EntityResponse].
    Returns:
        JSON: JSON в необходимом формате
    """
    logger.info(f"Пришел запрос от пользователя: {query.input}")
    if not query.input or not query.input.strip():
        return []
    try:
        ner_pipeline = request.app.state.ner_pipeline
        response = ner_pipeline(query.input)
        logger.info(f"Сырой ответ от модели {response}")
        logger.info(f"Отформатированный ответ {merge_spans(format_spans(response))}")
        return format(merge_spans(format_spans(response)))

    except Exception as e:
        logging.error(f"Ошибка при обработке запроса: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при обработке запроса",
        )
