from django.db import connection
from django.core.management.base import BaseCommand
from users.models import User
from edu.models import EduModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE users_user, edu_edumodel RESTART IDENTITY CASCADE;")

        admin = User.objects.create(email="admin@edu", password="admin", is_superuser=True, is_staff=True)
        admin.set_password("admin")
        admin.save()

        self.stdout.write(self.style.SUCCESS('Админ создан.'))

        EduModel.objects.create(number=1, name="Модель 1", description="Описание модели 1")
        EduModel.objects.create(number=2, name="Модель 2", description="Описание модели 2")

        self.stdout.write(self.style.SUCCESS('Модели созданы.'))
