# 사전

#cabinet = {3:"황형준", 100:"송보경"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5)) 
# print(cabinet.get(5),"사용 가능")
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3":"황형준", "B-100":"송보경"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabient["A-3"] = "김김김"
# cabinet["C-20"] = "뇸뇸뇸"  #사용중이라면 값 업데이트
# print(cabinet)

# 간 손님
del cabinet ["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 같이 출력 할 때
print(cabinet.item())


# 목욕탕 폐점
cabinet.clear()
print(cabinet)