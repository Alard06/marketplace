from django import forms


class SenderForm(forms.Form):

    last_name = forms.CharField(max_length=50,
                                required=True,
                                label='Фамилия')
    first_name = forms.CharField(max_length=50,
                                 required=True,
                                 label='Имя')
    patronymic = forms.CharField(max_length=50,
                                 required=True,
                                 label='Отчество')
    inn = forms.CharField(max_length=50,
                          required=True,
                          label='ИНН')
    phone_number = forms.CharField(max_length=11,
                                   required=True,
                                   label='Номер телефона')
    name = forms.CharField(max_length=50,
                           required=True,
                           label='Название магазина')
    description = forms.CharField(max_length=500,
                                  label='Дополнительно')