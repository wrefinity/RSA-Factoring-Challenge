#include <stdio.h>
/*
    Finds the smallest divisor, if any, of a given number `n`
    Returns:
        smallest divisor if found
        0 if n is prime
*/
int trial_division(long int num){
long int fac;

if (num % 2 == 0){
	printf("%lu=%lu*%i\n", num, num/2, 2);
	return 0;
}

fac = 3;
while (fac * fac  <= num)
{
	if (num % fac == 0){
		printf("%lu=%lu*%lu\n", num, num/fac, fac);
		return 0;
	}
	else{
		fac += 2;
	}
}
printf("%lu=%lu*%i\n", num, num, 1);
return 0;
}
