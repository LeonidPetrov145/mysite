# Инструкция по работе с системой     
 




# Скачать небоходимые файлы с гидхаб 
 
 

# Установить нужные для работы библиотеки  
pip install django  
pip install djangorestframework 
pip install django-filters 
pip install djangorestframework-simplejwt 
pip install pip install psycopg2 
 

# Запустьть систему через консоль введя команду  
Команда - python manage.py runserver 
 

# Вводите эти url запросы в url строку в браузере перед этими юрл запросами ввести https:// 
 
    # Маршрут для административной панели Django 
    admin/ 
     
    # Маршрут для аутентификации через DRF  
    api/v1/drf-auth/ 
     
    # Маршрут для отображения списка задач и создания новых задач 
    api/v1/tasklist/ 
     
    # Маршрут для обновления и получения конкретной задачи по её ID 
    api/v1/task/<int:pk>/ 
     
    # Маршрут для удаления конкретной задачи по её ID 
    api/v1/taskdelate/<int:pk>/ 
     
    # Маршрут для аутентификации через Djoser  
    api/v1/auth/ 
     
    # Маршрут для получения пары токенов access и refresh 
    api/token/ 
     
    # Маршрут для обновления токена доступа (access token) 
    api/token/refresh/ 
     
    # Маршрут для проверки валидности токена 
    api/token/verify/ 
 
 
# Если чтото не работает обращайтесь суда:@LeonidPochtiIlich - Telegram, +7(996)-644-31-60