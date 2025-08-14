import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Programa finalizado')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    try:
        match(opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                print('Código inválido')
    except Exception as e:
        print(f'Ops um erro ocorreu: {e}')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')
    nome = input('Por favor, informe o nome do restaurante: ')
    categoria = input('Agora informe a categoria do restaurante: ')
    ativo = True if input('Digite agora se o restaurante está ativo ou não (S/N)') == 'S' else False
    try:
        restaurantes.append({'nome':nome,'categoria':categoria,'ativo':ativo})
        print(f'Restaurante {nome} cadastrado com sucesso!')
    except:
        print('Ocorreu um erro durante o cadastro, tente novamente')
    voltar_ao_menu_anterior()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'.ljust(22)}')
    for restaurante in restaurantes:
        status = 'Ativado' if restaurante['ativo'] == True else 'Desativado'
        print(f'{restaurante['nome'].ljust(22)} | {restaurante['categoria'].ljust(22)} | {status}')
    voltar_ao_menu_anterior()

def alterar_status_restaurante():
    exibir_subtitulo('Alterando status do restaurante')
    for restaurante in restaurantes:
        status = 'Ativado' if restaurante['ativo'] == True else 'Desativado'
        print(f'Nome do restaurante: {restaurante['nome']} | Status: {status}')
    print()
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    try:
        for restaurante in restaurantes:
            if(restaurante['nome'] == nome_restaurante):
                restaurante['ativo'] = not restaurante['ativo']
                print(f'O status do restaurante foi alterado com sucesso!')
    except:
        print('Ocorreu um erro durante a alteração')
    voltar_ao_menu_anterior()

def voltar_ao_menu_anterior():
    input('Digite uma tecla para voltar ao menu anterior \n')
    main()

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
