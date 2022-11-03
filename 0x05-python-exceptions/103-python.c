#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>

/**
 * print_python_float - print some basic python float objects info
 * @p: pointer to PyObject p
 */

void print_python_float(PyObject *p)
{
	double d;
	char *s = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	d = ((PyFloatObject *)(p))->ob_fval;
	s = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
	fflush(stdout);
}

/**
 * print_python_bytes - print some basic python bytes objects info
 * @p: pointer to PyObject p
 */

void print_python_bytes(PyObject *p)
{
	size_t i, bytes;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	str = ((PyBytesObject *)(P))->ob_sval;
	bytes = PyBytes_Size(p);
	printf("  size: %ld\n",  bytes);

