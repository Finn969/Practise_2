#!/usr/bin/env python3

import pytest
from Code import example

def test_example1():
    assert example.example1("2 4 7 8 10") == 3
    assert example.example1("1 2 2") == 1

def test_example2():
    assert example.example2("bitcoin take over the world maybe who knows perhaps") == 3
    assert example.example2("Lets all go on holiday somewhere very cold") == 2
    assert example.example2("i want to travel the world writing code one day") == 1

def test_example3():
    assert example.example3([1,2,'a','b']) == [1,2]
    assert example.example3([1,'a','b',0,15]) == [1,0,15]
    assert example.example3([[1,2,'aasf','1','123',123]]) == [1,2,123]