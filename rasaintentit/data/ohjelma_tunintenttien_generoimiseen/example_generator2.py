import random
import sys


##Tämä pieni ohjelma kopioi alkuperäisen tiedoston jokaisen rivin uuteen tiedostoon,
##ja käyttää komentoriviargumentteina, esimerkiksi:
##python example_generator2.py tunintentit_gener.md course_codes.txt  uta_course_names.txt
##Tällöin se luo out_tunintentit_gener.md -tiedoston, jossa on jokainen kysymys niin monta kertaa kopioituna,
##kuin INTENT_MULTIPLIER sallii.

##Ohjelma olettaa, että tunintentit_gener.md:ssä on korvattu jokainen esimerkkikurssikoodi tähtimerkillä *.

## Ohjelma myös lisää esimerkkikysymykset siten, että
## ensin kirjoitetaan kopiot kysymyksestä kurssien *koodien* kanssa,
## ja sittenluodaan kopiot kurssien *nimien* kanssa.
## 
## Kurssien nimien kirjoittamisen yhteydessä ohjelma korvaa entiteetin (course) muotoon (coursename).
#EI toistaiseksi lisää alkuperäisen tiedoston oletusmateriaalia kuten "hi" ja "my name is John" jne

#lisää kuitenkin loppuun lookup-table-käskyt

#INTENT MULTIPLIER määrää, montako kertaa kopioidaan harjoitteludatan jokainen kysymys.
INTENT_MULTIPLIER = 30

#luetaan komentoriviltä argumentit tunintentit_gener.md (jossa hakasulkeissa tähtimerkit kurssien tilalla),
# kirjoitetaan uuteen out_tunintentit_gener.txt-tiedostoon,
# haetaan kahdesta viimeisestä argumentista kurssikoodit ja kurssinimet -- siinä järjestyksessä



with open(sys.argv[1], 'r') as intents, open("out_" + sys.argv[1], 'w') as out, open(sys.argv[2], 'r') as lookup, open(sys.argv[3], 'r') as lookup2:
    #kurssikoodit
    codes = lookup.readlines()
    #kurssinimet
    names = lookup2.readlines()
    #tunintentit_gener.md-rivit
    intent_list = intents.readlines()
    
    
    
    #tunintentit.md-tiedoston joka riviä käsitellään yksi kerrallaan:
    for row in intent_list:
        #jos rivillä EI ole kahdet #-merkit (eli jos find palauttaa -1)
        #tai jos se on hyvin lyhyt (< 2), se on joko
        #intentin otsikko (##intent:paikka esim) tai tyhjä rivi
        
        if row.find("##") < 0 and len(row) > 2:
            #kirjoitetaan annettu määrä kopioita kustakin kysymyksestä (intent multiplier),
            #uudet kopiot jokaisesta alkuperäisestä tunintentit_gener-rivistä kirjoitetaan peräkkäin,
            #ensin kurssikoodein ja sitten kurssien nimien kanssa
            for i in range(0, INTENT_MULTIPLIER):
             out.write(row.replace("*", random.choice(codes).strip()))
             #kurssien nimille eri entiteetti, coursename
             out.write(row.replace("*", random.choice(names).strip()).replace("(course)", "(coursename)"))
        #jos rivi alkaa ##-merkeillä tai on vain rivinvaihto,
        #kirjoitetaan se vain kerran
        else:
            out.write(row)
    #lisätään vielä lookup-käskyt
    out.write("\n<!--- lookup table list for course codes.  -->\n## lookup:course\n- data/course_codes.txt\n- data/uta_course_names.txt\n")
            
