'''
객체란 무엇인가?
파이썬의 모든것은 객체다
'''

#객체의 기본
class Person():
    pass

#타 언어와 다르게 인스턴스를 생성할때는 new 가 없다
someone = Person()

#__init__ 은 생성자 함수다
#self는 클래스 객체 자신을 가르친다
#이름이 정해져 있는것은 아니지만 self 로하는것이 약속
class Person():
    def __init__(self):
        pass

##name추가
##init은 필수는 아니다
class Person():
    def __init__(self, name):
        self.name = name

hunter = Person('test')
print(hunter.name)

'''
상속
'''
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())

#override
#__init__ 메소드를 포함한 모든 메서들를 오버라이드 할 수 있다.
class Car():
    def __init__(self, name):
        self.name = 'test'

    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def __init__(self, name, email): #init을 만들면 부모 클래스의 init이 오버라이딩 되기에 명시적으로 써야한다
        super().__init__(name)  ##
        self.email = 'test@naver.com'

    def exclaim(self):
        print("I'm a Yugo!")

    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car('test')
give_me_a_yugo = Yugo('test1','test2')

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())
print(give_me_a_yugo.need_a_push())



##get/set 속성과 propert

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('indise thet getter')
        return self.hidden_name

    def set_name(self, input_name):
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('howrkd')
print(fowl.name)


#데코레이터 쓰기
#위아 아래의 차이는 getter setter 를 다이레그로 쓸수 있느
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.hidden_name = input_name

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

#diameter는 setter속성이 없어서 바꿀수 없

#파이썬은 클래스 정의 외부에서 볼수업도록하는 네이밍 컨벤션이 있따
#__(더블 언더스코어)
class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name


fowl = Duck('Ho')
print(fowl.name)
fowl.name = 'test'
print(fowl.name)
'''
ERROR!
더블언더바가 붙으면 private처럼 사용 가
print(fowl.__name)
'''

#직접 접근을 못하는건 아니지만.. 어렵다
print(fowl._Duck__name)
