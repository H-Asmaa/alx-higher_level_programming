#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * struct dlistint_t - doubly linked list
 * @n: integer
 * @next: points to the next node
 * @prev: points to the previous node
 * Description: doubly linked list node structure
 * for project
 */
typedef struct dlistint_t
{
    int n;
    struct dlistint_t *next;
	struct dlistint_t *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);
#endif /* LISTS_H */
