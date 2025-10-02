from pydantic import BaseModel, Field


class QueryInfo(BaseModel):
    """Класс принятия данных
    Raises:
        ValueError: Ошибка в наличии всех полей для шаблона
    """
    input: str = Field(
        ...,
        example="Кола 2л без сахара",
        description="Пользовательский запрос для поиска товара"
    )


class EntityResponse(BaseModel):
    start_index: int = Field(
        ..., example=0, description="Начальная позиция сущности"
    )
    end_index: int = Field(
        ..., example=8, description="Конечная позиция сущности"
    )
    entity: str = Field(
        ..., example="B-TYPE", description="Тип сущности (BIO-формат)"
    )
