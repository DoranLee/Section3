# 이스케이프 : 특수문자 표현 방식, \ 역슬래쉬로 시작되는 문자열
# 줄바꿈 : \n (=Enter)
print('H\ne\nl\nl\no')

# 탭 : \t
print('번호\t이름\t\t번호')
print('1\t김철수\t1234')
print('2\t이훈\t\t2634')

# ", ' 출력 : \", \'
print("오늘은 \"파이썬\" 수업이 있는 날입니다.")   #C/C++/JAVA/C#
print('오늘은 "파이썬" 수업이 있는 날입니다.')     #Python만
print("오늘은 '파이썬' 수업이 있는 날입니다.")

# 키워드 속성
# 1. sep : 출력할 데이터들 사이에 넣을 문자열 / 생략시 공백
print(2022,1,18) #출력할 데이터 사이에 공백
print(2022,1,18,sep='-')
print(2022,1,18,sep='/')
# 2. end : 출력 후 넣을 문자열 / 생략시 줄바꿈
print('김철수',end=',') #줄바꿈되지 않고 ',' 들어감
print('김철수')
