#include <stdio.h>

struct student{
char name[30];
int scholar;
int course;
}number[10];

void main()
{

printf("Please enter the information about the students!\n");

for(int times=0;times<10;times++)
{
	printf("Student №%i\n",times+1);
	printf("Name: ");scanf("%s",number[times].name);
	printf("The amount of the scholarship: ");scanf("%i",&number[times].scholar);
	printf("Which course student is currently at: ");scanf("%i",&number[times].course);
	puts("________________________");
}
printf("the result of the the search\n");
int totalscholar=0;
for(int times=0;times<10;times++)
{
	if(number[times].course==2)
	{
		printf("Name:%s\n",number[times].name);
		printf("The amount of scholarship:%i\n",number[times].scholar);
		printf("The current course of the student: %i\n",number[times].course);
		puts("________________________");
		totalscholar+=number[times].scholar;
	}
}

printf("The total amount of the schjolarship paid for the students is equal to %i\n",totalscholar);
}
