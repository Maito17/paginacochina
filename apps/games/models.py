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
    tags = models.TextField(blank=True, default='', verbose_name='Tags')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'

    def __str__(self):
        return self.title

class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    url = models.URLField(verbose_name='Enlace')
    image = models.ImageField(upload_to='social_icons/', blank=True, null=True, verbose_name='Imagen de Icono')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.name

class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    image = models.ImageField(upload_to='plans/', verbose_name='Imagen')
    url = models.URLField(verbose_name='Enlace de Visita')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Plan de Suscripción'
        verbose_name_plural = 'Planes de Suscripción'

    def __str__(self):
        return self.title
