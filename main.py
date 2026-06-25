from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import RedirectResponse
from model import predict_prepa
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
import random
import os

app=FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.environ["cle_secrete"])

@app.get("/",response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="fr">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>PARCOURINF</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    min-height:100vh;
    background:
    radial-gradient(circle at top left,#2563eb 0%,transparent 35%),
    radial-gradient(circle at bottom right,#7c3aed 0%,transparent 35%),
    #050816;
    color:white;
    overflow-x:hidden;
}

header{
    text-align:center;
    padding:30px;
}

header h1{
    font-size:60px;
    font-weight:900;
    letter-spacing:2px;
    background:linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

header p{
    margin-top:10px;
    color:#cbd5e1;
    font-size:18px;
}

.hero{
    text-align:center;
    padding:80px 20px;
    max-width:1000px;
    margin:auto;
}

.hero h2{
    font-size:60px;
    margin-bottom:25px;
    line-height:1.1;
}

.hero span{
    background:linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero p{
    max-width:800px;
    margin:auto;
    font-size:22px;
    color:#d1d5db;
    line-height:1.7;
}

button{
    margin-top:40px;
    padding:18px 40px;
    border:none;
    border-radius:50px;

    background:linear-gradient(
    90deg,
    #2563eb,
    #7c3aed
    );

    color:white;
    font-size:20px;
    font-weight:bold;

    cursor:pointer;

    transition:0.3s;
}

button:hover{
    transform:translateY(-5px) scale(1.05);
    box-shadow:
    0 15px 35px rgba(96,165,250,0.4);
}

.cards{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:30px;
    padding:50px 20px 80px;
}

.card{
    width:320px;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(12px);

    border:1px solid rgba(255,255,255,0.1);

    border-radius:25px;

    padding:30px;

    transition:0.3s;
}

.card:hover{
    transform:translateY(-10px);
    border-color:#60a5fa;
}

.card h3{
    font-size:24px;
    margin-bottom:15px;
}

.card p{
    color:#cbd5e1;
    line-height:1.6;
}

.stats{
    display:flex;
    justify-content:center;
    gap:40px;
    flex-wrap:wrap;
    padding:20px;
    margin-bottom:60px;
}

.stat{
    text-align:center;
}

.stat h4{
    font-size:40px;
    color:#60a5fa;
}

.stat p{
    color:#cbd5e1;
}

@media(max-width:768px){

    header h1{
        font-size:42px;
    }

    .hero h2{
        font-size:38px;
    }

    .hero p{
        font-size:18px;
    }

    .card{
        width:90%;
    }

}

</style>

</head>

<body>

<header>

<h1>PARCOURINF</h1>

<p>Simulateur intelligent d'orientation post-bac</p>

</header>

<section class="hero">

<h2>
Comprendre ses chances,
<br>
<span>anticiper son avenir</span>
</h2>

<p>
Explore l'accessibilité de nombreuses formations,
simule l'évolution d'une candidature Parcoursup
et découvre les opportunités qui correspondent
à ton profil.
</p>

<form action="/choix">
<button>
 Commencer la simulation !
</button>
</form>

</section>

<div class="stats">

<div class="stat">
<h4>IA</h4>
<p>Analyse automatique</p>
</div>

<div class="stat">
<h4>40</h4>
<p>Jours simulés</p>
</div>

<div class="stat">
<h4>∞</h4>
<p>Scénarios possibles</p>
</div>

</div>

<section class="cards">

<div class="card">
<h3> Simulation dynamique</h3>
<p>
Observe jour après jour l'évolution d'une candidature et la progression des appels.
</p>
</div>

<div class="card">
<h3> Intelligence Artificielle</h3>
<p>
Un modèle de Machine Learning estime les probabilités d'admission à partir du profil renseigné.
</p>
</div>

<div class="card">
<h3> Orientation</h3>
<p>
Mieux comprendre les formations, leur sélectivité et les stratégies possibles.
</p>
</div>

</section>

</body>
</html>
"""

@app.get("/choix", response_class=HTMLResponse)
def form():
    return """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: #0b1220;
        color: white;
    }

    .wrapper {
        max-width: 1100px;
        margin: auto;
        padding: 30px;
    }

    .header {
        text-align: center;
        margin-bottom: 30px;
    }

    .header h1 {
        margin: 0;
        font-size: 34px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .header p {
        color: #a1a1aa;
        margin-top: 8px;
    }

    .grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }

    .card {
        background: #111a2e;
        border: 1px solid #1f2a44;
        border-radius: 14px;
        padding: 20px;
    }

    .card h2 {
        margin-top: 0;
        font-size: 18px;
        color: #93c5fd;
        margin-bottom: 15px;
    }

    .option {
        display: flex;
        align-items: center;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 8px;
        background: #0f172a;
        transition: 0.2s;
        cursor: pointer;
    }

    .option:hover {
        background: #111c36;
    }

    input[type="radio"] {
        transform: scale(1.2);
        accent-color: #60a5fa;
        margin-right: 10px;
    }

    label {
        cursor: pointer;
        width: 100%;
    }

    .btn {
        width: 100%;
        margin-top: 25px;
        padding: 14px;
        border: none;
        border-radius: 12px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.2s;
    }

    .btn:hover {
        transform: scale(1.02);
    }

    @media (max-width: 900px) {
        .grid {
            grid-template-columns: 1fr;
        }
    }
</style>
</head>

<body>

<div class="wrapper">

    <div class="header">
        <h1>PARCOURINF</h1>
        <p>Simulateur intelligent de parcours post-bac</p>
    </div>

<form action="/save">

<div class="grid">

    <div class="card">
        <h2>Orientation après le lycée</h2>

        <div class="option">
            <input type="radio" id="prepa" name="etude" value="prépa scientifique">
            <label for="prepa">Prépa scientifique</label>
        </div>

        <div class="option">
            <input type="radio" id="prepalitt" name="etude" value="prépa littéraire">
            <label for="prepalitt">Prépa littéraire</label>
        </div>

        <div class="option">
            <input type="radio" id="prepaecg" name="etude" value="prépa ECG">
            <label for="prepaecg">Prépa ECG</label>
        </div>

        <div class="option">
            <input type="radio" id="licencescience" name="etude" value="licence en sciences">
            <label for="licencescience">Licence en sciences</label>
        </div>

        <div class="option">
            <input type="radio" id="licencelitt" name="etude" value="licence en lettres et langues">
            <label for="licencelitt">Licence en lettres et langues</label>
        </div>

        <div class="option">
            <input type="radio" id="licencedroit" name="etude" value="licence en droit">
            <label for="licencedroit">Licence en droit</label>
        </div>

        <div class="option">
            <input type="radio" id="licenceeco" name="etude" value="licence en économie et gestion">
            <label for="licenceeco">Licence en économie et gestion</label>
        </div>

        <div class="option">
            <input type="radio" id="licencesante" name="etude" value="licence en santé">
            <label for="licencesante">Licence en santé</label>
        </div>

        <div class="option">
            <input type="radio" id="bts" name="etude" value="BTS">
            <label for="bts">BTS</label>
        </div>

        <div class="option">
            <input type="radio" id="but" name="etude" value="BUT">
            <label for="but">BUT</label>
        </div>

    </div>

    <div class="card">
        <h2>Spécialité principale</h2>

        <div class="option"><input type="radio" id="amc" name="spe" value="AMC"><label for="amc">AMC</label></div>
        <div class="option"><input type="radio" id="arts" name="spe" value="arts"><label for="arts">Arts</label></div>
        <div class="option"><input type="radio" id="bio" name="spe" value="Biologie Ecologie"><label for="bio">Biologie Ecologie</label></div>
        <div class="option"><input type="radio" id="eps" name="spe" value="EPS"><label for="eps">EPS</label></div>
        <div class="option"><input type="radio" id="hggsp" name="spe" value="HGGSP"><label for="hggsp">HGGSP</label></div>
        <div class="option"><input type="radio" id="hlp" name="spe" value="HLP"><label for="hlp">HLP</label></div>
        <div class="option"><input type="radio" id="llca" name="spe" value="LLCA"><label for="llca">LLCA</label></div>
        <div class="option"><input type="radio" id="llce" name="spe" value="LLCE"><label for="llce">LLCE</label></div>
        <div class="option"><input type="radio" id="maths" name="spe" value="maths"><label for="maths">Maths</label></div>
        <div class="option"><input type="radio" id="nsi" name="spe" value="NSI"><label for="nsi">NSI</label></div>
        <div class="option"><input type="radio" id="physique" name="spe" value="physique"><label for="physique">Physique-Chimie</label></div>
        <div class="option"><input type="radio" id="ses" name="spe" value="SES"><label for="ses">SES</label></div>
        <div class="option"><input type="radio" id="si" name="spe" value="SI"><label for="si">SI</label></div>
        <div class="option"><input type="radio" id="svt" name="spe" value="SVT"><label for="svt">SVT</label></div>

    </div>

    <div class="card">
        <h2>Deuxième spécialité</h2>

        <div class="option"><input type="radio" id="amc2" name="spe2" value="AMC"><label for="amc2">AMC</label></div>
        <div class="option"><input type="radio" id="arts2" name="spe2" value="arts"><label for="arts2">Arts</label></div>
        <div class="option"><input type="radio" id="bio2" name="spe2" value="Biologie Ecologie"><label for="bio2">Biologie Ecologie</label></div>
        <div class="option"><input type="radio" id="eps2" name="spe2" value="EPS"><label for="eps2">EPS</label></div>
        <div class="option"><input type="radio" id="hggsp2" name="spe2" value="HGGSP"><label for="hggsp2">HGGSP</label></div>
        <div class="option"><input type="radio" id="hlp2" name="spe2" value="HLP"><label for="hlp2">HLP</label></div>
        <div class="option"><input type="radio" id="llca2" name="spe2" value="LLCA"><label for="llca2">LLCA</label></div>
        <div class="option"><input type="radio" id="llce2" name="spe2" value="LLCE"><label for="llce2">LLCE</label></div>
        <div class="option"><input type="radio" id="maths2" name="spe2" value="maths"><label for="maths2">Maths</label></div>
        <div class="option"><input type="radio" id="nsi2" name="spe2" value="NSI"><label for="nsi2">NSI</label></div>
        <div class="option"><input type="radio" id="physique2" name="spe2" value="physique"><label for="physique2">Physique-Chimie</label></div>
        <div class="option"><input type="radio" id="ses2" name="spe2" value="SES"><label for="ses2">SES</label></div>
        <div class="option"><input type="radio" id="si2" name="spe2" value="SI"><label for="si2">SI</label></div>
        <div class="option"><input type="radio" id="svt2" name="spe2" value="SVT"><label for="svt2">SVT</label></div>

    </div>

</div>

<button class="btn" type="submit">Valider les choix</button>

</form>

</div>

</body>
</html>
"""

@app.get("/save")
def save(request: Request, etude:str, spe, spe2):
    request.session["etude"]=etude
    request.session["spe"]= spe
    request.session["spe2"]=spe2
    if spe==spe2:
        return ("/choix")
    else:
        return RedirectResponse("/formulaire")

@app.get("/formulaire",response_class=HTMLResponse)
def prepaform(request:Request):
    etude=request.session.get("etude")
    spe=request.session.get("spe")
    spe2=request.session.get("spe2")
    return f"""
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: #0b1220;
        color: white;
    }}

    .wrapper {{
        max-width: 900px;
        margin: auto;
        padding: 30px;
    }}

    .header {{
        text-align: center;
        margin-bottom: 25px;
    }}

    .header h1 {{
        margin: 0;
        font-size: 34px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .card {{
        background: #111a2e;
        border: 1px solid #1f2a44;
        border-radius: 14px;
        padding: 20px;
    }}

    h2 {{
        font-size: 16px;
        color: #93c5fd;
        margin-bottom: 15px;
    }}

    p {{
        margin: 10px 0 5px;
        color: #cbd5e1;
    }}

    input[type="text"], input[type="number"] {{
        width: 100%;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #2a3b5e;
        background: #0f172a;
        color: white;
        outline: none;
        margin-bottom: 10px;
    }}

    input[type="text"]:focus,
    input[type="number"]:focus {{
        border-color: #60a5fa;
    }}

    .radio-group {{
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 15px;
    }}

    .radio-option {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px;
        border-radius: 10px;
        background: #0f172a;
        border: 1px solid transparent;
        cursor: pointer;
        transition: 0.2s;
    }}

    .radio-option:hover {{
        border-color: #3b82f6;
        background: #111c36;
    }}

    input[type="radio"] {{
        accent-color: #60a5fa;
        transform: scale(1.2);
    }}

    button {{
        width: 100%;
        padding: 14px;
        margin-top: 15px;
        border: none;
        border-radius: 12px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.2s;
    }}

    button:hover {{
        transform: scale(1.02);
    }}

    .highlight {{
        color: #60a5fa;
        font-weight: bold;
    }}
</style>
</head>

<body>

<div class="wrapper">

<div class="header">
    <h1>PARCOURINF</h1>
</div>

<form action="/predict">

<div class="card">

<h2>
Je vais analyser ton profil pour les études inférieures, plus précisément pour la formation suivante:
<span class="highlight">{etude}</span>
</h2>

<p>Ta moyenne en <b>{spe}</b> :</p>
<p><input name="maths"></p>

<p>Ta moyenne en <b>{spe2}</b> :</p>
<p><input name="physique"></p>

<p>Ton classement dans ta classe :</p>
<p><input name="classement" type="text"></p>

<p>L'avis de tes professeurs :</p>

<div class="radio-group">

    <label class="radio-option">
        <input type="radio" id="mauvais" name="avis" value="0">
        Mauvais
    </label>

    <label class="radio-option">
        <input type="radio" id="moyen" name="avis" value="1">
        Moyen
    </label>

    <label class="radio-option">
        <input type="radio" id="bien" name="avis" value="2">
        Bien
    </label>

    <label class="radio-option">
        <input type="radio" id="excellent" name="avis" value="3">
        Excellent
    </label>

</div>

<p>La <b>{etude}</b> que tu vises est dans le top combien ? (1 à 100)</p>
<p><input type="number" name="prepa" min="1" max="100"></p>

<button type="submit">Analyser mon profil</button>

</div>

</form>

</div>

</body>
</html>
    """

@app.get("/predict",response_class=HTMLResponse)
def predict(maths:float,physique:float,classement:int,avis:float,prepa:int,request: Request):
    etude=request.session.get("etude")
    spe=request.session.get("spe")
    spe2=request.session.get("spe2")
    request.session["prepa"]=prepa
    avis_str="non indiqué"
    if avis==0:
        avis_str="mauvais"
    elif avis_str==1:
        avis_str="moyen"
    elif avis_str==2:
        avis_str="bien"
    else:
        avis_str="excellent"
    
    admis=predict_prepa(maths,physique,classement,avis)
    if etude=="prépa scientifique":
        if spe=="maths" or spe2=="maths" or spe=="physique" or spe2=="physique":
            admis=admis-(40/prepa)
        else:
            admis=admis-(50/prepa)
    elif etude=="prépa littéraire":
        if spe=="HLP" or spe2=="HLP" or spe=="HGGSP" or spe2=="HGGSP" or spe=="SES" or spe2=="SES":
            admis=admis-(25/prepa)
        else:
            admis=admis-(35/prepa)
    elif etude=="prépa ECG":
        if spe=="maths" or spe2=="maths" or spe=="physique" or spe2=="physique" or spe=="SES" or spe2=="SES":
            admis=admis-(35/prepa)
        else:
            admis=admis-(40/prepa)
    elif etude=="BUT":
        admis=admis-(30/prepa)
    elif etude=="médecine":
        if spe=="maths" or spe2=="maths" or spe=="physique" or spe2=="physique" or spe=="SVT" or spe2=="SVT":
            admis=admis-(40/prepa)
        else:
            admis=admis-(50/prepa)

    if admis<=0:
        decision="jamais"
    elif 0<admis<10:
        decision="rarement"
    elif 10<admis<30:
        decision="occasionnellement"
    elif 30<admis<50:
        decision="souvent"
    elif 50<admis<75:
        decision="très souvent"
    else:
        decision="presque tout le temps"
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body{{
        background-color:#374649;
    }}
    h1{{
        color:lightgreen;
        text-align:center;
    }}
    p{{
        color:lightblue;
        margin-left:10px;   
    }}

    h2{{
        color:lightblue;
        text-align:center;
    }}
    button{{
        transition:all 1s ease;
    }}
    button:hover{{
        border:10px yellow;
    }}
    .resulttext{{
        display:inline-flex;
        gap:50px;
        margin-left:125px;
    }}
    .style{{
        inline-flex:1;
        background-color:black;
        width:200px;
        height:100px;
        cursor:pointer;
        padding:5px;
        transition:all 0.3s ease;
    }}
    .style:hover{{
        background-color:lightblue;
        border-color:black;
        border-radius:50px;
    }}
    .container{{
        display:flex;
        gap:100px;
    }}
    .formation{{
        flex:1;
        background-color:black;
        color:white;
        border-color:lightblue;
        height:70px;
        padding:10px;
        border-radius:10px;
    }}
    .text{{
        color:black;
        font-size:40px;
        margin-left:10px;
        margin-bottom:50px;
    }}
    .style2{{
        background-color:black;
        width:200px;
        height:100px;
        cursor:pointer;
        padding:5px;
        transition:all 0.3s ease;
        margin-left:525px;
        margin-top:50px;
    }}
    .style2:hover{{
        background-color:lightblue;
        border-color:black;
        border-radius:50px;
    }}        

    #decale{{
        margin-left:50px;
    }}
    @media (max-width: 900px) {{
    .resulttext {{
        display: flex;
        flex-direction: column; 
        margin-left: 10px;   
        gap: 15px;
    }}
    .style2 {{
        margin-left: 10px;   
        margin-top: 20px;
    }}
    #boutonun,
    #boutondeux,
    #boutontrois {{

        margin-left:0;
        margin-right:0;

        width:100%;
        max-width:250px;
    }}

    .container{{
        flex-direction:column;
        align-items:center;
        gap:15px;
    }}
}}
    </style>
    </head>
    <body>
    <form action="/choix">
        <h1> Voici les résultats</h1>
        <div class="resulttext">
            <div class="style">
            <p>Ta moyenne en {spe} est de :<span class="text" id="decale">{maths}</span></p>
            </div>
            <div class="style">
            <p>Ta moyenne en {spe2} est de :<span class="text" id="decale">{physique}</span></p>
            </div>
            <div class="style">
            <p>Ton classement dans ta classe est de :<span class="text" id="decale">{classement}</span></p>
            </div>
            <div class="style"> 
            <p>L'avis des professeurs est :<span class="text">{avis_str}</span></p>
            </div>
        </div>
        <div class="style2">
            <p>Ta formation est classée top:<span class="text" id="decale">{prepa}</span></p>
        </div>
        <br><br>
        <h2>Avec ces résultats, ton taux d'admissibilité est de : {admis} % 
        <br><br>la formation envoie des propositions d'admission {decision}.</h2>
        <br><br>
        <div class="container">
        <button id="boutonun" class="formation"type="submit">Retour vers choix formation</button>
    </form>
    <form action="/formulaire">
        <button class="formation" id="boutondeux" name="etude" value="{etude}" type="submit">Retour vers formulaire de notes</button>
        </div>
    </form>
    <form action="/pause">
        <div class="container"> 
        <button class="formation" name="admis" value="{admis}"id="boutontrois" type="submit">Faire la simulation</button>
        </div>
    </form>
    </body>
    </html>
    """

@app.get("/pause")
def pause(admis:float,request:Request):
    request.session["admis"]=int(admis)
    request.session["n"]=1
    request.session["k"]=0
    request.session["l"]="not yet"
    return RedirectResponse("/simulation")

def save_k(request:Request):
    request.session["k"]=int(0)
    l="already"
    request.session["l"]=l

@app.get("/simulation", response_class=HTMLResponse)
def simulation(request:Request):
    n=request.session.get("n")
    admis=request.session.get("admis")
    etude=request.session.get("etude")

    if n==1:
        prepa=["prépa scientifique","prépa littéraire","prépa ECG"]
        licence=["licence en sciences","licence en lettres et langues","licence en économie et gestion","licence en droit","licence en santé"]
        but=["BUT"]
        bts=["BTS"]
        if etude in prepa:
            population=random.randint(200,1200)
            admis=100-admis
            admisgenerale=random.randint(40,100)
            chance=admisgenerale/100
            place=round(population*(admis/100))
            if place>population:
                population=place
            classes=random.randint(round(40*population/100),round(80*population/100))
            classes_pourcent=round(classes/population*320)
            dernier_candidat=random.randint(10,15)
            url="https://www.letudiant.fr/classements/classement-des-prepas-scientifiques-mp-maths-physique/vous-visez-polytechnique-ens.html"
        elif etude in licence:
            population=random.randint(1000,3000)
            admis=100-admis
            admisgenerale=random.randint(40,100)
            chance=admisgenerale/100
            place=round(population*(admis/100))
            if place>population:
                population=place
            classes=random.randint(round(95*population/100),population)
            classes_pourcent=round(classes/population*320)
            dernier_candidat=random.randint(10,50)
            url="https://www.letudiant.fr/classements/classement-de-la-reussite-en-licence.html"
        elif etude in but:
            population=random.randint(400,900)
            admis=100-admis
            admisgenerale=random.randint(40,100)
            chance=admisgenerale/100
            place=round(population*(admis/100))
            if place>population:
                population=place
            classes=random.randint(round(60*population/100),round(85*population/100))
            classes_pourcent=round(classes/population*320)
            dernier_candidat=random.randint(15,30)
            url="https://etudiant.lefigaro.fr/article/vie-etudiante/parcoursup-2025-classement-des-but-les-plus-attractifs-20250128/"
        elif etude in bts:
            population=random.randint(150,600)
            admis=100-admis
            admisgenerale=random.randint(40,100)
            chance=admisgenerale/100
            place=round(population*(admis/100))
            if place>population:
                population=place
            classes=random.randint(round(70*population/100),round(90*population/100))
            classes_pourcent=round(classes/population*320)
            dernier_candidat=random.randint(10,15)
            url="https://etudiant.lefigaro.fr/etudes/bts/classement/"
        
        request.session["url"]=url
        waitlist_rank=round(population*chance)
        dernier_candidat=round((dernier_candidat/100)*waitlist_rank)
        moyenne_liste=round((dernier_candidat+waitlist_rank)/2)
        waitlist_chances=random.randint(moyenne_liste,waitlist_rank)
        jour=(population-dernier_candidat)/(waitlist_chances-dernier_candidat)
        jour=round(jour*40)
        evolution=round((classes-dernier_candidat)/jour)
    else:
        evolution=request.session.get("evolution")
        dernier_candidat=request.session.get("dernier_candidat")
        admis=request.session.get("admis")
        admisgenerale=request.session.get("admis_generale")
        chance=request.session.get("chance")
        place=request.session.get("place")
        waitlist_rank=request.session.get("waitlist_rank")
        moyenne_liste=request.session.get("moyenne_liste")
        waitlist_chances=request.session.get("waitlist_chances")
        jour=request.session.get("jour")
        population=request.session.get("population")
        classes=request.session.get("classes")
        classes_pourcent=request.session.get("classes_pourcent")
        

    dynamique=random.randint(evolution-round(evolution/2),evolution+round(evolution/2))
    if 40>=n>1:
        dernier_candidat+=dynamique

    if 1<=n<40:
        finish_mess="<u>Phase principale active</u>, passe au jour suivant et vois la progression des places !"
    else:
        finish_mess="<u>Phase principale terminée</u>, va voir la décision sur ton voeu !"

    request.session["population"]=int(population)
    request.session["classes"]=int(classes)
    request.session["classes_pourcent"]=int(classes_pourcent)
    request.session["dernier_candidat"]=int(dernier_candidat)
    request.session["evolution"]=int(evolution)
    request.session["admis_generale"]=int(admisgenerale)
    request.session["chance"]=chance
    request.session["place"]=int(place)
    request.session["waitlist_rank"]=waitlist_rank
    request.session["moyenne_liste"]=moyenne_liste
    request.session["waitlist_chances"]=waitlist_chances
    request.session["jour"]=jour
    request.session["n"]=n+1

    dernier_candidatpx=320*dernier_candidat/population
    place_px=320*place/population

    if place<=dernier_candidat:
        voeux="tu as une proposition d'admission !"
        l=request.session.get("l")
        if l=="already":
            k=request.session.get("k")
            x=n-k
            request.session["k"]=int(k+1)
            request.session["x"]=x
        else:
            save_k(request)
            k=request.session.get("k")
            x=n-k
            request.session["k"]=int(k+1)
            request.session["x"]=x
    elif dernier_candidat<place<classes:
        voeux="Voeu en attente"
        if n>=40:
            voeux="Voeu refusé"
    else:
        voeux="Voeu refusé"

    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{
            background-color: rgb(15, 25, 60);
            display: flex; flex-direction: column; align-items: center;
            min-height: 100vh; margin: 0; padding: 20px; font-family: sans-serif;
        }}
        h3{{ font-family: fantasy; color: rgb(180, 190, 210); font-size: 40px; margin-bottom: 30px; }}

        .classement {{ position: relative; margin: 0 auto; width: 50px; height: 320px; }}
        .barre{{ width:50px; height:320px; border:1px solid #cfd4e5; background:white; position: relative; }}

        /* Positionnement des indicateurs */
        .remplissage{{ position:absolute; top:0; width:100%; height:{dernier_candidatpx}px; background:#3554a5; }}
        .mon-rang{{ position:absolute; top:{place_px}px; width:100%; border-top:2px solid #e28d76; }}
        .classes{{ position:absolute; top:{classes_pourcent}px; width:100%; border-top:2px solid red; }}

        /* --- STYLING DES BLOCS --- */
        .group-left {{ position: absolute; right: 70px; display: flex; align-items: center; gap: 5px; }}
        
        .badge-num {{ padding: 4px 8px; border-radius: 6px; font-weight: bold; font-size: 13px; }}
        .badge-txt {{ padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 500; white-space: nowrap; }}

        /* Couleurs Appels */
        .appel-num {{ background: #3554a5; color: white; }}
        .appel-txt {{ background: #e8edff; color: #3554a5; }}

        /* Couleurs Refus (Rouge/Blanc) */
        .refus-num {{ background: white; color: red; border: 1px solid red; }}
        .refus-txt {{ background: red; color: white; }}

        /* Couleurs Total */
        .total-num {{ background: #4a5568; color: white; }}
        .total-txt {{ background: #e2e8f0; color: #4a5568; }}

        /* --- TOI (Droite) --- */
        .group-right {{ position: absolute; left: 70px; display: flex; align-items: center; gap: 5px; top: {place_px}px; }}
        .toi-num {{ background: #c96d56; color: white; padding: 4px 8px; border-radius: 6px; font-weight: bold; }}
        .toi-txt {{ background: #ffe8e1; color: #c96d56; padding: 4px 8px; border-radius: 6px; font-weight: bold; }}

        /* Responsivité */
        .mobile-text {{ display: none; }}
        .desktop-text {{ display: inline; }}
        @media (max-width: 900px) {{ 
            .mobile-text {{ display: inline !important; }} 
            .desktop-text {{ display: none !important; }} 
        }}

        /* Positionnement vertical */
        #row-appel {{ top: {dernier_candidatpx - 10}px; }}
        #row-refus {{ top: {classes_pourcent - 10}px; }}
        #row-total {{ bottom: -30px; }}

        #finishmess {{ margin-top: 80px; text-align: center; color: #e8edff; font-family: fantasy; font-size: 22px; }}
        .btn-container {{ margin-top: 30px; display: flex; gap: 15px; justify-content: center; }}
        button {{ padding: 10px 20px; background: black; color: white; border: 1px solid lightblue; border-radius: 10px; cursor: pointer; }}
    </style>
    </head>
    <body>
        <h3>Jour {n}</h3>
        <div class="classement">
            <div class="barre">
                <div class="remplissage"></div>
                <div class="mon-rang"></div>
                <div class="classes"></div>
            </div>

            <div id="row-appel" class="group-left">
                <div class="badge-num appel-num">{dernier_candidat}</div>
                <div class="badge-txt appel-txt">
                    <span class="desktop-text">Dernier candidat appelé</span>
                    <span class="mobile-text">Dernier appelé</span>
                </div>
            </div>

            <div id="row-refus" class="group-left">
                <div class="badge-num refus-num">{classes}</div>
                <div class="badge-txt refus-txt">1er refusé</div>
            </div>

            <div id="row-total" class="group-left">
                <div class="badge-num total-num">{population}</div>
                <div class="badge-txt total-txt">
                    <span class="desktop-text">Total candidats</span>
                    <span class="mobile-text">Total</span>
                </div>
            </div>

            <div class="group-right">
                <div class="toi-num">{place}</div>
                <div class="toi-txt">TOI</div>
            </div>
        </div>

        <div id="finishmess">{finish_mess}</div>        
        <div class="btn-container">
            <form action="/simulation"><button type="submit">Jour suivant</button></form>
            <form action="/voeux"><button type="submit" name="voeux" value="{voeux}">Voir la décision</button></form>
        </div>
    </body>
</html>
"""

@app.get("/voeux")
def voeux_decision(voeux):
    if voeux=="tu as une proposition d'admission !":
        return RedirectResponse("/accepte")
    elif voeux=="Voeu en attente":
        return RedirectResponse("/attente")
    else:
        return RedirectResponse("/refus")
    
@app.get("/accepte",response_class=HTMLResponse)
def voeux_accepte(request:Request):
    x=request.session.get("x")
    etude=request.session.get("etude")
    prepa=request.session.get("prepa")
    return f"""
<html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{{
                background-color: rgb(255, 166, 0);
                margin: 0;
                padding: 15px;
                font-family: Arial, sans-serif;
            }}
            .main-container {{
                max-width: 800px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: center;
                margin-top: 40px;
                margin-bottom: 40px;
                font-size: 25px;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }}
            #text1{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            #text2{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            button{{
                transition:all 1s ease;
            }}
            button:hover{{
                border:10px yellow;
            }}
            #boutonun{{
                width: 200px;
            }}
            #boutondeux{{
                width: 270px;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 50px;
                margin-top: 20px;
            }}
            .formation1{{
                background-color:green;
                color:white;
                border-color:black;
                height:70px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            .formation2{{
                background-color:red;
                color:white;
                border-color:black;
                height:70px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            .retour{{
                background-color:black;
                color:white;
                border-color:red;
                height:40px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            
            @media (max-width: 768px) {{
                #text1, #text2 {{
                    font-size: 34px;
                }}
                p {{
                    font-size: 18px;
                }}
                .container {{
                    flex-direction: column;
                    align-items: center;
                    gap: 15px;
                }}
                #boutonun, #boutondeux {{
                    width: 100% !important;
                    max-width: 300px;
                }}
            }}
        </style>
    </head>
    <body>
    <div class="main-container">
        <form action="/simulation" style="text-align: left;">
            <button type="submit" class="retour">Retour à la simulation</button>
        </form>
        <span id="text1"><u>TU ES ACCEPTÉ</u></span>
        <span id="text2"><u>D'ADMISSION !</u></span>

        <p>Tu as reçu une proposition d'admission au jour {x} de la phase principale d'une formation {etude} du top {prepa}.</p>
        
        <div class="container">
            <form action="/choix/accepté">
                <button id="boutonun" class="formation1" type="submit">ACCEPTER</button>
            </form>
            <form action="/choix/refusé">
                <button class="formation2" id="boutondeux" type="submit">REFUSER</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""

@app.get("/choix/accepté",response_class=HTMLResponse)
def choix_accepté(request:Request):
    etude=request.session.get("etude")
    url=request.session.get("url")
    prepa=request.session.get("prepa")
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{{
                background-color: green;
                margin: 0;
                padding: 15px;
                font-family: Arial, sans-serif;
            }}
            .main-container {{
                max-width: 800px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: center;
                margin-top: 40px;
                margin-bottom: 40px;
                font-size: 25px;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }}
            #text1{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            button{{
                transition:all 1s ease;
            }}
            button:hover{{
                border:10px yellow;
            }}
            #boutonun{{
                width: 200px;
            }}
            #boutondeux{{
                width: 270px;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 50px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(116, 251, 116);
                border-color:rgb(255,255,192);
                height:70px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            
            @media (max-width: 768px) {{
                #text1 {{
                    font-size: 34px;
                }}
                p {{
                    font-size: 18px;
                }}
                .container {{
                    flex-direction: column;
                    align-items: center;
                    gap: 15px;
                }}
                #boutonun, #boutondeux {{
                    width: 100% !important;
                    max-width: 300px;
                }}
            }}
        </style>
    </head>
    <body>
    <div class="main-container">
        <span id="text1"><u>VOEU ACCEPTÉ !</u></span>

        <p>Maintenant, va voir précisément dans quel établissement de {etude} tu pourrais être prit selon ce que t'as visé (top {prepa}), t'as juste à cliquer <a href="{url}" style="color: yellow;">ICI</a> !</p>
        <p>Tu peux aussi retourner là où tu veux à l'aide des boutons ci-dessous</p>
        
        <div class="container">
            <form action="/choix">
                <button id="boutonun" class="formation1" type="submit">Retour vers choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" id="boutondeux" name="etude" value="{etude}" type="submit">Retour vers formulaire de notes</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""

@app.get("/choix/refusé",response_class=HTMLResponse)
def choix_refusé(request:Request):
    etude=request.session.get("etude")
    prepa=request.session.get("prepa")
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{{
                background-color: rgb(119, 80, 212);
                margin: 0;
                padding: 15px;
                font-family: Arial, sans-serif;
            }}
            .main-container {{
                max-width: 800px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: center;
                margin-top: 40px;
                margin-bottom: 40px;
                font-size: 25px;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }}
            #text1{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            button{{
                transition:all 1s ease;
            }}
            button:hover{{
                border:10px yellow;
            }}
            #boutonun{{
                width: 200px;
            }}
            #boutondeux{{
                width: 270px;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 50px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(119, 80, 212);
                border-color:rgb(255,255,192);
                height:70px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            
            @media (max-width: 768px) {{
                #text1 {{
                    font-size: 34px;
                }}
                p {{
                    font-size: 18px;
                }}
                .container {{
                    flex-direction: column;
                    align-items: center;
                    gap: 15px;
                }}
                #boutonun, #boutondeux {{
                    width: 100% !important;
                    max-width: 300px;
                }}
            }}
        </style>
    </head>
    <body>
    <div class="main-container">
        <span id="text1"><u>VOEU REFUSÉ !</u></span>

        <p>Tu penses pouvoir faire mieux que cette formation ({etude}) du top {prepa} ?</p>
        <p>Tu peux recommencer et changer le top {etude} que tu vises ou totalement recommencer à l'aide des boutons ci-dessous.</p>
        
        <div class="container">
            <form action="/choix">
                <button id="boutonun" class="formation1" type="submit">Retour vers choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" id="boutondeux" name="etude" value="{etude}" type="submit">Retour vers formulaire de notes</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""

@app.get("/attente", response_class=HTMLResponse)
def attente(request:Request):
    n=request.session.get("n")
    return f"""
<html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{{
                background-color: #3554a5;
                margin: 0;
                padding: 15px;
                font-family: Arial, sans-serif;
            }}
            .main-container {{
                max-width: 800px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: center;
                margin-top: 40px;
                margin-bottom: 40px;
                font-size: 25px;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }}
            #text1{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            #text2{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            button{{
                transition:all 1s ease;
            }}
            button:hover{{
                border:10px yellow;
            }}

            .retour{{
                background-color:black;
                color:white;
                border-color:red;
                height:60px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
                width: auto;
                max-width: 100%;
            }}
            span{{
                font-size:30px;
            }}
            
            @media (max-width: 768px) {{
                #text1, #text2 {{
                    font-size: 34px;
                }}
                p {{
                    font-size: 18px;
                }}
                span {{
                    font-size: 20px;
                }}
                .retour {{
                    width: 100%;
                    height: auto;
                    padding: 15px;
                }}
            }}
        </style>
    </head>
    <body>
    <div class="main-container">
        <span id="text1"><u>TU ES EN LISTE</u></span>
        <span id="text2"><u>D'ATTENTE</u></span>

        <p><u>Tu es encore en phase principale</u> (jour {n}),
         retourne à la simulation pour voir les résultats au 40ème jour (ou moins si t'es admis avant).</p>
        <form action="/simulation">
            <button type="submit" class="retour"><span>Retour à la simulation</span></button>
        </form>
    </div>
    </body>
</html>
"""

@app.get("/refus",response_class=HTMLResponse)
def refus(request:Request):
    place=request.session.get("place")
    classes=request.session.get("classes")
    population=request.session.get("population")
    dernier_candidat=request.session.get("dernier_candidat")
    etude=request.session.get("etude")
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{{
                background-color: red;
                margin: 0;
                padding: 15px;
                font-family: Arial, sans-serif;
            }}
            .main-container {{
                max-width: 800px;
                margin: auto;
                text-align: center;
            }}
            p{{
                text-align: center;
                margin-top: 40px;
                margin-bottom: 40px;
                font-size: 25px;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }}
            #text1{{
                font-size: 70px;
                display: block;
                font-family:Arial, Helvetica, sans-serif;
                text-align: center;
                color: rgb(15, 25, 60);
            }}
            button{{
                transition:all 1s ease;
            }}
            button:hover{{
                border:10px yellow;
            }}
            #boutonun{{
                width: 200px;
            }}
            #boutondeux{{
                width: 270px;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 50px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(255,255,192);
                border-color:rgb(255,255,192);
                height:70px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            .retour{{
                background-color:black;
                color:white;
                border-color:red;
                height:40px;
                padding:10px;
                border-radius:10px;
                cursor: pointer;
            }}
            
            @media (max-width: 768px) {{
                #text1 {{
                    font-size: 34px;
                }}
                p {{
                    font-size: 18px;
                }}
                .container {{
                    flex-direction: column;
                    align-items: center;
                    gap: 15px;
                }}
                #boutonun, #boutondeux {{
                    width: 100% !important;
                    max-width: 300px;
                }}
            }}
        </style>
    </head>
    <body>
    <div class="main-container">
        <form action="/simulation" style="text-align: left;">
            <button type="submit" class="retour">Retour à la simulation</button>
        </form>
        <span id="text1"><u>TU ES REFUSÉ</u></span>

        <p>Tu as été placé trop bas 
        ({place}ème sur {population}, le dernier candidat classé étant {classes}ème, et le dernier appelé {dernier_candidat}ème),
          tu n'as donc jamais reçu de proposition d'admission.</p>
          
        <div class="container">
            <form action="/choix">
                <button id="boutonun" class="formation1" type="submit">Retour vers choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" id="boutondeux" name="etude" value="{etude}" type="submit">Retour vers formulaire de notes</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""