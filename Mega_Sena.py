# coding: utf-8
"""
    .NOTES
    ===========================================================================
    Created with:   Visual Studio Code v1.45.1
    Created on:   	26/11/2020 11:52
    Created by:   	Mardonio Silva da Costa
    Organization: 	Small Tecnologia
    Filename:     	Mega_Sena.py
    ===========================================================================
    .DESCRIPTION
    Faz a analise de jogos já sorteados da mega sena,
    para prever os proximos resultado
    .UPDATES
        00/00/2020 - ? - ?
"""
from RedeNeural import RedeNeural

class MegaSena():
  def __init__(self):
    URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
    TARGET_PATH = 'D_mgsasc.zip'
    NAME_FILE_HTML = 'd_megasc.htm'
    DADOS = ['1ª Dezena','2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', '6ª Dezena', 'Ganhadores_Sena']
    DEZENAS = ['1ª dezena','2ª dezena', '3ª dezena', '4ª dezena', '5ª dezena', '6ª dezena']
    NUMBER_GAMES = 3
    PROBABLY_GOOD = 95
    GAME_TEST = [3, 22, 33, 35, 47, 55]
    TIPO_JOGO_NUMBER = 6
    rede = RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER)

if __name__ == "__main__":
    MegaSena()