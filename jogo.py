#importando bibliotecas uteis
import random


#definindo estado inicial do personagem
saude, poder = 5, 0
vitoria = 0

#definindo estado inicial do inimigo
saude_inimigo, poder_inimigo = 5, 0


#definindo eventos como funcoes
def sofrer_dano (saude, poder_inimigo):
    dano = (random.randint(1, 5) + poder_inimigo)
    saude = saude - dano
    print(f"Dano sofrido:{dano} \nSaude restante:{saude}") #testando
    if saude <= 0:
        print("Vocë foi destruido!\n\n")
    else:
        print("Voce foi ferido.\n\n")
    return saude

def recuperar_dano (saude):
    cura = random.randint(1, 5)
    saude = saude + cura
    if saude > 5: saude = 5
    print(f"Cura realizada:{cura} \nSaude total:{saude}\n")

    if saude == 5:
        print ("Seus ferimentos foram completamente recuperados!\n\n")
    else:
        print ("Seus ferimentos foram parcialmente recuperados.\n\n")
    return saude

def causar_dano (poder, saude_inimigo):
    dano = (random.randint(1, 5) + poder)
    saude_inimigo = saude_inimigo - dano
    print(f"Dano causado:{dano} \nSaude inimiga restante:{saude_inimigo}") # testando
    if saude_inimigo <= 0:
        print ("Vocë destruiu o inimigo!\n\n")
    else:
        print ("Vocë feriu o inimigo!\n\n")
    return saude_inimigo

def combater (combate, saude, saude_inimigo, poder, vitoria):
    lutando = True
    while lutando == True:
        print("-----------------------------")
        print("\nVocë ataca o inimigo...\n\n")
        saude_inimigo = causar_dano(poder, saude_inimigo)

        if saude_inimigo > 0:
            print("O inimigo te ataca!\n\n")
            saude = sofrer_dano(saude, poder_inimigo)

        else:
            print("Fim do combate.\n\n")
            print("-----------------------------")
            #poder aumentando por vitoria
            poder += 0.5
            vitoria += 1
            
            #simulando recuperar ferimentos
            print("Tentando recuperar ferimentos...\n\n")
            saude = recuperar_dano(saude)
            lutando = False
            return combate, saude, saude_inimigo, poder, vitoria
            
        if saude <= 0:
            lutando = False
            return combate, saude, saude_inimigo, poder, vitoria
                
        
#rodando o jogo
while True:
    print("-----------------------------")
    combate = input("Deseja enfrentar um inimigo? S/N\n\n").upper()
    if combate == "S":
        combate, saude, saude_inimigo, poder, vitoria = combater(combate, saude, saude_inimigo, poder, vitoria)
        saude_inimigo = 5
        
        if saude <= 0:
            print("-----------------------------")
            print (f"Saude final:{saude}\nPoder final:{poder}\nInimigos derrotados:{vitoria}\n\nFim de Jogo.")
            break 

    else:
        print("-----------------------------")
        print (f"Saude final:{saude}\nPoder final:{poder}\nInimigos derrotados:{vitoria}\n\nFim de Jogo.")
        break
    











