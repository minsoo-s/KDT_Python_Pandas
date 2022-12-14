#------------- 여러개 data를 저장하기(문자열, 리스트, 튜플, 딕셔너리, 집합)------------------
# 문자열, 리스트, 튜플 은 index를 가지는 공통점이 있다.
# 문자열 'ABC'
#        012
# 리스트 [D1, D2,....,DN]
#         0  1       N
# 튜플  (D1, D2,...,DN)
#        0  1      N
# 딕셔너리
# 집합
#------------------------------------------------------------------------------------


#-----------------리스트 자료형 List------------------------------------------------
# - 여러 종류의 여러개 데이터를 저장하는 타입
# - 여러개 데이터를 구별하기 위해서 인덱싱(Indexing) 사용
#---------------------------------------------------------------------------------
# 5명 점수를 저장하기
score=[98, 90, 70, 50,80, '40']
# 전체 데이터 모두 출력
print(f'score = >{score}, type => {type(score)}')
# 특정 요소만 출력 변수명[인덱스] ---> list의 element를 한개 빼오면 type이 list가 아님.
print(f'score=> {score[0]}, type => {type(score[0])}')
print(f'score=> {score[-1]}, type => {type(score[-1])}')
# 1,2,3번 요소 출력하기
print(f'score=> {score[1:4]}, {type(score[1:4])}')
# 규칙적 요소만 출력하기
# score[시작:끝:반복적으로 더할 값]
print(f'score 짝수요소=> {score[::2]}')
print(f'score 홀수요소=> {score[1::2]}')
print(f'score 3의 배수 요소=> {score[3::3]}')
# 복잡한 데이터-----------------------------------------------------------------------
data=[1,2,3,['a',[11,22],'b','c','d']]
#     0 1 2             3
#             0     1     2   3   4
#                 0   1
# 리스트 데이터의 갯수 확인 내장함수 => len(변수명)
print(f'data의 갯수=> {len(data)}')
print(f'data[0] : {data[0]}')
print(f'data[1] : {data[1]}')
print(f'data[2] : {data[2]}')
print(f'data[3] : {data[3]}')
print(f'data[3][0] : {data[3][0]}') # a 출력
print(f'data[3][1] : {data[3][1]}') # [11, 22] 출력
print(f'data[3][1][1] : {data[3][1][1]}') # 22 출력

