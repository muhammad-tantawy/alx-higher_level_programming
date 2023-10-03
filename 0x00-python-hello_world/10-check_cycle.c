#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;
	
	if (list == NULL || list->next == NULL)
	return (0);
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return 0;
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
