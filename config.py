

# Replace this file!

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')

s1 = ((P|Q)&(P|~Q))
s2 = ((~S|P)&(S|P))
s3 = ((S|~P)|~Q)
s4 = (Q|(P|~S))

s5 = (~(R|~T)|(~T>>(S&~R)))
s6 = ((R>>T)>>((T&~R)|S))