import streamlit as st
from random import randint

dico = {
    0: ["Bet", "Bet", "Bet", "Parier"],
    1: ["Cast", "Cast", "Cast", "Jeter"],
    2: ["Cost", "Cost", "Cost", "Coûter"],
    3: ["Cut", "Cut", "Cut", "Couper"],
    4: ["Hit", "Hit", "Hit", "Frapper"],
    5: ["Hurt", "Hurt", "Hurt", "Blesser"],
    6: ["Let", "Let", "Let", "Laisser, permettre"],
    7: ["Put", "Put", "Put", "Mettre"],
    8: ["Read", "Read", "Read", "Lire"],
    9: ["Set", "Set", "Set", "Poser, placer, installer"],
    10: ["Shut", "Shut", "Shut", "Fermer"],
    11: ["Upset", "Upset", "Upset", "Bouleverser, renverser"],

    12: ["Beat", "Beat", "Beaten", "Battre"],
    13: ["Become", "Became", "Become", "Devenir"],
    14: ["Come", "Came", "Come", "Venir"],
    15: ["Overcome", "Overcame", "Overcome", "Vaincre, surmonter"],
    16: ["Run", "Ran", "Run", "Courir"],

    17: ["Be", "Was / Were", "Been", "Être"],
    18: ["Do", "Did", "Done", "Faire"],
    19: ["Go", "Went", "Gone", "Aller"],
    20: ["Begin", "Began", "Begun", "Commencer"],
    21: ["Drink", "Drank", "Drunk", "Boire"],
    22: ["Ring", "Rang", "Rung", "Sonner"],
    23: ["Sing", "Sang", "Sung", "Chanter"],
    24: ["Swim", "Swam", "Swum", "Nager"],
    25: ["Bite", "Bit", "Bitten", "Mordre"],
    26: ["Hide", "Hid", "Hidden", "(Se) cacher"],

    27: ["Give", "Gave", "Given", "Donner"],
    28: ["Forbid", "Forbade", "Forbidden", "Interdire"],
    29: ["Forgive", "Forgave", "Forgiven", "Pardonner"],
    30: ["Drive", "Drove", "Driven", "Conduire"],
    31: ["Ride", "Rode", "Ridden", "Monter à cheval / vélo"],
    32: ["Rise", "Rose", "Risen", "S’élever, se lever"],
    33: ["Write", "Wrote", "Written", "Écrire"],
    34: ["Choose", "Chose", "Chosen", "Choisir"],
    35: ["Forget", "Forgot", "Forgotten", "Oublier"],
    36: ["Freeze", "Froze", "Frozen", "Geler"],
    37: ["Break", "Broke", "Broken", "Casser"],
    38: ["Speak", "Spoke", "Spoken", "Parler"],
    39: ["Steal", "Stole", "Stolen", "Voler, dérober"],
    40: ["Awake", "Awoke", "Awoken", "Se réveiller"],
    41: ["Shake", "Shook", "Shaken", "Secouer"],
    42: ["Take", "Took", "Taken", "Prendre"],
    43: ["Draw", "Drew", "Drawn", "Dessiner"],
    44: ["Fall", "Fell", "Fallen", "Tomber"],
    45: ["Fly", "Flew", "Flown", "Voler"],
    46: ["Blow", "Blew", "Blown", "Souffler"],
    47: ["Grow", "Grew", "Grown", "Grandir, faire pousser"],
    48: ["Know", "Knew", "Known", "Savoir"],
    49: ["Throw", "Threw", "Thrown", "Jeter"],
    50: ["Bear", "Bore", "Borne", "Supporter"],
    51: ["Tear", "Tore", "Torn", "Déchirer"],
    52: ["Swear", "Swore", "Sworn", "Jurer"],
    53: ["Wear", "Wore", "Worn", "Porter (un vêtement)"],
    54: ["Lie", "Lay", "Lain", "Être étendu(e)"],
    55: ["Eat", "Ate", "Eaten", "Manger"],
    56: ["See", "Saw", "Seen", "Voir"],

    57: ["Have", "Had", "Had", "Avoir"],
    58: ["Hear", "Heard", "Heard", "Entendre"],
    59: ["Make", "Made", "Made", "Faire, fabriquer"],
    60: ["Dream", "Dreamt", "Dreamt", "Rêver"],
    61: ["Learn", "Learnt", "Learnt", "Apprendre"],
    62: ["Mean", "Meant", "Meant", "Signifier"],
    63: ["Lead", "Led", "Led", "Mener, guider"],
    64: ["Leave", "Left", "Left", "Partir, quitter"],
    65: ["Bend", "Bent", "Bent", "(Se) courber"],
    66: ["Lend", "Lent", "Lent", "Prêter"],
    67: ["Send", "Sent", "Sent", "Envoyer"],
    68: ["Smell", "Smelt", "Smelt", "Sentir"],
    69: ["Spend", "Spent", "Spent", "Dépenser, passer"],
    70: ["Bleed", "Bled", "Bled", "Saigner"],
    71: ["Feed", "Fed", "Fed", "Nourrir"],
    72: ["Feel", "Felt", "Felt", "Sentir, ressentir"],
    73: ["Keep", "Kept", "Kept", "Garder"],
    74: ["Meet", "Met", "Met", "Rencontrer"],
    75: ["Sleep", "Slept", "Slept", "Dormir"],
    76: ["Sweep", "Swept", "Swept", "Balayer"],
    77: ["Weep", "Wept", "Wept", "Pleurer"],
    78: ["Build", "Built", "Built", "Construire"],
    79: ["Burn", "Burnt", "Burnt", "Brûler"],
    80: ["Bring", "Brought", "Brought", "Apporter"],
    81: ["Buy", "Bought", "Bought", "Acheter"],
    82: ["Fight", "Fought", "Fought", "Se battre"],
    83: ["Seek", "Sought", "Sought", "Chercher"],
    84: ["Think", "Thought", "Thought", "Penser"],

    85: ["Catch", "Caught", "Caught", "Attraper"],
    86: ["Teach", "Taught", "Taught", "Enseigner"],
    87: ["Lay", "Laid", "Laid", "Mettre, poser"],
    88: ["Pay", "Paid", "Paid", "Payer"],
    89: ["Say", "Said", "Said", "Dire"],
    90: ["Sell", "Sold", "Sold", "Vendre"],
    91: ["Tell", "Told", "Told", "Dire, raconter"],
    92: ["Stand", "Stood", "Stood", "Supporter"],
    93: ["Understand", "Understood", "Understood", "Comprendre"],
    94: ["Get", "Got", "Got", "Obtenir"],
    95: ["Shoot", "Shot", "Shot", "Tirer (sur)"],
    96: ["Lose", "Lost", "Lost", "Perdre"],
    97: ["Shine", "Shone", "Shone", "Briller"],
    98: ["Win", "Won", "Won", "Gagner"],
    99: ["Bind", "Bound", "Bound", "Lier, nouer, attacher"],
    100: ["Find", "Found", "Found", "Trouver"],
    101: ["Light", "Lit", "Lit", "Allumer"],
    102: ["Sit", "Sat", "Sat", "S’asseoir"],
    103: ["Stick", "Stuck", "Stuck", "Coller"],
    104: ["Strike", "Struck", "Struck", "Frapper, choquer"]
}

if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = {}
if "current" not in st.session_state:
    st.session_state.current = None
if "step" not in st.session_state:
    st.session_state.step = "question"
if "end" not in st.session_state:
    st.session_state.end = {}
if "dico" not in st.session_state:
    st.session_state.dico = dico.copy()
if "indice" not in st.session_state:
    st.session_state.current = None
if "indice2" not in st.session_state:
    st.session_state.current = None

st.title("Quiz Irregular Verbs")

if st.session_state.step == "question":
    st.session_state.reponse = ""
    if len(st.session_state.questions.keys()) >= len(st.session_state.dico.keys()):
        st.session_state.step = "fin"
        st.rerun()
    tab_indices = []
    for cle in st.session_state.dico.keys():
        tab_indices.append(cle)
    i = randint(0, len(tab_indices) - 1)
    while tab_indices[i] in st.session_state.end.keys():
        i = randint(0, len(tab_indices) - 1)
    indice = tab_indices[i]
    st.session_state.indice = indice
    st.session_state.step = "reponse"
    st.rerun()

if st.session_state.step == "reponse":
    indice2 = randint(0,len(st.session_state.dico[st.session_state.indice])-1)
    st.session_state.indice2 = indice2
    question = st.session_state.dico[st.session_state.indice][st.session_state.indice2]
    st.session_state.questions[st.session_state.indice] = question
    st.write("Verbe : "+question)
    with st.form("form_reponse"):
        reponse = st.text_input("Écris toutes les formes de ce verbe (ou 'stop' pour arrêter)", key="reponse_input")
        validee = st.form_submit_button("Valider")

    if validee:
        if reponse.lower() == "stop":
            st.session_state.step = "fin"
        else:
            st.session_state.step = "feedback"
            st.session_state.reponse = reponse
        st.rerun()

if st.session_state.step == "feedback":
    chaine = ""
    for car in st.session_state.dico[st.session_state.indice]:
        chaine += car + " "
    st.write("La réponse était : "+chaine)
    vrai_faux = st.radio("Tu as eu :", ["Vrai", "Faux"], horizontal=True)

    if st.button("Continuer"):
        if vrai_faux == "Vrai":
            st.session_state.score += 1
        elif vrai_faux == "Faux":
            st.session_state.end[st.session_state.indice] = st.session_state.dico[st.session_state.indice]
        st.session_state.step = "question"
        st.rerun()

if st.session_state.step == "fin":
    st.write("C'est fini ! Ton score est de : "+str(st.session_state.score)+"/"+str(len(st.session_state.questions.keys())-1)+ " Bravo mon coeur t'es trop forte !")
    if len(st.session_state.end.keys())>1:
        st.write("Tes reponses fausses etaient : ")
    elif len(st.session_state.end.keys()) == 1:
        st.write("Ta reponse fausse etait : ")
    else:
        st.write("Tu n'as eu aucune reponse fausse bravo !")
    for tab in st.session_state.end.values():
        chaine = ""
        for item in tab:
            chaine = chaine + str(item) + " "
        st.write(chaine)
    if st.button("Refaire"):
        st.session_state.score = 0
        st.session_state.questions = {}
        st.session_state.end = {}
        st.session_state.current = None
        st.session_state.step = "question"
        st.session_state.dico = dico.copy()
        st.session_state.indice = None
        st.session_state.indice2 = None
        st.rerun()
    elif st.button("Refaire avec tes erreurs"):
        if len(st.session_state.end) > 0:
            st.session_state.questions = {}
            st.session_state.score = 0
            st.session_state.current = None
            st.session_state.step = "question"
            st.session_state.dico = st.session_state.end.copy()
            st.session_state.end = {}
            st.session_state.indice = None
            st.session_state.indice2 = None
            st.rerun()
        else:
            st.warning("Tu n'as aucune erreur à refaire.")


