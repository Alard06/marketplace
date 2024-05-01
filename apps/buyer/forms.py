from django.contrib.auth.forms import UserCreationForm

from CustomUser.models import CustomUser


class RegisterBuyerForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'telephone_number',
                  'age',
                  'email',
                  'password1',
                  'password2']
