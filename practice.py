'''숫자 자료형'''

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

'''문자열 자료형'''

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

'''boolean 자료형 (참, 거짓)'''

print(5>10)
print(5<10)
print(True)
print(False)
print(not True)  
print(not False)  
print(not ( 5>10 ))
'''not은 반대를 의미'''

''' 변수 (값을 저장하는 공간)'''
#애완동물 소개
''' 문자열자료는(' ') 안에  숫자형자료는 따옴표 없이 '''
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal +'의 이름은 ' + name + '예요')
print(name+'는 ' +str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name+'는 어른일까요?' + str(is_adult))


''' 중간에 변수 선언'''
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal +'의 이름은 ' + name + '예요')
hobby = '공놀이'
print(name+'는 ' +str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name+'는 어른일까요?' + str(is_adult))

''' +를 , 로 바꾸면 str 선언 안해도 됨 대신 띄어서 나옴'''
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal +'의 이름은 ' + name + '예요')
hobby = '공놀이'
print(name,'는 ' ,age, '살이며, ' ,hobby , '을 아주 좋아해요')
print(name+'는 어른일까요?' + str(is_adult))

''' Ctrl + / 전체 주석 '''