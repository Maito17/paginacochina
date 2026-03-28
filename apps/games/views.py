from django.shortcuts import get_object_or_404, render
from apps.interactions.models import Review

# Vista detalle de juego solo visualización pública
def juego_detalle(request, juego_id):
    juego = get_object_or_404(Game, id=juego_id)
    comentarios = Review.objects.filter(game=juego).select_related('user').order_by('-created_at')
    comentarios_count = comentarios.count()
    promedio_rating = comentarios.aggregate(Avg('rating'))['rating__avg'] or 0
    es_popular = juego.views_count >= 10 or promedio_rating >= 4.5  # Ejemplo de criterio
    return render(request, 'games/juego_detalle.html', {
        'juego': juego,
        'comentarios': comentarios,
        'comentarios_count': comentarios_count,
        'promedio_rating': promedio_rating,
        'es_popular': es_popular
    })
from django.shortcuts import render, redirect
# Vista admin para panel de control (solo staff)
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_control(request):
    # Aquí podrías cargar datos relevantes si lo deseas
    return render(request, 'admin/admin_control.html')

from django.contrib.admin.views.decorators import staff_member_required
from apps.interactions.models import Review

# Vista admin para comentarios (solo staff)
@staff_member_required
def admin_comentarios(request):
    comentarios = Review.objects.select_related('game', 'user').all().order_by('-created_at')[:100]
    return render(request, 'admin/admin_comentarios.html', {'comentarios': comentarios})

# Vista admin para subir juegos
def admin_subir_juego(request):
    from .models import Category, Game
    categorias = Category.objects.all()
    mensaje = None
    error = None
    juego_guardado = None
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        nueva_categoria = (request.POST.get('new_category') or '').strip()
        descripcion_categoria = (request.POST.get('new_category_description') or '').strip()
        download_url = (request.POST.get('download_url') or '').strip()
        download_url_android = (request.POST.get('download_url_android') or '').strip()
        tags = request.POST.get('tags')
        estado = request.POST.get('estado')
        thumbnail = request.FILES.get('thumbnail')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        try:
            if nueva_categoria:
                categoria, creada = Category.objects.get_or_create(
                    name=nueva_categoria,
                    defaults={'description': descripcion_categoria}
                )
                # Fill description if category existed without one.
                if descripcion_categoria and not categoria.description:
                    categoria.description = descripcion_categoria
                    categoria.save(update_fields=['description'])
            else:
                categoria = Category.objects.get(id=category_id)

            juego = Game.objects.create(
                title=title,
                description=description,
                category=categoria,
                thumbnail=thumbnail,
                image1=image1,
                image2=image2,
                download_url=download_url or None,
                download_url_android=download_url_android or None
            )
            mensaje = 'Juego subido correctamente.'
            juego_guardado = juego
        except Exception as e:
            error = str(e)

    categorias = Category.objects.all().order_by('name')
    return render(request, 'admin/admin_subir_juego.html', {
        'categorias': categorias,
        'mensaje': mensaje,
        'error': error,
        'juego_guardado': juego_guardado
    })
from django.shortcuts import render

def portada(request):
    from .models import Game
    juegos_destacados = Game.objects.order_by('-created_at')[:3]
    juegos_recientes = Game.objects.order_by('-created_at')[:6]
    juegos_populares = Game.objects.order_by('-views_count', '-created_at')[:6]
    return render(request, 'dashboard/portada.html', {
        'juegos_destacados': juegos_destacados,
        'juegos_recientes': juegos_recientes,
        'juegos_populares': juegos_populares
    })

from django.core.paginator import Paginator
from .models import Game, Category
from django.db.models import Q, Avg

def busqueda_avanzada(request):
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    tags = request.GET.get('tags', '')
    exclude_tags = request.GET.get('exclude_tags', '')
    page_number = request.GET.get('page', 1)

    juegos = Game.objects.all()
    if query:
        juegos = juegos.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if categoria:
        juegos = juegos.filter(category__name__icontains=categoria)
    if tags:
        for tag in tags.split(','):
            juegos = juegos.filter(Q(title__icontains=tag.strip()) | Q(description__icontains=tag.strip()))
    if exclude_tags:
        for tag in exclude_tags.split(','):
            juegos = juegos.exclude(Q(title__icontains=tag.strip()) | Q(description__icontains=tag.strip()))

    paginator = Paginator(juegos.order_by('-created_at'), 12)
    page_obj = paginator.get_page(page_number)
    categorias = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'categorias': categorias,
        'query': query,
        'categoria': categoria,
        'tags': tags,
        'exclude_tags': exclude_tags,
        'total_resultados': paginator.count,
    }
    return render(request, 'dashboard/busqueda_avanzada.html', context)

def suscriptores(request):
    return render(request, 'dashboard/suscriptores.html')

def categoria(request):
    tipo = request.GET.get('tipo', '')
    juegos = []
    categoria_obj = None
    if tipo:
        categoria_obj = Category.objects.filter(name__iexact=tipo).first()
        if categoria_obj:
            juegos = Game.objects.filter(category=categoria_obj).order_by('-created_at')
    categorias = Category.objects.all()
    return render(request, 'dashboard/categoria.html', {
        'categoria_nombre': tipo,
        'categoria_obj': categoria_obj,
        'juegos': juegos,
        'categorias': categorias
    })

def suscripciones(request):
    return render(request, 'dashboard/suscripciones.html')

def redes(request):
    return render(request, 'dashboard/redes.html')
