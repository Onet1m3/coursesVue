# courses

#DO:

Сделаны базовые настройки для проекта.

1. Создано 3 приложения
    User - расширил модель, создал менеджера
    Courses - создал основные модели, сделал минимальную вьюху, урл. На фронт не вывел
    Log - создал таблицу для лога партнеров

2. Templates:
    создал base.html - для удобства вынес sidebar, navbar. Sidebar общается с бэком через context_processor, создал его в app.courses
                                                           Navbar пока захардкореню

    шаблон главной страницы index.html унаследовал от base.html и больше пока ничего не делал

3. Fixture:
    создал файл, можно пользоваться, но стоит добавить моделей для курсов


