last_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = int(input('1~12 사이의 월을 입력하세요 >>> '))
print('{}월은 {}일까지 있습니다'.format(m,last_day[m]))
