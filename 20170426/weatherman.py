'''
모듈을 PY확장자가 없는 파이썬 파일의 이름
'''
import report as rp #이름을 바꾸고 싶을 때는 alias를 한다.

description = rp.get_description()
print("today's weather:", description)

'''
메인 프로그램에서 report모듈을 임포트함
report.py의 get_description 함수에서 random모듈의 choice함수를 임포트

import 모듈네임
from 모듈네임 import 함수'''