#input 숫자로받기
#for 반복

# for i in range(2,3):
#     for j in range(1,3):
#         print(i*j)

#
# i=input("몇 단을 출력하시겠습니까? ")
# for j in range(10):
#         print(i*j)


#1)사용자로부터 몇 단을 출력할지 받을것
#2) 해당단을 곱하기 1에서 9까지 실행할것


dan=int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1,10):
    print("{}*{}={}".format(dan,num,dan*num))
