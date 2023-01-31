# Opendeurspel

# Database
Connection --> Ons definitieve "ontwerp" zal de remote_connection gebruiken, zodat we dus kunnen communiceren met een andere server.

Nuttig om te weten: 
    1) my_conn = my_connect.cursor(buffered=True)
    
    => Dit maakt een cursos aan voor de verbinding, die kan worden gebruikt om queries uit te voeren.

    2) def better_string(string)

    => Neemt een string-imput als argument en verwerkt deze string door bepaalde tekens te vervangen door lege strings.

Queries:
    1) def select_Culumn_out_of_database(tabel, kolom, IDin)

    => In het algemeen helpt deze functie om speciefieke gegevens uit een database op te halen op basis van een ID_nummer, door middel van een SELECT-query.

    2) def count_true_results(tabel, kolom, IDin)

    => In het algemeen helpt deze functie om het aantel waarheidswaardige resultaten in een database te tellen, door middel van een SELECT-query met een COUNT-functie.

    3) def insert_result(user_id, question_id , result)

    => Heel simpel, het gaat gewoon een nieuwe rij toevoegen aan de tabel "result" in de database.
