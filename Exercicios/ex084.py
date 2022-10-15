expr = str(input('Digite um Expressão '))
pilha =[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressaõ e valida')
else:
    print('Sua expressaõ não e valida')