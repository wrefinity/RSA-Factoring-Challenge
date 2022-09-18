#include <stdio.h>
/**
 * prime_division - Finds the smallest divisor
 * @n: number to find divisor
 * Returns: smallest divisor else 0 if n is prime
*/
int prime_division(long int n)
{
	long int fac;

	if (n % 2 == 0)
	{
		printf("%lu = %lu * %i \n", n, n / 2, 2);
		return (0);
	}

	fac = 3;
	while (fac * fac <= n)
	{
		if (n % fac == 0)
		{
			printf("%lu=%lu*%lu\n", n, n / fac, fac);
			return (0);
		}
		fac += 2;
	}
	printf("%lu = %lu * %i\n", n, n, 1);
	return (0);
}
