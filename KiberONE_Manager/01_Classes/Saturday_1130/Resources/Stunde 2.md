Stunde 2. Das Schreiben eines Programms in einem visuellen Editor der Schildkröte. **  
**Plan:   
1) Das Schreiben der Programme in einem visuellen Editor. 

2) Die Repeat-Zyklen. 

3) Die Verwendung der Programme in den anderen Programmen. Die Prozeduren. 

4) Der Bau von Gebäuden (Schlösser, Wolkenkratzer). 

**1. Das Schreiben der Programme in einem visuellen Editor   
**Man muss daran erinnern, wie man einen Roboter im Team-Modus steuert, und dann erzählen, dass das Senden von Befehlen an die Schildkröte durch Schreiben eines Programms automatisiert werden kann.   

**Was ist ein Programm? **(Man muss den Schülern diese 3 Definitionen erklären)   
a) Der Ausführende ist ein Mensch oder ein automatisches Gerät, das Befehle oder Algorithmen ausführt.   
b) Der Algorithmus ist eine Reihe von den Aktionen, die in einer bestimmten Reihenfolge angeordnet sind.   
c) Das Programm ist ein Algorithmus, der in einer Sprache geschrieben ist, die ein Ausführender versteht.   

Auf diese Weise, um ein Programm zu schreiben, müssen wir einen Algorithmus erfinden und ihn dann in einer Sprache, die die Schildkröte versteht, für sie schreiben.   
Dann muss man erzählen, dass unsere Schildkröte eine verständliche Sprache hat. Sie liest den Programmcode Zeile für Zeile von links nach rechts. Wenn sich zwischen den Befehlen leere Quadrate befinden, führt die Schildkröte diese Befehle hintereinander aus, ohne zu warten. Das Programm kann man mit der rechten unteren Taste (ein Dreieck) Run Program im Abschnitt Programm oder im Bedienpult starten. Außerdem kann man im Programm Befehle schreiben, um zu graben und Blöcke über und unter der Schildkröte zu stellen. 

  

Weiter muss man den Schülern Freiheit geben – lassen Sie sie ein Gebäude oder einen Tunnel erfinden und ein Programm schreiben, das es realisiert. Die häufigsten ersten Programme: eine Treppe bauen; die Schildkröte hoch in die Luft heben; einen Tunnel aus den Spalten mit der Höhe 2 und Breite 1 bauen; eine Spalte aus Blöcken bauen. Man muss helfen, die Fehler in den Programmen der Schüler zu korrigieren. 

**Hinweis: **Nachdem das Programm ausgeführt wurde, wird in der unteren Zeile des Bedienpults von der Schildkröte das Symbol Undo Last Program angezeigt, das Ergebnis der Ausführung des vorherigen Programms rückgängig machen.   
Bald verstehen die Schüler, dass es schwierig und zeitaufwendig ist, ein Programm nach einer Aktion zu einer Zeit zu schreiben, und es ist die Zeit, über die Zyklen zu erzählen. Es wird empfohlen, es am Beispiel eines Programms von einem Schüler für das Graben eines Tunnels oder den Bau einer Spalte oder Treppe zu tun. Das heißt, um zu zeigen, dass das erste Programm dasselbe wie das zweite macht: 

  

Man muss erklären, dass es die Sprache ist, in der man für die Schildkröte schreiben muss, damit sie versteht, was wir von ihr wollen. Und jedes falsche Wort in dieser Konstruktion führt zu einem Fehler – die Schildkröte kann nicht das tun, was sie nicht versteht.   
Man muss auch erzählen, dass das Wort „rep“ eine Abkürzung für das Wort „repeat“ ist, das als „wiederholen“ übersetzt wird, „do“ wird als „machen“ übersetzt und „end“ ist „das Ende“.   

**2) Die Repeat-Zyklen.   
**Die Wiederholung eines Befehls kann ohne die Konstruktion repeat beschrieben werden, dieselben Befehle werden zu einem Befehl „geformt“: 

  

**Hinweis: **Statt nach jedem Wort aus der Zykluskonstruktion zu suchen, kann man ein Wort repeat verwenden. Statt nach einer Zahl, do und end zu suchen, kann man auf die roten Quadrate klicken und die erforderlichen Quadrate auswählen. ****

  

Weiter müssen die Schüler ihre Programme mithilfe einer Zykluskonstruktion vereinfachen.   
Lassen Sie sie dann etwas Komplexeres erstellen (ein wichtiger Hinweis für Schüler – die Zyklen können ineinander verschachtelt sein). 

**Die zusätzliche Aufgabe.   
**Die Konstruktion repeat wiederholen. 2-3 Programme mit der Verwendung des Zyklus repeat schreiben:   
1) Gräbt einen langen Tunnel mit der Höhe 2 und Breite 1;   
2) Baut eine hohe Treppe (mit vielen Stufen) mit der Breite 1;   
3) Baut eine hohe Treppe mit der Breite 4.   
„Langer“ Tunnel, „viele“ Stufen bedeutet, dass die Komplexität des Schreibens des Programms nicht von der Länge des Tunnels oder der Anzahl der Stufen abhängt, darauf wirken nur eine oder zwei Zahlen.   

**3) Die Verwendung der Programme in den anderen Programmen. Die Prozeduren.   
**Zuerst werden wir den Kindern beibringen, eine Box (4 Wände) eines einfachen Einraumhauses zu bauen. Wir werden das Haus mithilfe der Wand und die Wand mithilfe der Spalte bauen.   
**Hinweis 1: **Man kann Boxen nach „Schichten“ bauen, aber es ist sehr anschaulich, mithilfe der Spalte zu bauen. ****Auf diese Weise ist es einfacher, die prozedurale Programmierung zu lehren. ****  
**Hinweis 2: **Wir werden die Türen manuell brechen, nachdem wir die Box gebaut haben. ****

Das erste Programm besteht darin, eine Spalte mit der Höhe 4 zu bauen. Das ist die optimale Höhe, es wird nicht empfohlen, sie zu ändern (Damit die Schüler verstehen können: wir bauen „wie im Überleben“, springen und stellen einen Block vor uns). Wir nennen das Programm column, um die Programmlesbarkeit zu gewährleisten. 

  

Die Wand sind mehrere Spalten, die nebeneinanderstehen. Aber der Algorithmus ist nicht so einfach: man muss nicht nur mehrere Spalten wiederholen, sondern auch nach jeder Spalte viermal vorwärts und nach unten gehen. Da die Schildkröte Ressourcen aus einem Slot nimmt, in den nur 64 Blöcke hineinpassen, ist es besser, eine Wand aus nicht mehr als 64 Blöcken zu erstellen. Einige Zeit nehmen wir unten an, dass wir Wände mit einer Länge von 8 erstellen, d.h. wir werden 8*4=32 Blöcke für eine Wand ausgeben.   
Wir beschreiben den Algorithmus vom Bau der Wand auf dem Bildschirm (der Tafel) schematisch. Wir stellen vor, das Symbol Ὤ (ein Quadrat, in dem es noch ein Quadrat gibt) kennzeichnet den Bau einer Spalte. Um eine Wand zu bauen, muss man „das Symbol Ὤ, vorwärts gehen, viermal nach unten gehen, das Symbol, …“ machen. Oder kürzer: „8-mal wiederholen (Symbol Ὤ, vorwärts gehen, 4-mal nach unten gehen)“.   
Es ist sehr bequem! Und die Schildkröte kann auch das gesamte Programm in ein Symbol schreiben! (Man muss zeigen, wie man die Diskette des Programms „column“ im neuen Programm „wall“ verwendet).   
Dieses Symbol nennt man die Diskette. Eine Diskette ist ein Datenträger, den man verwenden kann, um die Daten zu schreiben und zu speichern. Ja, jetzt verwenden wir einen Flash-Speicher anstelle von Disketten.   
Jetzt ist das Programm „column“ ein Unterprogramm für das Programm „wall“. Anstelle des Worts „Unterprogramm“ verwendet man das Wort „Prozedur“. Prozeduren reduzieren die Größe des Programms, dadurch kann man das Programm schneller schreiben und die Leser verstehen es leichter. 

  

Lassen Sie die Schüler das Programm der Wand wiederholen und mit seiner Hilfe ihre ersten „Boxen“ von Räumen erstellen. Das heißt, man muss den folgenden Algorithmus viermal wiederholen ( **Hinweis **: die Schildkröte die ganze Zeit in eine Richtung drehen, da wir uns beim Umrunden des „rechteckigen“ Gebäudes immer in eine Richtung drehen):   
1) die Ressourcen in den 1. Slot des Inventars von der Schildkröte laden;   
2) das Programm wall ausführen;   
3) warten, bis sich die Schildkröte bewegt hat;   
4) die Schildkröte nach links oder rechts drehen.   

Die Häuser brauchen die Dächer. Die Programme des Daches ( **Wie man erklärt: **über das Programm string – die Zeile erzählen; zeigen, wie eine Iteration des Programms roof – das Dach funktioniert; erklären, warum das Repeat-Zyklus alles richtig fertig macht. Wofür brauchen wir nach dem Zyklus im Programm des Daches eine Diskette?): 

  

  

Die Länge der Zeile beträgt 9, nicht 8, da wir als Ergebnis eine Wand mit der Länge 9 und nicht 8 haben. Weil die erste Spalte der neuen Wand auch die Spalte der alten Wand ist.   
  
Im Programm des Daches ist 4 der ganze Teil der Hälfte von 9 (bei jeder Iteration werden noch 2 Zeilen erstellt). Um eine unnötige Zeile nicht zu löschen, ist es besser, eine Zeile zu Ende nicht zu erstellen, sondern die letzte neunte Zeile außerhalb des Zyklus zu schreiben. Die Schildkröte muss man von einem solchen Ort über dem Haus zu starten (durch den Block nach oben von einer solchen Ecke des Raums): 

  

Wenn wir einen Raum mit der Größe mxn gebaut haben (auf dem Screenshot: m ist die Länge der Wand entlang des Sehens der Schildkröte, n ist die Länge der Wand quer über der Schildkröte), dann hat die Box die Größe (m+1)x(n+1) und die Anzahl der Wiederholungen in den Programmen der Zeile und des Daches soll bzw. gleich m+1 und [(n+1)/2] sein. Und wenn n + 1 ungerade ist, muss man die letzte Diskette im Programm der Wand löschen.   
Lassen Sie die Schüler das Programm des Daches wiederholen und die Dächer für ihre Boxen bauen.   

**4) Der Bau der Gebäuden (Schlösser, Wolkenkratzer).   
**Das Minihaus ist fertig! Aber das Programm der Wand ist immer noch bei der Schildkröte gespeichert, wir können es noch einmal ausführen. Wir können mehrere Räume nebeneinander wiederholen, wir können ein großes Haus, ein Schloss oder sogar einen Wolkenkratzer bekommen! Aber für jeden neuen Raum muss man die Schildkröte viermal starten und das ist eine lange Zeit. Das Problem, auf das wir gestoßen sind, ist, dass sich nur 64 Blöcke in einem Slot des Inventars der Schildkröte befinden können und die Schildkröte nur Gegenstände aus dem ersten Slot nimmt. Aber man kann den aktiven Slot der Schildkröte ändern! Das kann so gemacht werden (select slot und number): 

  

Wir erhalten das folgende Programm des Raums (jede Diskette ist ein Programm „wall“; man kann eine Drehung am Ende des Programms der Wand hinzufügen): 

  

**Hinweis: **Mit diesem Programm wird die Schildkröte ihre Arbeit mit einem Fehler beenden, da die letzte Spalte mit der ersten identisch ist. Idealerweise muss man das Programm zum nächsten Programm ändern (noch im Programm wall 8 zu 7 ändern; die erste Diskette in jeder Reihe ist wall, die zweite Diskette ist column), aber dann wird es überladen. Eine andere Variante besteht darin, dass man im Programm wall anstelle des Abstiegs den Satz „Wenn du den Block unter dir nicht fühlst, gehe nach unten“ schreibt. Aber bedingte Konstruktionen sind ein Thema der anderen Stunde. Man kann versprechen, dass wir später lernen werden, diesen Fehler zu beheben. 

  

Jetzt, wenn wir gelernt haben, 4 Starts des Programms für einen Raum zu vermeiden, kann man die Anzahl der Spalten in der Wand auf 16 erhöhen (die Höhe der Wand beträgt 4, 16*4=64 – mehr als 16 Spalten im Raum sind zu viel), wenn ihr einen geräumigeren Raum wünscht.   
Lassen Sie die Schüler neben dem ersten Raum mehrere Räume bauen.   
**Hinweis: **die Programme können zwischen Figuren übertragen werden. Im Abschnitt „Program“ in der Schildkröte in der unteren Zeile befindet sich ein Symbol der Diskette mit einem Pfeil nach unten. Es bedeutet, dass man eine Diskette mit dem Programm nehmen muss. Diese Diskette kann man auf eine andere Figur übertragen (die Taste q – das Objekt wegwerfen, das sich in der Hand befindet). Um diese Diskette auf die Schildkröte zu übertragen, muss man sie essen (sie in die Hand nehmen und die rechte Maustaste gedrückt halten). Zusammen mit dem Programm werden die darin verwendeten Prozeduren, wenn es diese Programme gibt, auf die Schildkröte übertragen. Mit der Schaltfläche mit dem Symbol der Diskette mit einem Pfeil nach unten und dem Buchstaben „A“ kann man eine Diskette mit dem Programm an alle Spieler senden. Diese Funktion steht nur dem Lehrer zur Verfügung.   
**Die zusätzliche Aufgabe.   
**Den Bau der Box des Raums wiederholen. Mehrere Räume nebeneinander bauen, um ein großes Haus zu erstellen. Wenn es ein Wolkenkratzer ist, sollen sich die Räume in unterschiedlichen Höhen befinden. Wenn es ein Schloss ist, muss man einen Zaun um es herum errichten (der Algorithmus ist der gleiche wie beim Bau einer Wand). Wenn man einen „gezackten“ Zaun wünscht, muss man die Spalten mit der Höhen 4 und 5 abwechseln.