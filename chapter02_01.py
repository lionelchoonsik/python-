#chapter02-1
#파이썬왕기초
#print 사용법

#기본출력
print('python star!')
print("python!")
print('''python!''')
print("""python!""")

#separator 옵션 = 띄어진 문자 사이에  sep=''으로 설정한 것을 넣어줌
print('p','y','t','h','o','n',sep='    ')
print('p','y','t','h','o','n',sep='')
print('p','y','t','h','o','n',sep='.')
print("010","7797","0192",sep="-")
print("python","google.com",sep="@")

#end 옵션=두 코드를 붙여줌
print('welcome to',end=' ')
print('IT news',end=' ')
print('website')

#file option
import sys
print('Learn pyhton',file=sys.stdout)
#EX) print('Learn pyhton',file='test.txt') 이 내용을 내가 지정한 test.txt 파일에 저장한다는 뜻 

#format 사용( d=정수 3  ,s=문자열 python  ,f=실수 3.1 등등 ..)
print('%s %s' % ('one','two')) #이걸 더 자주씀 -> 첫번째 s에 one 이 들어오고 ,두번째 s 에 two가 들어온다는 뜻
print('{} {}'.format('one','two')) #위에꺼랑 두개중에 하나 사용하면 됨
print('{1} {0}'.format('one','two')) # 0부터 시작인데 0이 뒤에있기 때문에 one 이 뒤에 옴ㅋㅋ

#2번째 수업

# %s
print('%10s' % ('nice')) #10자리수를 맞추는 함수
print('%10s' % ('nice1111'))
print('{:>10}'.format('mice'))

print('%-10s' % ('nice')) # 앞에 -가 붙으면 오른쪽부터 문자를 채워줌
print('%-10s' % ('nice1111'))
print('{:10}'.format('mice'))

print('{:_>10}'.format('mice'))
print('{:^10}'.format('mice'))#중앙정렬

print('%.5s'%('nice'))
print('%.5s'%('pythonstudy')) #5글자만 남기고 나머지는 삭제시켜주는함수(공간이 5개)
print('%5s'%('pythonstudy')) # . 안붙이면 안없어짐ㅋ
print('{:10.5}'.format('pythonstdy')) #공간은 10개만 있고 5개만 나오게 하는것


# %d
print('%d %d'%(1,2))
print('{} {}'.format(1,2))
print('%d   %d'%(3,4))
print('{}   {}'.format(3,4))

print('%4d'%(42)) #42를 네자리수로 만들어서 앞에 공백이 두개있음
print('{:4d}'.format(42))#:를 붙여줘야함

# %f
print('%1.8f'%(3.14348739)) #앞에 1.8이 정수는 1자리까지나오고 소수는 8자리까지 나오라는 뜻임
print('%3.4f'%(204.485747497))
print('%1.2f'%(23344444.22222))
print('{:f}'.format(3.1343434))
#example
print('%06.2f'%(3.142592)) # .포함해서 총 6자리로 만들어주는데 소수부분은 2번째까지만 나오고 부족한 정수부분은 0으로 채움
print('{:06.2f}'.format(3.142592))
print('%0000002.3f'%(3935.8034))
print('%07.3f'%(2.334455)) # .포함해서 총 7자리이고 소수점은 3자리까지 , 부족한부분은 0으로채움
print('{:<07.3f}'.format(2.334455))
# %s
print('%10s' %('nice')) #10자리수를 맞춰주는것
print('{:>10}'.format('nice'))#  > 이게 왼쪽 / 즉 왼쪽에서부터 시작해서 10자리로 만들어줘 라는 뜻
print('%.10s'%('haveagoodhayyou')) #10개만 나오게하는것
print('{:<11.5}'.format('haveagoodday')) #공간은 11개있는데 5개만나옴
print('{:>20.3}'.format('3983084040484'))
print('%-10s'%('nice')) #-는 오른쪽에서부터 채워준다는 뜻

# 결론 : 그냥 단어 를 출력할 때는 상관없지만 정수를 출력할때는 d , 실수를 출력할때는 f를 명시적으로 써줘야함