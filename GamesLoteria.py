# coding: utf-8
"""
    .NOTES
    ===========================================================================
    Created with:   Visual Studio Code v1.45.1
    Created on:   	26/11/2020 10:24
    Created by:   	Mardonio Silva da Costa
    Organization: 	Small Tecnologia
    Filename:     	GamesLoteria.py
    ===========================================================================
    .DESCRIPTION
    Faz a analise de jogos já sorteados de alguma loteria,
    para prever os proximos resultado
    .UPDATES
        00/00/2020 - ? - ?
"""

# IMPORTANDO BIBLIOTECAS
import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn             as sns
import missingno           as msno
import requests 
import zipfile
from bs4 import BeautifulSoup
import lxml

class GamesLoteria:
  def __init__(self):
    pass

  def setUrlDownload(self, url):
    self.url = url

  def setTargetPath(self, target_path):
    self.target_path = target_path

  def setNameFileHtml(self, fileHtml):
    self.fileHtml = fileHtml

  def setData(self, bolas_sorteadas):
    self.bolas_sorteadas = bolas_sorteadas

  def getUrlDownload(self):
    return self.url

  def getTargetPath(self):
    return self.target_path

  def getNameFileHtml(self):
    return self.fileHtml

  def getData(self):
    return self.bolas_sorteadas
  

  @staticmethod
  def downloadZipAndUnzip(url, target_path):
    print('Atualiznando jogos sorteados...')

    response = requests.get(url, stream=True)
    handle = open(target_path, "wb")
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    handle.close()
    with zipfile.ZipFile(target_path) as zf:
        zf.extractall()

  @staticmethod
  def getByAllGames(fileHtml):

    f = open(fileHtml, 'r', encoding='latin-1') 
    table=f.read()

    soup = BeautifulSoup(table, 'html.parser')
    table = soup.find(name='table')

    table_str = str(table)
    df = pd.read_html(table_str)[0]
    return df

  @staticmethod
  def createDataFrameModel(bolas_sorteadas, df, TIPO_JOGO_NUMBER):
    print('Criando datafram para usar no modelos...')
    df_clean = df
    index = 0
    anterior = ''
    for concurso in df['Concurso']:
        if(concurso == anterior):
            df_clean = df_clean.drop(index)
        index += 1
        anterior = concurso

    df_clean.shape

    df_nn = df_clean[bolas_sorteadas] 
    df_nn.columns = map(str.lower, df_nn.columns)
    df_nn.head(TIPO_JOGO_NUMBER)

    return df_nn

def gameInstanciado(url, target_path, fileHtml, bolas_sorteadas):
  gameLoteria = GamesLoteria()
  gameLoteria.setUrlDownload(url)
  gameLoteria.setData(bolas_sorteadas)
  gameLoteria.setTargetPath(target_path)
  gameLoteria.setNameFileHtml(fileHtml)
  return gameLoteria

if __name__ == "__main__":
  GamesLoteria()