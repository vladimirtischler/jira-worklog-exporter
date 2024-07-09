V tomto subore je popisany postup ako rozbehat skript. 

instalacia python-u:

WINDOWS:
na windows som uz mal nainstalovany python tak presny prikaz neviem ale na google isto bude alebo chatGPT isto pomoze

LINUX:


MACOS:
nemam MAC, tak neviem prikaz

instalacia kniznice pandas pre spravu excel suborov:

WINDOWS:
pip install pandas

LINUX:

MACOS:
nemam MAC, tak neviem prikaz

Teraz by sa uz malo dat spustit skript life_simplifier.py.

STIAHNUTIE Timesheet suboru z Jira cloud:

Pred spustenim skriptu treba stiahnut timesheet z jira cloud. Najdete ho, ked kliknete v pravom rohu na svoje meno, nasledne, ked sa vam zroluje dalsi panel zvolte My Work. Tam si zvolite obdobie, za ktore si chcete urobit .csv subor. Nasledne vpravo hned nad tabulkou s rozpisanymi hodinami, ktore ste stravili na ulohach najdete ikonu oblaku, ked na nu stlacite sa vyroluju moznosti k stiahnutiu. Treba vybrat Timesheet, hned na to by sa mal stiahnut subor, ktory potrebujeme.

SPUSTENIE SKRIPTU:

Treba sa dostat do adresara, kde je umiestneny skript. Nasledne spustit prikaz:

WINDOWS:
python life_simplifier.py

LINUX:


MACOS:
nemam, tak neviem presny prikaz 

Po tomto prikaze vypiseme udaje ako je meno, poznamka, ktora sa priradi ku kazdemu logu dna, adresa a rola. Po tomto kroku ak sa vsetko vykonalo spravne, by sa mal uz vytvorit finalny subor s nazvom timesheet ako vystup zo skriptu. Tento subor je uz validny ako vstupny subor do humanity.
POZOR: vzdy kazdy den rata od 8:00 pre zjednodusenie, ale na konci dna pocet hodin v danom dni sa stotoznuju len je mozne ze ak ste mali zapisane ze ste zacali pracovat napriklad od 10:00am, tak vam aj tak tento den zapise a zacne od 8:00am vo vystupnom .csv subore. Ale tak toto by nemal byt problem minimalne pre brigadnikov.

PS: Dufam ze som vam aspon trocha zjednodusil zivot s nahravanim hodin do humanity