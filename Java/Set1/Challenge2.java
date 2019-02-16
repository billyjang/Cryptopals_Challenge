import javax.xml.bind.DatatypeConverter;

public class Challenge2 {
    public static void main(String[] args) {
        String testString1 = "1c0111001f010100061a024b53535009181c";
        String testString2 = "686974207468652062756c6c277320657965";

        String resultString = fixedXOR(testString1, testString2);
        
        byte[] array = DatatypeConverter.parseHexBinary(resultString);
        for(int i = 0; i < array.length; i += 1) {
            System.out.print(array[i]);
        }
    }

    public static String fixedXOR(String s1, String s2) {
        byte[] rawBytes1 = DatatypeConverter.parseHexBinary(s1);
        byte[] rawBytes2 = DatatypeConverter.parseHexBinary(s2);

        String resultString = "";
        for(int i = 0; i < rawBytes1.length; i += 1) {
            int tmp = (rawBytes1[i] ^ rawBytes2[i]);
            resultString += tmp;
        }

        return resultString;
    }
}