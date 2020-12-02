from GamesLoteria import GamesLoteria

def resultado_lista_inteiro(resultado):
    resultado = list(map(int, resultado.split(",")))
    return resultado

def compara_resultado(resultado, x):
    resultado_ = set(resultado).intersection(x)
    acertos = len(resultado_)
    return acertos

def UltimoResultado(URL_DOWNLOAD, TARGET_PATH, NAME_FILE_HTML):
  #ATUALIZANDO RESULTADOS
  print('Baixando resultados...')
  GamesLoteria.downloadZipAndUnzip(URL_DOWNLOAD, TARGET_PATH)
  print('Atualizando resultados...')
  resultadosLotofacil = GamesLoteria.getByAllGames(NAME_FILE_HTML)
  ultimoresultado = resultadosLotofacil[-1:]
  if not NAME_FILE_HTML:
      return
  if NAME_FILE_HTML == 'd_lotfac.htm':
      bolasSorteadas = str(ultimoresultado[['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15']])
  elif NAME_FILE_HTML == 'd_lotman.htm':
      bolasSorteadas = str(ultimoresultado[['Bola1','Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6','Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11','Bola12', 'Bola13', 'Bola14', 'Bola15', 'Bola16', 'Bola17', 'Bola18', 'Bola19', 'Bola20']])
  elif NAME_FILE_HTML == 'd_megasc.htm':
      bolasSorteadas = str(ultimoresultado[['1ª Dezena','2ª Dezena', '3ª Dezena', '4ª Dezena', '5ª Dezena', '6ª Dezena']]) 
  concurso = str(ultimoresultado['Concurso'])
  print('Concurso =>', concurso[8:12])
  bolasSorteadas = bolasSorteadas[126:]
  bolasSorteadas = bolasSorteadas.replace('     ', ',')
  bolasSorteadas = bolasSorteadas.replace(' ', '')
  resultado = resultado_lista_inteiro(bolasSorteadas)
  print('Bolas Sorteadas =>', sorted(resultado))
  return resultado