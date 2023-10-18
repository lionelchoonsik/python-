#chapter 05-1
#파이썬 함수 및 중요성
#파이썬 함수식 및 람다(lambda)

#함수 정의 방법
#def function_name(parameter):
#    code

#예제1
def first_func(w):
    print("hello, ",w)

word='goodboy'
first_func(word)
"""
hello,  goodboy
"""

#예제2
def return_func(w):
    value="hello, "+str(w)
    return value

x=return_func('goodbab')
print(x)
"""
hello, goodbab
"""

#예제3(다중반환)
def func_mul(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return y1,y2,y3
x,y,z=func_mul(10)
print(x,y,z)
"""
100 200 300
"""

#튜플 리턴
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return y1,y2,y3

q=func_mul2(20)
print(type(q),q,list(q))
"""
<class 'tuple'> (200, 400, 600) [200, 400, 600]
"""

#list 리턴
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return [y1,y2,y3]

p=func_mul2(30)
print(type(p),p,set(p))
"""
<class 'list'> [300, 600, 900] {600, 900, 300}
"""

#dictionary 리턴
def func_mul3(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return ["v1:",y1,"v2:",y2,"v3:",y3]

d=func_mul3(30)
print(type(d),d)
"""
<class 'list'> ['v1:', 300, 'v2:', 600, 'v3:', 900]
"""

#중요
#*args  **kwargs 
# 별표가 하나붙은거 (언팩킹) ->솔직히 뭔말인지 모르겠음;;ㅅㅂ
#택배상자를 푸는걸 언패킹 , 택배상자를 쌓는것을 팩킹이라고함
def args_func(*args):
    for i,v in enumerate(args):
        print('result:{}'.format(i),v)
        print('------')

args_func('lee')#호출
args_func('lee','park')

"""
result:0 lee
------
result:1 park
------
"""
# **별표가 두개붙은거 (언팩킹)
def kwargs_func(**kwargs): #key와 value인 것을 매개변수로 넘길 때 사용하는것
    for v in kwargs.keys():
        print("{}".format(v),kwargs[v])
        print('------')

kwargs_func(name1='kim')
kwargs_func(name1='kim',name2='park')
"""
name1 kim
------
name1 kim
------
name2 park
------
"""

#전체혼합예제
def example(arg_1,arg_2,*arg,**args):
    print(arg_1,arg_2,arg,args)

example(10,20,'lee','kim','park',age1=20,age2=30,age3=40)
"""
10 20 ('lee', 'kim', 'park') {'age1': 20, 'age2': 30, 'age3': 40}
"""

#중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num+100)

nested_func(100) 
"""
in func
200
"""

#실행불가
#func_in_func(1000)

#lambda식 예제
#메모리 절약, 가독성 향상, 코드간결
#함수는 객체 생성-> 리소스(메모리)할당
#람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화
#남발 시 가독성 오히려 감소
"""
def mul_func(x,y):
    return x*y
# 위 식을 람다식으로 바꾼게 밑의 식임 == 두개가 똑같은.. return을 그냥 : 하나로 퉁침
lambda x,y:x*y
"""
def mul_func(x,y):
    return x*y
mul_func(10,50)
print(mul_func(10,50))
mul_func_var=mul_func
print(mul_func_var(20,50))
"""
500 나옴
1000 나옴
"""

#lambda
lambda_mul_func=lambda x,y:x*y

print(lambda_mul_func(50,50)) #2500 나옴 ㅋㅋ 쉬움 개꿀

def func_final(x,y,func):
    print(x*y*func(100,100))
    
func_final(10,20,lambda x,y:x*y)
