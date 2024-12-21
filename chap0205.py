#문자형 : 중요
# len : 문자의 길이 구해주는 함수
# str : 문자형
# 이스케이프 형식 : \ ['I\'m boy'] 여기는 '' 만 씀
# \t : tab 만큼 띄어쓰기
# \n :  줄바꿈
# raw string : 이스케이프 형식의 반대 , \들어가도 그냥 그대로 \출력하는거 raw_s1 =r"순무/t순무" 라고 씀

#문자열 생성
str1 = "나는 순무"
str2 = "나는 앵무"
str3 = "나는 앙무"
str4 = "고마워"

print(type(str1)) #<class 'str'>
print(len(str1)) #5

# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1)) # <class 'str'> 0
print(type(str2_t2), len(str2_t2)) # <class 'str'> 0

# escape 문자 사용

print("I'm boy") # 가능
# print('I'm boy') : 에러
print('I\'m boy') # 가능
print('a\t b') # a        b : tab 키만큼 간격이 벌어짐
print('a\n b') # 줄을 바꿔벌임
"""
a
 b
"""
print('a"\"b') #a""b

escape_str1 = "너는 \"순무\" 야?"
print(escape_str1) #너는 "순무" 야?
escape_str2 = '너는 순무\'s 야?'
print(escape_str2) #너는 순무's 야?

# 탭, 줄바꿈
t_s1 = "클릭 \t 순무" #클릭     순무
t_s2 = "클릭 \n 순무"
print(t_s1)
print(t_s2)

# Raw string 출력
raw_s1 =r"순무/t순무"
print(raw_s1) #순무/t순무
print()

#멀티라인 입력
multi_str ="""
문자열
멀티라인 입력
테스트
"""
multi_str2 ="""
문자열
멀티라인 입력
테스트
"""
print(multi_str)
print(multi_str2)
"""
문자열
멀티라인 입력
테스트


문자열
멀티라인 입력
테스트
"""

#문자열 연산
str_o1 = "순무는"
str_o2 = "바보"
str_o3 = "근데"
str_o4 = "귀여워"

#*****이거 진자 많이 쓰임*****
print(str_o1 * 3) #순무는순무는순무는
print(str_o1 + str_o2) #순무는바보
print('순' in str_o1) #순 이라는 글자가 str_o1에 있느뇨? 이렇게 물어보는거
print('귀여워' in str_o3) #귀여워 라는 글자가 str_03에 있느뇨? 없으니까  False로 나옴
print('귀여워' not in str_o3) #귀여워 라는 글자가 str_o3에 없느뇨? 없으니까 True 로 나옴

#문자열 형 변환
print(str(66),type(str(66))) #66 <class 'str'> 눈에 보이는건 숫자66으로 착각할 수 있지만 type으로 형을 알아보면 문자66이란걸 알 수 있음
print(str(10.1))
print(str(True),type(str(True))) #True <class 'str'>

#문자열 함수( upper isalnum, startswith count endswith isalpha 등등..)
str_o5 = "hi hi"
print("Capitalize:", str_o5.capitalize()) #첫글자를 대문자로 바꿔주는거
print("endswith:", str_o1.endswith("는")) # True :마지막 글자가 는 으로 끝나는지 확인할 수 있는거
print("replace:", str_o1.replace("순무는", "멍순무는")) # 멍순무는 : str_o1이 순무는 인데 이걸 멍순무는 이라고 바꿔줌
print("sorted:", sorted(str_o1)) # sorted: ['는', '무', '순'] 정렬해서 list 형태로 반환함
str_o6 = "야!니가!순무야?"
print("split:", str_o6.split("!")) #split: ['야', '니가', '순무야?'] : !를 기준으로 분리해서 lsit형태로 반환함

# 반복(시퀀스) like 버스정류장 줄서있는 사람들
im_str = "굿보이"
print(dir(im_str))
#출력 for i in im_str: -동안 i에서 im_str을 반복할거임 ㅅㄱ 라는 뜻
for i in im_str:
    print(i)

#슬라이싱 연습
str_s1 = "nice python"
print(len(str_s1)) #str_S1은 11글자임
print(str_s1[0:3]) # nic : 0 1 2 이렇게 나옴
print(str_s1[0:10]) # nice pytho
print(str_s1[:len(str_s1)]) #nice python
print(str_s1[1:11:2]) # iepto : 1부터 11인데 간격2띄워서 가져와라
print(str_s1[-5:]) # ython : 뒤에서 5번째부터 끌까지 나와라
print(str_s1[1:-2]) # ice pyth : 1번째글자부터 -2번째 글자 전까지 나와라
print(str_s1[::2]) #처음부터 끝까지 가져오는데 2칸 간격으로 가져와라

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) #122 : z에 해당하는 아스키코드는 122번이에요
print(chr(122)) # z : 아스키코드 122번에 해당하는 함수는 z에요
