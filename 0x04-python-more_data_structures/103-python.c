#include <Python.h>
#include <string.h>
/**
 * print_python_bytes - A function that prints info
 * about a python byte object
 * @p: the python byte object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *pyByte;
    Py_ssize_t size, max, count;
    char *byteString;

    pyByte = (PyBytesObject *)p;
    size = pyByte->ob_base.ob_size;
    byteString = pyByte->ob_sval;
    printf("[.] bytes object info");
    if (PyBytes_Check(pyByte))
    {
        printf("[ERROR] Invalid Bytes Object");
        return;
    }
    printf("  size: %li", size);
    printf("  trying string: %s", byteString);
    if (size >= 10)
        max = 10;
    else
        max = size + 1;
    printf("  first %li bytes: ");
    for (count = 0; count < max; count++){
        printf("%2x", byteString[count]);
        if (count + 1 == max)
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_list - A function that prints info
 * about a python list
 * @p: the python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
    PyListObject *pyList, item;
    PyTypeObject pytype;
    Py_ssize_t size, allocated, count;

    pyList = (PyListObject *)p;
    size = pyList->ob_base.ob_size;
    allocated = pyList->allocated;

    printf("[*] Python list info");
    printf("[*] Size of the Python list = %li", size);
    printf("[*] Allocated = %li", allocated);
    for (count = 0; count < size; count++)
    {
        item = (pyList->ob_item)[count];
        pytype = (PyTypeObject)item;
        printf("Element %li: %s", count, pytype.tp_name);
        if (strcmp(pytype.tp_name, "bytes"))
            print_python_bytes(item);
    }
}