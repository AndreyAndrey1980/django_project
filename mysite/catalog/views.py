from django.shortcuts import render
from .models import Product, Category, Blog
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from django.utils.text import slugify

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return self.model.objects.filter(publicate=True)


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class GetContact(TemplateView):
    template_name = "contact.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:list')




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


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('catalog:blog_list')

# def get_contact_info(request):
#    return render(request, "catalog/contact.html", {})


#def detail(request, product_id):
#    try:
#        product = Product.objects.get(id=product_id)
#    except Product.DoesNotExist:
#        raise Http404("Product does not exist")
#    context = {"product": product}
#    return render(request, "catalog/product_detail.html", context)


#def index(request):
#    products = Product.objects.all()
#    return render(request, "catalog/product_list.html", {"products": products})