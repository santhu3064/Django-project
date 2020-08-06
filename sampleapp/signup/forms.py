from django import forms
from django.core.exceptions import ValidationError

from django.core.validators import MaxLengthValidator


def NameRegValidator(value):
    name = value[0].lower()
    if name != "l":
        raise ValidationError("Name not starting with l")


class Signup(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    # name = forms.CharField(max_length=100, required=True, validators=[NameRegValidator])
    email = forms.EmailField(max_length=255, required=True)
    verify_email = forms.EmailField(max_length=255, required=True, label="Confirm Email Address")
    comments = forms.CharField(widget=forms.Textarea)
    bot = forms.CharField(required=False, widget=forms.HiddenInput,
                          validators=[MaxLengthValidator(0, "Caught the bot")])

    def clean(self):
        signup_data = super().clean()

        email = signup_data['email']
        v_email = signup_data['verify_email']

        if email != v_email:
            raise ValidationError("Emails not matching")

    #
    #
    # def catchbot(self):
    #     bot = self.cleaned_data['bot']
    #     if len(bot) > 0:
    #         raise ValidationError("Got The Bot")
    #     return bot
