public class problem_3
{
	public static void main(String[] args)
	{
		long number = 600851475143L;

		for(long i = 2L; i<number; i++)
		{
			if(number%i==0 && i>2)
			{
				if(prime_check(i))
				{
					System.out.println("prime divisor: " +i);
				}
			}
		}


	}

	public static boolean prime_check(long number)
	{
		for(long i=2L; i<number; i++)
		{
			if(number%i==0)
			{
				return false;
			}
		}

		return true;
	}
}
