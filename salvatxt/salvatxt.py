import pickle

ASSISTENTE = {}
pergunta = input("DIGITE SUA PERGUNTA: ")
resposta = input("DIGITE SUA RESPOSTA: ")
ASSISTENTE[pergunta] = resposta
arq = open('arq01.txt', 'wb')
pickle.dump(ASSISTENTE, arq)
print(ASSISTENTE)
arq.close()


arq = open('arq01.txt', 'rb')
dic = pickle.load(arq)
arq.close()
print(dic)