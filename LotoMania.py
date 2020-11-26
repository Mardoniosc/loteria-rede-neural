# coding: utf-8
"""
    .NOTES
    ===========================================================================
    Created with:   Visual Studio Code v1.45.1
    Created on:   	26/11/2020 14:45
    Created by:   	Mardonio Silva da Costa
    Organization: 	Small Tecnologia
    Filename:     	LotoMania.py
    ===========================================================================
    .DESCRIPTION
    Faz a analise de jogos já sorteados da LotoMania,
    para prever os proximos resultado
    .UPDATES
        00/00/2020 - ? - ?
"""
from RedeNeural import RedeNeural

class LotoMania():
  def __init__(self):
    URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
    TARGET_PATH = 'D_lotoma.zip'
    NAME_FILE_HTML = 'd_lotman.htm'
    DADOS = ['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15', 'Bola16', 'Bola17', 'Bola18', 'Bola19', 'Bola20', 'Ganhadores_20_Números']
    DEZENAS = ['bola1','bola2', 'bola3', 'bola4', 'bola5', 'bola6','bola7', 'bola8', 'bola9', 'bola10', 'bola11','bola12', 'bola13', 'bola14', 'bola15', 'bola16', 'bola17', 'bola18', 'bola19', 'bola20']
    NUMBER_GAMES = 3
    PROBABLY_GOOD = 90
    GAME_TEST = [71,63,11,44,84,11,55,93,8,29,82,62,17,64,24,14,37,97,49,51]
    TIPO_JOGO_NUMBER = 20
    TIPO_JOGO_NOME = 'Lotomania'
    RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER, TIPO_JOGO_NOME)

if __name__ == "__main__":
    LotoMania()