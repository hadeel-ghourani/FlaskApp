from ctypes import set_errno
from tkinter.font import nametofont

import pytest

from application.models.user import UserModel


def test_create_user():
    
    name = 'hadeelghourani'
    password = 'testingpass123'
    user = UserModel(name, password)
    assert user.name == name
    assert user.password == password