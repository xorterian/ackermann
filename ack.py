# Single-variable Ackermann function
def ack1(x):
  if x==0:
    return 0
  return x-1

# Two-variable Ackermann function
def ack2(x,y):
  if x==0:
    return y+1
  if y==0:
    return ack2( ack1(x), 1 )
  return ack2( ack1(x), ack2( x, ack1(y) ) )

# Three-variable Ackermann function
def ack3(x,y,z):
  if x==0:
    return ack2( y, z )
  if y==0:
    return ack2( x, z )
  if z==0:
    return ack3( ack2( x, y ), ack1(y), 1 )
  return ack3( ack1(x), y, ack3( x, ack1(y), ack3( x, y, ack1(z) ) ) )

# Four-variable Ackermann function
def ack4(x1,x2,x3,x4):
  if x1==0:
    return ack3( x2, x3, x4 )
  if x2==0:
    return ack3( x1, x3, x4 )
  if x3==0:
    return ack3( x1, x2, x4 )
  if x4==0:
    return ack4( ack3( x1, x2, x3 ), ack2( x2, x3 ), ack1(x3), 1 )
  return ack4( ack1(x1), x2, x3, ack4( x1, ack1(x2), x3, ack4( x1, x2, ack1(x3), ack4( x1, x2, x3, ack1(x4) ) ) ) )

# N-variable Ackermann function
# Input: vector of integers
def ack(x):
  N = len(x)
  if N==1:
    return max( 0, x[0]-1 )
  if x[0]==0:
    # return sum(x)+1
    if N==2:
      return x[1]+1
    return ack(x[1:])
  for i in range(1,N-1):
    if x[i]==0:
      return ack(x[:i-1]+x[i:])
  if x[N-1]==0:
    return eval('ack([ ack(['+ ']), ack(['.join([ str(x[i:N-1])[1:-1] for i in range(N-1) ]) +']), 1 ' +'])')
  fun = ''
  for i in range(N):
    fun += 'ack([ '+ ', '.join( [ 'ack(['+ str(x[j]) +'])' if i==j else str(x[j]) for j in range(N-1) ] ) + ', '
  fun += 'ack(['+str(x[N-1])+'])'+' ])' * N
  return eval(fun)
