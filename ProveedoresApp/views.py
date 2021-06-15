from django.shortcuts import render, get_object_or_404, redirect
from .models import proveedoresModel, categorias
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm, crearProveedor

# Create your views here.


def proveedores(request):
    queryset = request.GET.get("buscar")
    if queryset:
        proveedor = proveedoresModel.objects.filter(
            Q(ciudad__icontains=queryset) |
            Q(nombre__icontains=queryset)).distinct()

    proveedor = proveedoresModel.objects.all()

    paginator = Paginator(proveedor, 4)

    page = request.GET.get('page')

    proveedor = paginator.get_page(page)

    return render(request, 'proveedores/proveedores.html', {'proveedores': proveedor})


def proveedores_slug(request, slug_proveedor):
    post = get_object_or_404(proveedoresModel, slug=slug_proveedor)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.active = True
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'proveedores/listar_proveedores.html',
                  {'slugs': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def crear_proveedores(request):
    if request.method == 'POST':
        form_proveedores = crearProveedor(
            data=request.POST, files=request.FILES)

        if form_proveedores.is_valid():
            form_proveedores.save()
            return redirect('/altaproveedores/?valido')

        else:
            return redirect('/altaproveedores/?error')

    else:
        form_proveedores = crearProveedor()

    return render(request, 'proveedores/crear_proveedor.html', {'form_proveedor': form_proveedores})
