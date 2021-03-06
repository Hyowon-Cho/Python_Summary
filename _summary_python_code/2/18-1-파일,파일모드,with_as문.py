file = open('18.txt', 'w')
file.write('예시 파일입니다.')
file.close()

"""파일(file)
프로그래밍에서 중요한 부분중 하나가 파일처리임.
파이썬에서 파일은 파일객체로 사용할 수 있으며, open()함수로 파일을 열고, .close()메쏘드로 파일을 닫을 수 있음.

파일객체 = open(파일이름, 파일모드)
파일객체.close()

파일이름은 절대주소, 상대주소중 하나를 사용함.
그리고 파일의 이름과 확장자까지 들어가야함 (ex> '파일이름.txt')


파일모드는 종류가 다양함, 
파일 :
    읽기 전용 : 'r', 
    쓰기 전용 :
        파일 덮어쓰기(새로만듬) : 'w',
        파일 끝에 추가(덧붙이기) : 'a',
        파일이 있으면 에러 : 'x'
파일 모드 오른쪽에 +를 붙이면 읽기/쓰기 혼합 (ex> 'r+', 'w+', 'a+' ...)
파일 모드 맨오른쪽에 파일 종류를 붙여서 종류 지정 가능(기본값 텍스트파일(t)) b: 바이너리 파일 (ex> 'wb', 'w+b', 'a+b' ...)


파일의 종류는 텍스트(text)파일과 바이너리(binary)파일이 있는데,
텍스트 파일은 문자를 기반으로 하는 코드값을 저장하는 형식으로, txt파일등이 해당됨.
이런 텍스트 파일은 문자열 개념을 그대로 사용할 수 있음. 

바이너리(binary) 파일은 정보, 숫자값을 특별한 가공없이 저장하는 형식으로, 
jpg, png같은 그림파일, mp3같은 음악파일, exe같은 실행파일이 해당됨.

파이썬에서 파일을 열때 기본적으로 텍스트 모드로 읽고, b를 파일모드에 추가하면 바이너리 모드로 읽음.
                

그리고 파일객체를 사용해서 문자열을 읽고 쓸수 있음. (open()함수 뒤에, .close()메쏘드 전에 사용함)

.write() 메쏘드로 파일에 문자열을 쓸수 있고,
.read() 메쏘드로 파일에서 문자열을 읽은 값을 반환할 수 있음. (문자열로 반환)
"""
file = open('18.txt', 'r')
s = file.read()
print(s)
file.close()

"""with as 문
with open(파일이름, 파일모드) as 파일객체:
    실행문
    
과 같은 형식으로 자동으로 파일 객체를 열고 닫을 수 있음. (파이썬 2.5 부터 추가된 기능)
이러한 것을 context manager(특정작업(여기선 파일)의 context(파일을 열고 닫고, 예외처리)를 관리하는 객체),
컨텍스트 매니저라고 함. (컨텍스트 매니저에 대해선 심화 내용이다 보니, 나중에 알아보도록 함. 6폴더의 04-9-1 참고.)
"""

with open('18.txt', 'r') as f:
    print(f.read())
print("이렇게 with as 문을 빠져나가면 파일객체가 자동으로 닫힙니다. (close()함수 필요없이)")
