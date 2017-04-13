__author__ = 'leesangjun'

#offsetㅇ으로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

'''
Exception!!
print(marxes[4])
'''

#리스트 안의 리스트
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)
#리스트 나옴
print(all_birds[0])

#다중배열
print(all_birds[1][0])

#값바꾸기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

#슬라이스
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-1]) #리스트 반

#리스트 함수
marxes.append('Zeppo')
print(marxes)

#리스트 병
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

#insert(offset, data)
#offset이 리스트의 길이보다 길경우 그냥 끝에 추가한다
marxes.insert(3, 'Gummo')
print(marxes)
marxes.insert(10,'test')
print(marxes)

#remove
#값으로 삭제
marxes.remove('test')
print(marxes)

#오프셋으로 받아오기
#pop() - 항목 리턴과 동시에 삭제
#파라미터가 없을경우 -1
#pop(0), pop(-1) : 처음
print(marxes)
print(marxes.pop())
print(marxes)

#값으로 index찾기
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

'''Exception
print(marxes.index('test')) #값이 없으면 Exeption
'''

#존재여부 확인 : in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

print('Groucho' in marxes)
print('Test' in marxes)

#특정값이 얼마나 있는지 카운트
print(marxes.count('test'))   #파라미터필수

#문자열로 변환
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(',,,'.join(marxes))

#sort : 내부적으로 정령 : 실제값이 변경됨
#sorted : 정렬된 값 반환, 원본은 정렬 안됨
#같은 타입이거나 정부부동소수점조합 타입 정렬가능
#기본은 오름차순
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
print(sorted(marxes))
print(marxes)
print(marxes.sort())
print(marxes)

#내림차순
print(sorted(marxes, reverse=True))
marxes.sort(reverse=True)
print(marxes)

#리스트 개수 : len()
print(len(marxes))

#할당 복사
#기본적으로 Call By Reference
a = [1, 2, 3]
b = a
a[1] = 'test'
print(b)

#리스트를 복사하는 방법 3개  : copy, list()변환 , slice
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]

a[1] = 'test'
print(a)
print(b)
print(c)
print(d)

