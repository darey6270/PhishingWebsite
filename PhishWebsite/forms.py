from django import forms


class SearchForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control',
            'placeholder': 'E.g google.com'}))
