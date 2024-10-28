from django.shortcuts import render
from .models import Product, Category, Blog, Version
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from django.utils.text import slugify
from .forms import ProductForm, VersionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return self.model.objects.filter(publicate=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for i in range(0, len(context['object_list'])):
            product = context['object_list'][i]
            try:
                current_versions = Version.objects.filter(product=product, is_current=True)
                actual_version = current_versions[len(current_versions) - 1]
                print(actual_version)
                product.actual_version = actual_version
            except Exception:
                product.actual_version = {}

        return context


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class GetContact(TemplateView):
    template_name = "contact.html"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Product
    success_url = reverse_lazy('catalog:list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Product
    success_url = reverse_lazy('catalog:list')
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.slug = slugify(product.name)
            product.user_email = self.request.user.email
            product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Product
    success_url = reverse_lazy('catalog:list')
    form_class = ProductForm


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return self.model.objects.filter(publicate=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('catalog:blog_list')


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Version
    success_url = reverse_lazy('catalog:list')


class VersionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Version
    success_url = reverse_lazy('catalog:list')
    form_class = VersionForm


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'
    model = Version
    success_url = reverse_lazy('catalog:list')
    form_class = VersionForm

# def get_contact_info(request):
#    return render(request, "catalog/contact.html", {})


# def detail(request, product_id):
#    try:
#        product = Product.objects.get(id=product_id)
#    except Product.DoesNotExist:
#        raise Http404("Product does not exist")
#    context = {"product": product}
#    return render(request, "catalog/product_detail.html", context)


# def index(request):
#    products = Product.objects.all()
#    return render(request, "catalog/product_list.html", {"products": products})
