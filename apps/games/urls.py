from django.urls import path
from .views import (
    portada, busqueda_avanzada, suscriptores, categoria, suscripciones, redes,
    admin_comentarios, admin_subir_juego, admin_control, juego_detalle
)

urlpatterns = [
    path('', portada, name='portada'),
    path('juego/<int:juego_id>/', juego_detalle, name='juego_detalle'),
    path('busqueda-avanzada/', busqueda_avanzada, name='busqueda_avanzada'),
    path('suscriptores/', suscriptores, name='suscriptores'),
    path('categoria/', categoria, name='categoria'),
    path('categoria/rpg/', categoria, {'tipo': 'RPG'}, name='categoria_rpg'),
    path('categoria/unity/', categoria, {'tipo': 'Unity'}, name='categoria_unity'),
    path('categoria/remoy/', categoria, {'tipo': 'Remoy'}, name='categoria_remoy'),
    path('suscripciones/', suscripciones, name='suscripciones'),
    path('suscripciones/android/', suscripciones, {'tipo': 'Android'}, name='suscripciones_android'),
    path('suscripciones/joinplay/', suscripciones, {'tipo': 'Joinplay'}, name='suscripciones_joinplay'),
    path('suscripciones/apk/', suscripciones, {'tipo': 'APK'}, name='suscripciones_apk'),
    path('redes/', redes, name='redes'),
    path('redes/discord/', redes, {'tipo': 'discord'}, name='redes_discord'),
    # Panel personalizado
    path('panel/control/', admin_control, name='admin_control'),
    path('panel/comentarios/', admin_comentarios, name='admin_comentarios'),
    path('panel/subir-juego/', admin_subir_juego, name='admin_subir_juego'),
]
