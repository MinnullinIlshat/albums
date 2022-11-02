# albums

Приложение показывает список загруженных альбомов. 
Возможна сортировка альбомов по названию или по имени исполнителя. 
Для сортировки необходимо кликнуть на кнопку sort в соответствующей колонке. 

Requirements
------------

- Python (3.8, 3.9, 3.10)
- Django (4.0)
- Djagno REST Framework (3.7, 3.8, 3.9, 3.10, 3.11, 3.12)
- requests ('*')

Как запустить? 
----------

Сохраняем репозиторий и переходим в папку проекта

    $ git clone https://github.com/MinnullinIlshat/albums.git
    $ cd albums

Устанавливаем виртуальное окружение и Django, DRF и библиотеку requests

    ~/albums$ pipenv install django
    ~/albums$ pipenv shell
    (albums)$ pip install djangorestframework
    (albums)$ pip install requests
    
Запускаем приложение (находясь в основной папке проекта - albums):
    
    (albums)$ python manage.py runserver
    
Копируем ссылку http://127.0.0.1:8000/ или localhost

Для сортировки по столбцу нужно нажать кнопку sort. 
Результат API доступен по ссылке http://127.0.0.1:8000/api
