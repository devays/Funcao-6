
def voto(nascimento):
    ano = 2022
    calc = ano - nascimento
    if calc < 16:
        print(f'Com {calc} anos: NÃO VOTA.')
    elif calc > 18 and calc < 65:
        print(f'Com {calc} anos: VOTO OBRIGATÓRIO.')
    elif calc >= 16 or calc <=17 and calc > 65:
        print(f'Com {calc} anos: VOTO OPICIONAL.')

print('-'*25)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)