import pytest

# see https://github.com/tobgu/pyrthon/tree/master/tests
from pyrthon import register

register('tests.*')

# TODO: run tests? is this really necessary?
import tests.test_catalog
import tests.test_library
import tests.test_system
import tests.test_user_management

pytest.main()
