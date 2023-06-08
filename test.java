import edu.princeton.cs.introcs.StdRandom;

public class RandomStringGenerator {

    public static void main(String[] args) {
        int length = getLengthFromCommandLine(args);
        
        if (length < 0 || length > 100000) {
            System.out.println("Ungültige Länge. Bitte eine Länge zwischen 0 und 100000 angeben.");
            return;
        }
        
        String randomString = generateRandomString(length);
        System.out.println(randomString);
    }
    
    private static int getLengthFromCommandLine(String[] args) {
        if (args.length > 0) {
            try {
                return Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                return -1;
            }
        }
        return -1;
    }
    
    private static String generateRandomString(int length) {
        StringBuilder sb = new StringBuilder();
        String characters = "FLR"; // Mögliche Buchstaben: F, L, R
        
        for (int i = 0; i < length; i++) {
            int randomIndex = StdRandom.uniform(characters.length());
            char randomChar = characters.charAt(randomIndex);
            sb.append(randomChar);
        }
        
        return sb.toString();
    }
}