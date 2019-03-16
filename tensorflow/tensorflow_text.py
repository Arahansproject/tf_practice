import tensorflow as tf
"""
텐서플로에는 3가지의 핵심 데이터 구조가 있다.
Tensor + Flow
1. 상수 Constant
2. 변수 Variable
3. 플레이스홀더 Placeholder
   - 연산노드를 가리키는 텐서(다차원배열)
   - 텐서플로에서 그래프를 실행할 때 사용자가 
   - 데이터를 주입하는 통로 ---> 파라미터 개념

 tf.placeholder 과 tf.Variable 의 차이점
 tf.Variable 을 사용하면 선언할 때 반드시 초기값을 제공해야함
 tf.placeholder 을 사용하면 선언시 초기값을 제공하지 않고 
    런타임시 feed_dict 인수를 사용하여 값을 입력함
"""

p1 = tf.placeholder(dtype = tf.float32)
p2 = tf.placeholder(dtype = tf.float32)

t1 = p1 * 3
t2 = p1 * p2
session = tf.Session()
print(session.run(t1, feed_dict={p1 : 4.0, p2:[2.0, 5.0]}))

