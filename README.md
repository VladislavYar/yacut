# YaCut
## Описание
Проект представляет из себя создания коротких ссылок по средствам редиректа.
В БД хранится соответсвие короткой ссылки сайта проекта к длинной ссылке.
# Имеется API для создания короткой ссылки и её получения
```
/api/id/{short_id}/ - получить ссылку

/api/id/ - создать короткую ссылку
{
  "url": "string",
  "custom_id": "string"
}
```
## Как запустить
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:VladislavYar/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать БД и таблицы в ней:
```
flask db migrate
```
```
flask db upgrade
```
Запустить проект:
```
flask run
```