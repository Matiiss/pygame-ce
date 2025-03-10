from typing import (
    overload,
    Union,
    Callable,
    Protocol,
    Tuple,
    Sequence,
)

from pygame import Rect, FRect
from ._common import Coordinate, RectValue

_CanBeCircle = Union[Circle, Tuple[Coordinate, float], Sequence[float]]

class _HasCirclettribute(Protocol):
    # An object that has a circle attribute that is either a circle, or a function
    # that returns a circle
    circle: Union[_CanBeCircle, Callable[[], _CanBeCircle]]

_CircleValue = Union[_CanBeCircle, _HasCirclettribute]

class Circle:
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> None: ...
    @property
    def r_sqr(self) -> float: ...
    @r_sqr.setter
    def r_sqr(self, value: float) -> None: ...
    @property
    def d(self) -> float: ...
    @d.setter
    def d(self, value: float) -> None: ...
    @property
    def diameter(self) -> float: ...
    @diameter.setter
    def diameter(self, value: float) -> None: ...
    @property
    def area(self) -> float: ...
    @area.setter
    def area(self, value: float) -> None: ...
    @property
    def circumference(self) -> float: ...
    @circumference.setter
    def circumference(self, value: float) -> None: ...
    @property
    def center(self) -> Tuple[float, float]: ...
    @center.setter
    def center(self, value: Coordinate) -> None: ...
    @overload
    def __init__(self, x: float, y: float, r: float) -> None: ...
    @overload
    def __init__(self, pos: Coordinate, r: float) -> None: ...
    @overload
    def __init__(self, circle: _CircleValue) -> None: ...
    @overload
    def move(self, x: float, y: float, /) -> Circle: ...
    @overload
    def move(self, move_by: Coordinate, /) -> Circle: ...
    @overload
    def move_ip(self, x: float, y: float, /) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate, /) -> None: ...
    @overload
    def collidepoint(self, x: float, y: float, /) -> bool: ...
    @overload
    def collidepoint(self, point: Coordinate, /) -> bool: ...
    @overload
    def collidecircle(self, circle: _CircleValue, /) -> bool: ...
    @overload
    def collidecircle(self, x: float, y: float, r: float, /) -> bool: ...
    @overload
    def collidecircle(self, center: Coordinate, r: float, /) -> bool: ...
    @overload
    def colliderect(self, rect: RectValue, /) -> bool: ...
    @overload
    def colliderect(self, x: float, y: float, w: float, h: float, /) -> bool: ...
    @overload
    def colliderect(self, topleft: Coordinate, size: Coordinate, /) -> bool: ...
    @overload
    def update(self, circle: _CircleValue, /) -> None: ...
    @overload
    def update(self, x: float, y: float, r: float, /) -> None: ...
    @overload
    def update(self, center: Coordinate, r: float, /) -> None: ...
    def as_rect(self) -> Rect: ...
    def as_frect(self) -> FRect: ...
    def __copy__(self) -> Circle: ...
    copy = __copy__
