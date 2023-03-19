#chapter02-1-ex1
#파이썬왕기초
#print 사용법(2023년 추가)
#파이썬에서 3가지 print Formatting
#자주 나오는 질문도 참고함

"""" 
참고 : Escape code
\n : 개 행
\t : 문자
\\ :문자
\' :문자
\" : 문자
\000 : 널 문자
...
"""
###3가지 Format Practice

x=50
y=100
text=308276567
n='lee'

#출력1
ex1='n=%s,s=%s,sum=%d'%(n,text,(x+y)) #d=정수 s=문자열
print(ex1)

#출력2
ex2='n={n},s={s},sum={sum}'.format(n=n,s=text,sum=x+y) #이게 많이 사용됨
print(ex2)

#출력3 <-new!
ex3=f'n={n},s={text},sum={x+y}' #개편함 ㅋㅋ 걍 f'n={},~,' 이렇게만 해주면됨 f''  -->new!
print(ex3)


#구분기호
m=100000000
print(f'm:{m:,}') #,만 출력했을 뿐인데 알아서 구분기호로 나옴;;;;


#정렬
#^ : 이게 바로 가운데정렬 , < : 왼쪽정렬 , > : 오른쪽정렬
t=20
print(f't:{t:10}') #10자리를 확보함
print(f't center:{t:^10}') #가운데정렬
print(f't:{t:<10}')#왼쪽정렬


print(f't center:{t:-^10}')#10칸중 빈칸은 -로 채워줌
print(f't center:{t:。<10}')