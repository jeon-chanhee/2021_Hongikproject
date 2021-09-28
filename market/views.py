import re
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import permission_required, login_required

# csv 업로드 할 때 필요한 import
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from market.models import Recommendation,Product
import pandas as pd
import numpy as np
import csv
import io
from accounts.models import Profile
from accounts.forms import ProfileForm


# 추천 시스템에 필요한 라이브러리
from sklearn.neighbors import NearestNeighbors
import pymysql
from sqlalchemy import create_engine


def main(request):
    return render(request, "market/main.html")

logout = LogoutView.as_view()

login = LoginView.as_view(
    template_name="market/login_form.html",
    success_url="market"
)

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="market/signup_form.html",
    success_url=settings.LOGIN_URL,
)


@login_required
def profile(request):
    return render(request, "market/profile.html")


@login_required
def profile_edit(request):
    # 현재 유저 (request.user)에 대한 Profile

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

    return render(request, "market/profile_form.html", {
        "form": form,
    })




# db를 삽입
@permission_required('admin.can_add_log_entry')
def insert_user(request):
    # 해당 내용을 실행할 template 지정
    template = 'market/insert_user.html'

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

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context)

# db를 삽입
@permission_required('admin.can_add_log_entry')
def insert_db(request):
    # 해당 내용을 실행할 template 지정
    template = 'market/insert_db.html'

    prompt = {
        'order': 'DB 파일을 업로드해주세요.'
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
        _, c = Recommendation.objects.update_or_create(
            id=column[0],
            person=column[0],
            sex=column[2],
            age=column[3],
            job=column[4],
            family_amount=column[5],
            food1=column[6],
            food2=column[7],
            food3=column[8],
            item1=column[9],
            item2=column[10],
            item3=column[11],
            mbti=column[12],
        )
    # except:
        #messages.error(request,'데이터 입력오류')
        # return redirect(reversed("list"))

    prompt2 = {
        'order2': '업로드가 완료되었습니다.'
    }

    context = {}  # 빈 {dict} 이라도 채웁니다
    return render(request, template, context, prompt2)

# db에 있는 데이터 갖고오기
def make_data():
    aws_mariadb_url = "mysql+pymysql://root:0313@localhost:3306/market"
    engine_mariadb = create_engine(aws_mariadb_url)

    db_file = "recommendation"
    template = 'market/output.html'

    data = pd.read_sql_table(table_name=db_file, con=engine_mariadb)

    return data


def make_data_columns():
    aws_mariadb_url = "mysql+pymysql://root:0313@localhost:3306/market"
    engine_mariadb = create_engine(aws_mariadb_url)

    db_file = "recommendation"
    template = 'market/output.html'

    data = pd.read_sql_table(table_name=db_file, con=engine_mariadb)

    return data.columns.tolist()

# 데이터 전처리 후 
def similar_df():

    aws_mariadb_url = "mysql+pymysql://root:0313@localhost:3306/market"
    engine_mariadb = create_engine(aws_mariadb_url)

    db_file = "recommendation"
    template = 'market/output.html'

    datas = pd.read_sql_table(table_name=db_file, con=engine_mariadb)

    onehot_food1 = pd.get_dummies(datas['recom_food1'])
    onehot_food2 = pd.get_dummies(datas['recom_food2'])
    onehot_food3 = pd.get_dummies(datas['recom_food3'])
    onehot_thing1 = pd.get_dummies(datas['recom_item1'])
    onehot_thing2 = pd.get_dummies(datas['recom_item2'])
    onehot_thing3 = pd.get_dummies(datas['recom_item3'])
    onehot_job = pd.get_dummies(datas['recom_job'])

    onehot_food12 = onehot_food1.add(onehot_food2, fill_value=0, axis=1)
    onehot_food123 = onehot_food12.add(onehot_food3, fill_value=0, axis=1)

    onehot_thing12 = onehot_thing1.add(onehot_thing2, fill_value=0, axis=1)
    onehot_thing123 = onehot_thing12.add(onehot_thing3, fill_value=0, axis=1)

    test_df = pd.concat([onehot_food123, onehot_thing123], axis=1)

    test_df2 = pd.concat([onehot_job, test_df], axis=1)
    test_df2 = test_df2.astype('int')

    test = datas[['id', 'recom_sex', 'recom_age',
                  'recom_family_amount', 'recom_mbti']]

    test_total = pd.concat([test, test_df2], axis=1)

    train = test_total

    # 여성을 1로 남성을 0으로 두고, 몇몇 데이터를 float형으로 선언
    tmp = []
    for each in train['recom_sex']:
        if each == 'F':
            tmp.append(1)
        elif each == 'M':
            tmp.append(0)
        else:
            tmp.append(np.nan)

    train['recom_sex'] = tmp

    from sklearn.preprocessing import LabelEncoder
    from keras.utils import np_utils

    encoder = LabelEncoder()

    encoder.fit(train['recom_mbti'])
    mbti_encodered = encoder.transform(train['recom_mbti'])
    train['recom_mbti'] = mbti_encodered

    df = train.copy()
    df = df.drop('id', axis=1)
    df_col = df.columns.tolist()

    from sklearn.preprocessing import RobustScaler

    transformer = RobustScaler()
    transformer.fit(df)
    df = transformer.transform(df)
    df = pd.DataFrame(df)

    # 추천알고리즘
    tr = train[['id']].dropna()

    from sklearn.neighbors import NearestNeighbors

    NUM_RECOM = 3

    X = df.dropna().values
    nbrs = NearestNeighbors(n_neighbors=NUM_RECOM+1,
                            algorithm='ball_tree').fit(X)
    dist, rank = nbrs.kneighbors(X)

    similar_df = pd.DataFrame(columns=[f'rank_{i}'for i in range(1, NUM_RECOM+1)],
                              index=tr['id'].values,
                              data=rank[:, 1:])

    for cols in list(similar_df):
        tg_col = similar_df[cols]
        new_value = tr['id'].iloc[tg_col].tolist()
        similar_df[cols] = new_value

    return similar_df, train

# 사용자유사도에 따른 추천 기능 구현 및 가장 유사한 유저 추출 후 리스트화 시키기
def similar_user(user_id):

    df, train = similar_df()
    df_col = make_data_columns()
    datas = make_data()
    rec_df = pd.DataFrame(columns=df_col)

    for i, user in enumerate(df.loc[user_id]):
        rec_df = rec_df.append(
            train.loc[train['id'] == user], ignore_index=True)

    final = pd.merge(datas, rec_df, how='right', on='id')
    final = final[['id', 'recom_sex_x', 'recom_age_x', 'recom_job_x', 'recom_family_amount_x', 'recom_mbti_x',
                   'recom_food1_x', 'recom_food2_x', 'recom_food3_x', 'recom_item1_x', 'recom_item2_x', 'recom_item3_x']]
    final_num1 = final.iloc[0, :].tolist()

    return final_num1


def product_image(Httprequest):
    image = Product.objects.all()
    final_num1 = similar_user()


    for i in range (6,12):
        if final_num1[i] == image.name:
            print(image.photo)

# 유저가 선호하는 음식 및 물품 출력하기
@login_required
def recom_user(request):
    recom = Recommendation.objects.get(person=request.user.id)
    similar = similar_user(request.user.id)
    user = request.user
    product = Product.objects.all()
    food_name, food_num = chart_bar_food(request.user.id)
    item_name, item_num = chart_bar_item(request.user.id)
    return render(request,
                  "market/recom_user.html",
                  {
                      'user': user,
                      'recom': recom,
                      'similar': similar,
                      'product': product,
                      'food_list': similar[6:9],
                      'item_list': similar[9:12],
                      'food_name':food_name,
                      'food_num':food_num,
                      'item_name':item_name,
                      'item_num':item_num,
                  }
                  )


# 유저가 속한 mbti의 음식 그래프로 구현하기
def chart_bar_food(user_id):

    similar = similar_user(user_id)
    user_mbti = similar[5]
    aws_mariadb_url = "mysql+pymysql://root:0313@localhost:3306/market"
    engine_mariadb = create_engine(aws_mariadb_url)

    db_file = "recommendation"


    df = pd.read_sql_table(table_name=db_file, con=engine_mariadb)
    
    # Food1,2,3 컬럼명 변경 후 concat 활용해서 하나로 묶기
    df_food1 = df[['recom_mbti','recom_food1']]
    df_food1 = df_food1.rename(columns={'recom_food1':'Food'})

    df_food2 = df[['recom_mbti','recom_food2']]
    df_food2 = df_food2.rename(columns={'recom_food2':'Food'})

    df_food3 = df[['recom_mbti','recom_food3']]
    df_food3 = df_food3.rename(columns={'recom_food3':'Food'})
    
    food_total = [df_food1,df_food2,df_food3]
    food_mbti_sort = pd.concat(food_total)
    
    food_mbti_sort['Num'] = 0

    # Mbti별 음식 개수 세기
    df_food = food_mbti_sort.groupby(['recom_mbti','Food'])['Num'].count()
    df_food = pd.DataFrame(df_food)

    df_food = df_food.reset_index()

    df_food = df_food[df_food['recom_mbti'] == user_mbti]

    df_food = df_food.sort_values(by=["Num"], ascending=[False]) 
        
    food_name = df_food['Food'].tolist()
    food_num = df_food['Num'].tolist()

    

    return food_name,food_num

# 유저가 속한 mbti의 물건 그래프로 구현하기
def chart_bar_item(user_id):

    similar = similar_user(user_id)
    user_mbti = similar[5]
    aws_mariadb_url = "mysql+pymysql://root:0313@localhost:3306/market"
    engine_mariadb = create_engine(aws_mariadb_url)

    db_file = "recommendation"


    df = pd.read_sql_table(table_name=db_file, con=engine_mariadb)
    
    # Food1,2,3 컬럼명 변경 후 concat 활용해서 하나로 묶기
    df_item1 = df[['recom_mbti','recom_item1']]
    df_item1 = df_item1.rename(columns={'recom_item1':'Item'})

    df_item2 = df[['recom_mbti','recom_item2']]
    df_item2 = df_item2.rename(columns={'recom_item2':'Item'})

    df_item3 = df[['recom_mbti','recom_item3']]
    df_item3 = df_item3.rename(columns={'recom_item3':'Item'})
    
    item_total = [df_item1,df_item2,df_item3]
    item_mbti_sort = pd.concat(item_total)
    
    item_mbti_sort['Num'] = 0

    # Mbti별 음식 개수 세기
    df_item = item_mbti_sort.groupby(['recom_mbti','Item'])['Num'].count()
    df_item = pd.DataFrame(df_item)

    df_item = df_item.reset_index()

    df_item = df_item[df_item['recom_mbti'] == user_mbti]

    df_item = df_item.sort_values(by=["Num"], ascending=[False]) 
        
    item_name = df_item['Item'].tolist()
    item_num = df_item['Num'].tolist()

    

    return item_name,item_num    