public class problem_6
{
	public static void main(String[] args)
	{
		int num = 100;
		long answer =(long) sum1(num) - sum2(num);
		System.out.println(answer);
	}

	public static double sum1(int n)
	{
		double answer =Math.pow((n*(n+1))/2,2);
		//System.out.println("Sum1: " + answer);
		return answer;
	}

	public static long sum2(int n)
	{
		long answer = (n*(n+1)*(2*n+1))/6;
		//System.out.println("Sum2: " + answer);
		return answer;
	}
}
