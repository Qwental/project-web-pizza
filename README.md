# WEB-приложение для доставки пиццы

- [WEB-приложение для доставки пиццы](#web-приложение-для-доставки-пиццы)
    - [Запуск приложения](#запуск-приложения)


Ты фронтендер -> [тык](/README-front.md)
- [WEB-приложение для доставки пиццы]

### Запуск приложения
1. [Ты уже установил python] Установи зависимости: ```pip install -r requirements.txt```  
2. Выполни миграцию для БД - ```python manage.py migrate```
3. Создай админ-аккаунт (с ним ты войдешь в админку Django) - ```python manage.py createsuperuser```
4. Заполни БД тестовыми данными - ```python manage.py loaddata fixtures/main/category.json fixtures/main/products.json```
5. <u>Запуск приложения производиться всегда этой командой</u>  ```python manage.py runserver``` и перейди на http://127.0.0.1:8000/
В vscode можно настроить запуск с помощью ```ctrl/control + f5```, в PyCharm это работает по умолчанию (делать ничего не нужно)
    1. Установи расширение ```ms-python.debugpy```
    2. Создай файл в .vscode/launch.json (если он есть => пункт 3)
    3. Запиши в него следующее: 
    ```json 
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "justMyCode": true
          }
    ]}  
    ```
    Этот код добавит во вкладку ```Run and Debug (Ctrl/control+shift+d)``` конфигурацию под названием Django. Теперь в этой вкладке, нажав на ```F5```, или из любой другой точки - комбинацией ```ctrl/control + f5```
