#include "lists.h"
/**
 * reverseLinkedList - check the code
 * @head: pointer
 * Return: reversed list
 */
listint_t *reverseLinkedList(listint_t *head)
{
	listint_t *current = head;
	listint_t *previous = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	return (previous);
}
/**
 * is_palindrome - check the code
 * @head: pointer
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *current = *head;
	listint_t *reversed = NULL;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	if (len <= 1)
		return (1);
	current = *head;
	for (i = 0; i < len / 2; i++)
	{
		current = current->next;
	}
	reversed = reverseLinkedList(current);
	current = *head;
	while (reversed != NULL)
	{
		if (current->n != reversed->n)
			return (0);

		current = current->next;
		reversed = reversed->next;
	}
	return (1);
}
