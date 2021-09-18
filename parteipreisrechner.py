
def mitgliedsbeitrag_CDU(bruttoeinkommen):
    # SRC : 
    if bruttoeinkommen < 2500:
        return 6
    elif bruttoeinkommen >= 2500 and bruttoeinkommen < 4000:
        return 15
    elif bruttoeinkommen >= 4000 and bruttoeinkommen < 6000:
        return 25
    elif bruttoeinkommen > 6000:
        return 50

def mitgliedsbeitrag_SPD(nettoeinkommen):
    # SRC : https://www.spd.de/unterstuetzen/mitglied-werden/#accordion__toggle-button-75821-6
    if nettoeinkommen < 1000:
        return 6
    elif nettoeinkommen >= 1000 and nettoeinkommen < 2000:
        return 8
    elif nettoeinkommen >= 2000 and nettoeinkommen < 3000:
        return 26
    elif nettoeinkommen >= 3000 and nettoeinkommen < 4000:
        return 47
    elif nettoeinkommen >= 4000 and nettoeinkommen < 6000:
        return 105
    elif nettoeinkommen > 6000:
        return 300
    else:
        return "INVALID VALUE"

def mitgliedsbeitrag_grüne(nettogehalt):
    # SRC : https://www.gruene.de/mitglied-werden#accordion__title-1
    return nettogehalt*0.01

def mitgliedsbeitrag_FPD(bruttogehalt, inAusbildung):
    # SRC : https://mitgliedwerden.fdp.de/fragen-und-antworten-zur-mitgliedschaft#waskostetdas
    if inAusbildung==True:
        return 5
    else:
        if bruttogehalt < 2401:
            return 10
        elif bruttogehalt >= 2401 and bruttogehalt < 3601:
            return 12
        elif bruttogehalt >= 3601 and bruttogehalt < 4800:
            return 18
        elif bruttogehalt > 4800:
            return 24
        else:
            return "INVAID VALUE"

def mitgliedsbeitrag_AfD(nettoeinkommen):
    # https://www.afd.de/mitglied-werden/
    return max(120/12, nettoeinkommen*0.01)

def mitgliedsbeitrag_PARTEI():
    # https://www.partei-essen.de/mitmachen/
    return 10

##

if __name__ == "__main__":

    ausbildung = bool(input("Machen Sie gerade eine Aubildung?"))
    nettoGehalt = float(input("Wie Hoch ist Ihr Netto-Gehalt?"))
    bruttoGehalt = float(input("Wie Hoch ist Ihr Brutto-Gehalt?"))
    #ausbildung   = False
    #nettoGehalt  = 1233.37
    #bruttoGehalt = 1558.91
    #nettoGehalt  = 3500
    #bruttoGehalt = 5000
    ausgabe =  "CDU   : " + str(mitgliedsbeitrag_CDU(bruttoeinkommen=bruttoGehalt)) + "€\n"
    ausgabe += "SPD   : " + str(mitgliedsbeitrag_SPD(nettoeinkommen=nettoGehalt)) + "€\n"
    ausgabe += "FDP   : " + str(mitgliedsbeitrag_FPD(bruttogehalt=bruttoGehalt,inAusbildung=ausbildung)) + "€\n"
    ausgabe += "Grüne : " + str(mitgliedsbeitrag_grüne(nettogehalt=nettoGehalt)) + "€\n"
    ausgabe += "AfD   : " + str(mitgliedsbeitrag_AfD(nettoeinkommen=nettoGehalt)) + "€\n"
    ausgabe += "PARTEI: " + str(mitgliedsbeitrag_PARTEI()) + "€\n"
    print(ausgabe)