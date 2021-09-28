from django import forms
from django.forms import RadioSelect
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple, HiddenInput, SelectMultiple

from .models import Profile, Survey, FoodPrefer, ItemPrefer


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "sex",
            "age",
            "tel",
            "address",
            "job",
            "family_amount",
        ]
        widgets = {
            "job": RadioSelect,
            "family_amount": RadioSelect,
        }


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            "q1",
            "q2",
            "q3",
            "q4",
            "q5",
            "q6",
            "q7",
            "q8",
            "q9",
            "q10",
            "q11",
            "q12",
        ]
        widgets = {
            "q1": RadioSelect,
            "q2": RadioSelect,
            "q3": RadioSelect,
            "q4": RadioSelect,
            "q5": RadioSelect,
            "q6": RadioSelect,
            "q7": RadioSelect,
            "q8": RadioSelect,
            "q9": RadioSelect,
            "q10": RadioSelect,
            "q11": RadioSelect,
            "q12": RadioSelect,
        }


class FoodPreferForm(forms.ModelForm):
    class Meta:
        model = FoodPrefer
        fields = [
            "food1",
            "food2",
            "food3",
        ]
        widgets = {
            "food1": RadioSelect,
            "food2": RadioSelect,
            "food3": RadioSelect,
        }


class ItemPreferForm(forms.ModelForm):
    class Meta:
        model = ItemPrefer
        fields = [
            "item1",
            "item2",
            "item3",
        ]
        widgets = {
            "item1": RadioSelect,
            "item2": RadioSelect,
            "item3": RadioSelect,
        }
