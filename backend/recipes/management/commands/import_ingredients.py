import csv
import os

from django.core.management import BaseCommand, CommandError
from django.db.utils import IntegrityError
from foodgram import settings
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Create model objects'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data/ingredients.csv')
        fieldnames = ['name', 'measurement_unit']
        try:
            with open(file_path) as csv_file:
                for row in csv.DictReader(csv_file, fieldnames=fieldnames):
                    Ingredient.objects.create(**row)
        except IntegrityError:
            raise CommandError(
                'База данных заполнена')
        except FileNotFoundError:
            raise CommandError(
                f'Файл {file_path} не найден')
        except Exception:
            raise CommandError(
                'Ошибка выполнения import_ingredients'
            )
