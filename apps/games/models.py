from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Game(models.Model):
    class AndroidType(models.TextChoices):
        ANDROID = 'android', 'Android'
        JOINPLAY = 'joinplay', 'Joinplay'
        APK = 'apk', 'APK'

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='games/covers/')
    image1 = models.ImageField(upload_to='games/screenshots/', blank=True, null=True)
    image2 = models.ImageField(upload_to='games/screenshots/', blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)
    download_url_android = models.URLField(blank=True, null=True)
    android_type = models.CharField(
        max_length=20,
        choices=AndroidType.choices,
        blank=True,
        default='',
        verbose_name='Tipo Android',
        help_text='Clasifica el juego para las secciones Android, Joinplay o APK.',
    )
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'

    def __str__(self):
        return self.title
