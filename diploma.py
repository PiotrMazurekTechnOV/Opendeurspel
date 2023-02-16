import os
import database
from tkinter import *
from PIL import ImageTk, Image
import pdfkit

def create_file(user_id : str):
    unknown = database.select_result_amount_for(user_id)
    naam = "Doe"
    voornaam = "John"
    score = str(unknown[0])
    vragenaantal = str(unknown[1])
    file = open("diploma.html","w")
    text = '''
    <!DOCTYPE html>
        <head>
            <style>
            body{
                font-family: "Verdana";
                color: Black;
                font-size: 25px;
            }
            h1{
                font-family: "Garamond";
                font-size: 60px;
            }
            h4{
                position: relative;
                font-family: "Arial";
                font-size: 20px;
            }
            a{
                font-family: "Verdana";
                font-size: 30px;
            }
            .logo{
                margin-left: 10px; 
                margin-top: 10px;
                width: 35%;
            }
            .hand{
                height: 120px;
                margin-right: 10%;
            }
            .lower{
                position: absolute;
                bottom: 0px;
                right: 0px;
            }
            </style>

            <body>
                <img class="logo" src="technov-logo.png" alt="LOGO KOV">
                <div style="text-align: center;">
                    <hr><br>
                    <h1>CERTIFICATE OF COMPLETION</h1>
                    <br>
                    <p>Certificaat van <a>placeholder_naam</a></p>
                    <br>
                    <p>U heeft het einde van het opendeurspel bereikt<br>met een score van: <a>placeholder_score</a></p>
                    <br>
                    <p>In totaal hebt u <a>placeholder_nvragen</a> vragen beantwoord</p>
                </div>
                <br><br><br><br><br><br><br>
                <div>
                    <div style="font-size: 18px">
                        <p>We danken je voor je deelnemen aan ons opendeurspel.</p>
                        <p>Je hebt onze school en onze richtingen gezien.</p>
                        <p>TechnOV zal je altijd met open armen ontvangen.</p>
                        <p>We hoopen ook dat jullie nog een fijne dag hadden.</p>
                        <br>
                        <p>Met dank aan de ICT klas, 6ICT.</p>
                    </div>
                    <div class="lower">
                        <h4>Ondertekend door:</h4>
                        <img src="ondertekend.png" alt="Directeur" class="hand">
                    </div>
                </div>
            </body>
        </head>
    </html>
    '''
    new_text = text.replace("placeholder_naam", voornaam + " " + naam).replace("placeholder_score", score ).replace("placeholder_nvragen", vragenaantal)
    text = new_text
    file.write(text)
    file.close()
    pdfkit.from_file('diploma.html', "diploma.pdf", configuration=pdfkit.configuration(wkhtmltopdf=b'wkhtmltopdf.exe'), options={ "enable-local-file-access": ""})

def print():
    os.startfile('diploma.pdf',"print")

create_file("RD0")