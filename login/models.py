from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
 
class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            birth=birth,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, nickname,birth, password):
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
            birth=birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#원래 User모델은 AbstractUser라는 애를 상속받고 있음
#AbstractUser이 더 큰 부모이기 떄문에 그녀석을 가져다가 쓸것임
#AbstractUser에 대한 정보는 아래 페이지
#https://github.com/django/django/blob/1.10.5/django/contrib/auth/models.py#L300
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=50,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name='nickname',
        max_length=20,
        blank=False,
        unique=True,
        help_text='한글가능',
    )
    birth = models.DateField(
        verbose_name='birth',
        max_length=50,
        blank=False,
        unique=False,
        help_text='반드시 양식을 지켜주세요',
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
    objects = MyUserManager()
 
    USERNAME_FIELD = 'email'    # When username is required, You must use this field!
    REQUIRED_FIELDS = ['nickname','birth']
 
    def get_full_name(self):
        # The user is identified by their email address
        return self.email
 
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
 
    def __str__(self):              # __unicode__ on Python 2
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

##로그아웃 유저를 표현할 파이썬 클래스 (NOT 모델)
class AnonymouseUser:
    id = None
    pk = None
    nickname = ''
    is_staff = False
    birth = ''


class ActList(models.Model):
    actId = models.ForeignKey(MyUser)
    actNum = models.CharField(
        max_length=15,
        verbose_name='계좌번호',
        null=False,
        blank=False,
        unique=True,
    )
    actName = models.CharField(
        max_length=20,
        verbose_name='통장이름',
        null=False,
        blank=False,
    )
    actSummary = models.CharField(
        max_length=50,
        verbose_name='한줄설명',
        null=True,
        blank=False,
    )
    actInfo = models.TextField(
        max_length=50,
        verbose_name='통장정보',
        null=False,
        blank=True,
    )
    def __str__(self):
       return "'{}'의 '{}'".format(self.actId, self.actName)

'''
class Account(models.Model):
    actName = models.ForeignKey(ActList)
    actDate = models.DateField(
        verbose_name='날짜',
        null=False,
        )
    actIncome = models.BooleanField(
        verbose_name='수입'
        default=False,
        )
    actConsumption = models.BooleanField(
        verbose_name='지출'
        default=False,
        )

    actPrice = models.IntegerField(
        verbose_name='금액',
        max_length=10,
        )
    actCash = models.BooleanField(
        verbose_name='현금'
        default=False,
        )
    actCard = models.BooleanField(
        verbose_name='카드'
        default=False,
        )    
'''
