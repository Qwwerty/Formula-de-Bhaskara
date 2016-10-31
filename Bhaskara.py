# -*- coding: utf-8 -*-

# Importa sqrt do modulo math do Python
from math import sqrt

'''
Equações utilizadas como referencia:

Delta > 0 --- 1x² 0x -4 = 0 --- a=1, b=0, c=-4

Delta = 0 --- 1x² -6x 9 = 0 --- a=1, b=-6, c=9
Não haverá gráfico visto que o **np.arange()** irá iniciar e termina no mesmo numero,
isso porque quando delta é igual a zero a parabola apenas toca o eixo X.
Poderia ser gerada a tabela colocando valores menores e maiores que o encontrado em
X1 e X2, porem está não á função deste código.

Delta < 0 (3x**2 -2x + 1) - Quando Delta é menor que zero a função bhaskara deverá
entrar no **except ValueError** visto que não é possível fazer raiz de um numero negativo.

Concavidade para baixo:
Quando o **a** é negativo --- -2x -5x 3 = 0 --- a=-2, b=-5, c=3
'''

# Entrada de dados do usuário
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
print('[!] Equação digitada: %dx² %dx% d = 0 [!]\n' % (a, b, c))


def bhaskara():
    # Entrada de dados do usuário
    a = int(ed_A.get())
    b = int(ed_A.get())
    c = int(ed_A.get())
    print('[!] Equação digitada: %dx² %dx% d = 0 [!]\n' % (a, b, c))

    """
    Função realiza o calculo da formula de bhaskara.
    Nesta função são exibidos no terminal:

    #. Posição da parabola (voltada para cima ou para baixo).
    #. Valor do Delta.
    #. Valor da raiz quadrada.
    #. Valor de X1 e X2.

    Caso o valor de delta seja negativo não haverá raiz possível,
    Neste caso o código cai no **except ValueError**

    :return: Envia os valores obtidos.
    """
    try:
        # Variável **delta** receberá o valor da raiz quadrada de delta.
        # sqrt = raiz quadrada.
        delta = sqrt((b ** 2) - 4 * a * c)

        # Exibe no terminal a posição da concavidade da parabola.
        concavidade = '[!] A concavidade da parabola é voltada para cima [!]' if a >= 0 \
            else '[!] A concavidade da parabola é voltada para baixo [!]'
        print(concavidade)

        # Verifica se x1 e x2 serão iguais ou diferentes.
        if delta > 0:
            print('[!] O VALOR de DELTA é %.2f, A equação terá X1 e X2 DIFERENTES [!]' % (delta * delta))
            print('[!] A RAIZ QUADRADA DE DELTA é igual %.2f [!]\n' % delta)
        elif delta == 0:
            print('[!] O VALOR de DELTA é %.2f, a equação terá X1 e X2 IGUAIS [!]' % (delta * delta))
            print('[!] A RAIZ QUADRADA DE DELTA é igual %.2f [!]\n' % delta)

        # Realiza o calculo de X1 e X2 da formula de Bhaskara
        x1 = (-b - delta) / (2 * a)
        x2 = (-b + delta) / (2 * a)
        label_x1["text]"] = x1
        label_x2["text]"] = x2

        

        return {'delta': delta, 'x1': x1, 'x2': x2}

    except ValueError:
        print('[!] NÃO possui raízes reais [!]')
        print('[!] O valor de DELTA foi menor que zero[!]')
        print('[!] conjunto solução vazio: S={ø} [!]')

if __name__ == '__main__':
    bhaskara()

######INTERFACE GRAFICA########

from tkinter import *
#Tamnho da janela
janela = Tk()

janela.geometry("300x300+300+300")

#Nome do Programa
label_name = Label(janela, text="FORMULA DE BASKARAS", bg="#606060")
label_name.place(x=90, y=20)

#Vai entra as variaveis(A, B, C)
label_A = Label(janela, text="Valor A: ")
label_A.place(x=20, y=80 )

label_A = Label(janela, text="Valor B: ")
label_A.place(x=20, y=110 )

label_A = Label(janela, text="Valor C: ")
label_A.place(x=20, y=140 )

#Entrada de valores

ed_A = Entry(janela)
ed_A.place(x=90, y=80)

ed_B = Entry(janela)
ed_B.place(x=90, y=110)

ed_C = Entry(janela)
ed_C.place(x=90, y=140)

#Resultado
bt = Button(janela, text="Calcular", width=8, height=2, bg="#909090", command=bhaskara())
bt.place(x=20, y=170)

label_x1 = Label(janela, text="x1", bg="#606060")
label_x1.place(x=100, y=170)

label_x2 = Label(janela, text="x2", bg="#606060")
label_x2.place(x=100, y=190)

#Sair
bt_quit = Button




janela.mainloop()

