__author__ = 'leesangjun'

#컴프리헨션 : 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 콤팩트한 방법

#1~5까지의 정수 리스트를 만드는법
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

#range함수를 이용
number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)

#리스트에 직접 range넣기
number_list = list(range(1, 6))
print(number_list)

#리스트 컴프리 헨션
number_list = [number for number in range(1, 6)]
print(number_list)

#목록에 대한 값을 생성하는 변수,
#number의 표현식을 바꾸면 리스트 내용이 바뀜

number_list = [number-1 for number in range(1, 6)]
print(number_list)

#[표현식 for 항목 in 순회 가능한 객체 if 조건]
#1~5사이에서 홀수리스트를 만드는 컴프리헨션
a_list = [number for number in range(1,6) if number % 2 == 1]
print( a_list)

#컴프리헨션내에서 loop의 중복
rows = range(1, 4)
cols = range(1, 3)
for row in rows :
    for col in cols :
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
print(cells)

#딕셔너리 컴프리헨션
#{키 : 값 for 표현식 in 순회 가능한 객체

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}
print(letter_counts)

letter_counts = {letter : word.count(letter) for letter in set(word)}
print(letter_counts)

#set컴프리헨션
#{표현식 for 표현식 in 순회객체}
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

#제너레이터 컴프리헨션
#튜플은 컴프리헨션이 없다
#괄호를 쓰면 제네레이터 컴프리헨션

number_thing = (number for number in range(1,6))
print(number_thing)
print(type(number_thing))   #이건 제너레이
for number in number_thing:
    print(number)
#제너레이터는 한번만 실행 가능
number_list = list(number_thing)
print(number_list) #위에서 실행했기때문에 없는값 나옴

number_thing = (number for number in range(1,6))
print(list(number_thing))
