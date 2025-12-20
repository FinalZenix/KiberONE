*******Stunde 6. *****  
*****Plan: ***

***Teil 1. ***  
***1) Die Übertragung elektronischer Signale in Minecraft mit rotem Staub; *****  
*****2) Das Programm für die Autorisierung des Eigentümers des Hauses, seine Verbesserung. *****  
******

***Teil 2. ***

**1) Die Installation eines elektronischen Schlosses an eigener Haustür;   
2) Paint;   
3) Drucker;   
4) Monitore;   
5) Taschencomputer. ******

  

***Teil 1. ***

***1) Die Übertragung elektronischer Signale in Minecraft mit rotem Staub. *****  
*****Zeigen Sie, wie man ein elektronisches Signal mithilfe des Computers übertragen kann: ***

  

Der erste Parameter der Funktion ist eine Seite, an die man das Signal geben muss (left, right, top, back).   
Der zweite Parameter ist true oder false. true bedeutet „das Signal geben“, false ist für „die Signalgabe beenden“.   
Der nützliche Befehl ist sleep. sleep(a) lässt dem Computer „schlafen“, das heißt, während a Sekunden warten.   
Die Signalgabe nach links: 

  

Man kann links eine Lampe oder eine Tür daneben stellen, das Programm wird auch funktionieren.   
Erinnern Sie daran, was while ist, wie man einen endlosen Zyklus erstellt. Schreibt das Programm und platziert so die Lampen: 

  

  

Die Schüler können dieses Programm nicht wiederholen (Das ist eine Erinnerung an die while-Schleife und eine Demonstration der Möglichkeiten der Signalgabe). 

  
**Bemerkung: **die Ausführung desjenigen Programms (insbesondere Programme mit einer endlosen Schleife) kann man mithilfe der Tastenkombination Ctrl+t (man muss ca. 2-3 Sekunden halten, wenn ihr euch in der Konsole befindet) aufhören. Ich empfehle Ihnen nicht, in diesem Moment darüber den Schülern zu erzählen. 

  
**2) *****Das Programm für die Autorisierung des Eigentümers des Hauses, seine Verbesserung. *****  
**Jetzt schreiben wir das Programm der Überprüfung des Benutzerpassworts. Man muss jede Zeile des Programms erklären.   
**Bemerkung: **Man kann ein Programm der Überprüfung eines Log-ins mit einem Passwort schreiben. Ich empfehle Ihnen, diese Variante des Programms zu schreiben. 

  

Anstelle der Auslassungspunkte schreiben wir das, was wir wollen.   
Wenn ihr genug Zeit haben, kann man anstelle der Auslassungspunkte shell.run(“worm”) schreiben. Bitten Sie die Schüler, das Programm auf ihren Laptops zu wiederholen, zu speichern, die Fehler zu beheben und auszuführen. Und veranstalten Sie ein kleines Schlangen-Turnier. 

  
**Bemerkung: **Die Schlange kann man auch in der Konsole mit dem Befehl worm starten. Der Befehl shell.run lässt ein anderes Programm aus diesem Programm starten, es kann nützlich sein.   
Jetzt zur Sache – zur Öffnung der Tür. Stellt die Tür links vom Computer (rechts ist alles analogisch). Wir öffnen die Tür und schließen sie nach 5 Sekunden: 

  

Das Programm funktioniert, aber ich möchte, dass es besser wird. Unten gibt es mehrere Screenshots der Verbesserungsschritte. Man muss den Schülern jeden Verbesserungsschritt zeigen und begründen, wofür wir ihn brauchen. Die Schüler müssen das Programm verbessern, nachdem der Lehrer alle Verbesserungen gezeigt hat.   
1) Wir platzieren das Programm (ohne erste Zeile, begründen Sie, warum ohne diese Zeile) in eine endlose Schleife. Wenn das richtige Passwort eingegeben wurde und die Tür nach der Öffnung geschlossen wurde, „brechen“ wir die Schleife und beenden das Programm. 

  

2) Wir bitten um die Eingabe eines Passworts: 

  

3) Bei der Eingabe eines Passworts werden die Zeichen mit Sternchen versehen, damit andere Leute nicht sehen, was der Benutzer in den Computer eingibt (sie konnten das Passwort nicht sehen): 

  

  

**Die zusätzliche Aufgabe.   
**Kompliziert das Programm der Autorisierung für das Betreten des Hauses, damit das Programm zuerst den Namen des Eigentümers anfordert und, wenn der Name richtig ist, die Eingabe eines Passworts bietet. 

  

**Teil 2. **  
**  
1) Die Installation eines elektronischen Schlosses an eigener Haustür.   
**Jetzt werden wir die Türen zu unseren Häusern blockieren (der Lehrer muss diese Türen durch eiserne Türen ersetzen). Zu diesem Zweck stellt der Lehrer direkt neben dem Computer jedes Schülers ein CD-Laufwerk und gibt jeden Schüler eine Diskette: 

  

Die Schüler legen die Disketten in das Laufwerk. Dann können die Neugierigen den Befehl dir in die Konsole schreiben und den neuen Ordner disk sehen. Das ist kein Ordner, sondern eine Diskette – ein externes Speichermedium.   
Dorthin werden wir unser Programm übertragen, um es auf den Computer an der Haustür herunterzuladen. Man kann es mithilfe des Befehls «copy __ disk/__» machen, wo an der ersten fehlenden Stelle der Name des Programms mit der Autorisierung des Eigentümers stehen soll, und an der zweiten fehlenden Stelle der neue Name desselben Programms stehen soll. Das Programm wird auf die Disk kopiert. 

  

Weiter übertragen wir die Diskette mit dem Laufwerk zum Computer an der Tür, stellen das Laufwerk direkt neben den Computer und legen die Diskette in das Laufwerk. Wir schreiben «copy disk/__ startup» im Computer, wo anstelle der Lücke der neue Name des Programms geschrieben wird, der beim Kopieren des Programms vom vorherigen Computer eingestellt wurde. Das Programm wurde in startup umbenannt, sodass das Programm sofort beim Starten des Computers gestartet wird.   
Lassen Sie die Schüler das Programm an einem Computer mit einer Haustür testen.   
Jetzt muss man den Schülern erklären, dass der Computer immer hinter sich ausgeschaltet werden muss (gewöhnlich gibt es einen Schüler, der sein Haus betritt, sein korrektes Passwort in den Computer eingibt, aber ihn nicht ausschaltet. In diesem Fall bleibt der Computer entsperrt. Jeder kann edit startup in der Konsole schreiben, das Passwort für das Haus sehen oder sogar es ändern).   

**2) Paint.   
**In den Computern in Minecraft kann man nicht nur Textdateien und Programme, sondern auch Bilder erstellen. Dafür muss man in der Konsole den Befehl «paint __» schreiben, wo an der Stelle der Lücke der Name der Datei „Bilder“ geschrieben werden soll. Dieser Befehl erstellt und/oder öffnet für die Bearbeitung im Programm paint die Datei mit dem im Befehl geschriebenen Namen. Paint lässt die Rasterbilder zeichnen, das heißt, die Bilder nach Pixeln zeichnen.   
Man muss zeigen, wie man Bilder zeichnet – man kann die Farbe auswählen, nicht nur mit der linken, sondern auch mit der rechten Maustaste zeichnen, auf der man auch die Farbe einstellen kann. Man muss auch zeigen, dass schwarze und leere Pixel unterschiedliche Pixel sind. Nach der Bearbeitung muss man die Bilder unbedingt speichern, wie die anderen Dateien (Ctrl – Save).   
Man muss den Schülern Zeit geben, in Paint zu zeichnen. Der Lehrer zeichnet in der Datei picture. Jetzt muss man in der Konsole edit picture (nicht paint picture) schreiben. Anstelle eines farbigen Bildes sehen wir eine Reihe von Symbolen auf dem Bildschirm. Auf diese Weise werden die Farben der Pixel in einem Computer codiert. 

**Aufgabe: **Wir zeichnen das Logo KIBERone in diesem Editor. 

***3) Drucker. *****  
*****Jetzt muss man über einen Drucker erzählen. ***

  

  

Man muss den Drucker neben dem Computer stellen. Man muss im Drucker in die obere Zeile leere Blätter Papier (paper im Inventar) und links irgendeinen legen.   
Wenn ihr jetzt in den Textdateien und Programmen auf dem Computer die Ctrl-Taste drückt, wird ein neuer Befehl Print angezeigt. Er lässt diese Datei auf Papier mit einem Drucker drucken. Man muss zeigen, wie der Drucker eine Datei auf ein leeres Blatt druckt. Legt dann einen anderen Farbstoff in den Drucker, schreibt eine andere Textdatei und druckt sie auf dem Blatt Papier, das wir gerade verwendet haben. Einige Symbole werden durch neue ersetzt.   

**Bemerkung: **in den Bildern des Computers gibt es keine Funktion des Druckes auf dem Drucker. Diese Funktion ist von den Entwicklern nicht vorgesehen, da nur ein Farbstoff in den Drucker gelegt werden kann, aber die Bilder enthalten normalerweise mindestens zwei Farben. 

**Aufgabe: **die Anweisung drucken, wie man einen Computer beim Betreten Ihres Hauses verwenden kann. 

***4) Monitore. *****  
*****Es ist Zeit, über den Monitor zu erzählen. Wir werden Advanced Monitor verwenden. ***

  

Monitore können miteinander verbunden werden (wenn ihr zwei Monitore nebeneinander platziert, werden sie ein einheitlicher Doppelmonitor). Der maximale Monitor, den man erstellen kann, ist 8x6, das heißt, 8 in der Länge und 6 in der Höhe. Damit der Monitor funktioniert, kann man direkt neben ihm einen Computer platzieren. 

  

Um etwas auf dem Monitor anzuzeigen, muss man den Befehl «monitor __ __» in der Konsole schreiben, wo anstelle der ersten Lücke die Seite geschrieben werden muss, an die man ein Signal geben muss, (die Seite, auf der sich der Monitor befindet – right, left, back, top) und dann anstelle der zweiten Lücke das, was auf dem Monitor angezeigt werden muss (ein gewöhnlicher Befehl wie der Name eines Programms, mit dem es ausgeführt werden soll, edit test, paint picture, etc).   
**Bemerkung: **Advanced Monitor ****lässt darauf im Programm Paint mit der rechten Maustaste zeichnen. Genauer gesagt entspricht das Klicken mit der rechten Maustaste auf dem Monitor dem Klicken mit der linken Maustaste auf dem Computerbildschirm. 

Wir zeigen auf dem Monitor unser Logo an, das wir in Paint gezeichnet haben. 

  
**5) Taschencomputer. **

  

Die Computer mit den kleineren Bildschirmen, die man auf die Erde nicht stellen muss, werden direkt aus der Hand verwendet. Er hat fast die gleichen Funktionen wie ein großer Computer.   

**Die zusätzliche Aufgabe.   
**Zweistöckige Gebäude aus mehreren Räumen auf der Etage bauen und die Computer mit den Fragen an jede Tür stellen, die Antwort auf die Frage ist das Passwort des Eintritts (z. B. das Ergebnis der Addition von 100 und 338). Wir geben den Kindern die Schildkröten und die notwendigen Ressourcen. 

Wir bereiten eine Weise in der Nähe des Lagers vor und teleportieren die Schüler, die alles gemacht haben, zu uns und geben eine Schildkröte und Ressourcen.