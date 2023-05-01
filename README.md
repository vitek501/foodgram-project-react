# Foodgram - Продуктовый помощник

На этом сервисе пользователи смогут публиковать рецепты, подписываться 
на публикации других пользователей, добавлять понравившиеся рецепты в список
«Избранное», а перед походом в магазин скачивать сводный список 
продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

#### Функциональность
- Полная аутентификация пользователей.
- Создавать/редактировать/удалять собственные рецепты.
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл с количеством необходимых ингредиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

Проект доступен по адресам: http://62.84.117.180, http://yamdbfinal.ddns.net<br>
Документация: http://62.84.117.180/api/docs/

## Технологии, использованные при разработке
- python 3.7  
- Django 3.2
- djangorestframework 3.12.4  
- PostgreSQL
- Nginx
- Gunicorn
- Docker

## Запуск проекта в Docker:
Для того чтоб установить проект на локальную машину клонируйте репозиторий  
```
git clone https://github.com/vitek501/foodgram-project-react.git
cd foodgram-project-react 
```

Создать файл .env с переменными окружения.
```
cd infra
touch .env
```

Заполнить .env файл с переменными окружения.

```
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env

echo SECRET_KEY=<SECRET_KEY> >> .env
```

## Запуск
Установить и запустить приложения в контейнерах.
```
docker-compose up -d
```
Выполненить миграции, создать суперюзера, собрать статику и заполнить БД.
```
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 