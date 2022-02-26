#연산자
'''
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3  = 8   제곱
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 1
print(10//3) # 몫 3
print(10//4) # 몫    ex) 10 / 5 = 2 에서 몫은 2

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # 3은 3과 같은가? True
print(4 == 2) #False
print(3 + 4 == 7) # True

print(1 != 3) # 앞두가 같지않으면 True
print(not (1 != 3))

print((3 > 0) and (3 < 5)) # 앞뒤가 모두 만족 할 때 True = and연산
print((3 > 0) & (3 < 5)) # and 는 &로 대체 가능

print((3 > 0) or (3 > 5)) # 하나만 같아도 True
print((3 > 0) | (3 > 5)) # or sms | 로 대체가능 

print(5 > 4 > 3) #True  5는 4보다 크고 4는 3보다 크다  True
print(5 > 4 > 7) # False 


#간단한 수식

print(2 + 3 * 4) # 14
print((2 + 3 ) *4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)

number += 2
print(number)

number *= 2
print(number)

number /= 2
print(number)

number -= 2
print(number)

number %= 5
print(number)

#숫자처리함수
print(abs(-5)) # 5  abs는 절대값
print(pow(4,2 )) # 4^2   16 
print(max(5, 12)) # 최대값 반환 12 
print(min(5, 12)) # 최소값 반환 5 
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *  #math 라이브러리에 있는 모든 것을 이용하겠다
print(floor(4.99)) # 내림 . 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 무엇의 제곱근인가? 4 

#랜덤함수 (난수 무작위 숫자)
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random()* 10) # 0.0~ 10.0 미만의 임의의 값 생성
print(int(random() *10 ))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() *10 ))
print(int(random() *10 ))
print(int(random() *10 ) + 1) # 1 ~ 10 이하의 임의의 값 생성
'''

from random import *

#print(int(random() *45 ) + 1) # 1 ~ 45 이하의 임의의 값 생성
#print(int(random() *45 ) + 1)
#print(int(random() *45 ) + 1)
#print(int(random() *45 ) + 1)
#print(int(random() *45 ) + 1)
#print(int(random() *45 ) + 1)

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 randint는 자신포함