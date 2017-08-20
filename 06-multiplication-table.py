#
# name = input("몇 단을 출력하시겠습니까? ")
#
# # input(" ")
# # a = input(" ")
# b = 1
# while b < 10:
#     print(int(name), "*", b, "=", int(name) * b)
#     b = b + 1

# format type use
name = int(input("몇 단을 출력하시겠습니까?"))
for num in range(1, 10):
    print("{} * {} = {}".format(name, num, name * num))

# for문 사용
name = int(input("몇 단을 출력하시겠습니까?"))
for num in range(1, 10):
    print(name, "*", num, "=", name * num)
