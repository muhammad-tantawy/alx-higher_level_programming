#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{

	struct listint_t *slow = head;
	struct listint_t *fast = head->next;
	
	if (head == NULL || head->next == NULL)
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
