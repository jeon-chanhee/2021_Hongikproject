from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from accounts.forms import ProfileForm, SurveyForm, FoodPreferForm, ItemPreferForm
from accounts.models import Profile, Survey, FoodPrefer, ItemPrefer

import csv
import io

# csv 업로드 할 때 필요한 import
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.contrib.auth.models import User
import pandas as pd


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/signup_form.html",
    success_url=settings.LOGIN_URL,
)


login = LoginView.as_view(
    template_name="accounts/login_form.html"
)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def profile_edit(request):
    # 현재 유저 (request.user)에 대한 Profile이 있을 수도 있고, 없을 수도 있어요.

    # request.user.profile

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile_form.html", {
        "form": form,
    })


@login_required
def survey(request):
    try:
        survey = Survey.objects.get(user=request.user)
    except Survey.DoesNotExist:
        survey = None

    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES, instance=survey)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            from collections import Counter
            mbti_ei = survey.q1 + survey.q5 + survey.q6
            mbti_sn = survey.q4 + survey.q7 + survey.q8
            mbti_tf = survey.q9 + survey.q11 + survey.q12
            mbti_jp = survey.q2 + survey.q3 + survey.q10
            counter1 = Counter(mbti_ei)
            counter2 = Counter(mbti_sn)
            counter3 = Counter(mbti_tf)
            counter4 = Counter(mbti_jp)
            survey.mbti = max(mbti_ei, key=counter1.get)+max(mbti_sn, key=counter2.get) + \
                max(mbti_tf, key=counter3.get)+max(mbti_jp, key=counter4.get)
            survey.save()
            return redirect("survey")
    else:
        form = SurveyForm(instance=survey)

    return render(request, "accounts/survey_form.html", {
        "form": form,
    })


@login_required
def foodprefer(request):
    try:
        foodprefer = FoodPrefer.objects.get(user=request.user)
    except FoodPrefer.DoesNotExist:
        foodprefer = None

    if request.method == "POST":
        form = FoodPreferForm(request.POST, request.FILES, instance=foodprefer)
        if form.is_valid():
            foodprefer = form.save(commit=False)
            foodprefer.user = request.user
            foodprefer.save()
            return redirect("foodprefer")
    else:
        form = FoodPreferForm(instance=foodprefer)

    return render(request, "accounts/foodprefer_form.html", {
        "form": form,
    })


@login_required
def itemprefer(request):
    try:
        itemprefer = ItemPrefer.objects.get(user=request.user)
    except ItemPrefer.DoesNotExist:
        itemprefer = None

    if request.method == "POST":
        form = ItemPreferForm(request.POST, request.FILES, instance=itemprefer)
        if form.is_valid():
            itemprefer = form.save(commit=False)
            itemprefer.user = request.user
            itemprefer.save()
            return redirect("itemprefer")
    else:
        form = ItemPreferForm(instance=itemprefer)

    return render(request, "accounts/itemprefer_form.html", {
        "form": form,
    })


@permission_required('admin.can_add_log_entry')
def insert_profile(request):
    # 해당 내용을 실행할 template 지정
    template = 'accounts/insert_profile.html'

    prompt = {
        'order': 'get 방식으로 입력시 오류처리'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    # 오류처리2 : CSV 파일이 아닌경우 오류처리
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'CSV 가 아닙니다.')
        return None

    # 오류처리1, 2를 통과한 경우 내용의 적용
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # io_string 내용을 차례로 호출

    # try:
    for column in csv.reader(io_string,
                             delimiter=',', quotechar="|"):
        _, c = Profile.objects.update_or_create(
            user_id=column[0],
            sex=column[2],
            age=column[3],
            job=column[4],
            family_amount=column[5],
        )
    # except:
        #messages.error(request,'데이터 입력오류')
        # return redirect(reversed("list"))

    prompt2 = {
        'order2': '업로드가 완료되었습니다.'
    }

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context, prompt2)


@permission_required('admin.can_add_log_entry')
def insert_user(request):
    # 해당 내용을 실행할 template 지정
    template = 'accounts/insert_profile.html'

    prompt = {
        'order': '파일을 업로드하세요.'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    # 오류처리2 : CSV 파일이 아닌경우 오류처리
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'CSV 가 아닙니다.')
        return None

    # 오류처리1, 2를 통과한 경우 내용의 적용
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # io_string 내용을 차례로 호출

    # try:
    for column in csv.reader(io_string,
                             delimiter=',', quotechar="|"):
        _, c = User.objects.update_or_create(
            id=column[0],
            password=column[1],
            username=column[2],
        )
    # except:
        #messages.error(request,'데이터 입력오류')
        # return redirect(reversed("list"))
    prompt2 = {
        'order2': '업로드가 완료되었습니다.'
    }

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context, prompt2)


@permission_required('admin.can_add_log_entry')
def insert_food(request):
    # 해당 내용을 실행할 template 지정
    template = 'accounts/insert_food.html'

    prompt = {
        'order': '파일을 업로드하세요.'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    # 오류처리2 : CSV 파일이 아닌경우 오류처리
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'CSV 가 아닙니다.')
        return None

    # 오류처리1, 2를 통과한 경우 내용의 적용
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # io_string 내용을 차례로 호출

    # try:
    for column in csv.reader(io_string,
                             delimiter=',', quotechar="|"):
        _, c = FoodPrefer.objects.update_or_create(
            user_id=column[0],
            food1=column[6],
            food2=column[7],
            food3=column[8],
        )
    # except:
        #messages.error(request,'데이터 입력오류')
        # return redirect(reversed("list"))
    prompt2 = {
        'order2': '업로드가 완료되었습니다.'
    }

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context, prompt2)


@permission_required('admin.can_add_log_entry')
def insert_item(request):
    # 해당 내용을 실행할 template 지정
    template = 'accounts/insert_food.html'

    prompt = {
        'order': '파일을 업로드하세요.'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    # 오류처리2 : CSV 파일이 아닌경우 오류처리
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'CSV 가 아닙니다.')
        return None

    # 오류처리1, 2를 통과한 경우 내용의 적용
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)  # io_string 내용을 차례로 호출

    # try:
    for column in csv.reader(io_string,
                             delimiter=',', quotechar="|"):
        _, c = ItemPrefer.objects.update_or_create(
            user_id=column[0],
            item1=column[9],
            item2=column[10],
            item3=column[11],
        )
    # except:
        #messages.error(request,'데이터 입력오류')
        # return redirect(reversed("list"))
    prompt2 = {
        'order2': '업로드가 완료되었습니다.'
    }

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context, prompt2)
