Tento skript sluzi na export worklogu z Jira cloud do .csv suboru vo formate, ktory akceptuje Humanity. Nizsie je postup ako spustit skript a exportovat worklog.

INSTALACIA python-u:

WINDOWS:
na windows som uz mal nainstalovany python tak presny prikaz neviem ale na google isto bude alebo chatGPT isto pomoze

LINUX:
V Linuxe by uz mal byt nainstalovany defaultne. 
Prikaz pre overenie: python3 --version

MACOS:
nemam MAC, tak neviem prikaz

INSTALACIA kniznice pandas pre spravu .csv suborov:

WINDOWS:
pip install pandas

LINUX:
sudo apt-get install python3-pandas

MACOS:
nemam MAC, tak neviem prikaz

Teraz by sa uz malo dat spustit skript life_simplifier.py.

Vygenerovanie autorizacneho tokenu v Jira Cloud a nasledne ulozenie do suboru pre zjednodusenie:

Pred spustenim skriptu vytvorime subor s nazvom 'api_token' v adresari kde mame ulozeny aj skript. Nasledne si v Jira Cloud vygenerujeme API token. Token vygenerujeme nasledne, klikneme v pravom hornom rohu na ikony nasho profilu, potom vyberieme My Work, nasledne v lavom panely vyberieme API tokens a tam vidime na pravo button create token. Ked stlacime toto tlacidlo, tak sa nam vygeneruje API token, ktory vlozime do suboru api_token. Tento token vkladame do suboru preto, lebo ak by sme si ho neulozili tak v Jire sa uz spatne ku nemu nedostaneme a tak by sme si museli za kazdym vygenerovat novy token, co je trocha otravne.

SPUSTENIE SKRIPTU:

Treba sa dostat do adresara, kde je umiestneny skript. Nasledne spustit prikaz:

WINDOWS:
python life_simplifier.py

LINUX:
python3 life_simplifier.py

MACOS:
nemam, tak neviem presny prikaz 

Po tomto prikaze vypisete udaje ako je meno, email, poznamka, ktora sa priradi ku kazdemu logu dna, adresa, rola a obdobie, za ktore chceme vygenerovat worklog. Po tomto kroku, ak sa vsetko vykonalo spravne, by sa mal uz vytvorit finalny subor s nazvom timesheet ako vystup zo skriptu. Tento subor je uz validny ako vstupny subor do humanity.
POZOR: vzdy sa kazdy den rata od 8:00am pre zjednodusenie, ale pocet odpracovanych hodin v danom dni sa stotoznuje. Ide o to, ak ste mali zapisane, ze ste zacali pracovat napriklad od 10:00am, tak vam aj tak tento den zapise a zacne od 8:00am vo vystupnom .csv subore. Diskutoval som to s Michalom a nemal by byt s tym problem minimalne pre brigadnikov.

PS: Dufam ze som vam aspon trocha zjednodusil zivot s nahravanim hodin do humanity
