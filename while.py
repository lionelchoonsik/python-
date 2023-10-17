#chapther04-3
#python 반복문

#while <expr>:
#     <코드 작성(s)>

#while은 if문이랑 똑같음 , 단 조건을 만족할 때까지 무한 반복

#예제1
n=5
while n>0:
    n=n-1 #이 조건이 없으면 무한 반복됨
    print(n) 
    
#예제2

a=["foo","bar","abz"]

while a:
    print(a.pop(-1))
#a만 출렦하면 저 세 단어가 ㅈㄴ반복됨 이때 pop을 해주면 하나씩 빠지면서 출력됨
#pop은 끝에꺼를 빼주는 코드임
"""
abz
bar
foo
"""
#예제3
#break , continue
n=5
while n>0:
    n-=1
    if n==2:#n이 2일때 멈춤
        break
    print(n)
print("end")
"""
4
3
end
"""
#예제4
m=5
while m>0:
    m-=1
    if m==2:
        continue #2는 cintinue이기 때문에 while m>0으로 다시 감 그래서 1이 나오는거임
    print(m)
print("end")
"""
4
3
1
0
end
"""
#if 중첩
#예제5

i=1

while i<=10:
    print('i:',i)
    if i==6:
        break
    i+=1


#while - else 구문
#예제 6

n=10
while n>0:
    n-=1
    print(n)
    if n==5:
        break

else:
    print('else out')


#예제 7
a=['poo','ba','baz','px']
s='qux'
while i<len(a): #len(a)는 4임 왜냐면 저기 []안에 들어있는 글자가 4단어니까
    if a[i]==s:
        break
    i+=1
else:
    print(s,"not found in list")

#무한반복
#while True  -> 이러면 ㅈ댐

#예제8
a=['poo','ba','baz','px']

while True:
    if not a:
        break
    print(a.pop())

"""
px
baz
ba
poo
"""