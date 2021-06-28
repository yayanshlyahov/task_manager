import pytest

def validate_password(password: str) -> bool:
    numbers: str = '1234567890'
    symbols: str = '!@#$%^&*()_+=-`'
    valid: bool = True
    is_number: bool = False
    is_symbol: bool = False

    for p in password:
        if p in numbers:
            is_number = True
            break

    for p in password:
        if p in symbols:
            is_symbol = True
            break
    
    if not is_number:
        raise ValueError('No number in password')
    if not is_symbol:
        raise ValueError('No symbol in password')
    
    if len(password) < 8:
        raise ValueError('To short')
    if len(password) > 20:
        raise ValueError('To long')
    
    return True


def test_valid_password():
    assert validate_password('!1qwertyuj')


@pytest.mark.parametrize(
    'password, error', (
        ('!234', 'To short'),
        ('!234' * 5 + '1', 'To long'),
        ('23' * 10, 'No symbol in password'),
        ('!' * 10, 'No number in password'),
    )
)
def test_invalid_password(password, error):
    try:
        validate_password(password)
        assert False
    except Exception as exception:
        assert str(exception) == error