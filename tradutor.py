import sys
import codecs
from google_trans_new import google_translator 

def importarTexto():
    arquivo = open(sys.argv[1], 'r')
    texto = arquivo.read()
    arquivo.close()
    return texto

def traduzir(texto):
    tradutor = google_translator()
    traducao = tradutor.translate(texto, lang_tgt='pt')
    return traducao

def exportarTexto(traducao):
    arquivo = codecs.open('traducao.txt', 'w', 'utf-8')
    arquivo.write(traducao)
    arquivo.close()
    return "Tradução feita com sucesso!"

if __name__ == '__main__':
    texto = importarTexto()
    traducao = traduzir(texto)
    saida = exportarTexto(traducao)
    print(saida)