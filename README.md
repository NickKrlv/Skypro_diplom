Образовательные Модули Django & DRF Проект
Этот проект представляет собой небольшое веб-приложение, разработанное с использованием Django и Django Rest Framework, которое позволяет управлять "Образовательными Модулями". Каждый модуль содержит порядковый номер, название и описание.

Задача:

Целью проекта является реализация следующих функций для модели "Образовательные Модули":

CRUD операции: Создание (Create), Чтение (Read), Обновление (Update), Удаление (Delete) для каждого образовательного модуля.

Тестирование: Полностью покрыть все модели, сериализаторы и представления автоматизированными юнит-тестами.

Требуемый стэк:

Python 3.11: Язык программирования, на котором основан проект.

Docker: Платформа для разработки, развертывания и управления приложениями в контейнерах.

Django: Высокоуровневый Python-фреймворк для веб-разработки.

Django Rest Framework: Набор инструментов для построения Web APIs на базе Django.

Условия приемки
Открытый репозиторий: Код размещен в открытом репозитории на GitHub.

Документация: Создана документация по API redoc/swagger.

Автоматизированные юнит-тесты: Весь код покрыт автоматизированными юнит-тестами для обеспечения стабильности и надежности.

Оформление кода: Код оформлен согласно стандарту PEP8, чтобы обеспечить его читаемость и совместимость.

Readme файл: Предоставлен Readme файл, как этот, с описанием проекта, инструкциями по установке и запуску.

Использование Docker: В проекте использован Docker для упрощения процесса установки и запуска приложения.

Команды для удобства(без контейнера):

python -m venv venv
./venv/bin/activate
pip install -r requirements.txt

python makemigrations
python migrate

python manage.py load_data

python manage.py runserver

python manage.py test
coverage run --source='.' manage.py test
coverage report

Команды для удобства(с контейнером):

docker-compose up
