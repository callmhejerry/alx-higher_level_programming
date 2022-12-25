#include "lists.h"

/**
 * is_palindrome - A function that checks if
 * a singly linked list is a palindrome
 * @head: the pointer to the start of the linked list
 * Return: 0 if the is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *start;
    int length, mid, count, *new_list, end;

    if (*head == NULL){
        return (1);
    }

    start = *head;
    length = 0;

    while (start != NULL){
        start = start->next;
        length++;
    }
    new_list = (int *)malloc(sizeof(int) * length);
    if (new_list == NULL)
        return (0);
    start = *head;
    for (count = 0; count < length; count++){
        new_list[count] = start->n;
        start = start->next;
    }
    if (length % 2 != 0)
        mid = (length + 1) / 2;
    else
        mid = length / 2;
    for (count = 0, end = length - 1; count < mid; count++, end--){
        if (new_list[count] != new_list[end]){
            free(new_list);
            return (0);
        }
    }
    free(new_list);
    return (1);
}