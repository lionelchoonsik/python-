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