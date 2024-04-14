import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.List;

public class Exercises {

    private Scanner scanner;
    
    public Exercises() {
        this.scanner = new Scanner(System.in);
    }

    // Sum 2 numbers and show its result
    public void exercise_1() {
        try {
            System.out.println("Enter first number: ");
            double number1 = scanner.nextDouble();
            System.out.println("Enter second number: ");
            double number2 = scanner.nextDouble();
            double result = number1 + number2;
            System.out.println("The sum is: " + result);
        } catch (Exception e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    // Calculate the circle area with a given radius
    public void exercise_2() {
        try {
            System.out.println("Enter the radius of the circle: ");
            double radius = scanner.nextDouble();
            double area = Math.PI * Math.pow(radius, 2);
            System.out.println("The area of the circle is: " + String.format("%.4f", area));
        } catch (Exception e) {
            System.out.println("Please enter a valid number.");
        }
    }

    // Concatenate a string with spaces
    public void exercise_3() {
        try {
            System.out.println("Enter first string: ");
            String string1 = scanner.nextLine();
            System.out.println("Enter second string: ");
            String string2 = scanner.nextLine();
            String concatString = string1 + string2;
            System.out.println(concatString);
        } catch (Exception e) {
            System.out.println("Please enter valid Strings.");
        }
    }

    // Create a list and print it
    public void exercise_4() {
        List<Object> list1 = new ArrayList<>();
        list1.addAll(Arrays.asList(1, "two", "3.0", true));
        for (Object item : list1) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    // Multiplipy 2 numbers and show its result
    public void exercise_5() {
        try {
            System.out.println("Enter first number: ");
            double num1 = scanner.nextDouble();
            System.out.println("Enter second number: ");
            double num2 = scanner.nextDouble();
            double result = num1 * num2;
            System.out.println("Result: " + result);
        } catch (InputMismatchException e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    // Multiply 2 numbers without using * operator and show its result
    public void exercise_6() {
        try {
            System.out.println("Enter first number: ");
            int num1 = scanner.nextInt();
            System.out.println("Enter second number: ");
            int num2 = scanner.nextInt();
            int result = multiplyBySum(num1, num2);
            System.out.println("Result: " + result);
        } catch (InputMismatchException e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    private int multiplyBySum(int num1, int num2) {
        int result = 0;
        for (int i = 0; i < Math.abs(num2); i++) {
            result += num1;
        }
        return num2 > 0 ? result : -result;
    }

    // Read a text string and show its length
    public void exercise_7() {
        try {
            System.out.println("Enter a text string: ");
            String string = scanner.nextLine();
            int length = string.length();
            System.out.println("length: " + length);
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    // Calculate the mean of a list of numbers
    public void exercise_8() {
        try {
            System.out.println("Enter a list of numbers separated by spaces: ");
            String input = scanner.nextLine();
            String[] numbersStr = input.split(" ");
            double sum = 0;
            for (String numStr : numbersStr) {
                sum += Double.parseDouble(numStr);
            }
            double mean = sum / numbersStr.length;
            System.out.println("The mean of the numbers list is: " + mean);
        } catch (Exception e) {
            System.out.println("Please enter a valid list of numbers separated with spaces.");
        }
    }

    // Create a tuple of elements and print it, there is not tuples in Java
    public void exercise_9() {
        Object[] myTuple = {3, false, "one", 5.5};
        System.out.print("tuple: ");

        for (Object item : myTuple) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    // Power of a number
    public void exercise_10() {
        try {
            System.out.println("Enter base number: ");
            int base = scanner.nextInt();
            System.out.println("Enter exponent number: ");
            int exponent = scanner.nextInt();
            double result = Math.pow(base, exponent);
            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.out.println("Please enter valid integers.");
        }
    }

    // Return the Inverse of a String
    public void exercise_11() {
        try {
            System.out.println("Enter a String to find out its inverse: ");
            String string = scanner.nextLine();
            StringBuilder inverse = new StringBuilder(string).reverse();
            System.out.println("Inverse string: " + inverse.toString());
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    // Calculate the rectangle area with given base and height
    public void exercise_12() {
        try {
            System.out.println("Enter base: ");
            double base = scanner.nextDouble();
            System.out.println("Enter height: ");
            double height = scanner.nextDouble();
            double area = base * height;
            System.out.println("The area is: " + area);
        } catch (Exception e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    // Convert a whole number in string
    public void exercise_13() {
        try {
            System.out.println("Enter a number: ");
            int number = scanner.nextInt();
            System.out.println("The integer was: " + Integer.toString(number) + ", input function reads a string, so it needs to be converted to int.");
        } catch (Exception e) {
            System.out.println("Please enter a valid number.");
        }
    }

    // Replace a character in a string
    public void exercise_14() {
        try {
            System.out.println("Enter a string: ");
            String string = scanner.nextLine();
            System.out.println("Enter character to replace: ");
            String oldChar = scanner.nextLine();
            System.out.println("Enter character to replace with: ");
            String newChar = scanner.nextLine();

            if (oldChar.length() != 1 || newChar.length() != 1) {
                throw new Exception("Please enter single characters.");
            }

            if (!string.contains(oldChar)) {
                throw new Exception("Character not found in string.");
            }

            String newString = string.replace(oldChar, newChar);
            System.out.println("The new string is: " + newString);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    // Turn a string to lowercase
    public void exercise_15() {
        try {
            System.out.println("Enter a string: ");
            String inputString = scanner.nextLine();
            String lowerCaseString = inputString.toLowerCase();
            System.out.println("The lowercase string is " + lowerCaseString);
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    // Sort a list in ascending order
    public void exercise_16() {
        try {
            System.out.println("Enter a list of numbers separated by spaces: ");
            String input = scanner.nextLine();
            String[] numbersStr = input.split(" ");
            double[] numbers = new double[numbersStr.length];
            for (int i = 0; i < numbersStr.length; i++) {
                numbers[i] = Double.parseDouble(numbersStr[i]);
            }
            java.util.Arrays.sort(numbers);
            System.out.println("The sorted list is: " + java.util.Arrays.toString(numbers));
        } catch (Exception e) {
            System.out.println("Please enter a valid list.");
        }
    }

    // Calculate the power of a number without using the ** operator
    public void exercise_17() {
        try {
            System.out.println("Enter base number: ");
            int base = scanner.nextInt();
            System.out.println("Enter power number: ");
            int power = scanner.nextInt();
            int result = 1;
            for (int i = 0; i < power; i++) {
                result *= base;
            }
            System.out.println(result);
        } catch (Exception e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    // Extract a substring from a given string
    public void exercise_18() {
        try {
            System.out.println("Enter the string: ");
            String string = scanner.nextLine();
            System.out.println("Enter the start position: ");
            int startPos = scanner.nextInt();
            System.out.println("Enter the end position: ");
            int endPos = scanner.nextInt();

            if (startPos < 0 || endPos > string.length()) {
                throw new Exception("Positions are not valid.");
            }

            if (startPos > endPos) {
                throw new Exception("End position should be greater than start position.");
            }

            String substring = string.substring(startPos, endPos);
            System.out.println("The substring is " + substring);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    // Convert a float into a string
    public void exercise_19() {
        try {
            System.out.println("Enter a decimal number: ");
            double number = scanner.nextDouble();
            System.out.println("The integer number is: " + (int) number);
        } catch (Exception e) {
            System.out.println("Please enter valid numbers.");
        }
    }

    // Count the occurrence of a character in a given string
    public void exercise_20() {
        try {
            System.out.println("Enter a string: ");
            String string = scanner.nextLine();
            System.out.println("Enter a char: ");
            String charString = scanner.nextLine();
            if (charString.length() != 1) {
                throw new Exception("Please enter a single character.");
            }

            if (!string.contains(charString)) {
                throw new Exception("Character not found in string.");
            }

            int count = string.length() - string.replace(charString, "").length();
            System.out.println("The number of occurrences is: " + count);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    // Find and show the last character of a string
    public void exercise_21() {
        try {
            System.out.println("Enter a string: ");
            String string = scanner.nextLine();
            char lastChar = string.charAt(string.length() - 1);
            System.out.println("The last character is: " + lastChar);
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    // Multiply a string by a given number
    public void exercise_22() {
        try {
            System.out.println("Enter a string: ");
            String string = scanner.nextLine();
            System.out.println("Enter a number: ");
            int number = scanner.nextInt();
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < number; i++) {
                result.append(string);
            }
            System.out.println("The result is: " + result.toString());
        } catch (Exception e) {
            System.out.println("Please enter a valid string and number.");
        }
    }

    // Separate a string into substrings using spaces
    public void exercise_23() {
        try {
            System.out.println("Enter a string with spaces: ");
            String string = scanner.nextLine();
            String[] substrings = string.split(" ");
            System.out.println("The string separated into simple words is " + java.util.Arrays.toString(substrings));
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    // Verify if a word is palindrome
    public void exercise_24() {
        try {
            System.out.println("Enter a string to check if it is a palindrome: ");
            String string = scanner.nextLine();
            int length = string.length();
            int halfLength = (length / 2) + 1;
            boolean isPalindrome = true;

            for (int i = 0; i < halfLength; i++) {
                if (string.charAt(i) != string.charAt(length - i - 1)) {
                    isPalindrome = false;
                    break;
                }
            }

            if (isPalindrome) {
                System.out.println("The string is a palindrome");
            } else {
                System.out.println("The string is not a palindrome");
            }
        } catch (Exception e) {
            System.out.println("Please enter a valid string.");
        }
    }

    public void closeScanner() {
        scanner.close();
    }

    public static void main(String[] args) {
        Exercises exer = new Exercises();

        // exer.exercise_1();
        // exer.exercise_2();
        // exer.exercise_3();
        // exer.exercise_4();
        // exer.exercise_5();
        // exer.exercise_6();
        // exer.exercise_7();
        // exer.exercise_8();
        // exer.exercise_9();
        exer.exercise_10();
        // exer.exercise_11();
        // exer.exercise_12();
        // exer.exercise_13();
        // exer.exercise_14();
        // exer.exercise_15();
        // exer.exercise_16();
        // exer.exercise_17();
        // exer.exercise_18();
        // exer.exercise_19();
        // exer.exercise_20();
        // exer.exercise_21();
        // exer.exercise_22();
        // exer.exercise_23();
        exer.closeScanner();
    }
}
