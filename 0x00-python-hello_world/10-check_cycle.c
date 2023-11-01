#include <stdlib.h>
#include "lists.h"
/*
 * check_cycle - a C program to check if a singly_linked
 * @list: a singly_linked list
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *mortal, *pestle;

	if (list == NULL || list->next == NULL)
		return (0);
	mortal = list->next;
	pestle =list->next->next;
	while (mortal && pestle && pestle->next)
	{
		if (mortal == pestle)
			return (0);
		mortal = mortal->next;
		pestle = pestle->next->next;
	}
	return (0);
}
