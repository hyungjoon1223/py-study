# 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")   #튜플은 add라는 기능을 지원하지 않음

# name = "황형준"
# age = 27
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("황형준", 27, "코딩")
print(name, age , hobby)

# 집합 (set) /// 중복 x 순서 x
my_set = {1,2,3,3,3}
print(my_set)

java = {"황형준", "송보경", "권현도"}
python = set(["황형준", "박명수"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python를 할 수 있는 개발자)
print(java | python)
print(java.union(python))  # 순서가 보장되지 않음 랜덤

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어나 
python.add("김재우")
print(python)

# java를 까먹은사람
java.remove("김재우")
print(java)


#자료구조의 변경


