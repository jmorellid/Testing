
# OK - En una lista vacía hay cero elementos
# OK - Al agregar un elemento a una lista vacía hay un elemento
# OK - En una lista vacía no hay ninguna clave
# OK - Se puede recuperar un elemento de una lista no vacía a partir de su clave
# OK - Cuando se agrega un elemento a una lista no vacía con calve existente la lista actualiza el valor correspondiente
# OK - Cuando se agrega un elemento a una lista vacía la lista de calves estaá ordenada
# se puece borrar una pareja a partir de la clave

import pytest
from sys import path
from os import getcwd
import numpy as np
path.append(getcwd() + "/src") 
from lista import ClaseLista

def test_lista_vacia():
    """ Se prueba el comportamiento de la lista vacía """
    lista_vacia = ClaseLista()
    assert lista_vacia.count_elementos() == 0
    assert lista_vacia.count_claves() == 0

def test_lista_agrego_un_elemento():
    """ Se prueba el comportamiento de la lista al agregar un elemento """
    lista_un_elemento = ClaseLista()
    lista_un_elemento.add('Bocina', 'linda')
    assert lista_un_elemento.count_claves() == 1
    assert lista_un_elemento.count_elementos() == 1

def test_lista_find():
    """ Se prueba si se puede hallar correctamente un elemento en una lista partiendo de su clave """
    lista = ClaseLista()
    lista.add('bocina', 'linda')
    assert lista.find('bocina') == 'linda'

def test_actualizacion_de_valor():
    """ Se prueba si luego de agregar un elemento a la lista que tiene una clave existente, el elemento se actualiza correctamente  """
    lista = ClaseLista()
    lista.add('bocina', 'linda')
    lista.add('bocina', 'grande')
    assert lista.find('bocina') == 'grande'

def test_orden_lista():
    """ Corrobora que las claves estén ordenadas una vez que se agrega un elemento nuevo a la lista"""
    lista = ClaseLista()
    lista.add('a','y')
    lista.add('c','p')
    lista.add('b','r')
    assert np.array_equal(lista(), np.array(['a', 'b', 'c']))

def test_delete_item():
    """ Corrobora que se borre correctamente el elemento a partir de su clave"""
    lista = ClaseLista()
    lista.add('a','y')
    lista.add('c','p')
    lista.add('b','r')

    lista.delete('b')
    assert np.array_equal(lista(), np.array(['a', 'c']))



    




