import time

def intro():
    print("Willkommen zum textbasierten Adventure-Spiel!")
    time.sleep(1)
    print("Du stehst vor einer Höhle. Bist du bereit, hineinzugehen?")
    choice = input("Ja/Nein: ").lower()
    if choice == "ja":
        cave()
    else:
        print("Vielleicht das nächste Mal!")
        
def cave():
    print("\nDu betrittst die Höhle und siehst zwei Wege: links und rechts.")
    time.sleep(1)
    print("Welchen Weg wählst du?")
    choice = input("Links/Rechts: ").lower()
    if choice == "links":
        print("\nDu gehst nach links und triffst auf einen Drachen!")
        time.sleep(1)
        print("Was machst du?")
        choice = input("Kämpfen/Fliehen: ").lower()
        if choice == "kämpfen":
            print("\nDu kämpfst gegen den Drachen...")
            time.sleep(1)
            print("Du hast den Drachen besiegt! Glückwunsch, du gewinnst!")
        else:
            print("\nDu fliehst aus der Höhle und kehrst sicher nach Hause zurück. Spiel beendet!")
    else:
        print("\nDu gehst nach rechts und trittst in eine dunkle Kammer ein.")
        time.sleep(1)
        print("Es ist zu dunkel, um etwas zu sehen...")
        time.sleep(1)
        print("Du hörst ein seltsames Geräusch hinter dir.")
        time.sleep(1)
        print("Was machst du?")
        choice = input("Umsehen/Weitergehen: ").lower()
        if choice == "umsehen":
            print("\nDu drehst dich um und siehst ein gruseliges Monster!")
            time.sleep(1)
            print("Schnell, du musst handeln!")
            choice = input("Angreifen/Fliehen: ").lower()
            if choice == "angreifen":
                print("\nDu kämpfst gegen das Monster...")
                time.sleep(1)
                print("Leider ist das Monster zu stark und du wirst besiegt. Spiel beendet!")
            else:
                print("\nDu fliehst aus der Höhle und kehrst sicher nach Hause zurück. Spiel beendet!")
        else:
            print("\nDu gehst weiter in die Kammer hinein und triffst auf ein mysteriöses Artefakt!")
            time.sleep(1)
            print("Herzlichen Glückwunsch, du hast das Artefakt gefunden und das Spiel gewonnen!")
            
# Spiel starten
intro()
