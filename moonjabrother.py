#chapther 03_2
#문자형 -개중요!!!!!!!!!!!
#참고로 str은 문자열 이라는 뜻임 ㅋㅋ

str1="i am python"
str2='java'
str3='babo'
str4='soonmu'

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))
#길이를 구해주는 함수 = len()

#빈 문자열
str1_t1='' #안에 어떠한 것도 넣지 않은 것
str2_t2=str( ) #고급스킬 str() 넣으면 빈칸임

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))

# escape 문자 
#I'm boy
print("I'm boy")
# 하지만 print('I'm boy')를 하면 error 뜰거임 왜냐면 'I' 가 한쌍으로 인식되기 때문에..omg 이때는
print('I\'m boy') # 이렇게 \ 작대기 해줌 \\\\\\\\
print('a \t b') # \t 간격 띄어주는거
print('a \n b') #\n 줄바꿈
print('a \"\" b') # a "" b 이런 값이 나옴

escape_str1='Do tou have \"soonmu\"?'
print(escape_str1)
escape_str2='what\'s that?'
print(escape_str2)

#탭과 줄바꿈 
t_s1="click \t star!"
t_s2="new Line \n check!"
print(t_s1)
print(t_s2)

# Raw String \자체를 신경 안씀
raw_s1=r'd\python\test' # 소문자 r을 반드시 써야 로우 스트링임
print(raw_s1) # d\python\test 라고 \ 그대로 나옴 \를 문자에 써야할 때 씀

#멀티라인 입력 , 단 옆에 \ 역슬레시 필수 > 여러줄에 걸쳐 한번에 입력하는거
multi_str=\
'''
가나다
라마바
사아자
'''
print(multi_str)

#ex.
multi_str2='''큐트한
순무
기여버'''
print(multi_str2)

# 문자열 연산
str_o1='python'
str_o2='apple'
str_o3='how are doing'
str_o4='seoul daejeon'

print(str_o1*3)
print(str_o1+str_o2)
print('y'in str_o1)
print('z'in str_o1) # 이거 중요함 뭔뜻이냐면 str_o1에 y가 있어? 라는 뜻임 true false로 대답해줌
print('P'not in str_o2) # P가 stro2에 없어?

#문자열 형 변환
print(str(66),type(str(66))) #이새끼 형변환해도 66으로 나오는데? > 타입뭔지 돌려보면 66이 str로 나옴. 즉 문자 66이라는뜻
print(str(10.1),type(str(10.1)))
print(str(True),str(False)) #이건 그대로 트루 펄스로 나옴
print(int(True),int(False)) # 이건 1 0 으로 나옴

#문자열 함수(upper isalnum starswith count endswith isalpha...)

print("capitalize : ",str_o1.capitalize()) #.capitalize() 첫번째 글자만 대문자로 바꿔줌
print("endswith? : ",str_o2.endswith("s")) # .endswith("s") 끝글자가 s 냐고 물어보는 함수
print("replace : ",str_o1.replace("thon","good")) #str_o1 이 python 인데 여기 박혀있는 thon을 good으로 바꿔줌
print(str_o1.replace('py','pi'))
print("sortde : ",sorted(str_o1)) #이건 sort(str_o1) 로 해야댐  sortde :  ['h', 'n', 'o', 'p', 't', 'y']
print("split : ",str_o4.split('a')) # 'a'를 기준으로 단어를 분리할 때 씀 split :  ['seoul d', 'ejeon']

#반복 (시퀀스squence)
im_str='i\'m a good boy'
print(dir(im_str)) #  __iter__ 라는게 있다 하면 시퀀스임 > 반복이 된다는 뜻
#반복문 찍먹
for i in im_str:
    print(i)

#❤️슬라이싱 
str_s1='nice python'

print(len(str_s1)) #len 11개가 나옴 

#슬라이싱 연습
print(str_s1[0:3]) # 0번째글자부터 3번째 글자까지만 나와라 nic까지만 나오는거임
print(str_s1[5:11]) #공백도 문자취급하는거임 0번째글자=n 1=i 2=c 3=e 4=공벡 5번째글자=p ....
print(str_s1[:len(str_s1)]) # 앞에 안적으면 걍 첨부터 시작한거임 len(str_s1)은 글자수 전체 다 나타내는거니까 걍 문장 처음부터 끝까지 다 나오는거
print(str_s1[:len(str_s1)-1])# -1 해줫으니까 nice pytho 만 나옴
print(str_s1[1:4:2]) #1번째 글자부터 4번째까지 가져오는데 2개 단위로 가져와라 : ie 만 나옴
print(str_s1[-5:len(str_s1)]) # -는 글자 왼쪽부터 세는거임 y부터 끝까지 출력해라 
print(str_s1[1:-2]) # i부터 -2까지 나와라 : ython
print(str_s1[::2]) # 처음부터 끝까지 출력하는데 2칸 간격으로 출력해라
print(str_s1[::-1])# 처음부터 끝까지 출력하는데 순서를 오른쪽부터 출력해라 : nc yhn

#아스키코드(또는 유니코드)
a='z'
#z의 아스키 코드는 122이다.
print(ord(a)) # ord 는 아스키코드 호출. z의 아스키코드를 알려준거임
print(chr(122)) # chr은 아스키코드를 알파벳으로 보여주는거 