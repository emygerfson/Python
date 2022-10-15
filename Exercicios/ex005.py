n1 = int(input ('\33[4;31;44m digite um numero\33[m '))
n2 = int(input ('\33[4;31;42m digite outo numero\33[m '))
s = n1+n2
d = n1/n2
m = n1*n2
p = n1**n2
di = n1//n2
sd = n1%n2
print('a soma e {}, a divisão e , {},a multiplicação e {}'.format(s,d,m))
print('a potencia e {:.2f},a divisão inteira e {},o resto da soma e {}'.format(p,di,sd))

