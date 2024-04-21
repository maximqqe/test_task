Тестовое задание от Hammer Systems

Использованные технологии: Django, DRF, PostgreSQL, simple jwt

Описание функционала:
визуальный интерфейс отсутствует, вся работа происходит через Postman.
присутствует 5 ендпоинтов

1. api/users/get_code [POST]

Запрос для имитации отправления кода по номеру телефона. 
Как и сказано в условии, запрос приостанавливает работу сервера на 2 секунды.

2. api/users/login [POST]

Запрос на вход в систему. Требуется указать номер телефона и код (который должен быть отправлен на телефон), 
при успешном исполнении возвращает JWT access token, который действует 30 минут.
   
3. api/users/ [GET]

Запрос для получение списка всех пользователей, для каждого пользователя выводится номер телефона, 
собственный инвайт-код, введённый инвайт-код (если есть), список телефонов рефералов (если есть).

4. api/profile/ [GET]

Запрос для получения собственного профиля, для успешного выполнения нужно передать JWT access token, 
который выдается на странице api/users/login.
Запрос возвращает номер телефона текущего пользователя, его инвайт-код, инвайт-код который он ввёл (если ввёл), список его рефералов (если они имеются)

5. api/profile/ [PATCH]

Запрос для ввода чужого инвайт-кода. Для доступа также требуется предоставить JWT access token.
Каждый пользователь может вводить только один код. Пользователь не может ввести свой код. Также вводимый код должен существовать.

