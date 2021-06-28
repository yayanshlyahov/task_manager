from typing import Iterable, Optional, Union, Any, List, Tuple, Dict

items: List[ Union[int, str] ] = [1, 2, '123']

cosnt_items: Tuple = (1, 2, '123')

book: Dict[str, str] = {'Orwel': '1984'}


# FM-253: Create example function
def example(a: Dict[str, str]) -> Optional[int]:
    
    return None


def generator() -> Iterable[int]:
    yield 1
    yield 2

assert 1 == 2