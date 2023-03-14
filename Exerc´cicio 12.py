while(data_de_nascimento >= 1922) or (data_de_nascimento <= 2021):

      try: 
          nome = str(input("Digite seu nome completo "))
          data_de_nascimento = int(input("Digite sua data de nascimento"))  
          idade = 2021 - data_de_nascimento 
        
          if (data_de_nascimento < 1922) or ( data_de_nascimento > 2021):
            print("erro data de nascimento invalida")
     
      except Exception as e:
          print(e)