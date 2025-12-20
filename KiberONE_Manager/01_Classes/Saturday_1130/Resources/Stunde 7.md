Stunde 7 **  
**Plan:   
1) Das Programmieren der Animation; **  
**2) Die Befehlssteuerung von echten Robotern. **  
**

1) Das Programmieren der Animation. **  
**Wir erstellen mehrere Bilder und nennen sie p1, p2, …   
Bemerkung: **Wenn sich das neue Bild in der Animation vom vorherigen nicht wesentlich unterscheidet (z. B. die Animation einer Person, die mit der Hand winkt, oder die Animation einer Flagge, die im Wind weht – ein kleiner Teil des Bildes bewegt sich), empfehle ich, in der Konsole den Befehl **«copy p1 p2» **zu schreiben (wo 1 – das gerade gezeichnete Bild, 2 – das nächste Bild, das wir zu zeichnen planen). **  
Das heißt, wir kopieren das vorherige Bild und nennen es ein neues. Dann bearbeiten wir das neue Bild oder verwandeln p2 in das gewünschte.   
Wir schreiben solches Programm: 

  

Man muss erklären, was die for-Schliefe ist und wie sie die Variable x verwendet. 

while true do … end   
– eine endlose Schleife, das heißt, wir erstellen eine endlose Animation. Andere Befehle paintutils kann man finden, indem man in der Konsole help paintutils schreibt. Die Befehlsnamen sprechen für sich selbst (alle Befehle außer paintutils.loadImage zeichnen etwas auf dem Computerbildschirm). Insbesondere über zwei im Programm verwendeten Befehle: der erste Befehl lädt in die Variable a ein Bild mit der Adresse “p”..x im Computer. Der zweite Befehl zeichnet ein Bild aus der Variablen a, beginnend mit dem Pixel mit der Koordinate (1, 1), das heißt, aus der oberen linken Ecke des Computers. “p”..x bedeutet, den Wagen x in die Zeile “p” zu entladen, das heißt, bei der ersten Iteration des Zyklus erhalten wir “p1”, bei der zweiten “p2” und so weiter. 

term.clear() – der Befehl der Reinigung des Bildschirms.   
Wir erhalten eine sequentielle Änderung der Bilder p1, p2, ..., was eine Animation ist.   
Wir starten dieses Programm und verstehen, dass das Programm nicht so funktioniert, wie wir es brauchen. Vor der wiederholten Anzeige vom Bild p1 wird der Computerbildschirm nicht mit der schwarzen Farbe bedeckt. Es passiert, weil der Befehl term.clear() den Bildschirm nicht reinigt, sondern ihn mit der zuletzt verwendeten Farbe füllt. Wir ersetzen das Programm durch dieses Programm (vor der Reinigung des Bildschirms übermalen wir ein Pixel mit der schwarzen Farbe). 

  

Lassen Sie die Schüler Animationen erstellen und mit der Verzögerungszeit der Bilder in der Animation experimentieren. Man kann folgende Aufgabe geben: Ändert das Programm so, dass der schwarze Bildschirm nicht sichtbar ist, wenn die Animation ausgeführt wird. 

Die Aufgabe für die selbständige Arbeit. 

Wir zeichnen das Logo KIBERone, erstellen 5 Bilder, ändern abwechselnd die Farbe der Buchstaben und erstellen eine Animation auf einem großen Monitor. (Wir geben den Schülern die Monitore)   

**2) **Die Befehlssteuerung von echten Robotern 

Es ist Zeit, echte Roboterschildkröten zu erlernen. Das ist ein Computer mit den Werkzeugen und dem Inventar, der aufgetankt werden muss. Wir werden nur fortgeschrittene Schildkröten erlernen. 

  

Man muss zeigen, welche Schildkröten es gibt und was sie machen können (der Reihe nach: eine einfache Schildkröte ohne Werkzeug; eine Schildkröte mit einem drahtlosen Modem; eine Crafter-Schildkröte; eine Schildkröte mit einem Schwert; eine Schildkröte mit einer Schaufel; eine Schildkröte mit einem Pickel; eine Schildkröte mit einer Axt; Schildkröte mit einer Hacke).   
Wir werden wieder die Schildkröten mit den Pickeln erlernen. Um in den Befehlsmodus („Kontrollpult“) zu gelangen, muss man lua schreiben. 

  

Es ist überhaupt nicht diese Kontrollpult, die die grünen Schildkröten für Anfänger hatten. Um der Schildkröte einen Befehl zu geben, muss man ihn mit einem Text schreiben. Um zu sehen, welche Befehle man der Schildkröte geben kann, muss man in der Konsole help turtle schreiben (aber nicht aus dem Befehlsmodus – zuerst muss man den Befehl exit() eingeben).   
Um eine Schildkröte aufzutanken, muss man Kohle in den aktiven Slot legen und im Befehlsmodus turtle.refuel() schreiben. Wenn man keine Zahl in Klammern angibt, „frisst“ sie den gesamten Kraftstoff.   
**Bemerkung: **Ein Stapel Kohle reicht für eine Schildkröte für lange Zeit, auch bei harter Arbeit (zumindest für die gesamte Stunde). ****Wenn man die Schildkröte bricht, fällt Kohle heraus, für die sie keine Zeit hatte, um zu verwenden.   
Lassen Sie die Schüler die Schildkröten auftanken und sie im Befehlsmodus steuern.   

**Die zusätzliche Aufgabe.   
**1. Die Treppen mithilfe der Befehlsleiste der Schildkröte bauen. 

2. Ein Programm mithilfe einer Schleife modernisieren. 

3. Das Programm der Bewegung von der Schildkröte erstellen, das bestimmt, ob sich vor der Schildkröte ein Hindernis befindet, und wenn es gibt, nach rechts drehen.