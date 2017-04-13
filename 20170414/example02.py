#튜플 : 리스트와 거의 비슷
empty_tuple = ()
print(empty_tuple)

#하나이상의 요소가 있는 튜플을 만들때는 각 요소뒤에 콤마를 붙임..
one_marx = 'Groucho',
print(one_marx)

#두개 이상 요소가 있을떈 마지막에 콤마 안붙임
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

#...붙여도 딱히 상관은 없는데?
marx_tuple = 'Groucho', 'Chico', 'Harpo',
print(marx_tuple)

#괄호 붙이면 tuple이다?
one_tuple = ('test', )    #근데 이러면 그냥 String 임.ㅋㅋ
# 괄호가 있으나 마나 규칙은 위와 같다 하지만 괄호를 붙이면 튜플이란걸 알아보기가 쉽겠징
print(one_tuple)

#한번에 여러개 변수 할당하기
marx_tuple = ('test1', 'test2', 'test3')
a, b, c = marx_tuple
print(a)
print(b)
print(c)
#이걸 튜플 언패킹이라고 한다.
#근데 위에서 a, b, c 도 일종의 튜플인거넹
#swap도 편함
id = 'test'
password = 'testPass'

id, password = password, id
print(id)
print(password)

#리스트를 튜블로 만들수도 있당
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))
print(marx_list)

#####IMPORTANT###
'''
튜플과 리스트 : 튜플은 수정할 수 없다 append, insert등 함수도 없다
근데 왜 튜블을 사용하지?

1. 적은 공간사용
2. 손상이 안됨( 값이 변하지 않기에 보장할수있다)
3. 튜플을 딕셔너리의 키로 사용할수 있다
4. 네임드 튜플 : 객체 대안 사용
5. 함수의 인자들은 튜플로 전달된다.
'''


