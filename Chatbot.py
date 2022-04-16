import pickle
import wikipedia
import pyttsx3


perguntas = {'seu nome':'Dollynho'}
arq = open('arq01.txt', 'rb')
dic = pickle.load(arq)
arq.close()
 



perguntas.update(dic)
#print (perguntas)

aux = 0



def conversar(perguntas):
   laco = 0 
   cv=0
   #print(perguntas)
   while True:
     print(90*"-")
     questao = str (input("Dollynho : diga meu amigo ,\n Dollynho: voce pode digitar sair a qualquer momento \nvocê:   "))
     
     if(questao =='Sair') or (questao=='sair'):
      break
     else:

       try :
        print(f"Dollynho :{perguntas[questao]} ")
        #print("\n")
        cv=+1
       except : 
         print("Não sei , gostaria de me ensinar?")
         
         opc = int(input("Dollynho : Digita 1 - SIM ou 2 - Não \nVocê: "))
         if(opc==1):
           
           perguntas = ensinar(perguntas)
         else:
           break
        

def conversar_com_voz(perguntas):
   laco = 0 
   cv=0
   #print(perguntas)
   print(90*"-")
   Dolly = pyttsx3.init()

   Dolly.say("digita algo meu amigo ,ou você pode digitar sair a qualquer momento ")

   Dolly.runAndWait()
   print("Dollynho : digita meu amigo ,\n Dollynho: voce pode digitar sair a qualquer momento  ")

   while True:
     
     
     
     
     questao = str (input("você: "))
     
     if(questao =='Sair') or (questao=='sair'):
      Dolly.say("Entendido ... ")

      Dolly.runAndWait()
      break
     else:

       try :
        Dolly.say(f"{perguntas[questao]} ")
        Dolly.runAndWait()
        print(f"Dollynho :{perguntas[questao]} ")
        #print("\n")
        cv=+1
       except : 
         Dolly.say("Não sei , gostaria de me ensinar?")
         Dolly.runAndWait()
         print("Dollynho : Não sei , gostaria de me ensinar?")
         Dolly.say("Digita um para SIM, ou 2 para Não  ")
         Dolly.runAndWait() 
         opc = int(input("Dollynho : Digita 1 - SIM ou 2 - Não \nVocê: "))
         if(opc==1):
           perguntas = ensinar(perguntas)
           
         else:
           break       

          
def ensinar(perguntas):
  ASSISTENTE = {}
  pergunta = input("DIGITE SUA PERGUNTA: ")
  resposta = input("DIGITE SUA RESPOSTA: ")
  ASSISTENTE[pergunta] = resposta
  perguntas.update(ASSISTENTE)
  arq = open('arq01.txt', 'wb')
  pickle.dump(perguntas, arq)
  print(ASSISTENTE)
  arq.close()


     
def pesquisa() :
    
    aux2 = 0
    while(aux2 ==0):
     print(90*"-")
     print ("Dollynho : Essa é a aba de pesquisa ")
     print (" OU digite Sair a qualquer momento para sair ")

     wikipedia.set_lang('pt')
     pesq = str(input("Dollynho : digite sua pesquisa "))
     if(pesq =='Sair') or (pesq=='sair'):
      start(perguntas)
      aux2=1
      return aux2
     else:

      try:
        print(wikipedia.summary(pesq,sentences = 1))
      except:
        print("Dollynho: Desculpa não encontrei")
           

while True :
 
 print(90*"-")
 print("Dollynho: Olá sou a unidade virtual criada para te entrerter ")   
 print("Dollynho: eu sou o dollynho , seu amiguinho , o que deseja?")
 print("1 - Conversar ")
 print("2 - Ensinar ")
 print("3 - Pesquisar na Wiki")
 print("4 - Digita que eu falo ")
 print("5 - Sair ")

 escolha = int(input(">>>"))
 if (escolha == 1):
     conversar(perguntas)
     #aux1 = 0
     #return aux1
 elif(escolha == 2):
     perguntas = ensinar(perguntas)
     #aux1 = 0
     #return aux1
 elif(escolha == 3):
     pesquisa()

 elif(escolha == 4):
     conversar_com_voz(perguntas)
    
 elif(escolha == 5):
     print("Dollynho :até logo!")
     break

    



 