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

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if ((*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
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
				return (*head);
			}
			if (current->n >= new->n)
			{
				new->next = current;
				prv->next = new;
				return (*head);
			}
			current = current->next;
			prv = prv->next;
		}
	}
	return (*head);
}
