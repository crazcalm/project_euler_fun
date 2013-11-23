public class fibonacci
{
	public static void main(String[] args)
	{
		int[] numbers = {0,1};
		int sum = 0;

		while(numbers[1] < 4000000)
		{
			numbers = fib(numbers);
			//System.out.println(numbers[0]);

			if(numbers[0]%2 == 0)
			{
				sum += numbers[0];
			}
		}

		System.out.println(sum);


	}

	public static int[] fib(int[] num)
		{
			int tempt = num[1] +num[0];
			num[0]    = num[1];
			num[1]    = tempt;
			return num;
		}
}
