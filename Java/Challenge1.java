import javax.xml.bind.DatatypeConverter;

public class Challenge1 {
    public static void main(String[] args) {
        String testString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
        System.out.println(hexToB64(testString));
    }

    public static String hexToB64(String s) {
        byte[] rawBytes = DatatypeConverter.parseHexBinary(s);
        return DatatypeConverter.printBase64Binary(rawBytes);
    }
}