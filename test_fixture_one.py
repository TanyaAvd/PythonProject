# Создайте тестовый файл с именем test_fixtures.py.
# Напишите несколько фикстур — функций с декоратором @pytest.fixture() — которые возвращают данные (список, словарь или кортеж).
# Для каждой фикстуры напишите хотя бы одну тестовую функцию, которая её использует.
# Напишите два теста, использующих одну и ту же фикстуру.
# Запустите pytest --setup-show test_fixtures.py. Все ли фикстуры запускаются перед каждым тестом?
# Добавьте scope='module' к фикстуре из упражнения 4.
# Повторно запустите pytest --setup-show test_fixtures.py. Что изменилось?
# Для фикстуры из упражнения 6 измените return <data> на yield <data>.
# Добавьте операторы print перед и после yield.
# Запустите pytest -s -v test_fixtures.py. Имеет ли вывод смысл?
# Выполните команду pytest --fixtures. Видите ли вы список своих фикстур?
# Добавьте строку документации к одной из ваших фикстур, если вы её ещё не добавили. Повторно выполните команду pytest --fixtures, чтобы увидеть описание.

import string

import pytest

#@pytest.fixture( )
#Добавьте scope='module' к фикстуре из упражнения 4.
@pytest.fixture( scope='module')
def sample_list():
    """Возвращает  список."""
    print("Print до yield")
    yield [1, 2, 3, 4, 5]
    print("Print после yield")


@pytest.fixture()
def sample_dict():
    """Возвращает  словарь."""
    code=0
    dec_dict={}
    for i in string.ascii_lowercase:
        dec_dict[f'{code:02d}']=i
        code=code + 1
    dec_dict['26']=' '
    return dec_dict

@pytest.fixture()
def sample_tuple():
    """Возвращает  кортеж."""
    return (55.7558, 37.6173)

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
    """Использует фикстуру повторно"""
    assert sum(sample_list) == 15

def test_dict_keys(sample_dict):
    assert "00" in sample_dict

def test_tuple_values(sample_tuple):
    assert sample_tuple[0] > 0

#
#
# ------------------------------------------------------------ fixtures defined from Day_3.pytest_materials.Lection2.test_fixture_one -------------------------------------------------------------
# sample_list [module scope] -- test_fixture_one.py:12
#     Возвращает  список.
#
# sample_dict -- test_fixture_one.py:20
#     Возвращает  словарь.
#
# sample_tuple -- test_fixture_one.py:31
#     Возвращает  кортеж.