__author__ = 'leesangjun'

#변수
a = 7
print(a)

b = a
print(b)

#변수의 타입 / 리터럴의 타입

print(type(a))     #int
print(type(b))     #int
print(type(58))    #int
print(type(99.9))  #float
print(type('abc')) #str

#부동소수점 포함한 결과
print(9/5)

#정수(버림)
print(9//5)

#나머지 구하기
print(9 % 5)

#진수
print(0b10) #2
print(0o10) #8
print(0x10) #16

#TypeCase
print(int(True))    #0
print(int(False))   #1

#부동소수점 -> 소수점 버리고 정수 출력
print(int(98.6))
print(int(1.0e4))   #10000.0000

'''
print(int('test')) #exception
'''

#int는 32비트 (4바이트)
#파이썬 2 -> long 존재
#파이썬 3 -> log 없어지고 int가 더 큰 값을 처리

#float 부동소수
print(float('1.0e4'))
print(float('92.8'))

#문자열
print('snap')
print("SNAP")
print('''test''')
#multiline String
#양끝에 있는 공백 모두 보존
#멀티라인 주석으로도 많이
poem = '''씀
하이 모두들 안녕
    내가 누군지 아니
    이하 니다
    이하 니다
'''
print(poem)


#문자열 형변솬
print(str(92.8))
print(str(True))

#escape 문자
#\n : newLine
#\t : tab
#\\ : \
#...등
print('test\n testtest \n')

#문자열 겨합
print('test'+' man')
#문자열 복제
print('t'*6)

#문자 추출
#기본적으로 배열과 같다 하지만 배열과 결정적으로 다른점은 수정이 불가능하다는 점
letters = "show me the money"
print(letters[6]) #e
print(letters[-3]) #n
''' Exception - 문자열을 수정하려해서
letters[6] = 'k'
print(letters[6])
'''
'''Exception - 오프셋을 넘어가서
print(letters[100])
'''
#문자열 함수
name = 'Henny'
print(name.replace('H', 'P'))
print('P'+name[1:])

#슬라이스[start : end : step]
#[:] 처음부터 끝까지
#[start:] start부터 끝까지
#[:end] 처음부터 end-1까지
#[start:end] start부터 end-1까지
#[start:end:step] start부터 step만큼 건너뛰며 end-1까
#오프셋은 오른쫄 0, 1, 2, 왼쪽 -1, -2, -3..
letters = '1234567890'
print(letters[:])
print(letters[0:])
print(letters[:10])
print(letters[:-1])
print(letters[-3:]) #마지막 3글
print(letters[3:-2])
print(letters[::-1]) #역순출

#문자열 길이
print(len(letters))
#Split
print(letters.split('3'))
#join
arry = ['test', 'test1', 'test2']
print('join'.join(arry))

#String Function
print(letters.startswith('0'))
print(letters.startswith('1'))
print(letters.endswith('0'))
print(letters.find('234'))  #해당 문자열이 시작하는 offset리턴
print(letters.rfind('789')) #해당 문자열이 마지막으로 있는 offset 리턴
print(letters.count('0'))   #해당 문자열이 나오는 카운트
print(letters.isalnum())    #숫자와 알파멧으로만 되어있는

setup = 'a duck goes into a bar...'
print(setup.strip('.')) #양끝 . 삭제
print(setup.capitalize())   #첫단어 대문
print(setup.title())    #모든 단어의 첫글자 대문자
print(setup.upper())    #모두 대문자
print(setup.lower())    #모두 소문
print(setup.swapcase()) #대소문자 반대
print(setup.center(50)) #주어진 크기 내에서 가운데 정
print(setup.ljust(30))  #주어진 크기 내에서 왼쪽정렬
print(setup.rjust(50))  #주어진 크기 내에서 오른쪽정렬
print(setup.replace('a', 'a famous'))   #바꾸기
print(setup.replace('a', 'a famous', 1))  #1번까지 바꿈