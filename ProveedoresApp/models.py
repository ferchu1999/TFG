from django.db import models
from django.utils.text import slugify

# Create your models here.


class categorias(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria Proveedores'
        verbose_name_plural = 'Categorias Proveedores'

    def __str__(self):
        return self.nombre


class proveedoresModel(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    slug = models.SlugField(max_length=15, unique=True,
                            blank=True, auto_created=True)
    direccion = models.CharField(max_length=100)
    tfno = models.CharField(max_length=12)
    email = models.EmailField(verbose_name='Correo electronico')
    web = models.URLField(verbose_name='Página web', null=True)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    productos = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)
    img_proveedor = models.ImageField(
        upload_to='proveedores/imgs', default='proveedores/default.png', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['created']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(proveedoresModel, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(proveedoresModel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    nombre = models.CharField(max_length=80, null=True)
    comentario = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.nombre} on {self.comentario}'
