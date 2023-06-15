#include "lists.h"

/**
 * print_dlistint - check the code
 * @h: the head of the list
 * Return: size_t.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int nodes;

	nodes = 0;
	if (h != NULL)
	{
		while (h != NULL)
		{
			printf("%d\n", h->n);
			nodes++;
			h = h->next;
		}
	}
	return (nodes);
}
