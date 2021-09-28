from django.contrib import admin

from .forms import ProfileForm, SurveyForm, FoodPreferForm, ItemPreferForm
from .models import Profile, Survey, FoodPrefer, ItemPrefer


# admin 내부적으로 Form을 생성해서 사용

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ['user']


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    form = SurveyForm
    list_display = ['user', 'q1', 'q2', 'q3', 'q4', 'q5',
                    'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']
    #form = SurveyForm


@admin.register(FoodPrefer)
class FoodPreferAdmin(admin.ModelAdmin):
    form = FoodPreferForm
    list_display = ['user', 'food1', 'food2', 'food3']


@admin.register(ItemPrefer)
class ItemPreferAdmin(admin.ModelAdmin):
    form = ItemPreferForm
    list_display = ['user', 'item1', 'item2', 'item3']
