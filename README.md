# Сервис выделения сущностей из поискового запроса клиента в мобильном приложении торговой сети «Пятерочка»
Этот проект представляет собой сервис по определению сущностей для хакатона X5  
Всё разворачивается в Docker-контейнерах
## Запуск проекта
1. **Подготовка окружения**:
   - Должны быть установлены:
     - Docker
     - Docker Compose
   - Создайте файл `.env` в корне проекта c содержанием: API_URL = "http://api:8000/"
   - В путь ./api/src/models/ner_model_DeepPavlov_iter2_2126/ положить файлы обученной
     BERT модели, выложенной на ['HuggingFace'](https://huggingface.co/MegaLDN/rubert-finetune-goods_NER)

2. **Запуск**:
   ```bash
   docker compose up -d --build

├── api/            # Backend на FastAPI  
├── streamlit/      # Веб Streamlit-интерфейс  
├── nginx/          # Конфигурация Nginx для маршрутизации запросов  
├── .env            # .env файл  
└── docker-compose.yml  

3. **Возможности**:  
Доступен запрос по эндпоинту  http://v2943093.hosted-by-vdsina.ru/api/predict  
Доступен Swagger http://v2943093.hosted-by-vdsina.ru/docs  
Доступен базовый интерфейс по http://v2943093.hosted-by-vdsina.ru//ui  

4. **Презентационные материалы**:
https://drive.google.com/drive/folders/1H1FHN4bm3-w4Wiqw6XDigTBkqfTtUTvs?usp=sharing
