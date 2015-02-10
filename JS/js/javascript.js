function projectEuler()
{
	var n1 = 1; var n2 = 1; var fib = 0; var fibonacci = 0; var i = 0;

	while (fib < 4000000)
	{
		fib = n1 + n2;
		if (fib % 2 == 0)
			fibonacci += fib;
		if (i % 2 == 0)
			n1 = fib;
		else
			n2 = fib
		i++;
	}
	return fibonacci;
}