from cinematica import *

while True:
    # mostra menu na tela
    mostrar_menu()
    opcao = input('Opção do Usuário: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace(',', '.'))
            h = float(input('Informe a altura em metros: ').replace(',', '.'))
            print(f'Energia potêncial: {calcular_ep(m, h):,.2f} J.')
            continue
        case '2':
            m = float(input('Informe a massa em kg: ').replace(',', '.'))
            v = float(input('Informe a velocidade em m/s: ').replace(',', '.'))
            print(f'Enegia Cinética: {calcular_ec(m, v):,.2f} J.')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção Inválida!')
            continue