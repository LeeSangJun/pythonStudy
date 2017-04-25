import sys
print('Program arguments : ', sys.argv)

'''모듈의 참조 경로'''
'''
 디렉토리 이름의 리스트오 표준 sys모듈에 저장되어있는 zip아카이브 파일을 변수 path로 사용한다
 이 리스트를 접근하여 수정할 수 있다
'''

for place in sys.path:
    print(place)


'''
위 for문을 통해 검색디렉토리의 우선순위를 알 수 있다
임포트할 파일을 현재 디렉터리에서 가장 먼저찾는다. 중복된 모듈이 있으면 첫번째 조건을 사용한다
'''

