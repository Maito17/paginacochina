from django.db import migrations


def seed_default_categories(apps, schema_editor):
    Category = apps.get_model('games', 'Category')
    defaults = [
        ('RPG', 'Juegos de rol.'),
        ('Unity', 'Juegos desarrollados con Unity.'),
        ('Remoy', 'Categoria para contenido Remoy.'),
    ]

    for name, description in defaults:
        Category.objects.get_or_create(
            name=name,
            defaults={'description': description},
        )


def noop_reverse(apps, schema_editor):
    # Keep seeded categories on rollback to avoid accidental data loss.
    return


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_controlproxy_game_image1_game_image2'),
    ]

    operations = [
        migrations.RunPython(seed_default_categories, noop_reverse),
    ]
