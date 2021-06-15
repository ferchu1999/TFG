from django.db import models
from django.utils.text import slugify


# Create your models here.


class categoria_empresa(models.Model):
    categoria = models.CharField(
        verbose_name='Nombre de la categoria', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Categoria Empresa'
        verbose_name_plural = 'Categorias Empresa'

    def __str__(self):

        return self.categoria


class empresa(models.Model):

    TIPO_EMPRESA = (
        ('pequeña empresa', 'Pequeña Empresa'), ('mediana empresa', 'Mediana Empresa')
    )

    nombre = models.CharField(
        verbose_name='Nombre de la empresa', max_length=50, db_index=True)
    ciudad = models.CharField(max_length=50)
    slug = models.SlugField(max_length=15, unique=True,
                            blank=True, auto_created=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=100)
    codigoPostal = models.CharField(verbose_name='Código Postal', max_length=5)
    tfno = models.CharField(verbose_name='Numero de telefono', max_length=9)
    email = models.EmailField(verbose_name='Correo electronico')
    logo_empresa = models.ImageField(
        verbose_name='Logo de la empresa', upload_to='empresas/logos', default='empresas/default.png')
    categoria = models.ManyToManyField(categoria_empresa)
    descripcion = models.TextField(max_length=255)
    tipo_empresa = models.CharField(
        verbose_name='Tipo de Empresa', max_length=255, choices=TIPO_EMPRESA, blank=True)
    CIF = models.CharField(max_length=15, unique=True, blank=True)
    web = models.URLField(verbose_name='Pagina web', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['created']

    def __str__(self):

        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(empresa, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(empresa,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
