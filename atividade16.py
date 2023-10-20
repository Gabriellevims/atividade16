# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.
print("você tem direito a fila prioritária?")
pri= str(input("Digite corretamente se você é idoso, se é gestante, se é cadeirante ou nenhum destes:"))
if pri == "idoso" or pri == 'gestante' or pri=='cadeirante':
    print("você tem prioridade")
else:
    print("você não tem prioridade") 