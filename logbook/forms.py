__author__ = 'johanna'
from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from logbook.models import Journey

class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = ('main_image','image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'title', 'city', 'country', 'from_date',
                  'to_date', 'summary', 'description', 'marker_symbol', 'marker_color')

class TravellerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
