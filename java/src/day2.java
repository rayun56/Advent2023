import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class day2 {
    private static void part1() {
        // max values
        final int RED = 12;
        final int GREEN = 13;
        final int BLUE = 14;

        int r = RED;
        int g = GREEN;
        int b = BLUE;
        int validGames = 0;
        int sumOfIDs = 0;

        File fp = new File("./inputs/day2.txt");

        try {
            Scanner scan = new Scanner(fp);
            Scanner lineScan;

            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                line = line.replace(':', ' ');

                lineScan = new Scanner(line);
                lineScan.next(); // skips the 'Game' text
                int gameID = lineScan.nextInt();
                boolean lastInSet = false;
                boolean valid = true;
                while (lineScan.hasNext()) {
                    int cubeCount = lineScan.nextInt();
                    String cubeColor = lineScan.next();
                    if (cubeColor.endsWith(",")) {
                        cubeColor = cubeColor.substring(0, cubeColor.length() - 1);
                    }
                    if (cubeColor.endsWith(";")) {
                        cubeColor = cubeColor.substring(0, cubeColor.length() - 1);
                        lastInSet = true;
                    }
                    switch (cubeColor) {
                        case "blue":
                            b -= cubeCount;
                            break;
                        case "red":
                            r -= cubeCount;
                            break;
                        case "green":
                            g -= cubeCount;
                            break;
                    }
                    if (r < 0 || g < 0 || b < 0) {
                        valid = false;
                        break;
                    }
                    if (lastInSet) {
                        r = RED;
                        g = GREEN;
                        b = BLUE;
                        lastInSet = false;
                    }
                }
                if (valid) {
                    validGames++;
                    sumOfIDs += gameID;
                }
                r = RED;
                g = GREEN;
                b = BLUE;
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            return;
        }
        System.out.println("Valid games: " + validGames + "\nSum of valid IDs: " + sumOfIDs);

    }

    private static void part2() {
        File fp = new File("./inputs/day2.txt");
        int sumOfPowers = 0;
        try {
            Scanner scan = new Scanner(fp);
            Scanner lineScan;
            while (scan.hasNextLine()) {
                String line = scan.nextLine();
                line = line.replace(':', ' ');
                lineScan = new Scanner(line);
                lineScan.next();
                int gameID = lineScan.nextInt();

                int maxRed = 0;
                int maxBlue = 0;
                int maxGreen = 0;
                while (lineScan.hasNext()) {
                    int cubeCount = lineScan.nextInt();
                    String cubeColor = lineScan.next();
                    if (cubeColor.endsWith(",") || cubeColor.endsWith(";")) {
                        cubeColor = cubeColor.substring(0, cubeColor.length() - 1);
                    }
                    switch (cubeColor) {
                        case "blue":
                            maxBlue = Math.max(maxBlue, cubeCount);
                            break;
                        case "red":
                            maxRed = Math.max(maxRed, cubeCount);
                            break;
                        case "green":
                            maxGreen = Math.max(maxGreen, cubeCount);
                            break;
                    }
                }
                sumOfPowers += maxBlue * maxGreen * maxRed;
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            return;
        }
        System.out.println("Sum of powers: " + sumOfPowers);
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
}