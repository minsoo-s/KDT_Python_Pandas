# --------------------------------------------------------------
# 변수의 동작 범위 (Scope 스코프)
# --------------------------------------------------------------
# - 전역변수(Global Variable)  ---> 많이 사용하면 메모리 차지를 많이 해서 좋은 습관은 아님.
#     > 프로그램 실행 시 메모리에 생성
#     > 프로그램 종료 시 메모링에서 삭제
#     > 파일 안에 모든 곳에서 사용가능한 변수

# - 지역변수(Local Variable)
#       > 함수 실행시 메모리에 생성
#       > 함수 종료시 메모리에 삭제
#       > 함수 안에서만 사용 가능한 변수
#----------------------------------------------------------------
year=2022
msg="행복한 주말이군요!"

def testVariable(num):
    global year # 전역변수 수정 사용 알림
    year=3000
    print(num)
    print(year)
    print(msg)

testVariable(1000)
# print(f'num => {num}') ---> 함수안에 존재하는 지역변수는 사용불가.
print(f'year => {year}') #---> 전역변수 수정했기 때문에 함수 안, 밖 모두 year=3000이 된다.
                         #     만약, 전역변수 수정하지 않으면 함수 안의 year=3000, 함수 밖의 year=2022

# [print 기본값]--------------------------------------------------------------
# sep=" " ---> 기본 공백 설정되어 있음
# end="\n" ---> 기본 줄바꿈 설정되어 있음
# ---------------------------------------------------------------------------
print(10,20,30)
print(10,20,30, sep="*") #---> 공백 대신 '*' 삽입됨.
print(10,20,30,40, end='') #---> 줄바꿈 없어짐.
print(10,20,30)