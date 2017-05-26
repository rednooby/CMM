import re
from django.forms import ValidationError

'''
validators와 clean의 차이
validators는 모델에 정의한다, Modelform을 통해 모델의 validators정보도 같이 가져온다
clean은 특정 form에서 1회성 유효성 검사를 할때 (해당 폼에서만 한번 사용할떄),
		다수의 필드값을 묶어서 유효성 검사를 할때, (Ex. 3개의 게임서버가 있을때 1번서버만 아이디중복 확인하고 싶을떄)
		필드값을 변경할 필요가 있을때 (validator은 변경 불가능하며 값의 조건만 체크)
'''

'''
##계좌번호 숫자와 -만 사용하게 하는 유효성
def number_validator():
	if not re.match((r'^[0-9]$'),(r'^[-]')):
		raise ValidationError('숫자와 -만 입력 가능합니다.')
'''