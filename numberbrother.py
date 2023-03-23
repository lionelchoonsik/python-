#chapter03_01
#숫자형

#파이썬에서 제공하는 모든 typr(외울필요 절대 없음)
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list[] : 리스트 (시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""
#데이터타입
str1 ='pyhton'
bool = True
str2='anaconda'
float_v=10.0 #10==10.0
int_V=7
list=[str1,str2]
dict={
    "name": " machine learning",
    "version":2.0
} #name , version 은 key 임 2.0 과 머신러닝을 꺼내기 위해서는 name 과 version 입력이 필요함,사전형태

tuple=(7,8,9)
set={3,5,7}

# 괄호타입 list[] , dict{} , tuple(), set{}

#데이터타입출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_V))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(a,b): a의 y 제곱 = a**y = **해도 제곱이라는 의미
"""

#정수선언
i=77
i2=-13
big_int=76777777777777777777777777777777777

#정수출력
print(i)
print(i2)
print(big_int)

#실수출력
f1=0.9999
f2=3.14259
f3=-3.9
f4=3/9

print(f1)
print(f2)
print(f3)
print(f4)

#연산 실스  
i=39
i2=939
big_int=3827973298288888888888888
big_int2=8222222222222222222222
f1=0.2
f2=3/9

# + 계산
print(">>>>>> +")
print("i1+i2 :",i+i2)
print("f1+f2=",f1+f2)
print("big_int1+big_int2=",big_int+big_int2)

# * 계산
print(">>>>>> *")
print("i1*i2 :",i*i2)
print("f1*f2=",f1*f2)
print("big_int1*big_int2=",big_int*big_int2)

#형변환 실습
a=3. #0 을 생략할수있음 
b=6
c=.7 #0.7이라는 의미
d=12.7

#타입출력 = int 인지 float 인지 뭔지출력해주는거
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#형 변환
print(float(b)) #int b 는 6이라 정수였는데 float인 실수로 형변환을 시켜줌
print(int(float(b))) 
print(int(c))
print(d)
print(int(True)) # True 는 1을 의미하고 False 는 0을 의미함
print(float(False)) # false는 0인데 0의 float 형이니까 0.0 이 나옴
print(complex(3)) #복소수 : 문자형 -> 숫자형 (3+0j) 라고 나옴 거의 쓸일없음 ㅋㅋ개꿀
print(complex(False))

#수치연산함수
print(abs(-7)) #절대값

x,y=divmod(100,8) #divmod 는 100을 8로 나눈다음에 x에 몫 y에 나머지를 쓰는 함수임
print(x,y)
# divmod(100,8)=x,y 이 순서로 하면 에러뜸 무조건 x,y를 앞에 써야함

print(pow(5,3)) # 5의 3제곱

#외부모듈
import math #외부에서 끌어다 쓰는 모드 .이건 수학모드임

print(math.ceil(5.1)) #5.1 이상의 수에서 가장 작은 정수
print(math.pi) #파이를 호출해줌
