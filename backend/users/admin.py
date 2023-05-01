from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """ Класс для работы в админ-панели."""
    # Список полей, которые отображаются в админке
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'is_staff',
        'is_active',
        'date_joined',
    )
    # Список редактируемых полей
    list_editable = ('is_staff', 'is_active')
    # Поля которые поддерживают поиск
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # Поля, которые поддерживают фильтр
    list_filter = ('username', 'first_name', 'last_name', 'email')
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
