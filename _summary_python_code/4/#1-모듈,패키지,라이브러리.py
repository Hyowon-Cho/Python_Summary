summary = """ 
 모듈 vs 패키지 vs 라이브러리:
파이썬에서 볼수 있는 개념들로, 서로 비슷하면서도 차이가 있다.

* 모듈(module):
특정 기능을 .py 파일 단위로 작성한 것.
(함수, 변수, 클래스 같은 것들이 모여있는 파일)

파이썬이 제공하는 모듈 -> 표준 모듈
설치해서 사용하는 모듈 -> 서드파티 모듈
사용자가 만들어쓰는 모듈 -> 사용자 생성 모듈


* 패키지(package):
모듈을 묶은 것(관련된 기능끼리).
디렉토리(패키지)가 다른 디렉토리(모듈)을 포함하는 형태로 구조화함.

패키지이름.모듈이름
형식으로 사용함.
패키지는 모듈마다에 네임스페이스(namespace)를 제공.

파이썬 패키지 인덱스(Python Package Index, PyPI)를 통해 인터넷의 다양한 패키지를 설치후 사용 가능.
파이썬 패키지 인덱스는 파이썬 패키지들이 모여있는 저장소로, 
2020-4-19일 기준, 229,009 projects(프로젝트)와 1,784,025 releases(릴리즈(=버전)) 가 있음.
(링크 : https://pypi.org/ ) 


* 라이브러리(library):
모듈과 패키지를 묶어놓은 것.

파이썬의 기본 모듈, 패키지, 내장함수등 -> 파이썬 표준 라이브러리(Python Standard Library, PSL)
"""
print(summary)

""" 라이브러리 vs 프레임워크:
라이브러리(library) : 개발할 때 필요한 부속품 (가져다 쓰는 것)
프레임워크(framework) : 개발할 때 짜여진 기본틀 (이 위에 뭘 덧붙여 만드는 것)
"""