a=[10,2,1]
b=[11,10,5]
c=[4,3,2,1]

def resta(valores):
     resultado=[]
     diftotal=[]
     suma=0

     
     for i in range (len(valores)-1):
          print("valores "+str(valores[i]))
          resultado.append(valores[i]-valores[i+1]) 
          print("resultado ",resultado)
     
     def sumatorios(resultado) :
          for num in range (len(resultado)):
               suma = suma + resultado [num]
               print("resultado final ",suma)
               print("valores sumatorios "+str(resultado[i]))


resta(a)