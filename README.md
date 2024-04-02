WEB-приложение для доставки пиццы

Ты фронтендер -> [тык](/README-front.md)

## Запуск приложения
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

## Как заливать изменения в github
[Шпаргалка по Github](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
Ты уже сделал ```git clone <>```(делается один раз), переключился на рабочюю ветку (```git switch <название ветки для разработки>)```), синхронизировал последние изменения командой ```git fetch```(в идеале делать перед началом работы над проектом) и сделал какие-то изменения  
####  Для терминала
1. Введи в терминал следующее: ```git add .``` - добавить твои изменения в "буфер" git'a
2. Введи в терминал следующее: ```git commit -m "<comment>"``` - запишет изменения в git
3. Введи в терминал следующее: ```git push``` и удостоверься, что ты находишься в актуальной для разработки ветки (можно проверить комадой ```git status``` строка "On branch <название ветки>")
####  Для PyCharm [Официальная документация](https://www.jetbrains.com/help/pycharm/sync-with-a-remote-repository.html?ysclid=luie4yjgys843871173#pull)
1. Перейди в окно "Commit" (alt/кракозябра с мака+0)
2. В окне "Changes" поставь галочку, ниже в поле "Commit Message" напиши комментарий для коммита
3. Если это не единиственный коммит, нажми на кнопку "Commit", а затем продолжи работу ИЛИ если этот коммит последний, нажми на кнопку "Commit and Push" 
####  Для VSCode
[Шпаргалка по Github](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
