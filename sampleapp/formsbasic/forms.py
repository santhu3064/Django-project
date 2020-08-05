from django import forms


class Signup(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=255, required=True)
    comments = forms.CharField(widget=forms.Textarea)
