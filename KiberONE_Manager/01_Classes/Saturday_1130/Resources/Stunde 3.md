Stunde 3. Der Graben der Tunnel von der Schildkröte, die Gewinnung von Ressourcen. Die bedingten Konstruktionen. Die Zyklen. 

Plan:   
1) Die bedingten Konstruktionen. Die Verbesserung des Programms vom Graben der Tunnel.   
2) Die While-Schleifen. **  
  
**Die Gewinnung von Ressourcen. **  
**Die Schüler müssen sich daran erinnern, wie man einen Tunnel mit der Höhe von 2 und der Breite von 1 gräbt. Lassen Sie die Schüler dieses Programm selbständig schreiben. 

  

Aber der Tunnel ist niedrig. Wir werden den Schülern anbieten, das Programm selbständig so zu modifizieren, dass der Tunnel mit der Höhe von 3 ist. Wollen wir es beheben: 

  

Man muss den Schülern 10 Minuten Zeit geben, um mit diesem Programm die Tunnel zu graben, damit sie verstehen, dass sie ein besseres Programm wünschen.   
Die Aufgabe: 

Jetzt machen wir unsere Tunnel breiter. Stellen wir uns vor, dass jeder von uns nur eine Schildkröte hat und wir ihnen beibringen wollen, einen Tunnel mit der Höhe von 3 und der Breite von 3 zu graben. Wir werden den gesamten Tunnel entlang einer 3x3 Wand und jede Wand nach Spalten graben. Das Programm der Spalte (wir nennen es „column“) 

  

Mit diesem Programm gräbt die Schildkröte vor sich die Spalte mit der Höhe von 3 und steht an der Stelle ihrer Mitte. 

  

Die Schüler müssen versuchen, das zweite Programm, das Programm „wall“, selbständig zu schreiben, indem sie die Diskette des Programms der Spalte verwenden. Sie muss vor sich die 3х3 Wand von dieser Position graben: 

  

Man muss den Schülern etwa 30 Blöcke der Erde geben, damit sie die Wände vor den Schildkröten bauen und die Programme testen. Um die Schüler zu interessieren, organisieren wir den Rest der Stunde folgendermaßen: Die Schüler schreiben ein Programm des Grabens einer Wand, dann ein Programm des Grabens eines Tunnels, der Lehrer hilft mit den Fehlern und gibt die Hinweise. Jeden Schüler, der das Programm des Grabens eines Tunnels abgeschlossen hat, teleportiert der Lehrer unter die Erde um 8-10 Blöcke höher als Bedrock und gibt mehrere Stapel von Fackeln, eine Schildkröte und einen Pickel. (Wir schalten einfach den Modus vom Bau ein und graben manuell nach unten, dort bereiten wir den Platz für die Tunnel der Schüler vor). 

Die Schüler starten die Schildkröten, suchen nach Diamanten, Smaragden, Gold, rotem Staub, Lasurit. 

Für jeden gefundenen Fundort der oben genannten Ressourcen erhält der Schüler vom Lehrer bzw. 10, 5, 2, 1 oder 1 Diamant(en) zusätzlich. Über diese Bonusse muss man den Schülern vor dem Schreiben des Programms der Wand erzählen. Aber die Ressourcen müssen von der Schildkröte selbst ausgegraben werden oder an den Wänden des Tunnels sichtbar sein, sonst erhält der Schüler keinen Bonus. Am Ende der Stunde oder während der Stunde kann man die Ergebnisse der Schüler an die Tafel schreiben.   
Das Programm vom Graben der Wand: 

  

Aber nach dem Graben der Wand schaut die Schildkröte nicht in die Mitte der nächsten Wand. Um einen Tunnel zu graben, muss man eine Wand brechen, sich dann umdrehen, nach vorne gehen, nach links abbiegen, dann eine andere Wand brechen und so weiter. Um diese Aktionen zu automatisieren, fügen wir am Ende des Programms „nach rechts, nach rechts, nach vorne, nach links“ hinzu. Jetzt bricht die Schildkröte die Wand und sie ist bereit, eine nächste Wand zu brechen. 

  

Um einen langen Tunnel zu erstellen, muss man das Programm „wall“ in einen Zyklus platzieren. Es gibt zwei Möglichkeiten, es zu tun: den Programmcode mit einem Repeat-Zyklus umgeben oder ein neues Programm „tunnel“ erstellen und „repeat 99 do wall end“ schreiben.   
Während der Suche nach Ressourcen unter der Erde müssen die Schüler verstehen, dass Lava, Wasser, natürliche Höhlen und Kies die Hindernisse der Schildkröte mit diesem Programm sind. In der zweiten Hälfte der Stunde werden wir unser Programm verbessern, damit die Schildkröte nicht aufhört, wenn sie auf diese Schwierigkeiten stößt, und auch einen Tunnel von unendlicher Länge baut, nicht nur 99 Wände.   

Alle diese Programme müssen die Schüler selbständig zusammenstellen. Wenn es Schwierigkeiten gibt, besprechen wir sie zusammen. 

**Die zusätzliche Aufgabe.   
**Das Programm vom Graben des Tunnels mit der Höhe von 3 und der Breite von 3 wiederholen. 

Das Programm vom Graben eines quadratischen Tunnels mit einer Seitenlänge von 20, der Höhe von 3 und der Breite von 3 schreiben. 

Das Programm vom Graben eines Tunnels in Form eines Zickzacks mit einer Drehung nach rechts schreiben. ****

**Die bedingten Konstruktionen. Die Verbesserung des Programms vom Graben der Tunnel. **

Welche Wörter, die „detekt“ enthalten, wisst ihr? Richtig, ein Lügendetektor. Es gibt noch ein Wort. Genauer gesagt, ein Beruf. Ja, das stimmt, ein Detektiv. Sowohl der Detektiv als auch der Lügendetektor versuchen, etwas herauszufinden, zu erkennen. Entdecken. Das Wort detect wird aus dem Englischen als „erkennen“ übersetzt. Das Wort if bedeutet „wenn“ und das Wort then ist „dann“.   
Ihr erinnert euch daran, dass die Schildkröte einen Fehler ausgibt, wenn ihr sie bittet, einen Block vor sich zu brechen, obwohl es keinen Block davor gibt. Die bedingte Konstruktion, d.h. eine Konstruktion mit einer Bedingung, hilft uns, es zu vermeiden (der Name des Programms forw stammt vom Wort forward ab): 

  

Das heißt, wir haben ein Programm für die Schildkröte geschrieben: „Wenn du einen Block vor sich fühlst, dann gräbst, das Ende“.   
**Man muss an den Beispielen zeigen, **wie dieses Programm funktioniert – was passiert, wenn sich ein Block oder kein Block vor der Schildkröte befindet. Für die Anschaulichkeit kann man nach „end“ den Befehl „nach vorne gehen“ hinzufügen. Die Schildkröte wird in jedem Fall nach vorne gehen, wenn es sich ein unzerstörbarer Block oder ein Kiespfeiler vor ihr nicht befindet.   
Wir fügen am Ende des Programms „forw“ den Befehl „nach vorne gehen“ hinzu. Jetzt ersetzen wir in den Programmen column, wall und tunnel alle Befehle „nach vorne gehen“ (oder die Kombinationen von den Befehlen graben + nach vorne) auf die Diskette forw. Im Programm column ersetzen wir die Befehle „graben nach oben und unten“ bzw. auf die Konstruktionen „wenn du den Block oben fühlst, gräbst, das Ende“ und „wenn du den Block unten fühlst, gräbst, das Ende“. 

Wir haben unser Programm verbessert, jetzt hat die Schildkröte keine Angst vor Lava, Wasser und Leere.   
Man muss den Schülern 10-20 Minuten geben, um das Programm des Tunnels zu testen. Lassen Sie die Schüler erkennen, dass das letzte Problem mit dem Kies noch nicht gelöst ist. Fast alle Blöcke mit den Wörtern haben wir erlernt. 

For ist dieselbe Schleife wie repeat, aber mit der Verwendung der Variablen. Ihn und die Variablen werden wir bald auf einem anderen elektronischen Gerät erlernen. Und jetzt wollen wir erkunden, was das Wort „while“ bedeutet. 

  

Die While-Schleifen. **  
**Stellt ihr euch vor, ihr müsst die Straße überqueren, aber die Ampel leuchtet rot. Welchem ​​Algorithmus folgt ihr, wenn ihr die Straße ungefährlich überqueren wollt? Richtig, „ *solange *das rote Licht leuchtet, halt. Überquere dann die Straße“.   
Dieses Wort „ *solange *“ ist „while“. Noch ein Beispiel des Algorithmus mit dieser Konstruktion: „ *solange *du die Wand nicht fühlst, gehe nach vorne“.   
Der letzte Algorithmus kann man auch mit dem Programm für die Schildkröte beschreiben (das neue Wort – not – bedeutet „nicht“): 

  

Schauen wir uns Beispiele der Algorithmen mit dem Wort „solange“ an. Zum Beispiel, solange es 13 Uhr nachmittags nicht ist, erlernen wir Programmieren in Minecraft. Die folgenden Fragen richten an zwei verschiedene Schüler.   
Stell dir vor, du erhältst einen solchen Algorithmus und du musst Folgendes tun: „Solange 2x2=4, singe ein Lied“. Was wirst du tun? Richtig, du wirst immer das Lied singen. Da 2x2=4 immer ist.   
Und du erhältst den Algorithmus „solange 2+2=3, zeichne“. Was wirst du tun? Richtig, du wirst nie zeichnen, weil 2+2=4 und nicht 3. Und diese Gleichheit hängt nicht von der Zeit ab.   
Es bedeutet, dass man ein Programm mit der Konstruktion „solange (etwas Wahres), mache ..., das Ende“ schreiben muss, damit die Schildkröte unendlich arbeitet. Anstelle von (etwas Wahrem) kann man eine beliebige Phrase verwenden, auch nur das Wort „Wahr“ („Wahrheit“). Auf Englisch wird dieses Wort als „true“ übersetzt.   
Wir schreiben ein Programm, das wir ausführen, und die Schildkröte geht ohne Pickel endlos (das Graben von Blöcken ist verboten).   
Ein bisschen früher haben wir der Schildkröte beigebracht, nach vorne zum ersten Hindernis zu gehen. Wir sagen der Schildkröte, dass sie die folgenden Aktionen endlos wiederholen soll: Gehe nach vorne zum Hindernis; biege rechts ab. 

Wir bekommen das Programm: 

  

Jetzt verbessern wir das Programm vom Graben des Tunnels. Das letzte Problem ist Kies. Wie geht man durch einen Kiespfeiler? Man muss den Block vor sich selbst brechen, solange er dort ist! Das heißt, anstelle des alten Programms vom Durchgang nach vorne muss man Folgendes schreiben: „Solange du den Block fühlst, brich ihn, das Ende. Gehe nach vorne“: 

  

Damit die Schüler verstehen können, ich empfehle zu zeigen, wie eine Schildkröte mithilfe dieses Programms mit einem riesigen Kiespfeiler umgeht. Zum Beispiel, man kann mit dem Füllwerkzeug auf der vorletzten Registerkarte des Lehrermenüs ein großes Parallelepiped aus Kies erstellen, die Schildkröte in der Nähe seines Fundamentes platzieren und das Programm starten: 

  

Die zusätzliche Aufgabe. (Der Lehrer bereitet im Voraus unweit des Lagers einen offenen Platz vor und erstellt ein Steinkissen mit der Höhe von 10 Blöcken, verteilt Blöcke der Steine und Fackeln an die Schüler) **  
**Das verbesserte Programm vom Graben des Tunnels wiederholen. 

Ein Haus mit 2 Etagen und einen Keller mit einer Treppe mit der Verwendung von der Schildkröte bauen