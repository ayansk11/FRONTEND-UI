import java.util.Scanner;

public class VigenereCipher {
    
    public static void main(String[] args) {
        
        String original, key;
        String coded = "";
        String alphabets = "abcdefghijklmnopqrstuvwxyz";
        int letter, codeLetter, keyLetter, j = 0;;

        Scanner sc = new Scanner(System.in);

        System.out.print("ENTER TEXT TO BE ENCRYPTED/ENCODED: ");
        String s = sc.nextLine();
        original = s.toLowerCase();

        System.out.print("ENTER KEY: ");
        String k = sc.nextLine();
        key = k.toLowerCase();

        for (int i = 0; i < original.length(); i++) {
            
            if (alphabets.indexOf(original.substring(i, i+1)) != -1) {

                if (original.length() > key.length()) {

                    if (j >= key.length()) {

                        j = 0;
                        
                    }
                    
                    letter = alphabets.indexOf(original.substring(i, i+1));
                    keyLetter = alphabets.indexOf(key.substring(j, j + 1));
                    
                    codeLetter = letter + keyLetter;
                    codeLetter = codeLetter % 26;

                    coded = coded + alphabets.substring(codeLetter, codeLetter + 1);

                    j++;

                } else {

                    letter = alphabets.indexOf(original.substring(i, i+1));
                    keyLetter = alphabets.indexOf(key.substring(i, i + 1));

                    codeLetter = letter + keyLetter;
                    codeLetter = codeLetter % 26;

                    coded = coded + alphabets.substring(codeLetter, codeLetter + 1);
                    
                }

            } else {
                
                coded = coded + original.substring(i, i+1);
            }

            System.out.println(coded);
        }

        System.out.println(coded);
    }
}
