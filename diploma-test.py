import os
#import database
from tkinter import *
from PIL import ImageTk, Image
import pdfkit
def prntbutton():
    naam = "Doe"
    voornaam = "John"
    score = "8"
    vragenaantal = "12"
    #unknown = database.select_result_amount_for("RD0") 

    file = open("diploma-test.html","w")
    text = '''<!DOCTYPE html>
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
                        <p>Met dank van de ICT klas, 6ICT.</p>
                    </div>
                    <div class="lower">
                        <h4>Ondertekend door:</h4>
                        <img src="ondertekend.png" alt="Directeur" class="hand">
                    </div>
                </div>
            </body>
        </head>
    </html>'''

    new_text = text.replace("placeholder_naam", voornaam + " " + naam).replace("placeholder_score", score ).replace("placeholder_nvragen", vragenaantal)

    text = new_text
    file.write(text)
    file.close()
    pdfkit.from_file('diploma-test.html', "diploma-test.pdf", configuration=pdfkit.configuration(wkhtmltopdf=b'wkhtmltopdf.exe'), options={ "enable-local-file-access": ""})

def creatprint():
    os.startfile('diploma-test.pdf',"print")

root = Tk()
root.attributes('-fullscreen', True)
root.iconbitmap('kovlogo.ico')
root.title('Eind Resultaat')
root.geometry("1920x1080")

canvas= Canvas(root, width= 1920, height= 1080)
canvas.pack()
img= (Image.open("bg_score.png"))
resized_image= img.resize((1920,1080), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor=NW, image=new_image)

printbutton = Button(root, text='print diploma', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE, command=prntbutton)
printbutton.place(relx=0.5, rely=0.75, anchor=CENTER)

root.mainloop()