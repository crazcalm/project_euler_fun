//problem 3

function prime_check(num)
{

	for (var n= 2; n <num; n++)
	{
		if(num %n=== 0)
		{	
			console.log("false");
			return false;
		}
	}

	console.log("true");
	return true;
}

function main(number)
{
	for(var x=2; x <number+1; x++ )
	{
		if(number%x===0 && prime_check(x))
		{
			console.log(x);
			var answer = x;
		}
	}

	console.log(answer);
	return answer;
}

main(600851475143);
