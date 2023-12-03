from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.views import View
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import ProfileUpdateForm
from django.shortcuts import render
from .models import Product
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Возвращает текущего пользователя как объект для редактирования
        return self.request.user
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Дополнительные действия, которые вы можете выполнить перед выходом,
        # если это необходимо.

        logout(request)
        return redirect('home')
class ProfileView(TemplateView):
    template_name = 'profile.html'
class RegisterView(FormView):
    template_name = 'register.html'  # Указывайте свой путь к шаблону
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Перенаправление после успешной регистрации

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Если пользователь уже аутентифицирован, перенаправьте его на главную страницу
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
class CustomLoginView(LoginView):
    template_name = 'login.html'
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

@login_required
def cart(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'cart.html', {'orders': orders})

@login_required
@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=user)

    # Проверяем, есть ли продукт уже в корзине
    if product not in order.products.all():
        order.products.add(product)
        order.total_price += product.price
        order.save()

    return redirect('cart')


from django.shortcuts import get_object_or_404


@login_required
def remove_from_cart(request, order_id, product_id):
    order = get_object_or_404(Order, pk=order_id)
    product = get_object_or_404(Product, pk=product_id)

    # Проверка, что продукт действительно находится в корзине перед удалением
    if product in order.products.all():
        order.products.remove(product)
        order.total_price -= product.price
        order.save()

    return redirect('cart')
