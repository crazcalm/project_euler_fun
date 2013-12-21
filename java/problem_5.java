public class problem_5
{
	public static void main(String[] args)
	{

		int divisor = 20;

		for(long i =100000; i<10000000000L; i++)
		{
			if(mod(i,divisor))
			{
				System.out.println(i);
				break;
			}
		}

	}

	public static Boolean mod(long number, int divisor)
	{
		if(divisor > 1)
		{
			if(number % divisor ==0)
			{
				return mod(number, divisor-1);
			}
			else
			{
				return false;
			}
		}

		return true;
	}


}
