#chapter04-2
#파이썬 반복문
#for 실습(반복문)

#코딩의 핵심
#for in <collection>
#   <Loop body>

for v1 in range(10): #10개의 원소가 출력이 되는데 0부터 9까지 나옴. for v1 in rang(1000) 하면 0부터 999까지의 숫자가 출력되는거임
    print('v1 is',v1)
for v2 in range(1,11): 
    print('v2 is',v2) #1~10까지 나오는거
for v3 in range(1,11,2): #짝수의 집합, 홀수의 집합 구할 수 있음
    print('v3 is', v3) # 1~11까지 숫자 2 간격으로 나옴 1,3,5,7,9,11
print()
# 1~1000까지의 합을 구해보자
sum1=0
for v in range(1,1001):
    sum1+=v # ==   sum1=sum1+v
print('1~1000 sum: ',sum1)
#쉽게 구하는 방법 range
print('1~1000 sum: ',sum(range(1,1001)))
'''
a=b  (b를 a에 넣는다(할당한다) 라는 뜻)
a+=b  (복합할당 연산자: a=b+1, 즉 b+1을 a 에 할당한다)
a-=b   (a=b-1 , b-1를 a에 할당한다)
'''
#1부터 1000까지 숫자 중에 4의 배수를 구하시오
print('1~1000 4의 배수의 합: ',sum(range(4,1001,4)))

# Iterables 자료형 반복
#문자열 , 리스트 , 튜플 , 집합 , 사전 다 for문에서 사용 가능
# iterable 리턴 함수 : range , reverse , enumerate , filter , map , zip

#예제1
names=['kim','park','lee','choi']
for name in names:
    print('you are: ',name)
    '''
    you are:  kim
    you are:  park
    you are:  lee
    you are:  choi  
    name 이라고 하면 이렇게 성 4개 나오고 names라고 하면 모든 성 다 4번씩 나옴
    '''
#예제2
lotto_numbers=[11,19,21,23,38,87]
for n in lotto_numbers: # 이렇게 뒤에 갖다 붙이면 됨
    print('로또 번호는: ',n)
    '''
    로또 번호는:  11 
    로또 번호는:  19
    로또 번호는:  21
    로또 번호는:  23 
    로또 번호는:  38
    로또 번호는:  87
    '''
#예제 3번
word='beautiful'
for w in word:
    print('word: ',w)
    ''''
word:  b
word:  e
word:  a
word:  u
word:  t
word:  i
word:  f
word:  u
word:  l
    '''
#예제 4번
my_info=dict(
    name='lee',
    age='33',
    city='seoul'
)
for m in my_info:
    print('key',m)
'''
key name
key age
key city 
이렇게 key만 가져옴.. value 는 가져오지 않음
'''
for m in my_info:
    print('value',my_info[m])
    '''
value lee
value 33
value seoul
>my_info[m]하면 값 가져오기도 가능
    '''
for v in my_info.values():
    print('value: ',v)
    '''
value:  lee
value:  33
value:  seoul
>이렇게 해도 똑같음
    '''

    #예제5
name='fineApplE'
#이걸 전부 다 대문자로 출력하고 싶다?
for n in name:
    if n.isupper(): #isupper 대문자인지 검사하는거 islower는 소문자인지 검사
        print(n) # 검사해서 true 대문자로 나오면 그대로 n 출력
    else: #만약 아니라면 upper 시켜서 대문자로 바꿔서 출력함
        print(n.upper())

# 😊❤️break 문
#숫자 34를 찾아라

number=[14,3,4,7,10,24,17,2,15,34,36,46]
for n in number:
    if n==34:
        print("찾았어!: ",n)
        break
    else:
        print("아직 못찾음; 대신 이거 찾음: ",n)
'''
아직 못찾음; 대신 이거 찾음:  14
아직 못찾음; 대신 이거 찾음:  3
아직 못찾음; 대신 이거 찾음:  4
아직 못찾음; 대신 이거 찾음:  7
아직 못찾음; 대신 이거 찾음:  10
아직 못찾음; 대신 이거 찾음:  24
아직 못찾음; 대신 이거 찾음:  17
아직 못찾음; 대신 이거 찾음:  2
아직 못찾음; 대신 이거 찾음:  15
찾았어!:  34

'''

#continue (특정 데이터중에 불필요한 데이터를 continue 를 써서 skip 시키는거임)

 #예제
 #나는 bool형(True,False)를 빼고 출력하고싶어
lt=[1,2,'3',True,4.3,complex(4)] 
for l in lt:
    if type(l)is bool:
        continue #bool형은 skip
    print("current type: ",l,type(l)) #bool 형이 아닐 경우에만 출력 ㅇ
    #continue == pass 의 역할을 함
'''
current type:  1 <class 'int'>
current type:  2 <class 'int'>
current type:  3 <class 'str'>
current type:  4.3 <class 'float'>
current type:  (4+0j) <class 'complex'>

'''

#for-else 구문
number=[14,3,4,7,10,24,17,2,15,34,36,46]
for i in number:
    if i==49:
        print("찾았다 ")
        break
else:
    print("못찾음")

#구구단출력
for i in range(2,10,1):
    for j in range(1,10,1):
        print(i,"*",j,"=",i*j)
    print()
    """
    2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27

4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45

6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54

7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63

8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72

9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
    """

#변환예제
name2='soonmu'
print('reversed',reversed(name2)) # => 그냥 이렇게 출력하면 출력값이 안나옴... 형변환을 필수로 해줘야함
print('list',list(reversed(name2)))
print('tuple',tuple(reversed(name2)))
print('set',set(reversed(name2)))#set은 집합자료형이고 순서가 따로 없어서 뒤죽박죽임 그리고 같은 문자는 같은걸로 취급해서 한번만 나옴
"""
list ['u', 'm', 'n', 'o', 'o', 's']
tuple ('u', 'm', 'n', 'o', 'o', 's')
set {'o', 'm', 'u', 's', 'n'}
"""