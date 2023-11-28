#include "lists.h"
/**
 * insert_node - Insert node in order mode to linkedlist
 * @head: head
 * @number: num to be added
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *node = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (node->next)
	{
		if ((node->next)->n >= number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}

	new->next = NULL;
	node->next = new;

	return (new);
}
