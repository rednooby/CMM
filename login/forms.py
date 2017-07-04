from django import forms
from .models import MyUser, ActList, BankBook, ActBoard
from django.contrib.auth.forms import ReadOnlyPasswordHashField


#Form 처리: GET(입력폼을 보여줌), POST(데이터를 입력받아 유효성검증, 성공시 저장후 SUCCESS URL로 이동, 실패시 오류메시지와 입력폼을 다시 보여줌)
#검증이 통과한 값들은 사전 타입으로 제공되며 그것이 Cleaned_data임


class UserCreationForm(forms.ModelForm): #모델폼 사용
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
 
    class Meta:
        model = MyUser
        fields = ('email', 'nickname','birth')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''

        self.fields['nickname'].widget.attrs['placeholder'] = "닉네임"
        self.fields['nickname'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['placeholder'] = "비밀번호"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "비밀번호 확인"
        self.fields['password2'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['placeholder'] = "exampl@abc.com"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['placeholder'] = "yyyy-mm-dd"
        self.fields['birth'].widget.attrs['input type'] = "date"

    
    #패스워드 일치 유효성 검사
    def clean_password2(self):#clean멤버 함수를 통한 유효성+값변경까지. validator은 유효성검사만
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("입력하신 패스워드가 맞지 않습니다.")

        #단순한 패스워드 인지 유효성 검사
        #password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        
        return password2


    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])#패스워드는 항상 set_password로 입력받음(그래야 암호화를 해서 넘겨줌)
        #유효성 검사를 마치고 데이터를 넘겨줄떈 cleaned_data로 넘겨줌
        
        if commit:
            user.save()
        return user

#회원정보 수정#
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
 
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'nickname','birth', 'is_active', 'is_admin')
 
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ActListForm(forms.ModelForm):
    class Meta:
        model = ActList
        fields = ('act_num', 'act_name','act_summary','act_info')

    def __init__(self, *args, **kwargs):
        super(ActListForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=None

        #self.fields['actId'].widget.attrs['input type'] = "hidden"
        self.fields['act_num'].widget.attrs['placeholder'] = "계좌번호"
        self.fields['act_num'].widget.attrs['class'] = "form-control"
        self.fields['act_num'].widget.attrs['type'] = "text"
        self.fields['act_name'].widget.attrs['placeholder'] = "통장이름"
        self.fields['act_name'].widget.attrs['class'] = "form-control"
        self.fields['act_summary'].widget.attrs['placeholder'] = "한줄메모"
        self.fields['act_summary'].widget.attrs['class'] = "form-control"
        self.fields['act_info'].widget.attrs['placeholder'] = "통장설명"
        self.fields['act_info'].widget.attrs['class'] = "form-control"


class BankBookForm(forms.ModelForm):
    class Meta:
        model = BankBook
        fields = ['act_date', 'act_price','act_payment','act_part', 'act_content']

    def __init__(self, *args, **kwargs):
        super(BankBookForm,self).__init__(*args, **kwargs)
        
        '''
        self.fields['act_date'].widget.attrs['placeholder'] = "날짜"
        self.fields['act_date'].widget.attrs['class'] = "form-control"
        self.fields['act_price'].widget.attrs['placeholder'] = "금액(원)"
        self.fields['act_price'].widget.attrs['class'] = "form-control"
        self.fields['act_payment'].widget.attrs['placeholder'] = "카드/현금"
        self.fields['act_payment'].widget.attrs['class'] = "form-control"
        self.fields['act_part'].widget.attrs['placeholder'] = "수입/지출"
        self.fi:
        elds['act_part'].widget.attrs['class'] = "form-control"
        '''
        
class ActBoardForm(forms.ModelForm):
    class Meta:
        model = ActBoard
        fields = ['board_title', 'board_content']

    def __init__(self, *args, **kwargs):
        super(ActBoardForm,self).__init__(*args, **kwargs)

'''
###20170602 최초 BankBookForm
class BankBookForm(forms.ModelForm):
    class Meta:
        model = BankBook
        fields = ('act_date', 'act_price','act_payment','act_part')

    def __init__(self, *args, **kwargs):
        super(BankBookForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=None

        
        self.fields['act_date'].widget.attrs['input type'] = "date"
        
        self.fields['act_price'].widget.attrs['placeholder'] = "금액(원)"
        self.fields['act_price'].widget.attrs['class'] = "form-control"
'''


'''
###20170504_Backup code before update_Change of 'def __init__'###
class UserCreationForm(forms.ModelForm): #모델폼으로 불러옴
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    #패스워드가 맞지 않을때
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput, #별표로 나오게 함
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput,
        strip=False,
    )
    birth = forms.DateField(
        label=_("Birth"),
        widget=forms.TextInput,
        strip=False,
    )

    class Meta:
        model = User #모델이 유저 모델이면
        fields = ("username",) #유저네임만 가져와서 폼필드를 생성함
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

    ###패스워드 확인의 일치 유효성 검사###
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")#PW1 값가져오기
        password2 = self.cleaned_data.get("password2")#PW2 값가져오기
        if password1 and password2 and password1 != password2:#두개가 입력이 되어있고 and 두개의 암호가 틀릴때
            
            #에러를 낸다
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        #비번이 같을때 정상적으로 출력
        self.instance.username = self.cleaned_data.get('username')#cleaned_data를 사용해 username을 가져와 username에 저장
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)#패스워드도 가져와서 저장하는데 암호가 간단한 것은 아닌지 유효성 검사
        
        #유효성검사가 정상적으로 끝나면 그때 리턴받음
        return password2

    ###저장###
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])#set_password를 통해 입력을 받는다
        if commit:
            user.save()
        return user
'''
class ChangePwForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
        )
    new_password2 = forms.CharField(
        label=(u'Verify Password'), 
        widget = forms.PasswordInput(render_value=False)
        )


    def __init__(self, *args, **kwargs):
        super(ChangePwForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['new_password1'].widget.attrs['placeholder'] = "password"
        self.fields['new_password1'].widget.attrs['class'] = "form-control"
        self.fields['new_password2'].widget.attrs['placeholder'] = "password check"
        self.fields['new_password2'].widget.attrs['class'] = "form-control"


class DeleteUserForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DeleteUserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['password'].widget.attrs['placeholder'] = "password"
        self.fields['password'].widget.attrs['class'] = "form-control"

    def clean(self):
        password = self.cleaned_data['password']
        user = MyUser.objects.get(email=self.user.email)
        if user.check_password(password):
            pass
        else:
            raise forms.ValidationError("입력하신 비밀번호와 현재 아이디의 비밀번호와 일치하지 않습니다. 다시 입력하세요.")
            return password


class FindUserNameForm(forms.Form):
    nickname = forms.CharField(max_length=50)
    birth = forms.DateField(widget=forms.TextInput)
    
    class Meta:
        model = MyUser
        fields = ('nickname','birth')

    def __init__(self, *args, **kwargs):
        super(FindUserNameForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''

        self.fields['nickname'].widget.attrs['placeholder'] = "닉네임"
        self.fields['nickname'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['placeholder'] = "yyyy-mm-dd"
        self.fields['birth'].widget.attrs['input type'] = "date"

    def clean(self):
        nickname = self.cleaned_data['nickname']
        birth = self.cleaned_data['birth']
        data= MyUser.objects.filter(nickname=nickname, birth=birth).exists()
        if MyUser.objects.filter(nickname=nickname, birth=birth).exists():
            pass
        else:
            raise forms.ValidationError("입력하신 데이터로 조회한 결과 회원정보를 찾을 수 없습니다. 가입하는것을 추천합니다.")
        return data


class FindPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    birth = forms.DateField(widget=forms.TextInput)

    class Meta:
        model = MyUser
        fields = ('email','birth')

    def __init__(self, *args, **kwargs):
        super(FindPasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['email'].widget.attrs['placeholder'] = "email : example@abc.com"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['class'] = "form-control"
        self.fields['birth'].widget.attrs['placeholder'] = "yyyy-mm-dd"
        self.fields['birth'].widget.attrs['input type'] = "date"


    def clean(self):
        email = self.cleaned_data['email']
        birth = self.cleaned_data['birth']
        if MyUser.objects.filter(email=email, birth=birth).exists():
            pass
        else:
            raise forms.ValidationError("입력하신 데이터로 조회한 결과 회원정보를 찾을 수 없습니다. 가입하는것을 추천합니다.")
        return MyUser.objects.filter(email=email, birth=birth)
