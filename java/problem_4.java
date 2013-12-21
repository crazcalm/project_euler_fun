public class problem_4
{
	public static void main(String[] args)
	{

		//System.out.println("Hello");
		//System.out.println(palindrome("101010101"));
		//System.out.println(palindrome("10110101"));

		int number=0;

		for(int i = 100;i<1000;i++)
		{
			for(int j = 100; j<1000; j++)
			{
				if(palindrome(Integer.toString(i*j)))
				{
					if( number< i*j)
					{
						number  = i*j;
						System.out.println("Number is: " +number);
					}
				}
			}
		}
	}


	public static Boolean palindrome(String word)
	{
		for(int i = 0; i < word.length(); i++)
			{
				//System.out.println("Index i: "+ word.charAt(i) +", index -i: "  + word.charAt(word.length()-i-1));

				if(word.charAt(i) != word.charAt(word.length() -i -1))
				{
					return false;
				}
			}


		return true;
	}


}
