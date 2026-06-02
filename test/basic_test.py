import pygame
import main, classes
import pytest

def test_import():
    assert main is not None
    assert classes is not None