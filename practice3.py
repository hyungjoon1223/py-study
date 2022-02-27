# 문자열

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""

print(sentence3)

# 슬라이싱

jumin = "961223-1234567"

print("성별 : " + jumin[7])
print("연 :" + jumin[0:2])  # 0 부터 2 직전까지 ( 0, 2 )
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 :" + jumin[:6])
print("뒤 7자리 :" + jumin[7:])
print("뒤 7자리 (뒤에서부터) :" + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())  # 모두 소문자로 출력
print(python.upper())  # 모두 대문자로 출력
print(python[0].isupper()) # 첫번째 자리의 문자는 대문자인가? True
print(len(python)) # 문자열의 길이를 알려줌
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java"))  # -1 값을 반환 원하는 값이 없을 떄는 -1 반환
#print(python.index("Java")) 오류가 발생해서 프로그램이 돌아가지 않음
print('hi') # 46라인이 오류면 이 문장도 실행되지않고 에러

print(python.count("n"))  # n이 몇개인가?
