import java.util.*;

public class Main{
   public static void main(String[] args)
   {
	   Scanner scanner = new Scanner(System.in);
	   
	   int num = scanner.nextInt();
	   while(num != 1)
	   {
		   for(int i = 2; i <= num; i++)
		   {
			   if(num%i == 0)
			   {
				   System.out.println(i);
				   num = num/i;
				   break;
			   }
		   }
	   }
	   
	   scanner.close();
   }
}