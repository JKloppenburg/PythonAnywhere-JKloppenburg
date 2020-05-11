from django import forms
from django.core.validators import RegexValidator


#def check_size(value):
#    if len(value) < 6:
#        raise forms.ValidationError("Je naam is te kort")

class ContactForm(forms.Form):
#    name = forms.CharField(label='Naam', required = True, max_length = 100, validators = [check_size, ], widget=forms.TextInput(attrs={'placeholder': 'Naam'}))
    name = forms.CharField(label='Naam', required = True, max_length = 100, validators = [RegexValidator('^[a-zA-Z ]+$', message="Je naam kan alleen uit letters bestaan")], widget=forms.TextInput(attrs={'placeholder': 'Je naam'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email adres waarmee ik met jou in contact kan komen'}),required = True)
    message = forms.CharField(label='Bericht', required = True, widget=forms.Textarea(attrs={'placeholder': 'Hier kan je een bericht achterlaten'}))

