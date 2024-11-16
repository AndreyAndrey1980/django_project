from .models import Product, Blog, Version, Category
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from django.utils.text import slugify
from .forms import ProductForm, VersionForm, ProductFormForModerator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.core.cache import cache


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
                product.current_user_mail = self.request.user.email
                if self.request.user.groups.filter(name="moders").exists():
                    product.current_user_is_moderator = True
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

    def get_form_class(self):
        user = self.request.user
        if user.email == self.object.user_email:
            return ProductForm
        elif self.request.user.groups.filter(name="moders").exists():
            return ProductFormForModerator
        else:
            raise PermissionDenied


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


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        category_list = None
        if settings.CACHE_ENABLED:
            # Проверяем включенность кеша
            key = 'category'  # Создаем ключ для хранения
            category_list = cache.get(key)  # Пытаемся получить данные
            print(f"результат кэша {category_list}")
            if category_list is None:
                # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
                category_list = Category.objects.all()
                cache.set(key, category_list, 60)
        else:
            # Если кеш не был подключен, то просто обращаемся к БД
            category_list = Category.objects.all()
        # Возвращаем результат
        return category_list

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
