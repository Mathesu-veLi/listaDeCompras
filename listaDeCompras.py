import json
from Funções import *

opçãoEscolhida = False
produtosRegistrados = []
preçoTotal = 0

print(f'{"Lista de compras":^50}')

while True:
    print('')
    print(f'{"Escolha uma das opções abaixo":^50}')
    print(f'{"[0] Fechar Programa":^50}')
    print(f'{"[1] Registrar produtos":^50}')
    print(f'{"[2] Deletar algum produto":^50}')
    print(f'{"[3] Deletar todos os produtos":^50}')
    print(f'{"[4] Ver produtos registrados":^50}')
    print('')

    while True:
        opçãoEscolhida = str(input('Opção Escolhida: '))
        opçãoEscolhida = transformarStringEmNúmero(opçãoEscolhida)
        if opçãoEscolhida == False or opçãoEscolhida > 4:
            if opçãoEscolhida != 0:
                print('Digite um valor válido!')
            else: 
                break
        else: 
            break
    if opçãoEscolhida == 0: 
        break
    
    print('-'*50)

    if opçãoEscolhida == 1:
        confirmaçãoDeRegistroDeMaisProdutos = True
        while confirmaçãoDeRegistroDeMaisProdutos == True:
            nomeDoProduto = str(input('Nome do produto: ')).capitalize()
            
            preçoDoProduto = False
            while preçoDoProduto == False:
                preçoDoProduto = transformarStringEmNúmero(str(input('Preço do produto: R$')), float)
                if preçoDoProduto == False:
                    print('Digite um valor válido!')
                    
            preçoTotal += preçoDoProduto
            produtosRegistrados.append([nomeDoProduto, preçoDoProduto])
            confirmaçãoDeRegistroDeMaisProdutos = confirmarContinuação('Deseja cadastrar mais produtos?')
        
        salvamentoDeRegistro = {"Produtos": {}}
        for c in produtosRegistrados:
            salvamentoDeRegistro["Produtos"][c[0]] = c[1]
        salvamentoDeRegistro["Preço Total"] = preçoTotal
        
        with open('registro.json', 'w') as arquivoDeRegistro:
            json.dump(salvamentoDeRegistro, arquivoDeRegistro)
            
    if opçãoEscolhida == 2:
        with open('registro.json', 'r') as arquivoDeRegistro:
            registro = json.load(arquivoDeRegistro)
            for produto in registro["Produtos"]:
                print(produto)
                
            print('')
            produtoÀSerDeletado = str(input('Digite o nome do produto que deseja deletar (0 para voltar): '))
            
            if produtoÀSerDeletado not in registro["Produtos"]:
                while True:
                    print('Produto invalido! Certifique-se de digitar o nome correto!')
                    produtoÀSerDeletado = str(input('Digite o nome do produto que deseja deletar (0 para voltar): ')).capitalize()
                    if produtoÀSerDeletado in registro["Produtos"]: 
                        break
            
            if produtoÀSerDeletado != 0:
                registro["Preço Total"] -= registro["Produtos"][produtoÀSerDeletado]
                del registro["Produtos"][produtoÀSerDeletado]
                with open('registro.json', 'w') as arquivoDeRegistroEscrita:
                    json.dump(registro, arquivoDeRegistroEscrita)
                print(f'O "{produtoÀSerDeletado}" foi deletado com sucesso!')
                    
    if opçãoEscolhida == 3:
        with open('registro.json', 'r') as arquivoDeRegistro:
            registro = json.load(arquivoDeRegistro)
            confirmaçãoDeRemoçãoDeProdutos = confirmarContinuação(f'Tem certeza que deseja deletar os {len(registro["Produtos"])} produtos registrados?')
            if confirmaçãoDeRemoçãoDeProdutos == True:
                registro["Produtos"] = ''
                with open('registro.json', 'w') as arquivoDeRegistroEscrita:
                    json.dump(registro, arquivoDeRegistroEscrita)
                print('Produtos deletados com sucesso!')
        
    if opçãoEscolhida == 4:
        if verificarSeRegistroDeProdutosExiste() == True:
            with open('registro.json', 'r') as arquivoDeRegistro:
                registro = json.load(arquivoDeRegistro)
                
                if len(registro["Produtos"]) > 0:
                    print('Os produtos registrados até agora foram: ')
                    print('')
                    for produtos, preços in registro["Produtos"].items():
                        print(f'{produtos} R${preços:.2f}')
                    print('')
                    
                    print(f'Preço total: R${registro["Preço Total"]:.2f}')
                else:
                    print('Cadastre algum produto primeiro')
        else:
                    print('Cadastre algum produto primeiro')
        input('...')
