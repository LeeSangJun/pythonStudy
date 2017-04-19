__author__ = 'leesangjun'
#함수함수!!!!

#함수의 정의
def do_nothing() :
    pass

do_nothing()    #실행

#정의
def make_a_sound() :
    print('quack')

#호출
make_a_sound()

def agree():
    return True #값 반

if agree(): #반환된 값 if문에서 활
    print("agree")

#괄호안의 값을 매개변수, 인자, 파라미터라고 부른
def echo(anything):
    return anything + ' ' + anything

print(echo("testsetests"))

#함수가 명시적으로 return 을 하지 않으면
#함수는 None을 호출한다
#None 은 if 문에서 False로 평가되지만 실제로는 False랑은 조금 다름

test = None
if test:
    print("get False!!")

if test is None:
    print("it's nothing")

#위치 인자
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))    #순서대로 배개변수가 적용된다.

#키워드 인자
#배개변수에 이름을 지정할 수 있따
print(menu(entree='beef', dessert='bagle', wine = "dordeaux"))

#두개 섞어쓰기 가능
print(menu("wine_test", entree="test", dessert="dedede"))

#함수 정의 할 떄 기본값을 넣을 수 있다
#다만 기본값은 함수를 정의할때 계산되기 때문에 변경할 경우 계속 변경되어있다
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy(1)
buggy(2)

#위치인자 모으기 : *
#튜플로 반환해줌, 어떤게 들어가도 노상관

def print_args(*args):
    print('Positional argument tuple :', args)

print_args()
print_args(1,2,3,4)

#관용적을 가변인자의 이름은 args를 사용한다...
#키워드 인자 모으기 : **
def print_kwargs(**kwargs):
    print("kyword_arguments : ", kwargs)

print_kwargs(wine='merlot', entree = 'mutton', dessert='macaroon')  #키 : 밸류값으로 dictionary에 들어
##print_kwargs(wine='merlot', entree = 'mutton', dessert) #키값없으면 류남