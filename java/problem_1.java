public class problem_1
{

	public static void main(String[] args)
	{
		int number = 1;
		int sum    = 0;

		for(int n = 0; n < 1000; n++)
		{
			if(n%3==0 || n%5==0)
			{
				sum += n;
			}

		}

		System.out.println(sum);

	}

}
