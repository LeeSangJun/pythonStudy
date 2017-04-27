'''
메서드 타입

클래스 정의에서 메서드의 첫버째 인자가 self이면 이 멘서드는 인스턴스 메서트
- 일반적인 클래스를 생성할 때의 메서드

클래스 메서드는 클래스 전체에 영향을 끼침
- 클래스에 대한 어떤 변화가 모든 객쳉 영향을 끼침
@classmethod 데코레이터로 표현한다
첫번때 매개변수는 클래스 자신 (cls)로 모통 함
'''

class A():

    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("i'm a A!" + str(A.count))

    @classmethod
    def kids(cls):
        print("A has",cls.count, "little objects")

easy_a = A()
breezy_a = A()
wheezy_a = A()
print(easy_a.exclaim())
print(A.kids())

'''
정적메서드는 @staticmethod 데코레이터로표현
첫번째 매개변수가 없다
'''

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("commm")

#객체 생성할 필요 없이 부를 수 있다
print(CoyoteWeapon.commercial())


'''
덕 타이핑 :
파이썬은 다형성을 느슨하게 구현했다
'''
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"


'''
초기화 함수가 없으므로 부보의 __init__을 오버라이딩 하지 않음
파이썬은 자동으로 부모클래스의 __init__을 실행한다
서로 다른 say 메서드는 다른 동작을 한다.
그 외에 who(), says() 메서드를 갖고 있는 모든 객체에서 메서들ㄹ 실행 수 있따
'''

class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'

brook = BabblingBrook()

#obj에 들어가는 객체에 따라서 실행되는 내용이 다르다
#이걸 덕타이핑 이라고 한다
def who_says(obj):
    print(obj.who(), 'says', obj.says())


class Word():
    def __init__(self, text):
        self.text = text

    ##__eq__ 함수를 통해 파이썬 객체의 연산자를 조작했따
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)

#이를 특수메서드라고 하는데.
#연산자 오버라이딩을 할 수 있따
#특수메서드 종류는 홈페이지 참


#named Tuple
#네임드 튜플은 튜플의 서브클래스 이름과 위치로 접근가
#파이썬에서 네이티브로 지원하는건 아니고 모듈 필요

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)

parts = {'bill':'wide orange', 'tail' : 'long'}
duck2 = Duck(**parts)
print(duck2)