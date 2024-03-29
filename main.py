import os

from RedeNeural import RedeNeural
from loteria import resultados
from auxFunc import UltimoResultado

class MenuPrincipal():
    def __init__(self):
        self.menuPrincipalSystem()

    def menuPrincipalSystem(self):
        os.system('clear') or None
        # Apresentação
        print("\n\n ## Olá meu nome é SmalLoteria, sou um aplicativo de geração e validação de jogos. ##\n\n")

        def optionGames():
            print("""
          Essas são minhas Opções até o momento:
          (1) = Gerar Jogos 
          (2) = Conferir Jogos
          (0) = Para SAIR
      """)

        optionGames()

        first_choice = input("Qual a função desejada? ")

        if first_choice == "0":
            print("\n\n *** Agradeço sua companhia e espero que tenha ajudado. ***")
            exit()

        elif first_choice == "1":
            self.menuGeracaoDeJogos()

        elif first_choice == "2":
            self.menuResultadoLoteria()

        else:
            self.menuPrincipalSystem()

    def menuGeracaoDeJogos(self):
        os.system('clear') or None
        # Apresentação
        print("\n\n ## Olá meu nome é SmalLoteria, sou um aplicativo de geração de jogos. ##\n\n")

        def optionGames():
            print("""
                Essas são minhas Opções até o momento:
                (1) = Gerar Jogos Lotofacil 
                (2) = Gerar Jogos LotoMania
                (3) = Gerar Jogos MegaSena
                (0) = MenuPrincipal
            """)

        optionGames()

        first_choice = input("Qual a função desejada? ")

        if first_choice == "0":
            self.menuPrincipalSystem()

        elif first_choice == "1":
            self.createGamesLotofacil()

        elif first_choice == "2":
            self.createGamesLotoMania()

        elif first_choice == "3":
            self.createGamesMegaSena()

        else:
            self.menuGeracaoDeJogos()

    def createGamesLotofacil(self):
        NUMBER_GAMES = int(input ("\n Qual a quantidade de jogos a ser gerada? \n => "))
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'
        TARGET_PATH = 'D_lotfac.zip'
        NAME_FILE_HTML = 'd_lotfac.htm'
        DADOS = ['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15', 'Ganhadores_15_Números']
        DEZENAS = ['bola1','bola2','bola3','bola4','bola5','bola6','bola7','bola8','bola9','bola10','bola11','bola12','bola13','bola14','bola15']
        # NUMBER_GAMES = 3
        PROBABLY_GOOD = 95
        GAME_TEST = [1, 2, 3, 5, 7, 8, 10, 11, 12, 14, 15, 17, 21, 22, 24]
        TIPO_JOGO_NUMBER = 15
        TIPO_JOGO_NOME = 'Lotofacil'
        RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER, TIPO_JOGO_NOME)
        self.menuGeracaoDeJogos()

    def createGamesLotoMania(self):
        NUMBER_GAMES = int(input ("\n Qual a quantidade de jogos a ser gerada? \n => "))
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
        TARGET_PATH = 'D_lotoma.zip'
        NAME_FILE_HTML = 'd_lotman.htm'
        DADOS = ['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15', 'Bola16', 'Bola17', 'Bola18', 'Bola19', 'Bola20', 'Ganhadores_20_Números']
        DEZENAS = ['bola1','bola2', 'bola3', 'bola4', 'bola5', 'bola6','bola7', 'bola8', 'bola9', 'bola10', 'bola11','bola12', 'bola13', 'bola14', 'bola15', 'bola16', 'bola17', 'bola18', 'bola19', 'bola20']
        # NUMBER_GAMES = 3
        PROBABLY_GOOD = 90
        GAME_TEST = [71,63,11,44,84,11,55,93,8,29,82,62,17,64,24,14,37,97,49,51]
        TIPO_JOGO_NUMBER = 20
        TIPO_JOGO_NOME = 'Lotomania'
        RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER, TIPO_JOGO_NOME)
        self.menuGeracaoDeJogos()

    def createGamesMegaSena(self):
        NUMBER_GAMES = int(input ("\n Qual a quantidade de jogos a ser gerada? \n => "))
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
        TARGET_PATH = 'D_mgsasc.zip'
        NAME_FILE_HTML = 'd_megasc.htm'
        DADOS = ['1ª Dezena','2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', '6ª Dezena', 'Ganhadores_Sena']
        DEZENAS = ['1ª dezena','2ª dezena', '3ª dezena', '4ª dezena', '5ª dezena', '6ª dezena']
        # NUMBER_GAMES = 3
        PROBABLY_GOOD = 95
        GAME_TEST = [3, 22, 33, 35, 47, 55]
        TIPO_JOGO_NUMBER = 6
        TIPO_JOGO_NOME = 'Megasena'
        RedeNeural(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML, DADOS, DEZENAS, NUMBER_GAMES, PROBABLY_GOOD, GAME_TEST, TIPO_JOGO_NUMBER, TIPO_JOGO_NOME)
        self.menuGeracaoDeJogos()

    
    def menuResultadoLoteria(self):
        os.system('clear') or None
        # Apresentação
        print("\n\n ## Olá meu nome é SmalLoteria, sou um aplicativo de validação de resultado de jogos. ##\n\n")

        def optionGames():
            print("""
          Essas são minhas Opções até o momento:
          (1) = Resultados Jogos Lotofacil 
          (2) = Resultados Jogos LotoMania
          (3) = Resultados Jogos MegaSena
          (0) = MenuPrincipal
      """)

        optionGames()

        first_choice = input("Qual a função desejada? ")

        if first_choice == "0":
            self.menuPrincipalSystem()
        elif first_choice == "1":
            self.validGamesLotofacil()

        elif first_choice == "2":
            self.validGamesLotoMania()

        elif first_choice == "3":
            self.validGamesMegaSena()

        else:
            self.menuResultadoLoteria()

    def validGamesLotofacil(self):
        os.system('clear') or None
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'
        TARGET_PATH = 'D_lotfac.zip'
        NAME_FILE_HTML = 'd_lotfac.htm'
        RESULTADO_LOTOFACIL = UltimoResultado(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML)
        print('\n##### RESULTADO LOTOFACIL  ##### \n\n')
        tipo = 'lotofacil'
        nomeArquivo = 'Lotofacil'
        resultados(tipo, RESULTADO_LOTOFACIL, nomeArquivo)
        print('\n\n ########## LOTOFACIL  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuResultadoLoteria()

    def validGamesLotoMania(self):
        os.system('clear') or None
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
        TARGET_PATH = 'D_lotoma.zip'
        NAME_FILE_HTML = 'd_lotman.htm'
        RESULTADO_LOTOMANIA = UltimoResultado(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML)
        print('\n ##### RESULTADO LOTOMANIA  ##### \n\n')
        tipo = 'lotomania'
        nomeArquivo = 'Lotomania'
        resultados(tipo, RESULTADO_LOTOMANIA, nomeArquivo)
        print('\n\n ########## LOTOMANIA  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuResultadoLoteria()

    def validGamesMegaSena(self):
        os.system('clear') or None
        URL_DOWNLOAD = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
        TARGET_PATH = 'D_mgsasc.zip'
        NAME_FILE_HTML = 'd_megasc.htm'
        RESULTADO_MEGASENA = UltimoResultado(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML)
        print('\n ##### RESULTADO MEGA SENA  ##### \n\n')
        tipo = 'megasena'
        nomeArquivo = 'Megasena'
        resultados(tipo, RESULTADO_MEGASENA, nomeArquivo)
        print('\n\n ########## MEGA SENA  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuResultadoLoteria()
if __name__ == "__main__":
    MenuPrincipal()
