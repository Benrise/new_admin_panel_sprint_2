**Запуск сервисов для локальной разработки и тестирования**

Запуск PosgreSQL:
docker run -d \
  --name postgres \
  -p 5432:5432 \
  -v $HOME/postgresql/data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=123qwe \
  -e POSTGRES_USER=app \
  -e POSTGRES_DB=movies_database  \
  postgres:13 

Запуск Swagger:
docker run -d \
    --name swagger \
    -p 8080:8080 \
    -v $HOME/swagger/movies/openapi.yaml:/swagger.yaml \
    -e SWAGGER_JSON=/swagger.yaml \
    swaggerapi/swagger-ui
