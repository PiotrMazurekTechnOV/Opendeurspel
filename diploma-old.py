from PIL import *
from tkinter import *
from datetime import *
#import mysql.connector
import os
import pdfkit

root= Tk()
#maak fullscreen
root.attributes('-fullscreen', True)

root.iconbitmap('kovlogo.ico')

bg = PhotoImage(file = "bg_score.png")
imagelabel = Label(root, image = bg)
imagelabel.place(x = 0, y = 0,relwidth = 1, relheight = 1)

IDin = 0
vorigenaam = "placeholder_name"
vorigescore = "placeholder_score"
vorigevr = "placeholder_vraag"

vandaag = str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year) + "-"

#loginbutton
def lgnbutton():
    global naam, score, IDin, aantvr
    #onthoud login
    IDin = login.get()
    #haal alleen naam/score van login
    my_conn.execute(("SELECT naam FROM users WHERE ID = %s"),(IDin,))
    naam = my_conn.fetchone()
    my_connect.commit()
    my_conn.execute(("SELECT COUNT(*) FROM `results` WHERE user_id = %s AND NOT result = 0"),(IDin,))
    score = my_conn.fetchone()
    my_connect.commit()
    my_conn.execute(("SELECT COUNT(*) FROM `results` WHERE user_id = %s"),(IDin,))
    aantvr = my_conn.fetchone()
    my_connect.commit()
    #zorg ervoor dat nummer en naam correct geprint wordt
    naam = str(naam).replace(',','').replace('(','').replace(')','').replace("'",'')
    score = str(score).replace(',','').replace('(','').replace(')','').replace("'",'').replace("Decimal","")
    aantvr = str(aantvr).replace(',','').replace('(','').replace(')','').replace("'",'')

    #date + uur
    vandaag = str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year) + "-"

    if(score == "None"):
        hallo.configure(text = "ongeldig nummer"
                        , bg="#DF3740", font=("Constantia",15),relief = GROOVE)
    #configure label zodat de zin tevoorschijn komt
    else:
        hallo.configure(text = f"hallo {naam} , \n Je hebt een score van {score} gescoord op {aantvr}\n \n -{vandaag}"
                        , bg="#D5FCEC", font=("Constantia",15),relief = GROOVE)
        printbutton.place(relx=0.5, rely=0.6, anchor=CENTER)

    hallo.place(relx=0.5, rely=0.5, anchor=CENTER)

    okbutton.place(relx=0.7, rely=0.5, anchor=CENTER)

    #vergeet benoodigtheden voor login
    log.place_forget()
    login.place_forget()
    loginbutton.place_forget()

def prntbutton():
    global naam, score, vorigenaam, vorigescore, vandaag
    file = open("indexGIP.html","r")
    naam = 'test'
    score = '10'
    new_file_content = ""
    for line in file:
        stripped_line = line.strip()
        #new_line = stripped_line.replace(vorigenaam, naam ).replace(vorigescore, score ).replace(vorigevr, aantvr )
        #new_file_content += new_line +"\n"
    file.close()
    file = open("indexGIP.html","w")
    file.write(new_file_content)
    file.close()
    options = { "enable-local-file-access": ""
                }
    filename= naam+"_"+score+"_"+vandaag+'.pdf'
    pdfkit.from_file('indexGIP.html', filename, configuration=pdfkit.configuration(wkhtmltopdf=b'C:\Users\ZbigniewSzypkowski\OneDrive - Katholiek Onderwijs Vilvoorde Machelen Diegem vzw\Documenten\GitHub\Opendeurspel\wkhtmltopdf.exe'), options=options)
    os.startfile(filename,"print")
    
        
#okbutton
def kbutton():
    global naam, vorigenaam, score, vorigescore
    vorigenaam = naam
    vorigescore = score
    hallo.place_forget()
    okbutton.place_forget()
    printbutton.place_forget()

    login.delete(0,END)

    log.place(relx=0.5, rely=0.35, anchor=CENTER)
    login.place(relx=0.5, rely=0.5, anchor=CENTER)
    loginbutton.place(relx=0.6, rely=0.5, anchor=CENTER)

#login
log = Label(root, text = "Geef hier je nummer in:"
            ,font = ("Constantia",25) ,bg="#A1ACD9", fg="#3C1B3A",relief = RIDGE)
log.place(relx=0.5, rely=0.35, anchor=CENTER)
login = Entry (root, bd = 5)
login.place(relx=0.5, rely=0.5, anchor=CENTER)
loginbutton = Button(root, text='login', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                     ,command=lgnbutton)
loginbutton.place(relx=0.6, rely=0.5, anchor=CENTER)
printbutton = Button(root, text='print diploma', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                     ,command=prntbutton)
printbutton.place(relx=0.6, rely=0.5, anchor=CENTER)
#maak label en ok button en plaats ze later
hallo = Label(root,font = "Times")
okbutton = Button(root, text='OK', bg="#502E93", fg="#F9DEE3", font=("Constantia",15),relief = GROOVE
                  , command=kbutton)
#reset de html code als je het programma start
file = open("indexGIP.html","w")
text = '''

<!DOCTYPE html>
<html>
<head>
<style>
    body {
        text-align:center;
    }
    img{
        width:100%;
    }
    p {
        font-size: 60px;
    }
    hl {
        font-size: 60px;
    }
    .tiny {
        font-size: 35px;
    }
    .big {
        font-weight: bold;
    }
</style>

<body>
<div class="container center">
<img id = "foo" src="Fotos/kovlogo.jpg" alt="KOV LOGO FOTO"  alt ="" style="">
<br />
<h1 style="font-size: 60px;" align = "center" vertical-align = "middle">OPENDEUR SCORE</h1>
<p>Proficiat placeholder_name</p>
<p style="text-align : center;" >Enorm bedankt om ons spel te spelen op de TechnOV opendeurdag.</p>
<br />
<p style="text-align : center;" class = "big">Uw score is placeholder_score op placeholder_vraag.</p>
<br />
<p style="text-align : right;" class= "tiny">Het Technov Team</p>
</div>

</body>
</head>
</html>

'''
file.write(text)
file.close()
root.mainloop()