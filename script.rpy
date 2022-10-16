define a = Character("Albert", color = "#338DFF")
define b = Character("Bertrand", color = "#13fc03")
define c = Character("Charles", color = "#fc03a5")
define n = Character("Eco-Genie", color = "#9532a8")
image bureau = im.Scale("bureau.jpg",1280,720)
image cite = im.Scale("cite.jpg",1280,720)
image graphe = im.Scale("graphe.png", 800,400)
image feu_artifice = im.Scale("feu_artifice.jpg",1280,720)
image desastre = im.Scale("desastre.jpg",1280,720)
image endscene = im.Scale("endscene.png",1280,720)
image a1 = im.Scale("a1.png",400,600)
image a2 = im.Scale("a2.png",400,600)
image a3 = im.Scale("a3.png",400,600)
image b1 = im.Scale("b1.png",400,600)
image b2 = im.Scale("b2.png",400,600)
image b3 = im.Scale("b3.png",400,600)
image c1 = im.Scale("c1.png",400,600)
image c2 = im.Scale("c2.png",400,600)
image c3 = im.Scale("c3.png",400,600)
image g = im.Scale("genie.png",300,500)
define fastdissolve = Dissolve(0.4)

label start:
    $ GameRunning = True
    $ breponses = 0
    $ pseudo =""
    play music "audio/musique.mp3"
    
    show cite with fastdissolve
    
    show g:
        xalign 0.5
        ypos 0.3


    with fastdissolve 
    n "Bienvenu(e) au jeu France relance : The Game."

    menu:
        "Je suis..."
        "Monsieur le Président de la Republique Française":
            $ pseudo = "M. le Président "

        "Madame la Présidente de la Republique Française":
            $ pseudo = "Mme. la Présidente "

    $ pseudo += renpy.input("Entrez votre pseudo")
         
label s10:
    n "[pseudo], je vous explique la situation."
    n "Nous sommes en pleine crise sanitaire: la Covid-19."
    n "Le gouvernement français vient d’annoncer le confinement et la situation devient chaotique."
    n "Nous nous trouvons face à 3 situations:\nle télétravail, le travail sur site et le chômage."
    n "Le 25 mars 2020, l’INSEE relève une baisse de 35\% du PIB en seulement une semaine."
    n "Les demandes d’emplois s’élèvent à 840 000!"
    n "Voici un aperçu de l'évolution du PIB"
    hide g with fastdissolve
    show graphe:
        xalign 0.5
        ypos 0.15
    
    
    n "[pseudo], nous sommes clairement en pleine crise économique!"
    n "Il faut agir et vite!"
    hide graphe with fastdissolve
    show g with fastdissolve
    
    n "Le futur de notre pays est entre vos mains."
    n "A vous de faire les choix judicieux afin de sauver notre économie!"
    hide g with fastdissolve 
    hide cite with fastdissolve
    show bureau with fastdissolve
    show a1 with fastdissolve
    
    a "Nous voici à la première réunion du conseil présidentiel."
    a "Il est important de préserver le tissu productif et de geler les emplois."
    a "Il faudrait organiser un plan d’urgence afin de revenir à une situation stable comme celle de “l’avant crise”." 
    a "Qu'en pensez-vous [pseudo]?\nQuels sont les objectifs importants à atteindre?"
    
    hide a1 with fastdissolve
    show screen breponses with fastdissolve
    
    menu:
        "{size=30}- développement de nouvelles entreprises/activités\n- éviter l’augmentation du chômage\n- inciter les entreprises à emprunter afin de rester sur le marché":
            with fastdissolve
            jump s12
        "{size=30}- développement de nouvelles entreprises/activités\n- éviter l’augmentation du chômage\n- éviter les liquidations des entreprises":
            with fastdissolve
            jump s11 
            
        
            
label s11:
    show a2 with fastdissolve
    $ breponses+=1
    a "C’est exactement ça!"
    a "Il faudrait donc éviter l’augmentation du chômage..."
    a "et éviter la liquidation des entreprises qui auraient été viables en temps normal."
    hide a2 with fastdissolve
    jump s20

label s12:
    show a3 with fastdissolve
    a "Attention, les emprunts fréquents des entreprises ne feront qu’augmenter leurs dettes!"
    a "Avec la crise sanitaire, ils se retrouvent face à une situation où leur activité est en baisse." 
    a "Ils auront alors des difficultés à rembourser leur créditeur!"
    hide a3 with fastdissolve
    
label s20:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "En 2008, les taux d’intérêts augmentent et la difficulté des entreprises à rembourser les crédits persiste." 
    n "On aura alors une baisse des prix de l’immobilier et moins de consommation!"
    n "Le PIB chute considérablement et le chômage s’impose." 
    n "Pour y remédier, le gouvernement allemand a mis en place le “Kurzarbeit” ou chômage partiel pour éviter le licenciement des salariés." 
    n "En France, des prêts ont été accordés à certaines entreprises ainsi que des aides destinées aux ménages entre 2008 et 2010." 
    n "La crise de covid-19 est une crise sanitaire."
    n "La population était contrainte au confinement à partir de mars 2020 donc la consommation était moindre." 
    n "De plus, certaines entreprises devaient fermer. Il faut aider ces entreprises!"

    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show b1 with fastdissolve

    b "Afin de soutenir les entreprises en difficulté, l’Etat pourrait également mettre en place un plan d’urgence concernant le marché du travail."
    b "[pseudo], quel type d'activité faudra-t-il mettre en place pour les entreprises?"
    hide b1 with fastdissolve
    
    menu:
        "- moins d’heures de travail\n- maintien du contrat de travail\n- l’employé reçoit 84\% de son salaire\n- l’employeur est remboursé":
            with fastdissolve
            jump s21 
            
        "- maintien des heures de travail\n- maintien du contrat de travail \n- l’employé reçoit 100\% de son salaire\n- l’employeur n’est pas remboursé":
            with fastdissolve
            jump s22
    
label s21: 
    $ breponses+=1
    show b2 with fastdissolve
    b "Gagné! l’activité partielle est évidemment le choix raisonnable"
    b "Ce dispositif permettra d’éviter les licenciements résultant de la baisse de l’activité liée à l’épidémie de Covid-19."
    hide b2 with fastdissolve
    jump s30

label s22:
    show b3 with fastdissolve
    b "Nous voulons absolument éviter la faillite de l’entreprise!"
    b "L’employeur ne pourra pas rémunérer ses employés à 100\% alors que ces derniers ne travaillent pas à temps plein."
    hide b3 with fastdissolve

label s30:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "Pendant la crise sanitaire, la profusion des données (comme l’utilisation de Twitter ou bien les statistiques)..."
    n "a été le facteur clé dans la conception des politiques publiques."  
    n "Les politiques publiques rassemblent les décisions prises par l’Etat."
    n "Quelques rappels avant votre prochaine réunion..."
    n "{size=25}Une subvention est une aide financière allouée par un organisme public, sans aucune obligation de remboursement, en vue de financer une activité d'intérêt général."
    n "Un prêt, quant à lui, devra être éventuellement remboursé par le détenteur."

    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show c1 with fastdissolve
    c "A présent, nous avons déterminé les objectifs à atteindre afin de sauver l’économie."
    c "Mais comment pouvons-nous soutenir les entreprises françaises?"
    c "J’ai un tour de carte dans ma poche:\nle plan appelé “Quoi qu’il en coûte”"
    c "Je propose d’attribuer un soutien de 240 milliards d'euros au total, aux entreprises."
    c "Mais [pseudo], comment allons-nous répartir cette somme?"
    hide c1 with fastdissolve
    
    menu: 
        "⅓ de prêts et ⅔ de subventions":
            with fastdissolve
            jump s32
        "⅓ de subventions et ⅔ de prêts":
            with fastdissolve
            jump s31
    
    
label s31:
    show c2 with fastdissolve
    $ breponses+=1
    a "C’est une excellent répartition."
    hide c2 with fastdissolve
    jump s40

label s32:
    show c3 with fastdissolve
    a "Êtes-vous sûr de votre choix ?"
    a "⅔ de subventions représente quand même une grande part de dépenses."
    a "Elles constituent une dette importante pour l’Etat."
    a "C’est pourquoi, il serait préférable de répartir de la manière suivante:"
    a "⅓ en subventions et ⅔ prêts."   
    hide c3 with fastdissolve

label s40:
    show a1 with fastdissolve
    a "C’est décidé!"
    a "Nous allons alors répartir cette somme de la manière suivante:"
    a "80 milliards d’euros de subventions pour protéger le pouvoir d’achat des entreprises."
    a "et 160 milliards d’euros de prêts garantis par l'Etat (PGE)."
    a "Mais comment allons-nous répartir ces mesures de soutien sur le territoire français?"
    hide a1 with fastdissolve

    menu: 
        "Répartition égale sur tout le territoire.":
            with fastdissolve
            jump s41

        "Prioriser les territoires observant une baisse de leur activité.":
            with fastdissolve
            jump s42

label s41:
    show a3 with fastdissolve
    a "Il faut garder en tête les objectifs des mesures de soutien:"
    a "éviter les destructions massives d’emplois et d’entreprises."
    a "Il faudrait alors prioriser les territoires observant une baisse de leur activité."
    hide a3 with fastdissolve
    jump s50

label s42:
    $ breponses+=1
    show a2 with fastdissolve
    a "Vous avez tout à fait raison!"
    hide a2 with fastdissolve

label s50:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "Les entreprises ont fait face à une baisse de l’activité sans précédent."
    n "Elles ont bénéficié de subventions mais se retrouvent avec une dette brute importante."
    n "Cet endettement a augmenté avec les PGE et les reports de cotisations sociales."
    n "Cependant, leur endettement net est resté plutôt stable."
    n "La baisse de l’activité s’explique aussi par l’intensité de la crise, le développement du télétravail..."
    n "{size=25}et les effets de ruissellements (dans un département où les employés ne travaillent pas, les entreprises connaissent une baisse de leur activité)."
    n "La crise a touché de manière équivalente des territoires qui étaient prospères avant la crise et des territoires qui étaient plus vulnérables."
    n "Au total, une bonne centaine de milliards d’euros d’argent public a été dépensée par l’Etat pour maintenir l’économie à flot. "
    n "Cela a permis de sauver le pouvoir d’achat des Français, des centaines de milliers d’entreprises et des millions d’emplois."
    n "Vos choix ont été pertinents ! La catastrophe a donc été évitée!"
    n "Il faut continuer dans cette avancée afin de relancer l’économie."
    n "Quelques rappels pour votre prochaine réunion décisive..."
    n "Une politique de relance, aussi appelée plan de relance, désigne un ensemble de mesures qui ont pour but de relancer l'économie d'un pays..."
    n "ou d'une zone monétaire lors des périodes de faible croissance."
    n "Une dépression correspond à une baisse forte et durable de la production et de la consommation."
    n "A ne pas confondre avec une récession qui correspond à une phase de diminution de l’activité économique."
    n "La valeur ajoutée est avant tout un indicateur économique servant à mesurer la valeur ou la richesse créée par une entreprise."

    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show b1 with fastdissolve
    b "Très bien, projetons nous et pensons à un scénario post-crise covid."
    b "Je propose le plan de relance nommé France relance afin de relancer l'économie et ressortir renforcé de la crise."
    b "[pseudo], quels seraient les enjeux de ce plan de relance?"
    hide b1 with fastdissolve
    
    menu: 
        "- Ne pas sortir des mesures d’urgence trop vite \n- Eviter que la crise laisse des cicatrices\n- Anticiper les besoins des entreprises en sortie de crise":
            with fastdissolve
            jump s51
        
        "- Prendre des mesures d’urgence temporaires\n- Développement de la valeur ajoutée\n- Développement d’emplois industriels sur le sol français":
            
            with fastdissolve
            jump s52
    

label s51:
    $ breponses+=1
    show b2 with fastdissolve
    b "Réponse correcte ! Ces mesures seront essentielles à la reconstruction de notre économie."
    hide b2 with fastdissolve
    jump s60

label s52:
    show b3 with fastdissolve
    b "Mauvais choix !"
    b "Le plan de relance n’a pas pour objectif de prendre des mesures temporaires..."
    b "mais plutôt des mesures qui vont avoir des conséquences sur le long terme."
    hide b3 with fastdissolve

label s60:
    show c1 with fastdissolve
    c "[pseudo], passons à l’étape suivante de la conception de ce plan." 
    c "Quels sont les secteurs à cibler?"
    hide c1 with fastdissolve
    menu:
        "- L’amélioration de la compétitivité des entreprises et l’innovation \n- Transition écologique \n- Industrie pharmaceutique":
            with fastdissolve
            jump s61

        "- Transition écologique \n- L’amélioration de la compétitivité des entreprises et l’innovation \n- La cohésion sociale et territoriale":
            with fastdissolve
            jump s62

label s61:
    show c3 with fastdissolve
    c "C’est un mauvais choix..."
    c "Il faudrait davantage investir dans la cohésion sociale et territoriale."
    hide c3 with fastdissolve
    jump s70

label s62:
    $ breponses+=1
    show c2 with fastdissolve
    c "Oui! Bonne réponse!"
    hide c2 with fastdissolve

label s70:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "Faisons le point."
    n "L’objectif est tout d'abord d’accélérer la conversion écologique de l’économie française pour qu’elle soit plus durable et plus économe."
    n "{size=25}La compétitivité est également un aspect majeur permettant de favoriser un développement important de l’activité en France."
    n "{size=25}Enfin, la cohésion représente un volet significatif permettant d’éviter la hausse des inégalités en France en raison de l’impact économique de la crise."
    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show a1 with fastdissolve
    a "[pseudo], à votre avis, quelle est la somme totale que l’on doit attribuer?"
    hide a1 with fastdissolve

    menu:
        "250 milliards d’euros":
            with fastdissolve
            jump s71
        "100 milliards d’euros":
            with fastdissolve
            jump s72

label s71:
    show a3 with fastdissolve
    a "250 milliards d'euros? Cela paraît beaucoup, vous ne trouvez pas ?"
    a "Je pense qu'un budget de 100 milliards d’euros serait plus raisonnable."
    hide a3 with fastdissolve
    jump s80

label s72:
    $ breponses+=1
    show a2 with fastdissolve
    a "C’est noté!"
    hide a2 with fastdissolve


label s80:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "100 milliards (sur 2 ans) représentent 4\% du PIB. Très bien!" 
    n "Il serait judicieux de répartir les 100 milliards d’euros de la manière suivante:"
    n "30 milliards d’euros à la transition écologique"
    n "34 milliards d'euros à la compétitivité et l'innovation"
    n "36 milliards d’euros à la cohésion sociale et territoriale"
    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show b1 with fastdissolve
    b "[pseudo], comment devons-nous répartir ces aides sur le territoire français?"
    hide b1 with fastdissolve

    menu:
        "répartition en faveur de nouveaux projets et du relancement de l’activité":
            with fastdissolve
            jump s81 
        "répartition selon la baisse de l’activité":
            with fastdissolve
            jump s82

label s81:
    $ breponses+=1
    show b2 with fastdissolve
    b "Bonne réponse !"
    b "En effet, il faut s’intéresser à l’émergence de projets ainsi qu’à la création de l’activité dans chaque territoire..."
    b "{size=25}pour répondre aux différents type de besoins dans les secteurs de l’emploi, la formation ainsi que des transitions écologiques et numériques, etc."
    hide b2 with fastdissolve
    jump s90


label s82:
    show b3 with fastdissolve
    b "Mauvais choix"
    b "Il n'y a pas de corrélation forte entre les mesures de relance et la baisse d'activité..."
    b "mais on s'aperçoit que certaines des mesures du plan de relance ont bénéficié aux bassins d'emplois qui, avant la crise, étaient fragiles."
    b "Cela a permis de donner de l'élan à leur économie locale."
    hide b3 with fastdissolve

label s90:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "L'économie se base souvent sur des projections lors de la prise de décisions."
    n "Il faut toujours prendre en compte l'évolution du comportement des agents économiques."
    hide g with fastdissolve
    hide cite with fastdissolve
    show bureau with fastdissolve
    show c1 with fastdissolve
  
    c "[pseudo], selon vous, quelle est l'épreuve principale à relever dans les mois à venir? "
    hide c1 with fastdissolve

    menu:
        "Il s’agit de s'adapter en fonction de l'évolution des comportements de la population.":
            with fastdissolve 
            jump s91
        "Il s'agit de s'adapter en fonction de nos pays voisins.":
            with fastdissolve
            jump s92
  
label s91:
    $ breponses+=1
    show c2 with fastdissolve
    c "Bonne réponse!"
    c "Le comportement de la population a changé avec l'émergence de la crise." 
    
    hide c2 with fastdissolve
    jump final


label s92:
    show c3 with fastdissolve
    c "Mauvaise réponse!"
    c "Il ne faut pas s'adapter en fonction de ce que font les autres pays."
    c "Chaque pays possède sa propre manière de fonctionner."
    hide c3 with fastdissolve

label final:
    hide bureau with fastdissolve
    show cite with fastdissolve
    show g with fastdissolve
    n "{size=25}On notera une augmentation des achats en ligne mais également des investissements massifs dans la technologie de la communication."
    n "{size=25}Par ailleurs, on note la forte dimension sectorielle puisque les restaurants ainsi que les déplacements vers l’international ont pu revoir le jour."
    hide cite with fastdissolve
    hide g with fastdissolve
    if breponses >= 7:
      show feu_artifice with fastdissolve
      show g:
        xoffset 10
        ypos 0.3
      
      n "Félicitations! vous avez parfaitement géré la situation!"
      n "Notre économie est sauvée et la crise est sous contrôle!"
      n "Votre Eco-Genie reste toujours à votre disposition."
      hide g with fastdissolve
      hide feu_artifice with fastdissolve

    else:
      show desastre with fastdissolve
      show g:
        xoffset 10
        ypos 0.3
      
      n "Malgré vos efforts, l'économie n'a pas pu être sauvée..."
      n "Vous pouvez toujours recommencer une partie à partir du menu principal."
      n "Votre Eco-Genie reste toujours à votre disposition."
      hide g with fastdissolve
      hide desastre with fastdissolve

    scene
    show endscene with fastdissolve
    pause


    scene black with dissolve
    return
