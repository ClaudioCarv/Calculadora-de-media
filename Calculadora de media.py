from colors import cores #biblioteca de cores básicas
import platform #biblioteca para ver qual plataforma está sendo executado
import os #biblioteca para realizar alguns comandos CMD
import time #biblioteca para tempo de intervalo

#função para limpar o CMD
def limpar():
    if (platform.system() == 'Windows'):
        os.system('cls')

#Loop Repetição
while True:
    limpar()
    print('{}Calculadora de média{}'.center(40).format(cores['azul'], cores['limpa']))

    n1 = float(input('\nDigite aqui a primeira nota: '))
    n2 = float(input('Digite aqui a segunda nota: '))
    n3 = float(input('Digite aqui a terceira nota: '))

    #calculo da nota
    nota = (n1 + n2 + n3) / 3

    #possibilidades da nota
    if(nota >= 7.0):
        print('\n{}Nota {:.1f} Aprovado!{}'.format(cores['verde'], nota, cores['limpa']))
    elif (nota < 5.0):
        print('\n{}Nota {:.1f} Reprovado{}'.format(cores['vermelho'], nota, cores['limpa']))
    elif (nota > 5.0 and nota < 6.9):
        print('\n{} Nota {:.1f} Recuperação{}'.format(cores['amarelo'], nota, cores['limpa']))

    #variavel para rodar o programa novamente
    ec = str(input('\nCalcular novamente ? S/N: ')).lower()

    if( ec == 's'):
        print('Reiniciando')
        time.sleep(1)
    elif(ec == 'n'):
        print('{}Encerrado{}'.format(cores['vermelho'], cores['limpa']))
        time.sleep(1)
        limpar()
        break
    else:
        print('Digite corretamente o que se pede')
        print('{}Reiniciando{}'.format(cores['azul'], cores['limpa']))
        time.sleep(1)
