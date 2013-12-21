function fib(limit)
{

	var fib_1 = 0;
	var fib_2 = 1;
	var fib_n = 0;
	var sum   = 0;

	while(fib_n < limit)
	{
		fib_n = fib_2 + fib_1;
		fib_1 = fib_2;
		fib_2 = fib_n;

		//console.log(fib_1);

		if(fib_1 %2 ==0)
		{
			sum = sum + fib_1;
		}
	}

	console.log(sum);

}

fib(4000000);
