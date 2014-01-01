#include <stdio.h>

int 
main (int argc, char *argv[])
{
	unsigned long i;
	int array[10] = {11,12,13,14,15,16,17,18,19,20};
	unsigned long j;
	
	int k;
	int ok = 0;
	
	
	for (j = 300000000; j >= 2520; j -= 20) {
	 	ok = 0;
		for (k = 0; k < 10; k++) {
			if (j % array[k] != 0) {
				ok = 1;
				break;	
			}
			if (ok) {
				continue;
			}
		}
		if (!ok) {
			printf("%ld\n", j);
			break;
		}
	}
	
	return 0;
}
