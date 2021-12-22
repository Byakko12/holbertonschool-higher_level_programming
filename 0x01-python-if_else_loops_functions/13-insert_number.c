#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * *insert_node - inserts a new node at a sort linked list.
 * @head: variable that point to point to list
 * @number: data of node
 * Return: adress of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before = NULL;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL || head == NULL)
		return (NULL);

	new_node->n = number;
	if (head)
	{
		before = *head;
		if (number <= before->n)
		{
			new_node->next = before;
			*head = new_node;
		}
		else
		{
			while (before->next)
			{
				if (number <= before->next->n)
				{
					temp = before->next;
					before->next = new_node;
					new_node->next = temp;
					return (temp);
				}
				before = before->next;
			}
			temp = before->next;
			before->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (new_node);
}
