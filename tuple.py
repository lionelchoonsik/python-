#파이썬 튜플
#리스트와 비교 중요
#튜플 자료형 (순서o,중복o,수정x,삭제x) #불변 -> 한번 선언하면 끝까지 써야됨... 변하면 안되는 아주 중요한 문서들 쓸 때

#선언

'''
a=()
b=(1)

print(type(a),type(b)) # 두개 다 튜플로 나와야하는데 <class 'tuple'> <class 'int'> b는 숫자 하나라 인트로 나옴 그래서 튜플 한개를 쓸 때는 꼭 b=(1,) 이렇게 , 를 넣어줌 (2개부터는 노상관)
'''
a=()
b=(1,)
c=(11,12,13,14)
d=(100,1000,'Ace','Base','captin')
e=(100,1000,('Ace','Base','captin'))

#인덱싱
print(d[1])
print(d[1]+d[1])
print(d[-1]) #captin 나옴
print(e[-1]) #('Ace', 'Base', 'captin')
print(e[-1][1]) #base
print(list[e[-1][1]]) #list['Base']

#수정이 진짜 안될까??
'''d[0]=1500 ㄹㅇ 에러뜸'''

#슬라이싱
print(d[:3]) #(100, 1000, 'Ace')
print(d[2:]) #('Ace', 'Base', 'captin')
print(e[2][1:3]) #e에 2번째 숫자 ('Ace','Base','captin') 여기에서 1부터 3까지 나와라 ('Base', 'captin') 이렇게 나옴

#튜플 연산
print('>>>>>>>')
print('c+d=',c+d) #c+d= (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'captin')
print('c*3=',c*3) #c*3= (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)

#튜플함수
a=(5,2,3,1,4)
print(a)
print(a.index(3)) # a함수에서 숫자 3이 들어가 있는 부분은 몇번째ㅐ임? 답: 2번째
print(a.count(2)) #a 함수에는 2는 몇개나 들어있음? 답 : 1개

# ★팩킹,언팩킹(packing & unpacking)★

#팩킹 = 하나로 묶는거 , 즉 패키지, 패킹 이런뜻..
t=('foo','bar','soon','mu')
print(t)
print(t[0]) #foo
print(t[-1]) # mu

# 언팩킹1
(x1,x2,x3,x4)=t
print(type(x1),type(x2),type(x3),type(x4)) # <class 'str'> <class 'str'> <class 'str'> <class 'str'> 이렇게 나옴 . 즉 묶여잇던 걸 각각 풀어서 각각의 순서에 맞는 원소에 대입하는거
print(x1,x2,x3,x4) # foo bar soon mu

# 팩킹&언팩킹
t2=1,2,3 #() 괄호 유무 상관없이 걍 하나의 문자에 저렇게 묶여있으면 튜플 []은 리스트
t3=4,
x1,x2,x3=t2 
x4,x5,x6=4,5,6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)