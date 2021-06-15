from django.shortcuts import render, redirect, get_object_or_404
from .forms import crearEmpresa, CommentForm
from .models import empresa, Comment
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def empresas(request):

    queryset = request.GET.get("buscar")
    if queryset:
        empresas = empresa.objects.filter(
            Q(ciudad__icontains=queryset) |
            Q(nombre__icontains=queryset)).distinct()

    empresas = empresa.objects.all()

    paginator = Paginator(empresas, 4)

    page = request.GET.get('page')

    empresas = paginator.get_page(page)

    return render(request, 'empresas/empresas.html', {'empresas': empresas})


def empresas_slug(request, slug_empresa):
    post = get_object_or_404(empresa, slug=slug_empresa)
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

    return render(request, 'empresas/listar_empresas.html',
                  {'slugs': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def crear_empresa(request):
    if request.method == 'POST':
        form_crearEmpresa = crearEmpresa(
            data=request.POST, files=request.FILES)
        if form_crearEmpresa.is_valid():
            form_crearEmpresa.save()
            return redirect('/añadirempresa/?valido')

        else:
            return redirect('/añadirempresa/?error')

    else:
        form_crearEmpresa = crearEmpresa()

    return render(request, 'empresas/crear_empresa.html', {'form_empresa': form_crearEmpresa})
