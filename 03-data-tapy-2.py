# 목록 list , tuple
# 사전 dict - dictionary
# 집합 set

# list [] 사용
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))

# index는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])

# slice라는건 마지막 인덱스는 포함하지 않음.
print(list_a[0:2])

# append 는 리스트에 새로운 항목에 추가하고자 할 때 사용한다.
list_a.append(4)
print(list_a)
# remove는 해당 항목만 리스트에서 삭제할 때
list_a.remove(2)
print(list_a)
# clear 는 리스트 전체 항목을 삭제할 때
list_a.clear()
print(list_a)

# tuple () 가로에 값을 넣어주고 쉼표를 넣어줌으로 사용 가능
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
