# [딕셔너리 자료형(dict)] ----------------------------------------------
# - 값의 의미와 함께 저장하는 방식
# - 형식 : { key1:값, key2:값,..., keyn:값}
# - 요소 읽는 방법 : key로 값을 읽어옴.
# - 요소 삭제 방법 : key로 값을 삭제함.
# - 요소 변경 방법 : key로 값을 변경함.
# ===> 자유롭게 추가, 삭제, 변경 가능.`
# (!) key가 중복일 경우, 마지막 key값만 인정됨!
# (!) 객체 생성 시, key는 Tuple 가능, List 불가능! (Value에는 list 가능.)  / (추가,변경,불러오기를 할때는) 변수[key] 형태
# (!) 인덱싱 없음 => 키(key) 요소 읽기 => 변수명[key]
# (!) dict 자료형 요소 값 변경 (새로넣기) => 변수명[key] = 새로운 값
# (!) del 변수명[key] 또는 del(변수명[key])
#---------------------------------------------------------------------


# dict 자료형 객체 생성 -------------------------------------------------
dNums ={}
dNums1 ={1:100, 2:200, 3:100}
dNums2 ={1:100, '2':200, 3:100, 1:555}  #---> key가 중복일 경우, 마지막 key값만 인정됨.
dNums3 ={('홍길동', '대구'):100, '2':200, 3:100, ('홍길동','부산'):555}  #---> key는 튜플 사용해야 함. 변경되면 안됨.(ListX)

print(f'dNums => 타입 : {type(dNums)}, 갯수 : {len(dNums)}, 데이터 : {dNums}')
print(f'dNums1 => 타입 : {type(dNums1)}, 갯수 : {len(dNums1)}, 데이터 : {dNums1}')
print(f'dNums2 => 타입 : {type(dNums2)}, 갯수 : {len(dNums2)}, 데이터 : {dNums2}')
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')


# dict 자료형의 요소 읽기------------------------------------------------------------
# 인덱싱 없음 => 키(key) 요소 읽기 => [key]
print(f'dNums1[1]=>{dNums1[1]}')
print(f'dNums1["2"]=>{dNums2["2"]}')
print(f'dNums3[(\'홍길동\', \'대구\')]=>{dNums3[("홍길동", "대구")]}')
print(f'dNums3[(\'홍길동\', \'부산\')]=>{dNums3[("홍길동", "부산")]}')


# dict 자료형 요소 값 변경 즉, 새로넣기 => 변수명[key] = 새로운 값
dNums3["홍길동","대구"]="053"
dNums3[3]="054"
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')


# del 변수명[key] 또는 del(변수명[key])
del dNums3[3]
del dNums3['2']
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')


# dict에 요소 추가하기 => 변수명[key] = 값  ----> dict에서는 값 변경이나 추가나 방법이 같음. (List에서는 다름)
dNums3['Good']=2022
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')

dNums3[1225]="크리스마스"
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')

dNums3[1225]="메리"
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 : {len(dNums3)}, 데이터 : {dNums3}')

# in -------------------------------------------------------------------------
# 부분 in 전체 (전체가 부분을 포함하는지 여부에 대한 참/거짓)
print('123' in dNums3 , ('홍길동', '부산') in dNums3)
print('a' in "abc", "A" in "abc")
print('a' in ('a', 'b',2), 'a' in (1,2))