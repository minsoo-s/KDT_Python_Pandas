# ------------------------------------------------------------------
# 반복문 while 조건식:
# -------------------------------------------------------------------
count=0

print('----UP COUNNTING----')
while count<10:
    print(count)
    count=count+1

print('----DOWN COUNTING----')

while count>0:
    print(count)
    count=count-1

print('----1~50 범위에서 3의 배수----')
# -----------------------------------------------------------------------
# 리스트 데이터의 요소를 모두 출력
# -----------------------------------------------------------------------
# 1~50 범위에서 3의 배수로 구성된 데이터 만들기
nums=range(3,50,3)

idx=0
total=len(nums)
while idx<total:
    print(nums[idx])
    idx=idx+1

