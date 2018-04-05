# # 목록 List, tuple
# # 사전 dict - dictionary
# # 집합 set
# # List
# print("list")
# list_a=[1,2,3]
# print (list_a)
# #print (type([1,2,3]))
# #index 는 0부터 시작합니다.
# # print(list_a[0])
# # print(list_a[1])
# # print(list_a[2])
#
# #slice 는 list 를 짜는것 마지막 숫자 포함 안됨
# # print(list_a[0:1])
# list_a.append(4)
# print(list_a)
# list_a.remove(2)
# print(list_a)
# list_a.clear()
# print(list_a)

# tuple (1,)
print ("tuple")
tuple_a=(1,2,3)
print(tuple_a)
print(type(tuple_a))
tuple_a.append(4)
#tuple은 한번 생성 후 내부값 변경 불가

#dict (map) {}
#key & value
# dict_a={
#     "apple":"a type of fruits",
#     "pen" : "a thing to write"
#     }
#
# print(dict_a)
# print(dict_a["apple"])
# #edit value
# dict_a["pen"]="something to write"
# print(dict_a)

#set set([])
#set 은 집합
set_a= set([1,2,3])
set_b= set([2,4,6])
print(set_a)
print(set_b)

#교 합 차 여 집합
# 중복이 없다-중복제거 중요
print(set_a & set_b)
print(set_a )
