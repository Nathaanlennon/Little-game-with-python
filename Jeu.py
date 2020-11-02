hp = 5
gender = 1
name = "random_name"
kingdom = "random_kingdom"


def command(x):
    if x == "profile":
        print(hp)


def before_game():
    print("Salutations à toi, et bienvenue dans ce jeu. Avant toute chose, veux tu jouer ?")
    game = input("oui ? non ? (commandes pour les commmandes et code pour les mdp des chapitres)")
    if game == "oui":
        print(
            "Fantastique, alors avant toute chose, quelques règles et explications : Ce jeu est un RPG sur la "
            "console, donc les fonctionnalités ne seront pas formidables. Avant de hurler pour les choix limités ("
            "comme homme ou femme), il y a une raison, certains choix ont une incidence directe sur le scenario. Il "
            "est important de bien répondre quand il y a des choix, qui seront notés entre parenthèses. S'il n'y a "
            "rien, c'est que la réponse est libre. Enfin bref, bon jeu !")
        intro_game()
    elif game == "non":
        print("dommage, on espere te revoir une autre fois.")
    elif game == "code":
        code = input("quel est le code secret ?")
        if code == "1234":
            chap1()
    elif game == "commandes":
        print("la commande \"profile\" permet d'afficher le profil")
        before_game()
    else:
        print("soit serieux dans tes réponses !")


def intro_game():
    global gender
    while gender != 1 and gender != 2:
        gender = input("Quel est ton sexe ? (homme ou femme)")
        if gender == "homme":
            gender = 1
        elif gender == "femme":
            gender = 2
        else:
            print("error")
    global name
    global kingdom
    name = input("Quel est ton nom ?")
    kingdom = input("Quel est le nom du Royaume ?")
    print(
        f"Salut à toi jeune {name}, et bienvenue dans le monde fantastique de {kingdom}, prépare toi pour une "
        f"aventure riche en experiences !")
    chap1()


def chap1():
    print("Tout commence dans le petit village de Lionna.")
    print("Tu te réveilles dans ton lit, et la première chose que tu remarques c'est la lumière étrange ainsi que la "
          "chaleur venant de la fenetre.")
    r = "none"
    while r != "se lever" and r != "rester au lit":
        r = input("que veux tu faire ? (se lever ou rester au lit)")
        command(r)
        if r == "se lever":
            print("Tu te lèves et tu sors de ta maison avant qu'elle soit engloutie par les flammes.")
        elif r == "rester au lit":
            print("la chaleur et la lumière empirent, puis tu sens l'odeur de la fumée.")
            print(
                "avant d'avoir pu faire un mouvement, les flammes envahissent ta chambre et te brulent. Tu réussis à "
                "sortir mais tu es blessé")
            global hp
            hp -= 1
            print("{tu perds 1 pv}")
        else:
            print("error(or commands")
        print("Tu regardes impuissant ta maison partir en fumée au milieu de la nuit noire et te demandes comment "
              "l'incendie a pû démarer.")
        f = 0
        global gender
        if gender == 1:
            f = "ta soeur"
        elif gender == 2:
            f = "ton frère"
        print(f"Le chef du village arrive et t'explique que des monstres ont attaqués le village et y ont mis le feu. "
              f"Il explique également que des habitants ont été enlevés, notamment {f}")


before_game()
