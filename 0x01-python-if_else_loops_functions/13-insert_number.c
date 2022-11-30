#include "lists.h"
/**
  * insert_node - A function that adds a number to
  * a sorted singly linked list
  * @head: the variable that holds the address of the first
  * element in the list
  * @number: the number to add to the list
  * Return: the address of the newly inserted node
  */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *prev, *now, *new;
    
    now = *head;
    prev = *head;
    new = (listint_t *)malloc(sizeof(listint_t));
    if (!new)
        return (NULL);
    new->n = number;
    if (*head == NULL)
    {
        *head = new;
        new->next = NULL;
        return (new);
    }
    while (now != NULL)
    {
        if (now->n >= number)
        {
            if (prev == *head)
            {
                *head = new;
                new->next = now;
                return (new);
            }
            new->next = now;
            prev->next = new;
            return (new);
        }
        prev = now;
        now = now->next;
    }
    new->next = NULL;
    prev->next = new;
    return (new);
}
