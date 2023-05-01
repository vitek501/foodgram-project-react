from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        unique=True,
        verbose_name='Название',
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет',
        validators=[
            RegexValidator(
                '^#([a-fA-F0-9]{6})',
                message='Поле должно содержать HEX-код.'
            )
        ]

    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг',
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self) -> str:
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название ингредиента',
    )
    measurement_unit = models.CharField(
        max_length=20,
        verbose_name='Единицы измерения',
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self) -> str:
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название')
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/',
        blank=True
    )
    text = models.TextField(
        'Описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        through_fields=('recipe', 'ingredient'),
        blank=True,
        verbose_name='Ингридиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
    )
    cooking_time = models.IntegerField(
        'Время приготовления, мин',
        validators=[MinValueValidator(1)]
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.name[:50]}'


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='ingridients',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    amount = models.IntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')
        verbose_name = 'Ингидиенты в рецепте'
        verbose_name_plural = 'Ингридиенты в рецептах'

    def __str__(self):
        return f'{self.recipe} Ингридиенты: {self.ingredient}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_list'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепты',
        related_name='recipe_lists'
    )

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Список избранных'

    def __str__(self):
        return f'{self.user} - {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_user',
        verbose_name='Добавил в корзину'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_recipe',
        verbose_name='Рецепт в корзине'
    )

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ('-id',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Рецепт {self.recipe} в списке покупок у {self.user}'
