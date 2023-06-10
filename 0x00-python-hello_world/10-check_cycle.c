#include "lists.h"
/**
 * check_cycle - frees a listint_t list
 * @list: pointer to list
 * Return: void
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (slow != NULL && list->next != NULL)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
