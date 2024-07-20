import java.util.Scanner;

public class Main {
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		
		int num[] = new int[26];
		for(int i = 0; i < num.length; i++)
		{
			num[i] = 0;
		}
		
		String word = scanner.nextLine();
		word = word.toUpperCase();
		
		for(int i = 0; i < word.length(); i++)
		{
			char c = word.charAt(i);
			num[(int)c - 'A'] += 1;
		}
		
		int index = 0;
		for(int i = 0; i < num.length; i++)
		{
			if(num[index] < num[i])
				index = i;
		}
		for(int i = 0; i < num.length; i++)
		{
			if(num[index] == num[i] && i != index)
			{
				System.out.println("?");
				break;
			}
			if(i == num.length-1)
				System.out.println((char)(index + 'A'));
				
		}
		
		scanner.close();
	}
}