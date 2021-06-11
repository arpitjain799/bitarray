"""
This stub, as well as util.pyi, have been tested with
Python 3.9 and mypy 0.901
"""
from collections.abc import Iterable, Iterator
from unittest.runner import TextTestResult

from typing import BinaryIO, Hashable, Union, overload


Codedict = dict[Hashable, bitarray]


class decodetree:
    def __init__(self, code: Codedict, /) -> None: ...
    def nodes(self) -> int: ...
    def todict(self) -> Codedict: ...


class bitarray:
    def __init__(self,
                 initializer: Union[int, str, Iterable[int], None] = ...,
                 endian: str = ..., /) -> None: ...

    def all(self) -> bool: ...
    def any(self) -> bool: ...
    def append(self, value: int, /) -> None: ...
    def buffer_info(self) -> tuple[int, int, str, int, int]: ...
    def bytereverse(self) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> bitarray: ...
    def count(self,
              value: int = ...,
              start: int = ...,
              stop: int = ..., /) -> int: ...

    def decode(self, code: Union[Codedict, decodetree], /) -> list: ...
    def encode(self, code: Codedict, x: Iterable, /) -> None: ...
    def endian(self) -> str: ...
    def extend(self, x: Iterable[int], /) -> None: ...
    def fill(self) -> int: ...
    def find(self,
             a: Union[bitarray, int],
             start: int = ...,
             stop: int = ..., /) -> int: ...

    def frombytes(self, a: bytes, /) -> None: ...
    def fromfile(self, f: BinaryIO, n: int = ..., /) -> None: ...
    def index(self,
              a: Union[bitarray, int],
              start: int = ...,
              stop: int = ..., /) -> int: ...

    def insert(self, i: int, value: int, /) -> None: ...
    def invert(self, i: int = ...) -> None: ...
    def iterdecode(self,
                   code: Union[Codedict, decodetree], /) -> Iterator: ...

    def itersearch(self, a: Union[bitarray, int], /) -> Iterator[int]: ...
    def pack(self, b: bytes, /) -> None: ...
    def pop(self, i: int = ..., /) -> int: ...
    def remove(self, value: int, /) -> None: ...
    def reverse(self) -> None: ...
    def search(self, a: Union[bitarray, int],
               limit: int = ...) -> list[int]: ...

    def setall(self, value: int, /) -> None: ...
    def sort(self, reverse: int) -> None: ...
    def to01(self) -> str: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, f: BinaryIO, /) -> None: ...
    def tolist(self) -> list[int]: ...
    def unpack(self,
               zero: bytes = ...,
               one: bytes = ...) -> bytes: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> bitarray: ...
    @overload
    def __setitem__(self, i: Union[int, slice], o: int) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: bitarray) -> None: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...

    def __add__(self, other: bitarray) -> bitarray: ...
    def __iadd__(self, other: bitarray) -> bitarray: ...
    def __mul__(self, n: int) -> bitarray: ...
    def __imul__(self, n: int) -> bitarray: ...
    def __rmul__(self, n: int) -> bitarray: ...

    def __ge__(self, other: bitarray) -> bool: ...
    def __gt__(self, other: bitarray) -> bool: ...
    def __le__(self, other: bitarray) -> bool: ...
    def __lt__(self, other: bitarray) -> bool: ...

    def __and__(self, other: bitarray) -> bitarray: ...
    def __or__(self, other: bitarray) -> bitarray: ...
    def __xor__(self, other: bitarray) -> bitarray: ...
    def __iand__(self, other: bitarray) -> bitarray: ...
    def __ior__(self, other: bitarray) -> bitarray: ...
    def __ixor__(self, other: bitarray) -> bitarray: ...
    def __invert__(self) -> bitarray: ...
    def __lshift__(self, n: int) -> bitarray: ...
    def __rshift__(self, n: int) -> bitarray: ...
    def __ilshift__(self, n: int) -> bitarray: ...
    def __irshift__(self, n: int) -> bitarray: ...


class frozenbitarray(bitarray):
    def __hash__(self) -> int: ...


__version__: str
def bits2bytes(n: int, /) -> int: ...
def get_default_endian() -> str: ...
def test(verbosity: int = ..., repeat: int = ...) -> TextTestResult: ...
def _set_default_endian(endian: str) -> None: ...
def _sysinfo() -> tuple: ...