import pdfkit
import pathlib



file = open("diploma-test.html","w")
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
            font-family: "Comic Sans MS", "Comic Sans", cursive;
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
                    <p>We danken u aan het deelnemen van onze opendeurspel.</p>
                    <p>U hebt onze school eens gezien en onze vakken eens beleefd.</p>
                    <p>Onze school zal altijd met open armen staan voor nieuwe leerlingen.</p>
                    <p>We hoopen ook dat jullie nog een fijne dag hadden.</p>
                    <br>
                    <p>Met dank van het ICT klas, 6ICT.</p>
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
file.write(text)
file.close()

options = { "enable-local-file-access": ""
                }
pdfkit.from_file('diploma-test.html', "diploma-test.pdf", configuration=pdfkit.configuration(wkhtmltopdf=b'wkhtmltopdf.exe'), options=options)

#pdfkit.from_string(html_sample, output_path = "diploma-test.pdf")