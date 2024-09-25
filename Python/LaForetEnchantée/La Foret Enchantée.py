Loose=False
print("Bonjour et bienvenue dans la fôret enchantée")
print("Tu te trouve face à deux chemins : \n\tChemin 1 : Un sentier sombre où tu entends des bruits inquiétants.\n\tChemin 2 : Un sentier éclairé par des lucioles, plus calme.")

#premier mouvement
premier_mvt=int(input("Par quel chemin souhaitez vous passer ?"))
if premier_mvt == 1:
    print("\nTu avances prudemment, mais tu entends un bruit étrange venant des arbres.\n")
    
    # Rencontre avec le danger bruit
    
    print("Tu te trouve face à deux choix : \n\tChoix 1 : Tu t'arrêtes et cherches à identifier la source du bruit. \n\tChoix 2 : Tu continues à avancer rapidement en espérant que cela ne te suive pas.")
    
    mvt_bruit=int(input("Quel choix souhaitez vous faire ?"))
    
    if mvt_bruit == 1 :
        print("\nC'était un piège ! Un groupe de brigands t'attrape et te vole tout ce que tu possèdes. Tu as échoué !")
        Loose=True
    elif mvt_bruit == 2:
        print("\nBonne décision ! Tu as évité le piège et tu continues ton chemin.")

    # Rencontre avec le danger loup-garou
    
elif premier_mvt == 2:
    print("\nTu marches tranquillement, mais soudain, un loup-garou apparaît.\n")
    print("Tu te trouves face à deux choix : \n\tChoix 1 : Courir vers un grand arbre pour te cacher.\n\tChoix 2 : Te battre avec une épée que tu trouves par terre.")
    
    mvt_loup_garou=int(input("Quel choix souhaitez vous faire ?"))

    if mvt_loup_garou == 1 :
        print("\nMalheureusement, le loup-garou te rattrape. Tu n'as pas été assez rapide. Fin de l'aventure.")
        Loose=True
    elif mvt_loup_garou ==2 :
        print("\nIncroyable ! Tu as réussi à le vaincre, et tu continues ta route.")


#La rivière magique :
if Loose!=True :
    print("\nAprès avoir évité le danger, tu arrives devant une rivière. Deux options s'offrent à toi :\n\tOption 1 : Traverser la rivière à la nage. \n\tOption 2 : Suivre la rivière en espérant trouver un pont plus loin.")
    mvt_riviere=int(input("Quel choix souhaitez vous faire ?"))
    if mvt_riviere == 1 :
        print("\nMauvais choix. L'eau de la rivière est empoisonnée. Fin de l'aventure.")
        Loose=True
    elif mvt_riviere == 2 :
        print("\nBravo ! Tu trouves un pont après quelques minutes de marche.")


#Le pont maudit
if Loose!=True :
    print("Tu arrives finalement à un vieux pont en bois, mais une étrange créature apparaît et te dit que tu dois résoudre une énigme pour traverser.")
    print("L'énigme est la suivante : \"Je suis léger comme une plume, mais personne ne peut me tenir longtemps. Qui suis-je ?\"")
    print("\n\tRéponse 1 : \"Le souffle.\"\n\tRéponse 2 : \"L'eau.\"\n\tRéponse 3 : \"L'ombre.\"")
    reponse_enigme=int(input("Quelle est votre réponse ?"))
    if reponse_enigme==1 :
        print("\nFélicitations ! La créature te laisse passer, et tu continues ta quête.")
    elif reponse_enigme==2 or reponse_enigme==3:
        print("\nMauvaise réponse. La créature te jette dans la rivière et tu échoues.")
        Loose=True

if Loose!=True :
    print("\nAprès avoir traversé le pont, tu aperçois enfin la sortie de la forêt. \nCependant, un dernier choix crucial s'impose :")
    print("\tOption 1 : Prendre un raccourci à travers un champ de fleurs toxiques.\n\tOption 2 : Suivre le sentier principal, plus long mais sûr.")
    mvt_sortie=int(input("Quelle est votre choix ?"))
    if mvt_sortie ==1 :
        print("\nLe champ de fleurs toxiques t'endort à jamais. Fin de l'aventure.")
        Loose=True
    elif mvt_sortie ==2 :
        print("\nFélicitations ! Tu sors enfin de la forêt enchantée, sain et sauf.")
