#include "lists.h"

/**
 * check_cycle - function checks if cycle exists
 * @list: the header of list
 * Return: 0 if no cycle or 1 if found
 */
int check_cycle(listint_t *list)
{

	listint_t *slow = list;
	listint_t *fast = list->next;
	
	if (list == NULL || list->next == NULL)
		return 0;
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return 0;
	}

	slow = slow->next;
	fast = fast->next->next;

	return 1;
}
