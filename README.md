WEB-приложение для доставки пиццы

Ты фронтендер -> [тык](/README-front.md)

## Запуск приложения
1. [Ты уже установил python] Установи зависимости: ```pip install -r requirements.txt```  
2. Из командой строки введи команду ```python manage.py runserver``` и перейди на http://127.0.0.1:8000/  
В vscode можно настроить запуск с помощью ```ctrl/control + f5```, в PyCharm это работает по умолчанию (делать ничего не нужно)
    1. Установи расширение ```ms-python.debugpy```
    2. Создай файл в .vscode/launch.json (если он есть => пункт 3)
    3. Запиши в него следующее: 
    ```json {
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

## Как активировать [али шо?] базу данных (актуально для разработки)
1. Выполни миграцию для БД - ```python manage.py migrate```
2. Создай админ-аккаунт (с ним ты войдешь в админку Django) - ```python manage.py createsuperuser```
3. Заполни БД тестовыми данными - ```python manage.py loaddata fixtures/main/category.json fixtures/main/products.json```

## Обозначения папок [чтобы не заблудиться]
```
.
├── db.sqlite3
├── main
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── main
│   │       ├── base.html
│   │       ├── components
│   │       │   └── cart.html
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pizza
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README-front.md
├── README.md
├── requirements.txt
└── static
    ├── fonts
    │   └── HelveticaNeueCyr-Roman.woff2
    ├── img
    ├── scripts
    │   └── cart.js
    └── styles
        ├── style.css
        └── themes.css
```
