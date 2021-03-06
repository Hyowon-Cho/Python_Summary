"""
블로그 포스팅 : https://bodhi-sattva.tistory.com/59
(좀더 세부적으로 정리했습니다.)
"""

a = 1
b = 0
c = -9
print(a, type(a), b, type(b), c, type(c))
# type(변수)는 그변수의 자료형을 반환하는 함수이다.
""" 숫자자료형
우리가 흔히 사용하는 그 숫자를 담는 자료형이 바로 숫자 자료형이다.
숫자자료형에는 3가지가 있었는데,
정수, 실수, 복소수에 따라서 각각 int, float, complex 자료형이 있다.

첫번째는 위와 같은 int 자료형으로, 정수형(integer) 숫자다.
(python3 이전 버전에서는 32비트의 저장공간을 차지하며, 범위도 약-21억~21억만큼이고, 대신에 long
이라는 자료형으로 메모리가 허락하는 선에서 무제한의 범위를 사용할 수 있었는데, python3으로 오면서 
long자료형이 없어지고, 대신에 int가 long같이 크기제한이 없어졌다고 한다.)
int()함수 라는것이 있는데 인자값을 int 자료형으로 반환한다.

두번째는 float 자료형으로, 실수형(floating-point) 숫자다.
"""
d = -4.2
e = 4.2E1
print(d, type(d), e, type(e))
n1 = float('nan')
n2 = float('inf')
print(n1, type(n1), n2, type(n2))
"""
바로 소수점 아래의 값도 있는 숫자를 말하며, 
유호자릿수는 15자리까지이다.
float()함수로 실수로 변환한 값을 가져올 수 있는데, 이걸 이용해서
inf(양의무한), nan(불가능한수), -inf(음의무한)까지도 대입할 수 있다.
변수 e 와 같이 부동소수점 표현으로 입력할 수도 있다.
참, 추가로 8진수와 16진수도 사용할 수 있다. 
2진수도 0b를 쓰면 가능하다. 그리고 대소문자 구별없이 써도된다(0x든 0X든 상관없음)
"""
f = 0o12
# 8진수(0o)
g = 0x12
# 16진수(0x)
print(f, type(f), g, type(g))
"""
물론 저장될때 따른 자료형이 있는 것이 아니며, 10진수로 변환되서 저장된다.
세번째로 복소수도 포함하는 자료형인 complex 도 있덴다.
허수기호를 j, J로 표현하며, 
complex()함수로 복소수를 만들수도 있다.
complex(n)은 n+0j인 복소수로, complex(n, m)은 n+mj인 복소수가 되고,
complex('n+mj')도 n+mj인 복소수가 된다.
.real(실수부), .imag(허수부), .conjugate(컬레복소수), abs(절댓값 반환)
과 같은 함수로 응용할 수 있다.
"""
h = 2 + 3j
print(h, type(h))
print(h.real, h.imag, h.conjugate(), abs(h))
i = 1j
print(i, i**2, i**3, i**4)
"""숫자 연산자:
+, -, /, *
같은 사칙연산은 기본적으로 제공한다. 그리고 추가로
** : 제곱 연산자  (2**3 == 8)
% : 나머지 연산자  (5%2 == 1)
// : 몫 연산자  (5//2 == 2)
도 제공한다.
"""
print(float('3.2'), float(2))
