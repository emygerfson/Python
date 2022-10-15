while True:
    n = int(input('Qual tabuada você quer ver: '))
    if n < 0:
        break
    print('--=--' * 10)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('--=--' * 10)
print('Acabou')
