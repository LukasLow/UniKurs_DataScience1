# (nicht so abgeben, diese Datei dient dazu, den Code heraus zu kopieren)

## Aufgabe 1

java ```
```
public class RecursiveSum {
    public static int summe(int[] v, int von, int bis) {
        // Basisfall: Wenn von und bis den gleichen Index haben,
        // geben wir den Wert an dieser Position zurück
        if (von == bis) {
            return v[von];
        } else {
            // Aufteilung des Indexbereichs in zwei Teile
            int mitte = (von + bis) / 2;
            
            // Rekursiver Aufruf für den linken Teilbereich
            int summeLinks = summe(v, von, mitte);
            
            // Rekursiver Aufruf für den rechten Teilbereich
            int summeRechts = summe(v, mitte + 1, bis);
            
            // Rückgabe der Summe beider Teilbereiche
            return summeLinks + summeRechts;
        }
    }
    
    public static void main(String[] args) {
        // Überprüfen, ob mindestens ein Argument (Zahlenfolge) übergeben wurde
        if (args.length < 1) {
            System.out.println("Es wurde keine Zahlenfolge übergeben.");
            return;
        }
        
        // Erstellen des Feldes basierend auf den übergebenen Argumenten
        int[] zahlenfolge = new int[args.length];
        for (int i = 0; i < args.length; i++) {
            zahlenfolge[i] = Integer.parseInt(args[i]);
        }
        
        // Aufrufen der summe-Methode und Ausgabe des Ergebnisses
        int gesamtsumme = summe(zahlenfolge, 0, zahlenfolge.length - 1);
        System.out.println("Die Gesamtsumme der Zahlenfolge beträgt: " + gesamtsumme);
    }
}
```
Dieser Code verwendet die zweifach rekursive Methode `summe`, um die Summe der Werte im Feld `v` von Index `von` bis Index `bis` zu berechnen. Die Methode teilt den Indexbereich in zwei möglichst gleich große Teilbereiche auf und ruft sich selbst rekursiv für jeden dieser Teilbereiche auf. Die Ergebnisse der Teilbereiche werden dann miteinander addiert, um die Gesamtsumme zu erhalten.

In der `main`-Methode wird überprüft, ob mindestens eine Zahlenfolge als Argument übergeben wurde. Wenn ja, wird ein Feld erstellt und mit den übergebenen Zahlen initialisiert. Anschließend wird die `summe`-Methode aufgerufen und das Ergebnis ausgegeben.

## Aufgabe 2

java
```
public class Geld {
    private int euro, cent;

    // Konstruktor
    public Geld(int e, int c) {
        euro = e;
        cent = c;
        adjustCent();
    }

    // 1. Private Methode zur Anpassung der Cent-Werte
    private void adjustCent() {
        if (cent >= 100) {
            int additionalEuro = cent / 100;
            euro += additionalEuro;
            cent %= 100;
        }
    }

    // 2. Methode zum Überprüfen der Gleichheit von Geldbeträgen
    public boolean equals(Geld g) {
        return euro == g.euro && cent == g.cent;
    }

    // 3. Methode zum Hinzufügen eines Geldbetrags
    public void add(Geld g) {
        euro += g.euro;
        cent += g.cent;
        adjustCent();
    }

    // 4. Überschreiben der toString-Methode
    @Override
    public String toString() {
        return euro + "," + (cent < 10 ? "0" + cent : cent) + " Euro";
    }

    // 5. Test-Unit zur umfassenden Überprüfung der Klasse
    public static void test() {
        // Testfall 1
        Geld betrag1 = new Geld(5, 75);
        Geld betrag2 = new Geld(2, 90);
        Geld betrag3 = new Geld(8, 65);
        System.out.println(betrag1);  // Ausgabe: 5,75 Euro
        System.out.println(betrag1.equals(betrag2));  // Ausgabe: false

        // Testfall 2
        betrag1.add(betrag2);
        System.out.println(betrag1);  // Ausgabe: 8,65 Euro

        // Testfall 3
        betrag1.add(betrag3);
        System.out.println(betrag1);  // Ausgabe: 17,30 Euro
        System.out.println(betrag2);  // Ausgabe: 2,90 Euro

        // Testfall 4
        Geld betrag4 = new Geld(0, 230);
        System.out.println(betrag4);  // Ausgabe: 2,30 Euro
    }

    // Hauptmethode zum Ausführen der Test-Unit
    public static void main(String[] args) {
        test();
    }
}
