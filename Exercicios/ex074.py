times = ('palmeiras','Corinthias','Atletico Mineiro','Fluminense',
         'Atletico Paranaense','internacinal','Flamengo','Bragantino',
         'Santos','São Paulo','Ceara','Botafogo','Avai','Goias','Cuiaba',
         'Curitiba','America MG','Atletico GO','Fortaleza','Juventude')
print('=='*15)
print(f'Listas de times do brasileirão :{times}')
print('=='*15)
print(f'Os 5º times são : {times[0:4]}')
print('=='*15)
print(f'O 4 ultimos colocados sâo : {times[16:20]}')
print('=='*15)
print(f'A ordem Alfabeticas dos times são: {sorted(times)}')
print('=='*15)
print(f'O São Paulo esta em {times.index("São Paulo")+1}ª lugar. ')
print('=='*15)
