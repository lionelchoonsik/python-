#chapter04-1
#파이썬 제어문
#if실습 ★ㅁ★
'''
한글 깨질때...!
import sys
import io
이거 맨 위에다 붙이면됨 ㅋㅋ
'''

#기본형
print(type(True)) #<class 'bool'> 0이 아닌 수,'abc' 이런 문자들 ,[1,2,3,4],(1,2,3),{1,2,3}... 이런건 다 트루로 취급함
print(type(False)) #<class 'bool'> 0," ",[],{} 이렇게 0 이거나 빈 문자열 이면 false 라고 취급함

#example
if True:
    print('good') #good 이 문자열이기 때문에 True여서 실행되는거임 만약 good 이 아니고 0이거나 빈문자열이었으면 false로 취급되서 아예 출력이 안나옴

if False:
    print('bad')

#example2
if True:
    print('bad!')
else:
    print('good!')

#관계연산자
#>,>=,<,<=,==,!= (!= 는 같지 않다 라는 뜻)

x=15
y=10
#양변이 같은 경우 참
print(x==y) # False라는 답이 나옴

#양 변이 다를 때 참
print(x!=y) #True라고 나옴 

#왼쪽이 클 때 참
print(x>y)

#왼쪽이 크거나 같을 때 참
print(x>=y)

#오른쪽이 클 때 참
print(x<y)

#오른쪽이 크거나 같을 때 참
print(x<=y)

#example3
city=""
if city:
    print("you are in: ",city) #이건 city가 빈칸이라 답이 false기 때문에 당연히 실행이 안됨 만약 city='zz'면 실행됨

else:
    print("please enter your city")

#example4
city2="bucheon"
if city2:
    print("you are in: ",city2) # city2가 문자열이라 true여서 you are in:  bucheon 라고 실행됨

else:
    print("please enter your city")

#논리연산자(중요!)
# and , or , not

a=75
b=40
c=10

print(a>b and b>c) # a>b , b>c 를 모두 만족해야 true가 나옴
print(a>b or b>c) #둘중에 하나만 만족해서 true 뜸
print(not a>b) # a>b보다 큼...찐 맞음 근데 앞에 not이 붙었기때문에 반대로 출력되는거라 false 뜸
print(not c>b) 

#산술(+-*/), 관계(>= < <=) , 논리(and or not) 우선순위
#산술>관계>논리
print(3+12>7+3) #산술먼저해줌 3+12 / 7+3 그리고 관계를 따짐 15>10은 true니까 true 뜸
print(5+10*3>7+3*20) # 오른쪽이 더 크기때문에 false
print(5+10>3 and 7+3==10) # 1)5+10이 3보다 크다: true 2) 7+3==10이다 :true 3)true and true 니까 true
print(5+10>0 and not 7+3==10) #1)5+10>0 : true 2)7+3==10:true 3)true and not true ==true and false (not은 아예 반대로 바꿔줌) 답: false

#if else / 중첩부분
score1=90
score2='A'

#예시4)복수의 조건이 모두 참일 경우에 실행
if score1>=90 and score2=='A':
     print('pass')
else:
    print('fail')

#예시5
id1='vip'
id2='admin'
grade='platinum'

if id1=='vip'or id2=='admin':
    print('관리자 입장')
if id2=='admin' and grade=='platinum':
    print("최상위 관리자")
else:
    print('관리자아니면ㄲㅈ')

#예시6
#다중조건문 elif
#elif 개중요!!!!! else는 걍 if 아니면 다 저거 였는데 elif는 계속 조건 추가할 수 있음.....

num=90
if num>=90:
    print('grade: A')
elif num>=80:
    print('grade: B')
elif num>=70:
    print('grade: C')
else:
    print('you are loser')

#중첩조건문 if 안에 if가 있는것
grade='A'
total=70
if grade=='A':
    if total>=90:
        print('장학금 100% 님 ㅊㅋ') #A등급을 받은 학생 내에서 또 total 점수가 90점 이상인 사람들만 장학금 100%라는 뜻
    elif total>=80:
        print('장학금 80%') #A등급을 받은 학생중에 total 점수가 80 이상인 사람은 장학금80%
    else:
        print("장학금 50%") #A등급 받은 학생들중 여기에 포함되지 않은 학생은 장학금 50%
else:
    print("님은 공부못해서 장학금없음 ㅋㅋㅅㄱ") #애초에 A등급 아니면 장학금 아예 없음 ㅋㅋ

# in, not in
q=[10,20,30]
w={70,80,90,100}
e=dict(
    name='lee',
    city='seoul',
    grade='A')
r=(10,20,13)

print(15 in q) # false 
print(90 in w) #true
print(12 not in r) #12는 r 에 없어서 false 지만 not 이 붙어서 true가 됨
print('name'in e) 
print('seoul' in e) #이때 seoul은 e 에 있지만 key가 아니고 value에 있기때문에 이렇게 돌리면 false가 나옴 이때 
print('seoul' in e.values) # 이렇게 값 valuse를 호출하면 true 라고나옴 ㅋㅋ
