# WEB-приложение для доставки пиццы

- [WEB-приложение для доставки пиццы](#web-приложение-для-доставки-пиццы)
    - [Запуск приложения](#запуск-приложения)


Ты фронтендер -> [тык](/README-front.md)
- [WEB-приложение для доставки пиццы]


При DEBUG=False пиши ```python manage.py runserver --insecure```
При DEBUG=True пиши ```python manage.py runserver```
###### Для чего это?
При DEBUG=False начинают работать 404 и тп ошибки вместо стандартных заглушек; при разработке ставим DEBUG=True; подробнее про флаг **insecure** здесь [здесь](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#cmdoption-runserver-insecure)

### Запуск приложения
1. [Ты уже установил python] Установи зависимости: ```pip install -r requirements.txt```  
2. Выполни миграцию для БД - ```python manage.py migrate```
3. Создай админ-аккаунт (с ним ты войдешь в админку Django) - ```python manage.py createsuperuser```
   * Чтобы перейти в админку, дважды кликни на кнопку ""Войти
4. Заполни БД тестовыми данными - ```python manage.py loaddata fixtures/new_all_data.json```
5. <u>Запуск приложения производиться всегда этой командой</u>  ```python manage.py runserver --insecure``` при DEBUG=FALSE и перейди на http://127.0.0.1:8000/
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
            "args": ["runserver --insecure"],
            "django": true,
            "justMyCode": true
          }
    ]}  
    ```
    Этот код добавит во вкладку ```Run and Debug (Ctrl/control+shift+d)``` конфигурацию под названием Django. Теперь в этой вкладке, нажав на ```F5```, или из любой другой точки - комбинацией ```ctrl/control + f5```
