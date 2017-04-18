#if, elseif else

disaster = True  #선언
if disaster :    #조건이 참이면 실행 #파이썬에서의 IF문은 콜론(:)으로 조건을 명시
    print("Woe!")
else:
    print("Whee!")

#비교연산자
'''
==
!=
<
<=
>
>=
in  : 멤버십(셋...등등)
'''

#부울 연산자(and, or, not) 는 비교연산자보다 우선순위 낮음
x = 8
print(5 < x and x < 10)
#순서 헷갈리고 싶지 않다면 괄호를 쓰면 된당
#파이썬에서는 여러번 비교 가능
#각각의 연산자는 위치에따라서 and 연산을 한다고 생각하면 된다.
print( 5 < x < 10 < 1)

#부울 연산에서 False로 인식되는것들
'''
null    : None
0       : 0
부동소수0 : 0.0
빈문자열
빈 리스트
빈 튜플
빈 딕셔너리
빈셋
'''
# 그 외에는 True
some_list = []
if some_list :
    print("There's something in here")
else:
    print("empty")


#while
count = 1
while count <= 5 :
    print(count)
    #count++        #이거 없음
    count += 1


#break
while True:
    stuff = input("string to capitalize : ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

#continue
while True:
    value = input("Integer, please")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0 :
        continue
    print(number, "squred is", number*number)

#while - else
#while 이 전부 실행되지 않았을 때 else 실행
numbers = [1 ,3 ,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found event number', number)
        break
    position += 1
else:
    print('No even number foungq')  #break문으로 반복문이 끝나지 않으면 실행된다.

#for문
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

#배열은 각 값에대해 순회한다
word = 'cat'
for letter in word:
    print(letter)

accusation = {'room' : 'ballroom', 'weapon':'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)


#튜플 반환
for card, contents in accusation.items():
    print('card', card, 'has the contents', contents)

#ZIP()
#여러 시퀀스를 병렬로 순회할 수 있다
#가장 짧은 시퀀스가 완료되면 zip()은 멈춘다
test = ['1', '2', '3']
test1 = ['11', '22', '33']
test2 = ['111', '222', '333', '444']

for t1, t2, t3 in zip(test, test1, test2):
    print( t1, " - ", t2, " - ", t3, " - ")


english = "monday", "Tuesday", "Wednsday"
french = "Lundi", "Mardi", "Mercredi"

print(list(zip(english, french)))
print(dict(zip(english, french)))

#숫자 시퀀스 생성 : range()
#리스트나 튜플같은 자료구조를 생성하여 저장하지 않더라도 특정범위 내에서 숫자 스트림 반환
#range(start, stop, step)
#start : 0부터 시작 stop은 필

for x in range(0, 3):
    print(x)

for x in range(2, -1, -1):
    print(x)

print(range(0, 11, 2))
print(list(range(0, 11, ))) #짝수 리스트

#ZIP이나 range나 둘다 iterator객체를 반환하면 그것을 list, dict, tuple, set으로 변환시킨 후 사용해야 한다.