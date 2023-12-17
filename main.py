import aplinka
from aplinka import zaidimo_lenta, pasisveikinimas

zaidimas = "Vyksta"

pasisveikinimas()

while zaidimas == "Vyksta":
    if (((aplinka.vienas != "X") or (aplinka.du != "X") or (aplinka.trys != "X")) and
            ((aplinka.vienas != "0") or (aplinka.du != "0") or (aplinka.trys != "0")) and
            ((aplinka.vienas != "X") or (aplinka.keturi != "X") or (aplinka.septyni != "X")) and
            ((aplinka.vienas != "0") or (aplinka.keturi != "0") or (aplinka.septyni != "0")) and
            ((aplinka.vienas != "X") or (aplinka.penki != "X") or (aplinka.devyni != "X")) and
            ((aplinka.vienas != "0") or (aplinka.penki != "0") or (aplinka.devyni != "0")) and
            ((aplinka.du != "X") or (aplinka.penki != "X") or (aplinka.astuoni != "X")) and
            ((aplinka.du != "0") or (aplinka.penki != "0") or (aplinka.astuoni != "0")) and
            ((aplinka.keturi != "X") or (aplinka.penki != "X") or (aplinka.sesi != "X")) and
            ((aplinka.keturi != "0") or (aplinka.penki != "0") or (aplinka.sesi != "0")) and
            ((aplinka.trys != "X") or (aplinka.penki != "X") or (aplinka.septyni != "X")) and
            ((aplinka.trys != "0") or (aplinka.penki != "0") or (aplinka.septyni != "0")) and
            ((aplinka.trys != "X") or (aplinka.sesi != "X") or (aplinka.devyni != "X")) and
            ((aplinka.trys != "0") or (aplinka.sesi != "0") or (aplinka.devyni != "0")) and
            ((aplinka.septyni != "X") or (aplinka.astuoni != "X") or (aplinka.devyni != "X")) and
            ((aplinka.septyni != "0") or (aplinka.astuoni != "0") or (aplinka.devyni != "0"))):
        zaidimo_lenta()
        skaicius = int(input("Pirmasis žaidėjas \nPasirinkikte skaičių \n"))
        if skaicius == 1:
            aplinka.vienas = "X"
        elif skaicius == 2:
            aplinka.du = "X"
        elif skaicius == 3:
            aplinka.trys = "X"
        elif skaicius == 4:
            aplinka.keturi = "X"
        elif skaicius == 5:
            aplinka.penki = "X"
        elif skaicius == 6:
            aplinka.sesi = "X"
        elif skaicius == 7:
            aplinka.septyni = "X"
        elif skaicius == 8:
            aplinka.astuoni = "X"
        elif skaicius == 9:
            aplinka.devyni = "X"
        else:
            print("Pasirinkote neteisingą skaičių")
            continue

        zaidimo_lenta()
        skaicius = int(input("Antrasis žaidėjas \nPasirinkikte skaičių \n"))
        if skaicius == 1:
            aplinka.vienas = "0"
        elif skaicius == 2:
            aplinka.du = "0"
        elif skaicius == 3:
            aplinka.trys = "0"
        elif skaicius == 4:
            aplinka.keturi = "0"
        elif skaicius == 5:
            aplinka.penki = "0"
        elif skaicius == 6:
            aplinka.sesi = "0"
        elif skaicius == 7:
            aplinka.septyni = "0"
        elif skaicius == 8:
            aplinka.astuoni = "0"
        elif skaicius == 9:
            aplinka.devyni = "0"
        else:
            print("Pasirinkote neteisingą skaičių")
            continue

    else:
        print(aplinka.vienas)
        zaidimas = "Baigėsi"
        zaidimo_lenta()

        if (((aplinka.vienas == "X") and (aplinka.du == "X") and (aplinka.trys == "X")) or
            ((aplinka.vienas == "X") and (aplinka.keturi == "X") and (aplinka.septyni == "X")) or
            ((aplinka.vienas == "X") and (aplinka.penki == "X") and (aplinka.devyni == "X")) or
            ((aplinka.du == "X") and (aplinka.penki == "X") and (aplinka.astuoni == "X")) or
            ((aplinka.keturi == "X") and (aplinka.penki == "X") and (aplinka.sesi == "X")) or
            ((aplinka.trys == "X") and (aplinka.penki == "X") and (aplinka.septyni == "X")) or
            ((aplinka.trys == "X") and (aplinka.sesi == "X") and (aplinka.devyni == "X")) or
            ((aplinka.septyni == "X") and (aplinka.astuoni == "X") and (aplinka.devyni == "X"))):
            print("Laimėjo pirmasis žaidėjas")

        elif (((aplinka.vienas == "0") and (aplinka.du == "0") and (aplinka.trys == "0")) or
            ((aplinka.vienas == "0") and (aplinka.keturi == "0") and (aplinka.septyni == "0")) or
            ((aplinka.vienas == "0") and (aplinka.penki == "0") and (aplinka.devyni == "0")) or
            ((aplinka.du == "0") and (aplinka.penki == "0") and (aplinka.astuoni == "0")) or
            ((aplinka.keturi == "0") and (aplinka.penki == "0") and (aplinka.sesi == "0")) or
            ((aplinka.trys == "0") and (aplinka.penki == "0") and (aplinka.septyni == "0")) or
            ((aplinka.trys == "0") and (aplinka.sesi == "0") and (aplinka.devyni == "0")) or
            ((aplinka.septyni == "0") and (aplinka.astuoni == "0") and (aplinka.devyni == "0"))):
            print("Laimėjo antrasis žaidėjas")
