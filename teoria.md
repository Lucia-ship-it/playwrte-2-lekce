browser = chromium, firefox, webkit



context = 1 okno prehliadaca


page = 1 zalozka v prehliadaci


v praxi sa tie operacne systemy mozu chovat trosku inak

 #vytvorime si svoju vlastnu stranku

 sync_playwright = pridame si do importu
synchronni idu metody cele za sebou
 asynchronni nepracuje podla danych krokov postupne, treba tam volat vysledok

 launch ma moznost veeela parametrov, mozem nastavit aj velkost obrzovky napr pre mobil
 
 headless= True - spusta sa na pozazi a true je defaultne

 ak bude false - budeme vidiet, ako sa to deje a chova sa to viac ako realny uzivatel
 nevyhoda - ako uzivatel s tym mozem interagovat a klikat tam. coz moze dopadnut spatne

 slow_mo- jednotlive operacie sa robia trosku pomalsie. aby sme to vobec stihli vidiet