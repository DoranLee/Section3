# input() 함수
# input('화면에 출력할 내용')
name = input('이름을 입력하세요 : ')
print('입력하신 이름은 {}'.format(name))
print(type(name))  # 무엇을 입력하든 str type

# 문자열로 입력 받은 후 원하는 타입으로 형변환해야 함
# 정수 입력 (int)
num = int(input("숫자 하나 입력 : "))
print('입력하신 숫자는 {}'.format(num))
print(num, type(num))

# 실수 입력 (float)
r = float(input("원의 반지름 하나 입력 : "))
print('입력하신 반지름은 {}'.format(r))
print(r, type(r))

