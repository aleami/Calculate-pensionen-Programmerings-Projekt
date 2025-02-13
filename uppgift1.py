#Ett programm som visar sin nuvarande pensionsålder samt ger valet om man vill öka eller sänka sin pension.

#Detta är hvudrubriken för detta program
#print för en output
print('Pension Koll')
print('============')

#Här frågar vi användaren ens för- och efternamn
#För att användaren ska kunna svara så använder vi input.
#Variabeln F använder vi för att ange förnamnnet.
#Variabeln e använder vi för att ange efternamn.
#input används för att användaren ska kunna skriva svar på en fråga till exempel.
f = input('Skriv in ditt förnamn: ')

e = input('Skriv in ditt efternamn: ')

#I variabeln å frågar vi användarens ålder
#För att det är siffror så skriver vi integer som representerar heltal.
#För att användaren ska kunna svara så skriver vi input.
å = int(input('Vad är din ålder? '))

#Här talar vi om för koden med en variabel att det går att skriva j för att svara ja.
#Detta anger vi med variabeln b, vilket identifierar Ja.
b = 'j'

#Här talar vi om för koden med en variabel att det går att skriva Nej med ett liten n bara.
#Detta anger vi med variabeln z, vilket identifierar Nej.
z = 'n'

#Variabeln s berättar om att pensions åldern subtraherat med personens ålder så får vi pensionsåren som är kvar
#Variabeln å berättar om personens ålder
s= 65 - å

#Variabeln s2 berättar om ålden subtraherat med pensions åldern så får vi när personen gick i pension. 
#Variabeln å berättar om personens ålder
s2= å - 65

#Här använder vi variabeln å som berättar personens ålder
#Om åldern är lika med 65år 
if å == 65:

#Så hamnar vi här
#Vilket talar om att personen redan har gått i pension 
#print används för en output
  print('\nDu har gått i pension!')

#Om åldern är lika med eller över 66 så har  
#Personen redan gått i pension eftersom pensionsåldern är 65.
#Variabeln å berättar om personens ålder
elif å>= 66:

#vi hammnar här om åldern är över 66
#print för en output
#Här talar koden om personens namn med variablerna f, e
#Variablerna f är input för förnamn
#Variabeln e är input för efternamn
#Koden talar om att personen redan har gått i pension av följande anledning: s2= å - 65
  print('\nOj', f,e,'!','Du gick i pension för', s2, 'år sedan.')

#Variabeln å talar om personens ålder
#Om åldern är under 64 år
if å<64: 
  
#Så hamnar vi här:
#Här talar koden om personens namn med variablerna f, e
#Variablerna f är input för förnamn
#Variabeln e är input för efternamn
#talar om hur många år personen har kvar tills pension av följande anledning: s= 65 - å
  print('Hej', f, e,'!','Det är nu', s, 'år kvar tils du går i pension')

#Variabel 'ö'(är en input om man vill ha ökad pension)
#Om åldern är lägre en 64 så frågar man användaren om den vill öka pensionen
#input för att personen ska kunna skriva sitt svar
#\n används för att hoppa över en rad
  ö = input('\nVill du att vi ökar din pension?(j/n) ') 

#Om svaret på frågan är 'Ja' skriver användaren j som vi har beteckat med variabeln b.
  if ö== b:

#Svarar man j så hamnar vi här:
#Här frågas användaren hur många år man vill ökar sin pension med.
#För att det är siffror så skriver vi integer som representerar heltal.
#input sätts in för att användaren ska kunna svara
#variabel sätts som m för att sedan kunna hänvisa till dena kod.
# m är input för att antal år man vill öka sin pension
    m = int(input('\nHur många år vill du öka din pension? '))

#variabeln s3 talar om att om pensionsåldern som är 65 subtraheras med åldern, samt adderat med  antal år man vill öka sin pension så fär man fram pensionen efter ökning som är kvar.
    s3= 65 - å + m

#Här berättar koden användarens pension efter ökning.
#Print för en output
#Här talar koden om personens namn med variablerna f, e
#talar om hur många år personen har kvar, efter ökning tills pension av följande anledning: s3= 65 - å + m
    print('\nKlart!', f,e,'!','Du har nu', s3, 'år kvar tills du går i pension!')

#Kvitto med variabeln s3
#Kvittot talar om personens hela namn, ålder och hur många år kvar efter ökningen av pension
#\n talar om att hoppa över en rad
#\t talar om att hoppa in längre ut på raden
    print('\n\t\t\tKvitto')

    print('           .........')
#start på kvittot (print används därför)
    print('\n+------------------------------+')

    print('|                              |')

#Här anväder vi en variabel som heter rubrik
#kvittots rubrik är pension status
# variabeln sätts till rubrik som skriver ut en rubrik
    rubrik = 'Pension status'

#Vi använder x som en variabel som är input för att få en rubrik i mitten.
#rubriken anger vi nu i mitten 
#Rubriken sätts nu i mitten genom datatypen center och nummer 26 för hur långt in på raden texten ska vara på.
    x = rubrik.center(26)

#Print används för att få en output 
#Denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida.
#Koden talar om att varabeln x ska skrivas ut här.
#Variabeln x är input för att rubriken ska finnas i mitten. 
#i koden ska rubriken finnas vilket är angivet med x och hur mycket sträcket ska hoppa ut i raden betecknas såhär:{:>2}
#Format används för att konvertera '|' till en sträng.
    print("|", x, " {:>2}" .format ('|'))

#Här använder vi en variabel som heter förnamn
#Variabeln tallar om att på denna rad så ska det finas en underrubrik som heter 'förnamn'.
#Samt str vilket svaret från användaren läggs in här 
#str läggs in för att variabeln f som innehåler siffror ska kunna konverteras till en sträng.
#Variabeln f är input för personens förnamn.
    förnamn = "Förnamn: " + str(f)

#Print används för att få en output 
#Denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida på kvittot.
#i koden ska förnamnet finnas vilket är angivet med förnamn som ska skrivas ut på denna rad och hur mycket sträcket ska hoppa ut i raden vilket  betecknas såhär:{:>17}
    print("|  ",förnamn, "{:>14}" .format ('|'))

#Vi använder variabeln som heter efternamn
#Variabeln talar om att i denna rad så ska det finnas en underrubik som heter 'Efternamn:' 
#Samt str vilket svaret från användaren läggs in här 
#str läggs in för att konvertera e till en sträng
#variabel e är input för personens efternamn.

    efternamn = "Efternamn: " + str(e)

#Print används för att få en output 
#Denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida.
#Koden talar om att variabeln efternamn skrivs ut på denna rad.
# Samt hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>16}
#Format används för att konvertera '|' till en sträng.
    print("|  ", efternamn, "{:>11}" .format ('|'))

#Vi använder en variabel som heter ålder
#Koden talar om att underubriken för denna rad är 'Ålder:'
#Samt att str(å) konverteras till en sträng.
#variabel å är input för personens ålder
    ålder = 'Ålder: ' + str(å)

#Print används för att få en output 
#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida på kvittot.
#Koden talar om att variabeln ålder skrivs ut på denna rad.
#Samt hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>17}
    print("|  ", ålder,'år', "{:>15}" .format ('|'))
    
#Användarens pensionstid skrivs här 
#Variabeln talar om att underrubriken ska vara "pension" på denna rad och str ska konvertera variabeln s3 (om hur många år kvar av pensionen) som hänvisar till sifror, vilket konverteras till en sträng.
    pension = 'Pension: ' + str(s3)

#print för en output
#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida på kvittot.
#Koden talar om att variabeln pension ska skrivas ut på denna rad
#Samt hur mycket sträcket ska hoppa ut i raden betecknas såhär:{:>9}
    print("|  ",pension, 'år kvar', '{:>8}' .format ('|'))

#sträck på var sin sida
    print('|                              |')

    print('|                              |')

#Ny variabel som heter 'text' som ger output välkommen åter på sista raden.
    text = 'Välkommen åter!'

# variabel r som anger att texten ska vara i mitten på kvittot
#med avstånd 26
    r = text.center(26)

#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida på kvitot.
#Variabeln r ska finnas på denna rad med avståndet {:>3}
#Format används för att göra om '|' till en sträng.
    print("|", r, "{:>3}" .format ("|"))

#Slutet av kvitot
    print('+------------------------------+')

#print för en output
#Koden skriver ut en rad som visar slutet på programmet
#\n betecknar hur många rader den ska hoppa över
    print('\n\n            Tack för att du har användt den här tjänsten!')

#Däremot om svaret är nej på frågan som har variabeln m så kommer vi hit
#ö är lika med n som är betecknat med z,vilket är förkortningen för nej.
# Variabeln ö är inputen för frågan om att öka sin pension
  if ö>= z:

#Svar n som är hänvisat med variabeln Z, som menas Nej så hamnar vi här.
#Yttligare en fråga
#Här frågas användaren om den vill sänka sin pension.
#input sätts in för att användaren ska kunna svara
#variabel h används för inputen för att sänka sin pension
#\n används för att hoppa över en rad.
    h = input('\nVill du att vi sänker din pension?(j/n) ')

#Om svaret är Ja om den vill sänka sin pension hamnar vi här 
#h är lika med j som är betecknat med b
#Variabeln h hänvisar på frågan om man vill sänka sin pension.
    if h<=b:

#Om svaret är ja på frågan som är hänvisat med variabel h så hamnar vi här.
#Här frågas användaren sedan om antal år den vill sänka sin pension.
#För att det är siffror så skriver vi integer som representerar heltal.
#input sätts in för att användaren ska kunna svara
#variabel t används för inputen för sänkning av pension
#\n talar om att hoppa över en rad
      t = int(input('\nHur många år vill du sänka din pension? '))

#Här använder vi en variabel som heter k
#Variabeln k talar om att om pensionsåldern subtraheras med personens ålder samt antal år den vill sänka sin pension med så får vi antal år kvar tills pension efter sänkning
      k= (65 - å - t )

#Print används för output
#Koden berättar andvändarens pension efter sänkning
#kvittot ska ha 2 sträck: | på vardera sida.
#Här talar koden om personens namn med variablerna f, e
# f betecknar för användarens förnamn
# e betecknar för användarens efternamn
#k betecknar antal år kvar
      print('\nKlart!', f,e,'!','Du har nu', k, 'år kvar tills du går i pension!')

#Print används för output
#\n talar om att hoppa över en rad
#\t talar om att hoppa in längre ut på raden
#kvitto är rubriken 
      print('\n\t\t\tKvitto')

      print('           .........')

      print('\n+------------------------------+')

      print('|                              |')

#Variabeln sätts till rubrik som skriver ut en rubrik
#Kvittots rubrik är pension status
      rubrik = 'Pension status'

#Här använder vi en variabel som är x.
#Variabeln x är input för att variabel rubrik ska centreras.
#Rubriken sätts nu i mitten genom datatypen center med avstånd 26 för hur långt in på raden texten ska vara på.
      x = rubrik.center(26)

#Print använd för att få en output 
#Denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida av kvittot.
#Koden talar om att när denna kod skrivs ut här så ska allt som variabeln x hänvisar skrivs på denna rad.
#variabeln X ska finnas här som är input för att rubrik variabeln som hänvisar till en rubrik ska vara i mitten på kvittot.
#Här talar koden också om hur mycket sträcket ska hoppa ut i raden betecknas såhär:{:>2}
#Format används för att göra om '|' til en sträng.
      print("|", x, " {:>2}" .format ('|'))

#Kvittot med raden angivit med förnamn
#Här använder vi variabeln förnamn
#variabeln talar om att när den skrvs ut så ska en underrubrik finnas på den raden som heter 'Förnamn:'
#Samt str vilket svaret från användaren läggs in här 
#str läggs in för att konvertera f (som hänvisar till siffror) till en sträng.
#Variabeln f är input för användarens förnamn.
      förnamn = "Förnamn: " + str(f)

#Print används för att få en output 
#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida.
#Koden talar om att när den skrivs ut så ska allt i variabeln förnamn skrivas ut på kvitot i denna rad.
#samt hur mycket sträcket ska hoppa ut i raden vilket vi  betecknar såhär:{:>17}
#Format används för att göra '|' till en sträng 

      print("|  ",förnamn, "{:>14}" .format ('|'))

#Här använder vi variabeln efternamnet
#Variabeln talar om att när koden skrivs ut så ska det finnas en underrubrik i kvittot som heter 'efternamn', samt en str som konverterar variabeln e till en sträng.
#Samt str vilket svaret från användaren läggs in här 
#Variabeln e är input för användarens efternamn.

      efternamn = "Efternamn: " + str(e)

#Print används för att få en output 
#Denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida.
#Här talar koden om att i outputen så ska variabeln efternamn skkrivas ut.
#Samt berättar koden också för programmet om hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>16}
      print("|  ", efternamn, "{:>11}" .format ('|'))

#Här använder vi variabeln ålder.
#Koden talar om att variabeln ålder är input för underrubriken Ålder samt str som kommer konvertera variabeln å till en sträng då varabeln å hänvisar till siffror
#ariabeln å är nputen för användarens ålder.
      ålder = 'Ålder: ' + str(å)
  
#Print används för att få en output 
#denna kod berättar att kvittot ska ha 2 sträck: | på ardera sida.
#Vi använder variabeln ålder som hänvisar till detta: ålder = 'Ålder: ' + str(å)
#i koden ska åldern finnas vilket är angivet med ålder och hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>17}
      print("|  ", ålder,'år', "{:>15}" .format ('|'))

#Här använder vi variabeln d som är input för antal år kvar av pensionen efter sänkning av pensionen.
#Koden talar om att pensionsåldern subtraherat med personens ålder samt subbrtaherat med t vilket är variabel som hänvisar till antal år man vill sänka sin pension, så får man antal pension man har kvar efter sänkning.

      d = 65 - å - t
  
#Här använder vi variabeln pension
#Variabeln är en input på användarens pensionstid som är kvar.
#koden talar om att underrubriken ska vara pension och att det ska finnas en str som gör om variabelb d till en sträng då varabeln d innehåller siffror.
#Variabeln d är input för hur många år det är kvar tills pensionen.
      pension = 'Pension: ' + str(d)

#Print används för en output
#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida av kvittot.
#Koden talar om att variabeln pension ska skrivas ut här som hänvisar till detta: pension = 'Pension: ' + str(d). 
#Här ska det också finnas hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>9}
#Format används för att göra '|' till en sträng.
      print("|  ",pension, 'år kvar', '{:>8}' .format ('|'))

#sträck på vardera sida
      print('|                              |')

      print('|                              |')

#Ny variabel som är 'text' som ger output välkommen åter på sista raden på kvitot.
      text = 'Välkommen åter!'

# variabel r använder vi här som anger att texten ska vara i mitten på kvittot med avstånd 26
      r = text.center(26)

#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida.
#Variabeln r används här som är input för en text ska vara i mitten.
#Här ska sträcken ha avstånd {:>3}
      print("|", r, "{:>3}" .format ("|"))

#Slutet av kvitot
      print('+------------------------------+')

#Print används för en output
#Här skriver koden ut en rad som visar slutet på programmet
#\n betecknar hur många rader den ska hoppa över
      print('\n\n            Tack för att du har användt den här tjänsten!')

#Här använder vi variabeln h vilket är inputen för frågan om man vill sänka sin pension.
#Om svaret på frågan är nej, som vi hänvisar med variabel z
    if h >=z:

#så hamnar vi här med bara ett kvitto
#\n talar om att hoppa över en rad
#\t talar om att hoppa in längre ut på raden
#print använder vi för en output.
     print('\n\t\t\tKvitto')

     print('           .........')

     print('\n+------------------------------+')

     print('|                              |')

#Vi använder oss av variabeln rubrik för denna kod
#kvittots rubrik är pension status
#variabeln sätts till rubrik som skriver ut en rubrik
     rubrik = 'Pension status'

#Rubriken sätts nu i mitten genom datatypen center med avstådet 26 för hur långt in på raden texten ska vara på.
#Här använder vi variabeln x för att hänvisa denna kod.
#Variaeln rubrik hänvisar till rubriken som vi vill ha på kvittot.
     x = rubrik.center(26)

#Print används för att få en output 
#Här talar koden om att kvittot ska ha 2 sträck: |.
#i koden ska rubriken finnas med vilket är angivet med variabeln x och hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>2}
#Format används för att convertera '|' till en sträng.
     print("|", x, " {:>2}".format ('|'))

#Här använder vi en variabel som heter 'förnamn'
#variabeln betecknat med förnamn hänvisar till att underrubriken på denna rad kommer vara 'förnamn:'
#Samt str vilket svaret från användaren läggs in här 
#Här hänvisar den också till str som converterar f variabeln till en sträng. 
#Variabeln f hänvisar till personens förnamn
#str läggs in för att det är en text och inga siffror
     förnamn = "Förnamn: " + str(f)

#Print använd för att få en output 
#Denna kod berättar kvittot att det ska finnas 2 sträck: |som finns vardera sida av kvittot.
#i koden finns det en variabel som heter förnamn som hänvisar till detta: förnamn = "Förnamn: " + str(f) samt talar koden också om hur mycket sträcket ska hoppa ut i raden betecknas vlket betecknas såhär:{:>17}

     print("|  ",förnamn, "{:>14}" .format ('|'))

#Här använder vi variabeln efternamn.
#Variabeln tallar om att det ska finnas en underrubrik som heter 'efternamn:'. Samt en str som converterar variabeln e till en sträng.
#Variabeln e hänvisar till personens efternamn.
#variabeln betecknat med efternamn och hur outputen blir
#Samt str vilket svaret från användaren läggs in här 
#str läggs in för att det är en text och inga siffror

     efternamn = "Efternamn: " + str(e)

#Print använd för att få en output 
#Denna kod berättar om att kvittot ska ha 2 sträck: |, på vardera sida av kvittot.
#I koden hänvisar man till variabeln efternamn vilket hänvisar till personens efternamn. 
#Sedan talar koden också om hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>16}
#Format används för att '|' ska bli till en sträng
     print("|  ", efternamn, "{:>11}" .format ('|'))

#Här använder vi en variabel som vi kallar för 'ålder'
#Koden talar om att på nästa rad av kvitot så ska det finnas en underrubrik som är 'ålder:' samt en str som hänvisar till variabeln å, vilket variabeln å hänvisar till personens ålder.
#str gör om å variabeln som inehåller siffror till en sträng
#raden efter talar om åldern och åldern som användaren skrev in vilket vi anger med str och variabeln å
     ålder = 'Ålder: ' + str(å)

#Print används för att få en output 
#denna kod berättar att kvittot ska ha 2 sträck: | på vardera sida på kvittot.
#i koden ska åldern finnas vilket är angivet med variabeln 'ålder'.
#Koden tala också om hur mycket sträcket('|') ska hoppa ut i raden betecknas såhär:{:>17}
#Format används för att '|' ska bli en sträng
     print("|  ", ålder,'år', "{:>15}" .format ('|'))

#Variabeln i denna kod är 'pension'
#Variabeln 'pension'är input för hur många år det är kvar tills pension.
#Användarens pensionstid skrivs in i nästa rad och koden talar om att underrubrik ska vara pension och str ska hänvisa till variabeln s som länkar på hur många år det är kvar av pensionen.
#Vi använder str för att konvertera värden (siffror) till en sträng så att de kan kombineras med andra strängar, vilket menas att de kan kombineras med andra texter.
#Därfö sätter vi s i str för att variabeln s hänvisar till sifror.

     pension = 'Pension: ' + str(s)

#Här berättar koden om att i kvittot ska det finnas 2 sträck: | på vardera sida.
#i koden ska antal år kvar av pension finnas vilket är angivet med pension och hur mycket sträcket ska hoppa ut i raden vilket betecknas såhär:{:>9}
#Format används för att '|' ska bli en sträng
     print("|  ",pension, 'år kvar', '{:>8}' .format ('|'))

#sträck på var sin sida av kvittot
#Print används för output
     print('|                              |')

     print('|                              |')

#Ny variabel 'text' som ger output välkommen åter på sista raden på kvittot.
     text = 'Välkommen åter!'

# variabel r används här, som anger att texten ska vara i mitten på kvittot
#med avstånd 26
     r = text.center(26)

#print används här för att få en output.
#Format används för att '|'ska bli en sträng
#I den här koden berättar det för programmet att kvittot  ska ha 2 sträck: | på sidorna av kvittot.
#Variabeln r fins i denna rad för att kunna hänvisa till att texten ska vara i mitten i denna rad där sträcken ska ha avstånd {:>3} på den radet.
     print("|", r, "{:>3}" .format ("|"))

#Slutet på kvittot
     print('+------------------------------+')

#Koden skriver ut en rad som visar ett slut meddelande på programmet
#\n betecknar hur många rader den ska hoppa över
#print används för att något ska kunna skrivas ut (output)
     print('\n\n            Tack för att du har användt den här tjänsten!')