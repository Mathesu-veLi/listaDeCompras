def transformarStringEmNúmero(stringÀSerTransformada, tipoDeDado = int):
    try:
        if tipoDeDado == int:
            númeroTransformado = int(stringÀSerTransformada)
        elif tipoDeDado == float:
            númeroTransformado = float(stringÀSerTransformada)

        return númeroTransformado
    except ValueError:
        return False


def confirmarContinuação(mensagemDeConfirmaçãoDeContinuação):
    confirmaçãoDeContinuação = str(input(f'{mensagemDeConfirmaçãoDeContinuação} [S/N]: ')).lower()
    if validarContinuação(confirmaçãoDeContinuação) == True:
        if 's' in confirmaçãoDeContinuação:
            return True
        else:
            return False
    else:
        print('Dados inválidos! Tente novamente!')
        confirmarContinuação()


def validarContinuação(continuar):
    if continuar in 'sn':
        return True
    else:
        return False


def verificarSeRegistroDeProdutosExiste():
    try:
        registroDeProdutos = open('registro.json', 'r')
        return True
    except FileNotFoundError:
        return False