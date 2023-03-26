#chapther03-6
#집합  sets 특징
#순서 x 중복 x
#중복 x가 뭔뜻이냐면 a=set(1,1,1,2,2) 이렇게 있으면 출력해도 1,2 밖에 출력안됨

#선언
a=set()
b=set([1,2,3,4]) #list를 set에 넣은것
c=set([1,4,5,6])
d=set([1,2,'pen','cat','dog'])
e={'foo','ba','o'} # 분명히 dictionary 형태인데 일반적인 딕셔너리 형처럼 'key':'value'  형태가 아니고 걍 값만 있다면 이거슨 set임
f={42,'foo',(1,2,3),3.141592} #이렇게 별거 다 넣을 수 잇음

print(type(a),a,2 in a) #<class 'set'> set() False '2 in a' 처럼 2가 a에 있냐고 물어보는것도 가능
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)

#튜플변환(set->tuple)
t=tuple(b) #set b를 튜플로 바꿔줌
print(type(t),t)#<class 'tuple'> (1, 2, 3, 4)
print(t[0],t[1:3]) # 1 (2, 3) : 이렇게 묶여진 값으로 잘 나옴

#리스트변환(set->list)
l=list[c]
ll=list[e]
print(type(l),l)
print(type(ll),ll)

#길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

#집합 자료형 활용
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2) # s1 과 s2 의 교집합을 보여줘 라는 뜻 {4, 5, 6}나옴
print(s1.intersection(s2)) #이것도 위랑 똑같은 말임. intersection 이 & 로 된거...

print(s1|s2) #합집합
print(s1.union(s2)) # 위랑 똑같은 합집합 |==.union

print(s1-s2) #차집합
print(s2.difference(s2)) #차집합 -==difference

#중복원소가 있는지 알려주는 함수
print(s1.isdisjoint(s2)) #false 가 나오면 중복원소가 있다는 뜻이고 true면 없다는 뜻

#부분집합이 있는지 확인해주는 함수
print(s1.issubset(s2)) #s1이 s2의 부분집합이냐? 라고 묻는거 이것도 true false 로 나옴
print(s1.issuperset(s2)) #이건 반대의 경우.. 

#추가&제거
s1=set([1,2,3,4])
#데이터 추가하는 메소드 : add
s1.add(5)
print(s1) #{1, 2, 3, 4, 5}라고 나옴
#데이터 제거하는 메소드 : remove,discard
s1.remove(5)
print(s1) # {1, 2, 3, 4} 라고 나옴
s1.discard(1)
print(s1) #{2, 3, 4} 라고나옴
#싹 지우고 싶을때 (이건 list도 쓸 수 있음)
s1.clear()
print(s1) #set() 안에 있던 데이터가 다 지워짐
a=[1,2,3,4]
a.clear()
print(a) #[] 라고나옴

