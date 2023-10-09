from typing import Sequence, Union

def safe_first_element(lst: Sequence) -> Union[None, lst[0]]:
    if lst:
        return lst[0]
    else:
        return None
