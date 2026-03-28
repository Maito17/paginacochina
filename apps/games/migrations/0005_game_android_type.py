from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_download_links_optional_and_android'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='android_type',
            field=models.CharField(blank=True, choices=[('android', 'Android'), ('joinplay', 'Joinplay'), ('apk', 'APK')], default='', max_length=20),
        ),
    ]