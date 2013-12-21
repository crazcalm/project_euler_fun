//problem 4

function palindrome(word)
{

	for(var x = 0; x<= word.length; x++)
	{
		if(word[x] !== word[word.length -1 -x])
		{
			//console.log("false");
			return false;
		}
	}
	
	//console.log("true");
	return true;

}

function main()
{

	var answer = 0;

	for(var x=100; x< 1000; x++)
	{
		for(var y =100; y<1000; y++)
		{
			var test = x*y;
			//console.log(test);
			if(palindrome(test.toString()) && test > answer)
			{
				console.log(test);
				answer = test;
			}
		}
	}

	console.log(answer);
	return answer;
}


main();
