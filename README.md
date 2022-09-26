# Ackermann
Multi-variable Ackermann function extension

## Story
Wilhelm Ackermann constructed functions like this to show there are primitive- and even general recursive functions. For primitive function is example if we talk about succession, addition, multiplication, the multi-variable functions of these operators and the known composition (functional product) making new primitive functions like exponentiation, factorial, tetration and so on. By extending the functional product, we come to the non-primitive- so-called general recursive functions like the known two-variable Ackermann-, the Rózsa-function and the three-variable Hyper-operator. These can produce really big numbers with small inputs.

It is useful to give the growth of time/space-complexity of a problem. E. g. flipping the bits is O(n) which is P, matrix-inversion with a bad algorithm is O(n!) which is NP, searching in chess-tree is O(exp(n)) which is EXP, deciding whether a set of operators is complete in n-ary logic is 2^2^O(n) which is 2-EXP, etc. Till c-EXP where c is constant each problem is in ELEMENTARY, but for example tetration is above of this zoo, also like pentation but still primitive recursive. Ackermann which is a highly much more growing function, is general recursive as mentioned: O(Ack(n,1)), O(Hyper(2,n,3)) and TREE(n) are not ELEMENTARY.


## Usage of the functions of ack.py
Let the one-variable ack is x-1 from x=1.
Let the two-variable ack is the same as defined by Ackermann.
Let the multi-variable acks are defined like in the ack.py, in general formulas:
ack(x_1, x_2, ..., x_{n-1}, x_n) = ack( x_1-1, x_2, ..., x_{n-1}, ack( x_1, x_2-1, x_3, ..., x_{n-1}, ack( x_1, ... ...( x_1, ..., x_{n-1}, x_n-1 ) ... ) ) )
In words: we embed n-variable functions itself to the right place, and in the i-th depth we get x_i-1 instead of x_i. That is it.

## Open questions
*HOW TO EXTEND ACKERMANN TO REAL VARIABLES?*
