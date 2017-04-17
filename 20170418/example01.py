__author__ = 'leesangjun'

#SET
#키만 남은 딕셔너리
#값이 유닠하다
#존재하는지 판단여부는 셋으로 하고 값은 딕셔너리로 봄

empty_set = set()   #빈 {} 는 딕셔너리가 됨 그래서 빈 set은 set()으로 생
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

print(set('letter')) #중복된 t하나가 사라졌다
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])) #리스트도 바꿀수있음
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))) #튜플도 바꿀 수 있음
print(set({'apple':'red', 'orange':'yellow', 'cherry':'red'})) #딕셔너리는 키만 반환

#in 으로 값 멤버 체크
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'}
}

#보드카가 들어있는 음료수(name, contents 는 튜플이다.
print(drinks.items())   #items()함수는 딕셔너리 키 : 값 을 튜플의 리스트로 반환해준다. for문에서 튜플 언패킹해서
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

#콤비네이션 연산자...?
# 셋값의 조합을 확인하고 싶다면? 셋 인터섹션 연산자 (set intersection operator)인 &을 사용
#cream, kahlua 가 들어있는 키값을 찾음 만약 없으면 False로 간주되는 빈셋을 반환

for name, contents in drinks.items():
    if contents & {'cream', 'kahlua'} :
        print(name)
    print(contents & {'ccc'} ) #False

#보드카는 있지만 크림이 없는 키
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b)    #교집합 연산자
print(a.intersection(b)) #교집합 함수

print(bruss & wruss)    #교집

#유니온 '|'
print( a |  b)
print(a.union(b))
print(bruss | wruss)    #중복되는건 사라짐

#- (차집합 / difference
print(a-b)
print(a.difference(b))
print(bruss - wruss)    #작은거에서 큰거뺴니....없음...
print(wruss.difference(bruss))

#^ / symmetric_difference() : 익스클루시브(대칭차집합) - 한쪽 셋에는 있지만 양쪽 모두에 들어잇지 않은 멤버

print(a ^ b)
print(a.symmetric_difference(b))

#<= / issubset() : 부분집합 확인

print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)   #모든 셋은 자신의 서브
#프로퍼 서브셋
#자신은 프로퍼서브셋 아님
print(a < a)

#전체적으로 집합으로 설명하고 있는데,,, 그냥 값이 하나밖에 올수 없는 목록이라고 생각하면 쉬울듯...(순서 보장안됨)
#그냥 상식적으로 생각하는대로 동함

#슈퍼셋은 서브셋의 반대
# > / issuperset()
print(a >= b)
print(a.issuperset(b))
print(wruss.issuperset(bruss))
#프로퍼 슈퍼셋 : 서브셋과 같

#예시..
#딕셔너리의 경우 키는 불변하기 때문에 리스트 딕셔너리 셋은 딕셔너리의 키가 될수 없지만 튜플은 딕세너리의 키가 될수잇다
''' #Exception
test_dic = {
    ['test', 'test1'] : 'myHouse'
}
print(test_dic)
'''

test_dic = {
    (44.79, -93.14, 285) : "my House",
    (38.89, -77.03, 13) : "The White House",
}
print(test_dic)