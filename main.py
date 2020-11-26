from LotoFacil import LotoFacil
from Mega_Sena import MegaSena
from LotoMania import LotoMania

class Principal():
  def __init__(self):
    self.menuSistema()

  def menuSistema(self):
    valor = -1
    while(valor != 0):
      print('Escolha uma das opções abaixo:')

  def createGamesLotofacil(self):
    LotoFacil()

  def createGamesLotoMania(self):
    LotoMania()

  def createGamesMegaSena(self):
    MegaSena()

if __name__ == "__main__":
    Principal()