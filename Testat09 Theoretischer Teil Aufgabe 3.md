
## 3.1

Das Ergebnis der Quadratwurzelberechnung ist genau genug, wenn die absolute Differenz zwischen dem Quadrat des berechneten Ergebnisses und dem ursprünglichen Wert kleiner oder gleich einer vordefinierten Toleranz ist. In der Regel ist es genau genug, auf vier Nachkommastellen zu runden, da auf diese Weise die Abweichung bei höchstens einem Zehntausendstel liegt, was weniger als ein Prozent bedeutet.

## 3.2

```java
public class SquareRootCalculator {
    public static double calculateSquareRoot(double x) {
        return binarySearch(0, x, x);
    }
    
    private static double binarySearch(double low, double high, double target) {
        double mid = (low + high) / 2;
        double result = mid * mid;
        
        if (Math.abs(result - target) <= 0.00001) {
            return mid;
        } else if (result < target) {
            return binarySearch(mid, high, target);
        } else {
            return binarySearch(low, mid, target);
        }
    }
}
```