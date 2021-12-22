from django import forms
from .models import CustomerInformation


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['addressName'].label = 'Nazwa adresu'

    class Meta:
        model = CustomerInformation
        fields = ('id', 'addressName', 'phone_number', 'email', 'street', 'city', 'zip_code', 'default')

    def save(self, commit=True, *args, **kwargs):
        user = kwargs.get('user', False)
        if user:
            self.instance.user = kwargs['user']
        return super().save(commit=commit)
