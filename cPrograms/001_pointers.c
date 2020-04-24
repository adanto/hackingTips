#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	

	int a = 1;

	int * pTa = &a;

	printf("The value is %d\n", a);
	printf("Pointer is %x\n", pTa);
	printf("Pointer value is %d\n\n", *pTa);
	*pTa += 1;
	printf("The value is %d\n", a);
	printf("Pointer is %x\n", pTa);
	printf("Pointer value is %d\n\n", *pTa);

	typedef struct { 
		char * name;
		int age;
	} person;

	person * person1 = (person *) malloc(sizeof(person));

	person person2;
	person2.name = "Carlos";
	person2.age = 3;

	free(person1);

	printf("%x\n\n", &person1);

	char vow[] = "AEIOZ";
	char *pvow = &vow;
	int i;

	for (i = 0; i < 5; i++) {
		printf("&vow[%d]: %d, pvow + %d: %u, vow + %d: %u\n", i, vow[i], i , *(pvow + i), i, *(vow + i));
	}

	printf("\n");
	
	for (i = 0; i < 5; i++) {
		printf("&vow[%d]: 0x%x, pvow + %d: 0x%x, vow + %d: 0x%x\n", i, vow[i], i , *(pvow + i), i, *(vow + i));
	}

	printf("\n");

	for (i = 0; i < 5; i++) {
		printf("vow[%d]: %c, *(pvow + %d): %c, *(vow + %d): %c\n", i, vow[i], i , *(pvow + i), i, *(vow + i));
	}
}
