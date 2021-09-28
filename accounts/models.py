from django.conf import settings
#from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from .choices import JOB_CHOICES, FAMILY_AMOUNT_CHOICES, Q1_CHOICES, Q2_CHOICES, Q3_CHOICES, Q4_CHOICES, Q5_CHOICES, Q6_CHOICES, Q7_CHOICES, Q8_CHOICES, Q9_CHOICES, Q10_CHOICES, Q11_CHOICES, Q12_CHOICES, FOOD1_CHOICES, FOOD2_CHOICES, FOOD3_CHOICES, ITEM1_CHOICES, ITEM2_CHOICES, ITEM3_CHOICES


class Profile(models.Model):
    # 장고 3.x 에 추가된 기능
    class SexChoices(models.TextChoices):
        FEMALE = ("F", "여성")
        MALE = ("M", "남성")

    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,
        default=SexChoices.FEMALE,
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    age = models.CharField(max_length=3, db_column='customer_age')
    tel = models.CharField(max_length=11, db_column='customer_tel')
    address = models.CharField(max_length=200, db_column='customer_address')
    job = models.CharField(
        max_length=50,
        choices=JOB_CHOICES,
        default=1,
    )

    family_amount = models.PositiveIntegerField(
        choices=FAMILY_AMOUNT_CHOICES,
        default=1,
    )

# class SurveyQuestion(models.Model):
#     question = models.TextField(db_column='survey_question')

#     class Meta:
#         # managed = True
#         db_table = 'survey_question_content'


class Survey(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    q1 = models.CharField(
        max_length=50,
        choices=Q1_CHOICES,
        default=1,
    )

    q2 = models.CharField(
        max_length=50,
        choices=Q2_CHOICES,
        default=1,
    )

    q3 = models.CharField(
        max_length=50,
        choices=Q3_CHOICES,
        default=1,
    )

    q4 = models.CharField(
        max_length=50,
        choices=Q4_CHOICES,
        default=1,
    )

    q5 = models.CharField(
        max_length=50,
        choices=Q5_CHOICES,
        default=1,
    )

    q6 = models.CharField(
        max_length=50,
        choices=Q6_CHOICES,
        default=1,
    )

    q7 = models.CharField(
        max_length=50,
        choices=Q7_CHOICES,
        default=1,
    )

    q8 = models.CharField(
        max_length=50,
        choices=Q8_CHOICES,
        default=1,
    )

    q9 = models.CharField(
        max_length=50,
        choices=Q9_CHOICES,
        default=1,
    )

    q10 = models.CharField(
        max_length=50,
        choices=Q10_CHOICES,
        default=1,
    )

    q11 = models.CharField(
        max_length=50,
        choices=Q11_CHOICES,
        default=1,
    )

    q12 = models.CharField(
        max_length=50,
        choices=Q12_CHOICES,
        default=1,
    )

    mbti = models.CharField(max_length=4)


class FoodPrefer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    food1 = models.CharField(
        max_length=20,
        choices=FOOD1_CHOICES,
        default=1,
    )

    food2 = models.CharField(
        max_length=20,
        choices=FOOD2_CHOICES,
        default=1,
    )

    food3 = models.CharField(
        max_length=20,
        choices=FOOD3_CHOICES,
        default=1,
    )


class ItemPrefer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    item1 = models.CharField(
        max_length=20,
        choices=ITEM1_CHOICES,
        default=1,
    )

    item2 = models.CharField(
        max_length=20,
        choices=ITEM2_CHOICES,
        default=1,
    )

    item3 = models.CharField(
        max_length=20,
        choices=ITEM3_CHOICES,
        default=1,
    )

# survey클래스 안에 survey result랑 mbti의 기능이 모두 들어가도록 하고 싶음

# class SurveyResult(models.Model):

#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(
#         SurveyQuestion, on_delete=models.CASCADE)
#     response = models.CharField(max_length=100, db_column='survey_response')

#     class Meta:
#         # managed = True
#         db_table = 'survey_result'
#         # constraints = [
#         #     models.UniqueConstraint(
#         #         fields=["customer", "survey_question"],
#         #         name="uk_survey_result"

#         #     )

#         # ]

#     def __str__(self):
#         return self.customer.username


# class Mbti(models.Model):
#     survey_result = models.ForeignKey(SurveyResult, on_delete=models.CASCADE, db_column='survey_result')
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     mbti_code = models.CharField(max_length=4)

#     # class Meta:
#     #     # managed = True
#     #     db_table = 'mbti'
#     #     constraints = [
#     #         models.UniqueConstraint(
#     #             fields=["survey_result", "customer"],
#     #             name="uk_mbti"

#     #         )

#     #     ]

#     def __str__(self):
#         return self.customer.username
