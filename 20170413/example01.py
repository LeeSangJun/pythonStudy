#튜플 : 불변(Immutable) - 항목 할당 후 바꿀 수 없음
#리스트 : 변경 가능

##리스트
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wendsday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Micheal']   #값이 Uinqe할 필요는 없

another_empty_list = list()
print(another_empty_list)

#string to list
print(list('cat'))

#Tuple to List
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

#split은 리스트 리턴
birthday = '1/6/1952'
print(birthday.split('/'))

splittime = 'a/b//c/d///e'
print(splittime.split('/'))
print(splittime.split('//'))