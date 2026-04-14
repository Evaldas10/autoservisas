from .models import Car, CarComment, Order
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Car, CarMake, CarModel


class CarCommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields = ['content']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class OrderInstanceCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'reader', 'due_back', 'status']
        widgets = {"due_back": forms.DateInput(attrs={'type': "date"})}


class CarRegisterForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "license_plate", "phone", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = CarModel.objects.none()

        if 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['model'].queryset = CarModel.objects.filter(
                    make_id=make_id)
            except:
                pass
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.make.carmodel_set.all()
