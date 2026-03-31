from django.shortcuts import render
from .models import Car, Order, OrderLine, Service
from django.views import generic
from django.core.paginator import Paginator  # importuojamas puslapiavimui
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Car, CarComment
from .forms import CarCommentForm
from django.shortcuts import render, redirect
from .forms import UserChangeForm  # vartotojo duomenu keitimas
from .forms import CustomUserCreateForm


def get_visit_count(request):
    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1
    return num_visits


def index(request):
    num_visits = get_visit_count(request)
    num_car = Car.objects.count()
    num_order = Order.objects.count()
    num_orderLine = OrderLine.objects.count()
    num_service = Service.objects.filter(price="5").count()

    cars = Car.objects.all()
    orders = Order.objects.all()
    services = Service.objects.all()

    my_context = {
        "num_car": num_car,
        "num_order": num_order,
        "num_orderLine": num_orderLine,
        "num_service": num_service,
        "cars": cars,
        "orders": orders,
        "service": services,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=my_context)


def about(request):
    return render(request, template_name="about.html")


def cars(request):
    num_visits = get_visit_count(request)
    cars = Car.objects.all()
    paginator = Paginator(cars, per_page=2)  # padaromas puslapiavimas
    page_number = request.GET.get("page")
    paged_cars = paginator.get_page(page_number)
    context = {
        "cars": paged_cars,
        "num_visits": num_visits,
    }

    return render(request, template_name="cars.html", context=context)


def car(request, car_pk):
    num_visits = get_visit_count(request)
    car = Car.objects.get(pk=car_pk)
    order = Order.objects.filter(car=car).last()
    order_lines = OrderLine.objects.filter(order=order)

    # --- KOMENTARO IŠSAUGOJIMAS ---
    if request.method == "POST":
        form = CarCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.client = request.user
            comment.save()
            return redirect("car", car_pk=car.pk)
    else:
        form = CarCommentForm()

    context = {
        "car": car,
        "order": order,
        "num_visits": num_visits,
        "order_lines": order_lines,
        "form": form,
    }
    return render(request, "car.html", context)


class OrderListView(generic.ListView):

    model = Order
    template_name = "orders.html"
    context_object_name = "orders"
    paginate_by = 2  # kiek puslapyje bus rodoma objiektu


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"


# pajieska


def search(request):
    num_visits = get_visit_count(request)
    query = request.GET.get("query")
    context = {
        "car_search_results": Car.objects.filter(make__icontains=query)
    }

    context = {
        "num_visits": num_visits,
    }

    return render(request, template_name="search.html", context=context)


class MyCarInstanceListView(LoginRequiredMixin, generic.ListView):

    model = Order
    template_name = "my_cars.html"
    context_object_name = "instances"

    def get_queryset(self):
        return Order.objects.filter(reader=self.request.user)

# vartotojo registracija


class SingUp(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = "singup.html"
    success_url = reverse_lazy("login")


# profilio redagavimas

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserChangeForm
    template_name = "profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
