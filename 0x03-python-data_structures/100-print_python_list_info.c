#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - A function that prints some
 * basic info about python lists
 * @p: the pyObject to print info about
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    PyListObject *pylist = (PyListObject *)p;
    PyListObject **list = pylist->ob_item;
    int i;
    printf("[*] Size of the Python List = %i\n", (*pylist).ob_size);
    printf("[*] Allocated = %i\n", pylist->allocated);
    for (i = 0; list[i] != NULL; i++) {
        PyTypeObject *item = list[i];
        printf("Element %i: %s\n", i, item->tp_name);
    }
}
