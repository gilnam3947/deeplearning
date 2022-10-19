##############딕셔너리
#딕셔너리(dictionary)도 값을 저장하는 자료구조이다. 하지만 딕셔너
#리에는 값(value)과 관련된 키(key)도 저장된다. 
# 사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 며칠" 등으로 구별할 수 있다.
# 파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다. 
#요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데,
# 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

#파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 하는데, 
#단어 그대로 해석하면 사전이라는 뜻이다. 즉 "people"이라는 단어에 "사람", 
#"baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 
#딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형이다. 
#예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

#딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 
#Key를 통해 Value를 얻는다. 이것이 바로 딕셔너리의 가장 큰 특징이다.
#baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는
#것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.




import numpy as np;

# 딕셔너리 선언
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)

# 딕셔너리 공백 만들고 추가
capitals ={}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"  # 키와 값
print(capitals)


# 딕셔너리 항목 방문하기
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
    print( key,":", capitals[key])
    
    
    
# 딕셔너리 함축 pdf 39page
values =[1,2,3,4,5,6] 
dic ={ x : x**2 for x in values if x%2==0 }
print(dic)

# 딕셔너리 함축의 예
dic ={ i:str(i) for i in [1,2,3,4,5]}
print( dic )

fruits =["apple","orange","banana"]
dic ={ f:len(f) for f in fruits }
print( dic )    