from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'post_categories')
    list_display = ('title', 'author', 'published') # para mostrar las columnas en el admin
    ordering = ('author', 'published') # para ordenar las entradas por autor y fecha
    search_fields = ('title', 'content', 'author__username') # Agregar un campo de busqueda. Importante agregar username que es un campo de la tabla users
    list_filter = ('author__username', 'categories__name')  

    def post_categories(self, obj):
        return ",".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)