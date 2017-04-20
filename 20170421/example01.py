#docstring
#함수 시작부분에 문자열을 포함시켜 함수정의에 문서를 붙일 수 있담

def func_test(arg):
    'echo returns its input arguement'
    return

#여러줄 쓸수도 있고 서식도 쓸수 있따

def func_test01(thing, check):
    '''
    PRINT THE FIRST AUG
    The operation is :
    :param argu:
    :return:
    '''
    if check:
        print(thing)

#help를 이용하면 docstring을 출력할수있따
help(func_test01)
print(func_test01.__doc__)


#일급객체 : 함수
#함수는 일급객체다. 자바스크립트 공부해라 그럼 알수있따

def answer():
    print(42)

answer()

def run_somthing(func):
    func()

run_somthing(answer)
print(type(run_somthing))

#함수는 불하기 때문에 딕셔너리의 키로 사용 가능
#파이썬에서도 클로저를 사용할 수 있다.

def knights2(saying):
    def inner2():
        return "we are the knight who say : %s" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a)
print(b)
print(a())
print(b())


#익명함수 : lambda()
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['test1', 'test2', 'test3', 'test4']
edit_story(stairs, lambda word: word.capitalize()+'!')

#제너레이터 : 파이썬의 시퀀스를 생성하는 객체
# 일반 함수는 이전 호출에 대한 메모리가 없고 항상 똑같은 상태로 첫번째 라인부터 순회하지만
# 제너레이터는 마지막으로 호출된 항목을 기억하고 다음값을 반환한다
# 제너레이터 함수를 쓰면 복잡한 시퀀스를 새성할 수 있다
# yield문으로 값을 반환한다

def my_range(first = 0, last = 10, step = 1):
    number = first
    while number < last :
        yield number
        number += step

print(my_range)
print(my_range(1, 5))


#데코레이터
#소스코드 안바꾸고 디버그문 보고싶은 경우가 있따 어쩃든 뭘좀 붙여볼떄..
# 데코레이터는 하나의 함수를 취해 또다르 ㄴ함수를 반

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function : ', func.__name__)
        print('Positional arguments: ', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result', result)
        return result
    return new_function

#어떤 함수가 와도 정의한 함수를 쓸 수있따
def add_ints(a, b):
    return a+b

print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints) #수종으로 데커레이터 할
cooler_add_ints(3, 5)

@document_it
def add_ints_deco(a,b):
    return a+b

print(add_ints_deco(1, 2))
#데코레이터는 가장 아래 함수(함수 명과 가장 가까운 곳의 데코레이터) 부터 시작된다

#네임스페이스와 스코프
#네임스페이스는 특정 이름이 유일하고 다른 네임스페이스에서의 같은 이름과 관계 없다
#메인 프로그램은 전역 네임스페이스
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

#함수에서 전역변수 값 바꾸려하면 에러
'''
def change_and_print_global():
    print("inside : ", animal)
    animal ='test'
    print('after : ', animal)

change_and_print_global()
'''

#함수 내에서 처음 사용하기 전에 변수선언을 한다면 그건 지역변수가 된다
#전역으로 만들고 싶다면 global키워드를 이용한다

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside_change : ', animal)

change_and_print_global()

#locals() : 로컬 네임스페이스내용이 담긴 딕셔너리
#globals() ;글로벌 네임스페이스 내용이 담긴 딕셔너

animal = 'fruitbat'
def change_local():
    animal='wombat'
    print("locals:", locals())

change_local()

print('globals', globals())

#_와 __의 사용
#두개의 언더스코어(__)로 시작하고 끝나능 림은 파이썬 내의 사용을 위해 예약되어있음
#변수선언할때 쓰면 안됨
#함수의 이름 : function.__name__에 있음
#docstring : function.__doc__
#메인프로그램은 이름이 __main__으로 할당되어있


#에러 처리 try / catch
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('errorororororo')

#인자없는 except는 모든 예외타입
short_list = [1, 2, 3]
while True:
    value = input('Postion [q]')
    if value == 'q':
        break

    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('bad Index', err)
    except Exception as other:
        print('other', other)

#예외 만들기
class UppercaseException(Exception):
    pass

words =['test1', 'test2', 'teest3', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)