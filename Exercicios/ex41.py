not1 = float(input('Digite a Primeira Nota '))
not2 = float(input('Digite a Segunda Nota '))
media = (not1 + not2) / 2
if media > 7.0:
    print('Parabens sua media foi {}. Vc esta \33[0:34m APROVADO \33[m '.format(media))
elif media >= 5.0 and media <= 7.0:
    print('Sua media foi {} . Voce esta de \33[0:33m RECUPERAÇÂO \33[m'.format(media))
else:
    print('SUa media foi {} Você esta \33[0:31m REPROVADO \33[m'.format(media))



