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
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }}
    h1{{
        color:lightgreen;
        text-align:center;
        margin-top: 20px;
    }}
    p{{
        color:lightblue;
        margin: 5px 0;   
    }}
    h2{{
        color:lightblue;
        text-align:center;
        padding: 0 20px;
    }}
    .resulttext{{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        max-width: 1100px;
        margin: 30px auto;
        padding: 0 20px;
    }}
    .style{{
        background-color:black;
        width:220px;
        min-height:110px;
        cursor:pointer;
        padding:15px;
        border-radius:10px;
        transition:all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .style:hover{{
        background-color:lightblue;
        color: black !important;
        border-radius:25px;
    }}
    .style:hover p, .style:hover .text {{
        color: black;
    }}
    .text{{
        color:white;
        font-size:28px;
        font-weight: bold;
        display: block;
        margin-top: 5px;
    }}
    .style2{{
        background-color:black;
        width:220px;
        min-height:110px;
        cursor:pointer;
        padding:15px;
        border-radius:10px;
        transition:all 0.3s ease;
        margin: 20px auto;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .style2:hover{{
        background-color:lightblue;
        border-radius:25px;
    }}
    .style2:hover p, .style2:hover .text {{
        color: black;
    }}
    .container{{
        display:flex;
        justify-content: center;
        gap:30px;
        max-width: 900px;
        margin: 20px auto;
        padding: 0 20px;
        flex-wrap: wrap;
    }}
    .formation{{
        width: 250px;
        background-color:black;
        color:white;
        border: 2px solid lightblue;
        height:60px;
        padding:10px;
        border-radius:10px;
        cursor: pointer;
        font-size: 14px;
        font-weight: bold;
        transition: 0.2s;
    }}
    .formation:hover {{
        background-color: lightblue;
        color: black;
        transform: scale(1.05);
    }}
    @media (max-width: 600px) {{
        .resulttext {{
            flex-direction: column; 
            align-items: center;
        }}
        .style, .style2 {{
            width: 90%;
        }}
        .container {{
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }}
        .formation {{
            width: 90%;
        }}
    }}
    </style>
    </head>
    <body>
    <form action="/choix">
        <h1> Voici les résultats</h1>
        <div class="resulttext">
            <div class="style">
                <p>Ta moyenne en {spe} est de :</p>
                <span class="text">{maths}</span>
            </div>
            <div class="style">
                <p>Ta moyenne en {spe2} est de :</p>
                <span class="text">{physique}</span>
            </div>
            <div class="style">
                <p>Ton classement dans ta classe est de :</p>
                <span class="text">{classement}</span>
            </div>
            <div class="style"> 
                <p>L'avis des professeurs est :</p>
                <span class="text">{avis_str}</span>
            </div>
        </div>
        <div class="style2">
            <p>Ta formation est classée top :</p>
            <span class="text">{prepa}</span>
        </div>
        <br>
        <h2>Avec ces résultats, ton taux d'admissibilité est de : {admis} % 
        <br><br>la formation envoie des propositions d'admission {decision}.</h2>
        <br>
        <div class="container">
        <button class="formation" type="submit">Retour vers choix formation</button>
    </form>
    <form action="/formulaire">
        <button class="formation" name="etude" value="{etude}" type="submit">Retour vers formulaire de notes</button>
    </form>
    <form action="/pause">
        <button class="formation" name="admis" value="{admis}" type="submit">Faire la simulation</button>
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
    else:
        pass

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
            pass
    else:
        voeux="Voeu refusé"

    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>

        body{{
            background-color:rgb(15, 25, 60);
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: white;
        }}

        h3{{
            font-family: fantasy;
            text-align: center;
            font-size: 40px;
            font-style: italic;
            color: rgb(180, 190, 210);
            margin-top: 20px;
        }}

        .main-container {{
            max-width: 1000px;
            margin: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .classement{{
            display:flex;
            justify-content: center;
            align-items: flex-start;
            margin: 40px auto;
            position: relative;
            width: 100%;
            max-width: 600px;
        }}

        .bloc{{
            position:relative;
            display: flex;
            justify-content: center;
            width: 100%;
            height: 420px;
        }}

        .annee{{
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            padding: 3px 15px;
            border-radius: 12px;
            background:#e7ebf8;
            font-size:14px;
            color: black;
            font-weight: bold;
        }}

        .barre-container {{
            position: relative;
            height: 320px;
            width: 60px;
            margin-top: 20px;
        }}

        .barre{{
            width: 100%;
            height: 100%;
            border: 2px solid #cfd4e5;
            border-radius: 4px;
        }}

        .barre-2024{{
            position:relative;
            background: rgba(255,255,255,0.1);
        }}

        .remplissage{{
            position:absolute;
            top:0;
            left:0;
            right:0;
            height:{dernier_candidatpx}px;
            background:#3554a5;
            border-radius: 2px 2px 0 0;
        }}

        .mon-rang{{
            position:absolute;
            left: -10px;
            right: -10px;
            top:{place_px}px;
            border-top:3px dashed #e28d76;
        }}

        .classes{{
            position:absolute;
            left: -10px;
            right: -10px;
            top:{classes_pourcent}px;
            border-top:3px solid red;
        }}

        /* CÔTÉ GAUCHE (Infos globales et dernier appelé) */
        #messageall{{
            position:absolute;
            right: calc(50% + 45px);
            top: -5px;
            text-align: right;
            white-space: nowrap;
        }}
        #waitlist_message{{
            position:absolute;
            right: calc(50% + 95px);
            top: {dernier_candidatpx + 10}px;
            text-align: right;
        }}
        .appel2024{{
            position:absolute;
            right: calc(50% + 42px);
            top: {dernier_candidatpx + 10}px;
        }}

        /* CÔTÉ DROIT (Toi et Refusé/Total) */
        #messagerang{{
            position: absolute;
            left: calc(50% + 95px);
            top: {place_px + 10}px;
        }}
        .rang{{
            position:absolute;
            left: calc(50% + 42px);
            top: {place_px + 10}px;
        }}
        #messagerefus{{
            position:absolute;
            left: calc(50% + 95px);
            top: {classes_pourcent + 10}px;
        }}
        .refus{{
            position:absolute;
            left: calc(50% + 42px);
            top: {classes_pourcent + 10}px;
        }}
        .classe2024{{
            position:absolute;
            left: calc(50% + 42px);
            bottom: 60px;
        }}

        /* STYLES DES LABELS ET BOXES */
        #messageall span, #waitlist_message span, #messagerang span, #messagerefus span,
        .appel2024 span, .classe2024 span, .rang span, .refus span {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: bold;
        }}

        #all-text{{ color:#e8edff; background:#3554a5; }}
        #waitlist-text{{ color:#e8edff; background:#1e3a8a; max-width: 150px; text-align: right;}}
        .appel2024 span {{ background:#e8edff; color:#3554a5; }}
        #rang-text{{ background-color: #c96d56; color: #ffe8e1; }}
        .rang span{{ background:#ffe8e1; color:#c96d56; }}
        #refus-text{{ color:red; background:white; }}
        .refus span{{ background:red; color:white; }}
        .classe2024 span{{ background: #4b5563; color: white; }}

        #finishmess{{
            position: absolute;
            bottom: 0px;
            width: 100%;
            text-align: center;
        }}
        #finishtext{{
            color:#e8edff;
            font-size:22px;
            font-family: Arial, sans-serif;
            font-weight: bold;
        }}

        .btn-container {{
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
            width: 100%;
            flex-wrap: wrap;
        }}

        button {{
            padding: 12px 25px;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s;
            min-width: 180px;
        }}

        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(96,165,250,0.3);
        }}

        @media (max-width: 768px) {{
            #messageall, #waitlist_message, #messagerang, #messagerefus {{
                display: none;
            }}
            .classement {{
                max-width: 320px;
            }}
            .appel2024 {{ right: calc(50% + 35px); }}
            .rang {{ left: calc(50% + 35px); }}
            .refus {{ left: calc(50% + 35px); }}
            .classe2024 {{ left: calc(50% + 35px); }}
            
            .appel2024 span::before {{ content: "Dernier appelé: "; font-weight: normal; font-size: 10px; opacity: 0.8; }}
            .rang span::before {{ content: "TOI: "; font-weight: bold; font-size: 10px; }}
            .refus span::before {{ content: "Refus: "; font-weight: normal; font-size: 10px; }}
            .classe2024 span::before {{ content: "Total: "; font-weight: normal; font-size: 10px; }}
            
            .appel2024 span, .classe2024 span, .rang span, .refus span {{
                white-space: nowrap;
                font-size: 11px;
                padding: 4px 8px;
            }}
            #finishtext {{
                font-size: 16px;
            }}
            button {{
                width: 100%;
            }}
        }}

        </style>
    </head>
    <body>
    <div class="main-container">
        <h3>Jour {n}</h3>
        
        <div class="classement">
            <div class="bloc">
                <div class="annee">2026</div>

                <div id="messageall">
                    <span id="all-text">Tous les candidats de la liste</span>
                </div>
                <div id="waitlist_message">
                    <span id="waitlist-text">Dernier candidat appelé aujourd'hui</span>
                </div>
                <div class="appel2024">
                    <span>{dernier_candidat}</span>
                </div>

                <div class="barre-container">
                    <div class="barre barre-2024">
                        <div class="remplissage"></div>
                        <div class="mon-rang"></div>
                        <div class="classes"></div>
                    </div>
                </div>

                <div id="messagerang">
                    <span id="rang-text">VOTRE RANG</span>
                </div>
                <div class="rang">
                    <span>{place}</span>
                </div>
                
                <div id="messagerefus">
                    <span id="refus-text">Rang du premier refusé</span>
                </div>
                <div class="refus">
                    <span>{classes}</span>
                </div>

                <div class="classe2024">
                    <span>{population}</span>
                </div>
                
                <div id="finishmess">
                    <span id="finishtext">{finish_mess}</span>
                </div>        
            </div>
        </div>

        <div class="btn-container">
            <form action="/simulation">
                <button>Jour suivant</button>
            </form>
            <form action="/voeux">
                <button type="submit" name="voeux" value="{voeux}">Voir la décision du voeu</button>
            </form>
        </div>
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
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                text-align: center;
            }}
            .content-wrapper {{
                max-width: 800px;
                margin: auto;
            }}
            p{{
                margin: 40px 0;
                font-size: 22px;
                line-height: 1.5;
                color: rgb(15, 25, 60);
                font-weight: bold;
            }}
            h1 {{
                font-size: 50px;
                font-family: Arial, sans-serif;
                color: rgb(15, 25, 60);
                margin-top: 30px;
                line-height: 1.2;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 40px;
                flex-wrap: wrap;
                margin-top: 30px;
            }}
            button{{
                padding:15px 30px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                border-radius:10px;
                border: none;
                transition: 0.2s;
                min-width: 200px;
            }}
            button:hover{{
                transform: scale(1.05);
            }}
            .formation1{{
                background-color:green;
                color:white;
            }}
            .formation2{{
                background-color:red;
                color:white;
            }}
            .retour{{
                background-color:black;
                color:white;
                padding: 10px 20px;
                font-size: 14px;
                min-width: auto;
                margin-bottom: 20px;
            }}
            @media (max-width: 600px) {{
                h1 {{ font-size: 32px; }}
                p {{ font-size: 18px; }}
                .container {{ flex-direction: column; gap: 15px; align-items: center; }}
                button {{ width: 100%; }}
            }}
        </style>
    </head>
    <body>
    <div class="content-wrapper">
        <form action="/simulation">
            <button type="submit" class="retour">← Retour à la simulation</button>
        </form>
        <h1><u>TU AS UNE PROPOSITION D'ADMISSION !</u></h1>

        <p>Tu as reçu une proposition d'admission au jour {x} de la phase principale d'une formation {etude} du top {prepa}.</p>
        
        <div class="container">
            <form action="/choix/accepté">
                <button class="formation1" type="submit">ACCEPTER</button>
            </form>
            <form action="/choix/refusé">
                <button class="formation2" type="submit">REFUSER</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""
@app.get("/choix/accepté",call_back=None,response_class=HTMLResponse)
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
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                text-align: center;
                color: white;
            }}
            .content-wrapper {{
                max-width: 800px;
                margin: auto;
            }}
            h1{{
                font-size: 50px;
                color: rgb(15, 25, 60);
                margin-top: 40px;
            }}
            p{{
                margin: 30px 0;
                font-size: 22px;
                line-height: 1.6;
            }}
            a {{
                color: #ffffc0;
                font-weight: bold;
                text-decoration: underline;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
                margin-top: 40px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(116, 251, 116);
                border: 2px solid rgb(255,255,192);
                padding: 15px 25px;
                font-size: 16px;
                font-weight: bold;
                border-radius:10px;
                cursor: pointer;
                transition: 0.2s;
                min-width: 220px;
            }}
            .formation1:hover, .formation2:hover {{
                transform: scale(1.05);
                background-color: rgb(20,20,20);
            }}
            @media (max-width: 600px) {{
                h1 {{ font-size: 34px; }}
                p {{ font-size: 18px; }}
                .container {{ flex-direction: column; gap: 15px; align-items: center; }}
                .formation1, .formation2 {{ width: 100%; }}
            }}
        </style>
    </head>
    <body>
    <div class="content-wrapper">
        <h1><u>VOEU ACCEPTÉ !</u></h1>

        <p>Maintenant, va voir précisément dans quel établissement de {etude} tu pourrais être pris selon ce que tu as visé (top {prepa}), tu as juste à cliquer <a href="{url}" target="_blank">ICI</a> !</p>
        <p>Tu peux aussi retourner là où tu veux à l'aide des boutons ci-dessous :</p>
        
        <div class="container">
            <form action="/choix">
                <button class="formation1" type="submit">Retour choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" name="etude" value="{etude}" type="submit">Retour formulaire de notes</button>
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
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                text-align: center;
                color: white;
            }}
            .content-wrapper {{
                max-width: 800px;
                margin: auto;
            }}
            h1{{
                font-size: 50px;
                color: rgb(15, 25, 60);
                margin-top: 40px;
            }}
            p{{
                margin: 30px 0;
                font-size: 22px;
                line-height: 1.6;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
                margin-top: 40px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(200, 180, 255);
                border: 2px solid rgb(255,255,192);
                padding: 15px 25px;
                font-size: 16px;
                font-weight: bold;
                border-radius:10px;
                cursor: pointer;
                transition: 0.2s;
                min-width: 220px;
            }}
            .formation1:hover, .formation2:hover {{
                transform: scale(1.05);
            }}
            @media (max-width: 600px) {{
                h1 {{ font-size: 34px; }}
                p {{ font-size: 18px; }}
                .container {{ flex-direction: column; gap: 15px; align-items: center; }}
                .formation1, .formation2 {{ width: 100%; }}
            }}
        </style>
    </head>
    <body>
    <div class="content-wrapper">
        <h1><u>VOEU REFUSÉ !</u></h1>

        <p>Tu penses pouvoir faire mieux que cette formation ({etude}) du top {prepa} ?</p>
        <p>Tu peux recommencer et changer le top {etude} que tu vises ou totalement recommencer à l'aide des boutons ci-dessous.</p>
        
        <div class="container">
            <form action="/choix">
                <button class="formation1" type="submit">Retour choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" name="etude" value="{etude}" type="submit">Retour formulaire de notes</button>
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
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                text-align: center;
                color: white;
            }}
            .content-wrapper {{
                max-width: 800px;
                margin: auto;
            }}
            h1{{
                font-size: 50px;
                color: rgb(15, 25, 60);
                margin-top: 40px;
                line-height: 1.2;
            }}
            p{{
                margin: 40px 0;
                font-size: 24px;
                line-height: 1.6;
            }}
            .retour{{
                background-color:black;
                color:white;
                border: 2px solid red;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                border-radius:10px;
                cursor: pointer;
                transition: 0.2s;
                margin-top: 20px;
                width: auto;
                display: inline-block;
            }}
            .retour:hover {{
                transform: scale(1.05);
            }}
            @media (max-width: 600px) {{
                h1 {{ font-size: 34px; }}
                p {{ font-size: 18px; }}
                .retour {{ width: 100%; }}
            }}
        </style>
    </head>
    <body>
    <div class="content-wrapper">
        <h1><u>TU ES EN LISTE D'ATTENTE</u></h1>

        <p><u>Tu es encore en phase principale</u> (jour {n-1}),<br>
         retourne à la simulation pour voir les résultats au 40ème jour (ou moins si tu es admis avant).</p>
         
        <form action="/simulation">
            <button type="submit" class="retour">Retour à la simulation</button>
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
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                text-align: center;
                color: white;
            }}
            .content-wrapper {{
                max-width: 800px;
                margin: auto;
            }}
            h1{{
                font-size: 50px;
                color: rgb(15, 25, 60);
                margin-top: 40px;
            }}
            p{{
                margin: 40px 0;
                font-size: 22px;
                line-height: 1.6;
            }}
            .container{{
                display:flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
                margin-top: 40px;
            }}
            .formation1, .formation2{{
                background-color:black;
                color:rgb(255,255,192);
                border: 2px solid rgb(255,255,192);
                padding: 15px 25px;
                font-size: 16px;
                font-weight: bold;
                border-radius:10px;
                cursor: pointer;
                transition: 0.2s;
                min-width: 220px;
            }}
            .formation1:hover, .formation2:hover {{
                transform: scale(1.05);
            }}
            .retour{{
                background-color:black;
                color:white;
                border: 1px solid white;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 8px;
                cursor: pointer;
                margin-bottom: 20px;
            }}
            @media (max-width: 600px) {{
                h1 {{ font-size: 34px; }}
                p {{ font-size: 18px; }}
                .container {{ flex-direction: column; gap: 15px; align-items: center; }}
                .formation1, .formation2 {{ width: 100%; }}
            }}
        </style>
    </head>
    <body>
    <div class="content-wrapper">
        <form action="/simulation">
            <button type="submit" class="retour">← Retour à la simulation</button>
        </form>
        <h1><u>TU ES REFUSÉ</u></h1>

        <p>Tu as été placé trop bas <br>
        ({place}ème sur {population}, le premier candidat refusé étant {classes}ème, et le dernier appelé {dernier_candidat}ème),<br>
          tu n'as donc pas reçu de proposition d'admission.</p>
          
        <div class="container">
            <form action="/choix">
                <button class="formation1" type="submit">Retour choix formation</button>
            </form>
            <form action="/formulaire">
                <button class="formation2" name="etude" value="{etude}" type="submit">Retour formulaire de notes</button>
            </form>
        </div>
    </div>
    </body>
</html>
"""