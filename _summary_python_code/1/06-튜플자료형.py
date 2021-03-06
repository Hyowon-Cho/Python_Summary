t1 = (1,)
t2 = (1, 2)
t3 = 1, 2, 3
t4 = ('a', 'b', ('ab', 'cd'))
t5 = tuple('ppap')
t6 = tuple([1, 2, 3, 4])
print(t1, t2, t3, t4, t5, t6)
"""튜플(typle) :
리스트랑 비슷한데, 다른점이라면 튜플은 요소 값을 삭제, 수정할 수 없다.(읽기전용이다)
요소 값을 중간에 못바꿔서 리스트를 튜플대신에 많이 쓰지만, 튜플이 속도가 빠르덴다.
tuple() 함수로 군집자료형(연속되는 값들)을 튜플자료형으로 변환할 수 있다.

생성하는 법이 독특한데, 리스트는 []가 테두린데, 튜플은 ()가 테두리다. 근데 ()없이도 생성이 가능하다.
(왜냐면 괄호 없이 값을 콤마로 구분하면, 그걸 하나로 묶어서 튜플 객체로 생각한다.)
그리고 한개 요소에서는 ,를 뒤에 붙이는데, 왜그런지 생각해보니까 숫자, 문자열이랑 차별을 두는 거였다.
(튜플을 선언할때 ()없이 생성가능하다 보니까 요소가 1개일때 비군집 자료형이랑 생성방식이 겹치게 된다.)
t01 = 1  # type(t01) == int
t02 = 1, # type(t02) == tuple

튜플도 시퀀스(순서가 있는 군집)자료형이기 때문에 아래 문법을 사용 가능하다.
인덱싱과 슬라이싱이 가능하다. 다차원 튜플도 된다.
그리고 기본연산인 +(더하기), *(곱하기)도 리스트처럼 된다.
리스트에서 봤던 내장함수도 튜플과 동일하다.
"""


def ppap(li):
    return li[0], li[-1]


print(ppap("ppap!"))
first, last = ppap("ppap!")
print(first, last)
"""튜플에 대한 알쓸잡지:
함수의 반환 값이 위같이 여러개일 경우 튜플로 반환된다.
이걸 변수들에게 대입하면 각각 변수에 각각의 값이 들어간다. (해체 할당과 비슷하덴다)
(a, (b,(c, d))) = (4,(3,(2,1)))
이렇게도 가능하다.    
"""
a = '국'
b = '밥'
a, b = b, a
print(a, b)
'''
예전에 신발끈공식으로 두 변수의 값을 바꿀때 temp 변수를 선언해서 바꿔줄 필요가 없다!
튜플을 이용해서 한줄로 해결 가능하다.
'''

tp = (1, 3, 5, 7, 9)
print(len(tp), max(tp), min(tp))
""" 튜플 내장함수, 메쏘드:
튜플 내장함수는, 리스트에서 사용했던 그대로 len(), max(), min()을 사용할 수 있다.
메쏘드는 다른자료형과 다르게 다행이도(?) .count(), .index()만 있다.
"""

print(tp.count(1), tp.index(1))
"""
.count(), .index() 함수도 사실 리스트와 같이 사용할 수 있다.
"""


