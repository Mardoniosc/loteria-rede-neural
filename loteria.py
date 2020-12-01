# coding: utf-8
from auxFunc import compara_resultado, resultado_lista_inteiro
import os.path


def ganhosPorTipo(tipo, acertos, ganhos, jogo):
    if tipo == 'lotofacil':
        if acertos == 15:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 1124060
        elif acertos == 14:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 1500
        elif acertos == 13:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 25
        elif acertos == 12:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 10
        elif acertos == 11:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 5
        else:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
    elif tipo == 'lotomania':
        if acertos == 20:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos +  6462616.45
        elif acertos == 19:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 60614.89
        elif acertos == 18:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 1789.45
        elif acertos == 17:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 212.03
        elif acertos == 16:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 41.45
        elif acertos == 15:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 8.35
        elif acertos == 0:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 181843.77
        else:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
    elif tipo == 'megasena':
        if acertos == 6:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 5124060
        elif acertos == 5:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 27540
        elif acertos == 4:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))
            ganhos = ganhos + 759
        else:
            print("Resultado do %d° jogo acertou %d" % (jogo, acertos))

    return ganhos


def resultados(tipo, numeros_sorteador, nomearquivo):
    ganhos = 0
    jogo = 1
    if os.path.isfile(nomearquivo + '.txt'):
        with open(nomearquivo + '.txt', 'r') as fd:
            for x in fd:
                if x != '' and x != "\n":
                    y = (resultado_lista_inteiro(x))
                    acertos = compara_resultado(numeros_sorteador, y)
                    ganhos = ganhosPorTipo(tipo, acertos, ganhos, jogo)
                    jogo += 1
        print("\n\nGanho total aproximado é de R$ %.2f" % ganhos, "Reais")
    else:
        print('Arquivo ', nomearquivo + '.txt não foi encontrado!')
