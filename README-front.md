# Web-pizza frontend

Работаем над всеми файлами *.html, *.css, *.js

## Правила написания HTML и CSS [***ОБЯЗАТЕЛЬНО***]
1. Для неймингов используем BEM, в разработке допускается писать любые названия (потом их удалять)
2. Сайт должен работать и на Unix, и на Windows : Ира и Амелия на MacOS, поэтому следим внимательно за атрибутами -webkit-*
3. __КАЖДЫЙ__ [div, обозначающий начало секции или чего-то важного] блок должен иметь входной комментарий - кто он и за что отвечает
4. TODO-ушки помогают Вове для всяких Mira-штук -- больше => лучше (?)
5. Эстетика в коде === эстетика в душе
6. Еще не устал от правил? [ЕЩЕ БОЛЬШЕ ПРАВИЛ](https://google.github.io/styleguide/htmlcssguide.html)

## Перед началом работы
### VSCode
- Установи VSCode(желательно)
- Нажми `Ctrl/control + Shift + P`, там введи `Show Recommended Extensions` и установи рекомендуемые расширение для удобной работы:
  - vscode-django-support - поддержка шаблонок Django
  - Todo Tree - красивый список задач
  - Prettier - Code formatter || vscode-django-support - автоматический "улучшайзер" кода (отступы/пробелы и тп)
  - Bookmarks - закладки чтобы не потеряться в полотне HTML-кода
  - CSS Peek - быстрый поиск css
  - vscode-pets - милые зверушки
  - Live Share (мб не понадобиться)
  - REST Client (мб не понадобиться)
- автоматически установятся следующие настройки (также для удобства):
  ```json
  {
    "files.encoding": "utf8",
    "editor.tabSize": 2,
    "files.autoSave": "afterDelay",
    "editor.formatOnSave": false,
  }
  ```

* В VSCode проверь, что снизу установлены следующие параметры:
  - Spaces: 4
  - UTF-8 (кодировка)
  - LF
  - Prettier = одна или две галочки
- Для форматирования кода используй комбинацию клавиш ```ctrl/control + shift + i``` или ту, которая установлена в настройках (пкм по полю с кодом, format document -> справа будет указана комбинация клавиш)
- ГОТОВО!!111
### WebStorm/Pycharm/...
Я таким не пользуюсь и тебе не советую, но если пользуешься, почитай [официальную документацию](https://prettier.io/docs/en/webstorm); 
помимо этого в WebStorm/Pycharm/... изначально нет поддержки великого и могучего, так что... 


### Запуск Development (с Django)
```python manage.py runserver```

## Необходимые характеристики AKA полезные шпаргалки
- [BEM-нейминг](https://ru.bem.info/methodology/quick-start/)
- [css](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [прикольное видева](https://youtube.com/@AleksanderLamkov?si=38l6Z1tdCwhmltWy)