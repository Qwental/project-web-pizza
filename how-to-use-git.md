- [Работа с Git и Github {name=git}](#работа-с-git-и-github-namegit)
  - [Для терминала](#для-терминала)
  - [Для PyCharm](#для-pycharm)
  - [Для VSCode](#для-vscode)


### Работа с Git и Github [](#){name=git}
[Шпаргалка по Github](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
Ты уже сделал ```git clone <>```[то есть смог подключить ssh-ключи и авторизовать свой компьютер на github](делается один раз), переключился на рабочюю ветку (```git switch <название ветки для разработки>)```), синхронизировал последние изменения командой ```git fetch```(в идеале делать перед началом работы над проектом) и сделал какие-то изменения  
####  Для терминала
1. Введи в терминал следующее: ```git add .``` - добавить твои изменения в "буфер" git'a
2. Введи в терминал следующее: ```git commit -m "<comment>"``` - запишет изменения в git
3. Введи в терминал следующее: ```git push``` и удостоверься, что ты находишься в актуальной для разработки ветки (можно проверить комадой ```git status``` строка "On branch <название ветки>")
####  Для PyCharm
1. Перейди в окно "Commit" (alt/кракозябра с мака+0)
2. В окне "Changes" поставь галочку, ниже в поле "Commit Message" напиши комментарий для коммита
3. Если это не единиственный коммит, нажми на кнопку "Commit", а затем продолжи работу ИЛИ если этот коммит последний, нажми на кнопку "Commit and Push", а в появившемся окне кнопку "Push" [подробнее про комиты и пуши](https://www.jetbrains.com/help/pycharm/commit-and-push-changes.html)
4. Чтобы перейти на ветку, необходимо нажать на кнопку справа от названия проекта, ниже нажать на вкладку "Remote", затем на название нужной ветки и там на "Checkout" [подробнее про работу с ветками](https://www.jetbrains.com/help/pycharm/manage-branches.html?ysclid=luieepkudu227860449#create-branch),  
[подробнее про работу с синхронизацией](https://www.jetbrains.com/help/pycharm/sync-with-a-remote-repository.html?ysclid=luie4yjgys843871173#pull)
####  Для VSCode
[официальная документация](https://code.visualstudio.com/docs/sourcecontrol/overview) (в теории повторяет то, что в PyCharm, но другие вкладки/клавиши и мизерные различия)


[Шпаргалка по Github](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
