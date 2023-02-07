# Opendeurspel

# DataBase
Connection --> Ons definitieve "ontwerp" zal de remote_connection gebruiken, zodat we dus kunnen communiceren met een andere server.

Nuttig om te weten: 
    1) my_conn = my_connect.cursor(buffered=True)
    
    => Dit maakt een cursos aan voor de verbinding, die kan worden gebruikt om queries uit te voeren.

    2) def better_string(string)

    => Neemt een string-imput als argument en verwerkt deze string door bepaalde tekens te vervangen door lege strings.

Queries:
Parameters: 
    - Data = In het algemeen stelt deze parameter voor, wat je eigenlijk wilt van die speciefieke tabel.
    - IDin = Elke tabel heeft ID's voor elke nieuwe rij in de database.
    - clas = simpel weg, alle klassen waarbij we een vraag zullen plaatsen.
    
    1) def select_users(data, IDin)
    => Alle data van de tabel users selecteren.

    
    2) def select_answer(data, IDin)
    => Alle data van de tabel answer selecteren.


    3) def select_question_text(clas)
    => Je gaat de vragen selecteren uit de tabel questions.


    4) def select_question_type(clas)
    => Je gaat de type's van de vragen selecteren uit de tabel questions.


    5) def select_results(data,IDin)
    => Alle data van de tabel results selecteren.

    
    6) def count_true_results(tabel, kolom, IDin)
    => In het algemeen helpt deze functie om het aantel waarheidswaardige resultaten in een database te tellen, door middel van een SELECT-query met een COUNT-functie.
    
    
    7) def insert_result(user_id, question_id , result)
    => Heel simpel, het gaat gewoon een nieuwe rij toevoegen aan de tabel "result" in de database.


    8) def insert_question_with_answer(question,multy,clas, answer, possible) + def insert_answers(answer, questions_id, correct, possible)
    => Je gaat de twee tabellen tegelijkertijd gebruiken.


    9) def update_questions(question,multy,clas)
    => In de tabel "questions", elke variabele veranderen met de variabele die hij heeft gekregen.


    10) def insert_user(name,last_name,email_adres,email_kind,age_child,direction,contact,phone_number,code)
    => Wordt gebruikt om een nieuwe user toe te voegen aan je database met specifieke data.

    
    11) def update_user(name,last_name,email_adres,email_kind,age_child,direction,contact,phone_number,code)
    => In de tabel "user", elke variabele veranderen met de variabele die hij heeft gekregen.


# Opstelling

