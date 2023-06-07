#include "lists.h"
/**
 * insert_node - check code
 * @head: pointer
 * @number: a variable
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *prv;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		current = (*head)->next;
		prv = *head;
		while (prv != NULL)
		{
			if (current == NULL)
			{
				new->next = NULL;
				prv->next = new;
				return (new);
			}
			if (current->n >= new->n)
			{
				new->next = current;
				prv->next = new;
				return (new);
			}
			current = current->next;
			prv = prv->next;
		}
	}
	return (new);
}
