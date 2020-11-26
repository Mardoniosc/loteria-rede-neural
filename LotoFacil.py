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

class LotoFacil():
  def __init__(self):
    URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'
    TARGET_PATH = 'D_lotfac.zip'
    NAME_FILE_HTML = 'd_lotfac.htm'
    DADOS = ['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15', 'Ganhadores_15_Números']
    DEZENAS = ['bola1','bola2','bola3','bola4','bola5','bola6','bola7','bola8','bola9','bola10','bola11','bola12','bola13','bola14','bola15']
    NUMBER_GAMES = 3
    PROBABLY_GOOD = 95
    GAME_TEST = [1, 2, 3, 5, 7, 8, 10, 11, 12, 14, 15, 17, 21, 22, 24]
    TIPO_JOGO_NUMBER = 15
    RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER)

if __name__ == "__main__":
    LotoFacil()