# divmod : 몫과 나머지
# abs : 절대값
# pow(2,3) == 2**3
# import : 외부에서 끌어다 쓰는거


#정수는 a만 나머지는 실수
a = 3. #3.0
b = 6
c = .7 #0.7
d = 12.7

# 타입 출력
print(type(a),type(b),type(c),type(d)) #<class 'float'> <class 'int'> <class 'float'> <class 'float'>

#형변환
print(float(b), int(a), int(c), int(d)) #6.0 3 0 12
print(int(True)) # 1 : 참은1 거짓은0
print(float(int(False))) #0.0
print(complex(3)) # 복소수 (3+0j)
print(complex(False)) #0j

#수치연산함수
print(abs(-7)) #abs는 절대값
x, y =divmod(100,8) # divmod는 100을 8로 나눴을 때 몫과 나머지의 변수를 알려줌
print(x,y) # 12,4 
print(pow(5,3),5**3) #125 125

#외부 모듈 : 외부에서 끌어다쓰는거
import math
print(math.ceil(5.1)) # 6 : 5.1 이상의 수 중에서 가장 작은 정수를 찾음
print(math.pi) #3.141592653589793