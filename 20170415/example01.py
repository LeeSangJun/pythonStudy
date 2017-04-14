#딕셔너리
#딕셔너리는 리스트와 비슷하다.
#하지만 순서를 보장하지 않고 KEY-VALUE 타입으로 구성된다
#키는 보통 문자열을 쓰지만... immutable한 어떤 값을 써도 된당
#자바 해시맵, 자바스크립트 오브젝트 등등 사실 비슷한건 많이 있다

#딕셔너리 생성
empty_dict = {}
print(empty_dict)

test_dict = {
    "day" : "A period of....",
    "positiye" : 'Mistaken at....',
    "misfortune" : "the kind of ....."
}

print(test_dict)
print(test_dict['day'])

#Dict() : dictionary로 변환
#두 값으로 이루어진 시퀀스를 딕셔너리로 변환 가
lol = [['a','b'], ['c','d'], ['e','f']]
make_dict = dict(lol)
print(make_dict)

test_a = [('a', 'b'),('c', 'd'),('e', 'f')]    #튜플도 된다
test_b = (('a', 'b'),('c', 'd'),('e', 'f'))    #튜플도 된다
test_c = (['a', 'b'],['c', 'd'],['e', 'f'])    #튜플도 된다
test_d = ('ab', 'cd', 'ef')         #...이것도 된다?
test_e = ['ab', 'cd', 'ef']

print(dict(test_a))
print(dict(test_b))
print(dict(test_c))
print(dict(test_d))
print(dict(test_e))


#항목 추가 / 변경하
test_dict = {
    "day" : "A period of....",
    "positiye" : 'Mistaken at....',
    "misfortune" : "the kind of ....."
}

test_dict["day"] = "test"   #키값을 통해서 바꿀 수 있음.
print(test_dict)

#딕셔너리의 key 값은 항상 유니크 해야
#같은 키를 사용할 경우 마지막에 압력된값이 나온당
test_dict = {
    "key1" : "value1",
    "key2" : "value2",
    "key1" : "value3"
}
print(test_dict)

#두개의 딕셔너리를 병합 : update()

pythons = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4',
    'key5' : 'value5'
}

others = {
    'key1':'value 1_1',
    'key6':'value6'
}

#파라미터에 있는 키값으로 덮어씌워진다.
pythons.update(others)
print(pythons)


#항목 얻기
pythons['key1']
'''
EXCEPTION :::
키가 존재하지 않으면 익셉션이 난다
pythons['key1000']
'''
#방지하기 위해서는..
#1. in으로 있는지 없는지 확인
print('key1' in pythons)
#2. get()함수 사용
print(pythons.get('key1'))
print(type(pythons.get('key1000'))) #값이 없으면 None으로 뜬다 : None의 타입은 NoneType
print(pythons.get('key1000', "alertValue")) #값이 없으면 디폴트값도 넣을 수 있음

#모든 키 얻기
#리스트 형태로 반환해준다(이건 파이썬 2)
signals = {'green' : 'go',
           'yellow' : 'go faster',
           'red' : 'stop'
           }

print(signals)
print(signals.keys())  #dict_keys 형태로 보내주는데 리스트로 쓰고싶으면 list()이용해서 변환시켜야 한다
print(list(signals.keys()))
#값을 얻기 위해서는 value()사용
print(signals.values()) #이건 dict_values형태로 보내줌
test = list(signals.values())
print(test[1])

#키 값세트를 얻고자 할떈 : items()
#튜플로 반환
print(signals.items()) #이또한 역시 리스트로 안줌.
print(list(signals.items()))

#리스트와 마찬가지로 call by reference
signals = {'green': 'go', 'yellow': 'go faster', 'red' : 'stop'}
save_signals = signals
print(signals['green'])
signals['green'] = 'test'
print(save_signals['green'])

#복사 위해서는 copy()사용
signals = {'green': 'go', 'yellow': 'go faster', 'red' : 'stop'}
copy_sig = signals.copy()
signals["green"] = 'confuse'
print(signals)
print(copy_sig)

