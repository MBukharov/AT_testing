import pytest

vowels = ['a','e','i','o','u','y']

def count_vowels(stroka):
    sum = 0
    for char in stroka.lower():
        sum += 1 if char in vowels else 0
    return sum

#ТЕСТИРОВАНИЕ
@pytest.mark.parametrize('input,expected',[
    ('aeeeuuuyyy',10),
    ('aey',3),
    ('rtgh',0),
    ('AweyOI',5),
    ('aweSOME',4)
])
def test_count_vowels(input,expected):
    assert count_vowels(input) == expected