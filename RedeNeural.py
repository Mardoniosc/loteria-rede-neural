# coding: utf-8
"""
    .NOTES
    ===========================================================================
    Created with:   Visual Studio Code v1.45.1
    Created on:   	26/11/2020 11:53
    Created by:   	Mardonio Silva da Costa
    Organization: 	Small Tecnologia
    Filename:     	RedeNeural.py
    ===========================================================================
    .DESCRIPTION
    Faz estudo de dados de loteria com a biblioteca de TensoFlow,
    para prever os proximos resultado
    .UPDATES
        00/00/2020 - ? - ?
"""

from keras.models  import Sequential
from keras.layers  import Dense
from sklearn.model_selection import train_test_split
from GamesLoteria import GamesLoteria, gameInstanciado, np, pd, msno
import random

# VARIAVEIS GLOBAIS


class RedeNeural():
  def __init__(self, URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER):
    self.URL_DOWNLOAD = URL_DOWNLOAD
    self.TARGET_PATH = TARGET_PATH
    self.NAME_FILE_HTML = NAME_FILE_HTML
    self.DADOS = DADOS
    self.DEZENAS = DEZENAS
    self.NUMBER_GAMES = NUMBER_GAMES
    self.PROBABLY_GOOD = PROBABLY_GOOD
    self.GAME_TEST = GAME_TEST
    
    gameInstanciadoLoteria = gameInstanciado(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS)
    
    np.random.seed(8)
    print('Separando target e classes...')
    # Separando target e classes
    GamesLoteria.downloadZipAndUnzip(gameInstanciadoLoteria.getUrlDownload(), gameInstanciadoLoteria.getTargetPath())

    df = GamesLoteria.getByAllGames(gameInstanciadoLoteria.getNameFileHtml())
    # Check dataset
    df.shape
    df.dtypes
    
    df_nn = GamesLoteria.createDataFrameModel(gameInstanciadoLoteria.getData(), df, TIPO_JOGO_NUMBER)

    # Definição do seed para a reproducidade do modelo

    features = df_nn.iloc[:,0:TIPO_JOGO_NUMBER]
    target   = df_nn.iloc[:,TIPO_JOGO_NUMBER]

    # Dividindo dataset entre treino e teste
    print('Dividindo dataset entre treino e teste')
    X_train, X_test, y_train, y_test = train_test_split(target, features, test_size=0.33, random_state=8)

    # Criando modelo
    print('Criando modelo...')
    modelo = Sequential()
    modelo.add(Dense(10, input_dim=TIPO_JOGO_NUMBER, activation='relu'))
    modelo.add(Dense(12, activation='relu'))
    modelo.add(Dense(1, activation='sigmoid'))

    # Compilando o modelo
    print('Compilando modelo...')
    modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Treinando modelo
    print('Treinando modelo...')
    modelo.fit(y_train, X_train, epochs=30, batch_size=10)

    # Avaliando modelo
    print('Avaliando modelo...')
    scores = modelo.evaluate(y_test, X_test)
    print("\n")
    print("Acuracia do modelo")
    print("\n%s: %2f%%" % (modelo.metrics_names[1], scores[1]*100))

    # Teste de probabilidade de um jogo
    numero_sorteio = [GAME_TEST]
    print('Realiznaod teste de probabilidade no jogo -> ', numero_sorteio)

    y_predict = pd.DataFrame(numero_sorteio)
    y_predict

    predict_class = modelo.predict_classes(y_predict)
    print("1 = Tem chance de ganhar / 0 = Não tem chance de ganhar")
    print("\n")
    print("Previsão Modelo: ",predict_class[0][0])

    # Achando a probabilidade
    predict_proba = modelo.predict_proba(y_predict)
    print("Probabilidade: ", round((predict_proba[0][0]*100),2), "%")

    self.gameTip(NUMBER_GAMES, PROBABLY_GOOD, df_nn, modelo, TIPO_JOGO_NUMBER, DEZENAS)

  @staticmethod
  def gameTip(jogos, probabilidade_boa, df_nn, modelo, TIPO_JOGO_NUMBER, dezenas_simbol):
      jogo_ok = False
      print("####################################################################")
      print("################        Dicas para concurso nº      ################")
      print("################               {0}                 ################".format(df_nn.shape[0]+1))
      print("####################################################################")
      listJogos = []
      for x in range(jogos):
          random.seed(TIPO_JOGO_NUMBER)
          probabilidade_atual = 0

          # Gerando list com as dezenas sorteadas
          dezenas_sorteadas = df_nn[dezenas_simbol].values.tolist()
    
          # Gera sequencia de numeros até que a probabilidade seja maior ou igual que 99%
          while(probabilidade_atual < probabilidade_boa):

              # Gera sequencia de número
              if TIPO_JOGO_NUMBER == 6:
                dezenas = random.sample(range(1, 60), TIPO_JOGO_NUMBER)

              elif TIPO_JOGO_NUMBER == 15:
                dezenas = random.sample(range(1, 25), TIPO_JOGO_NUMBER)

              elif TIPO_JOGO_NUMBER == 20:
                dezenas = random.sample(range(0, 99), TIPO_JOGO_NUMBER)

              # Numero gerado já foi sorteado?
              if not dezenas in dezenas_sorteadas and not dezenas in listJogos:

                  # Valida qual a probabilidade da seguência ser sorteada
                  probabilidade_atual = int(modelo.predict_proba(pd.DataFrame([dezenas]))[0][0]*100)
                  # print(' Probabilidade atual => ', probabilidade_atual ,'% Numero sorteados =>',dezenas, '\n')
          listJogos.append(dezenas)  
          print("Probabilidade de {0} % -> Dezenas: {1}".format(probabilidade_atual, sorted(dezenas)))
