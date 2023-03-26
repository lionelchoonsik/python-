#chapter03-5
#파이썬 딕셔너리(key&value)
#범용적으로 가장 많이 사용
#순서가 없고 , key 중복을 허용하지 않음 , 수정 o, 삭제o

#선언
'''
tuple:
a=()
a= 빈칸

list:
a=[]

dictionary:
a={}
'''
a={'name':'kim','phone':'010779970192','birth':'000615'} #a={'key' : '값'} 이렇게 선언하는 형식
b={'0':'hello soonmu'}
c={'arr': [1,2,3,4]}
d={
    'name':'kimyewon',
    'city': 'bucheon',
    'age': '24',
    'grade': '4'
} #긴거 선언할 때는 이렇게 엔터쳐서함

e=dict(
    name='kimsoonmu',
    city='bucheon',
    age='9'
) # 이게 더 편함!!! 개꿀 ㅋㅋ {}앞에 dict 만 써주면 됨

print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)

#출력
print(a['name'])#a의 name을 가져와라 = kim 가져옴
print(a.get('mom')) #> mom 이런 key 안적어놧음 ㅋㅋget으로 접근할 경우에는 없는 key를 적어도 에러가 뜨지않고 none 으로 떠서 편하게 디버깅간응
print(b.get(0))# == print(b[0])
print(e.get('city')) # bucheon 나옴
print(e.get('age')) #순무 나이 나옴 ㅎㅎ

#딕셔너리 추가
a['address']='seoul' #{'name': 'kim', 'phone': '010779970192', 'birth': '000615', 'address': 'seoul'} 주소가 추가됨
print(a)
a['kg']=['밥먹고난뒤 4.5kg','굶고난뒤 4.2kg']
print(a)

#딕셔너리 길이
print(len(a)) #len은 key의 개수를 세는 거임
print(len(b))
print(len(c))
print(len(d))
print(len(e))

#dict_keys , dict_values, dict_items :반복문 iter에서 쓰는데 지금 안배움

print(a.keys()) #dict_keys(['name', 'phone', 'birth', 'address', 'kg']) 키 값들만 가져옴
print(b.keys())
print(c.keys())
print(d.keys())
print(e.keys())

print(list(a.keys())) #['name', 'phone', 'birth', 'address', 'kg'] list 형태로 나옴

print(a.values()) # 값 value 만 가져오는거 
print(b.values())
print(c.values())
print(d.values())

#key와 values 를 동시에 가져오는 메소드도 있을까? 있다
#item!!!
print(a.items()) # key + 값 둘 다 가져옴 
print(b.items())
print(c.items())
print(d.items())

print(a.pop('name')) #a의 name 을 꺼내서 가져갈거얌 kim
print(a) #name 딕셔너리가 없어짐... 
'''e=dict(
    name='kimsoonmu',
    city='bucheon',
    age='9'
) '''
print(e.popitem())
print(e) # 끝에있는 키와 값이 사라짐...
print(e.popitem())
print(e) 
print(e.popitem())
print(e)
'''
('age', '9') 첫번째 e.popitem해서 age:9를 뜯어옴
{'name': 'kimsoonmu', 'city': 'bucheon'} 나이를 뜯어오니까 e에서 남는게 이거임
('city', 'bucheon')두번째 e.popitem 해서 city를 뜯어옴
{'name': 'kimsoonmu'} 그래서 남는게 이거임.
('name', 'kimsoonmu') 세번째 e.pop해서 마지막 남은것도 뜯어감..
{} 결국 딕셔너리안에 아무것도 안남게됨 ㅇㅇ
''' 
#in 연산자
print('birth' in a)#birth 라는 key가 a안에 있어? 라는 뜻 true false 로 답 나옴
print('city'in b)

#수정 -보완설명
a['test']='test_dict'
print(a) #이건 추가하는법

a['address']='daegu'
print(a) #이건 수정하는법

a.update(birth='910904') #정확하게 수정하는법 birth의 값을 910904로 바꿔줌
print(a)

temp={'address':'busan'} #또다른 수정법
a.update(temp)
print(a)