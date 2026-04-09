from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_seed_default_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='download_url_android',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='download_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
