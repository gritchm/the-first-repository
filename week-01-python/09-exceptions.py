# exceptions
# 에러 처리는 Try & Except, 에러 일으킬때는 Raise
# Error 발생 시키면 좋은점은 이런 경우는 절대 있으면 안됨, 어떤 위치에서 났는지 확인
# 처음 예외는 모르면 고역이지만 알면 나중에 나에게 유리하게 쓸수있다 코드속에서도 활용가능


# #ZeroDivisonError
# 1/0

#try 는 예약어
#try 블록 수행중에 오류가 발생하면 except 블록이 수행된다.
#except 오류이름을 적는경우, 이름이 일치하는경우만 블록을 수행하게됨

def divide_by(first,second):
    try:
        return first/second
    #except:예외의 이름을 직접적어줘야 나중에 처리가능
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
#4/2=2
print(divide_by(4,2))
print(divide_by(4,0))


# Exception 만들기 - 클래스의 상속 개념통해서 만들기
# Exception 클래스가 있음 in python
#프로그램 수행 도중 특수한 경우에만 예외처리를 하기 위해서 종종 오류를 만들어서 사용하게 된다
# Pass: Class 나 Def 의 내용을 지금당장 구현 X 패스하겠다 말그대로
# 개발중에 지나가거나 상속을 받는경우 추가구현 필요없기때문에
# Class의 경우 Camelcase사용
# Def는 _ 사용
class EvenNumberDevisionError(Exception):
    pass

def divide_by_odd_number(first,second):
    if second % 2 == 0:
        raise EvenNumberDevisionError
    else:
        return first / second

print(divide_by_odd_number(6,3))
print(divide_by_odd_number(6,2))
