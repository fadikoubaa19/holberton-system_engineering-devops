#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - for holbertonschool
 *
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	}

/**
 * main - for holbertonschool
 *
 * Return: always 0
 */
int main(void)
{
	int index;
	pid_t zombie;

	for (index = 0; index < 5; index++)
	{
	zombie = fork();
	if (zombie == 0)
		return (0);
	printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
