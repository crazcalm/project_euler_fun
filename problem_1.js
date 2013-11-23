
function problem(limit)
{
	
	var sum = 0;
	
	for (var num = 0; num < 1000; num++)
	{	
		if(num%3== 0 || num%5==0)	
		{

			sum = sum + num;
		}
		
	}
	
	return sum;
}

console.log(problem(1000));

/*

var sum = 0;
for(var num=0; num<10;num++)
{
	if(num%3==0 || num%5==0)
	{
		console.log(num);
		sum+=num;
	}
}

console.log(sum);
*/
