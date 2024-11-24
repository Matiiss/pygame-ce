from collections.abc import Callable
from typing import overload, Union, Protocol

from pygame import Rect, FRect
from pygame.typing import Point, RectLike, SequenceLike

class _HasCircleAttribute(Protocol):
    # An object that has a circle attribute that is either a circle, or a function
    # that returns a circle
    @property
    def circle(self) -> Union[_CircleLike, Callable[[], _CircleLike]]: ...

_CircleLike = Union[
    Circle, tuple[Point, float], SequenceLike[float], _HasCircleAttribute
]

class _HasLineAttribute(Protocol):
    # An object that has a line attribute that is either a line, or a function
    # that returns a line
    @property
    def line(self) -> Union[_LineLike, Callable[[], _LineLike]]: ...

_LineLike = Union[Line, SequenceLike[float], SequenceLike[Point], _HasLineAttribute]

_CanBeCollided = Union[Circle, Rect, FRect, Point]
_CanBeIntersected = Union[Circle]

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
    def center(self) -> tuple[float, float]: ...
    @center.setter
    def center(self, value: Point) -> None: ...
    @property
    def top(self) -> tuple[float, float]: ...
    @top.setter
    def top(self, value: Point) -> None: ...
    @property
    def left(self) -> tuple[float, float]: ...
    @left.setter
    def left(self, value: Point) -> None: ...
    @property
    def bottom(self) -> tuple[float, float]: ...
    @bottom.setter
    def bottom(self, value: Point) -> None: ...
    @property
    def right(self) -> tuple[float, float]: ...
    @right.setter
    def right(self, value: Point) -> None: ...
    @overload
    def __init__(self, x: float, y: float, r: float) -> None: ...
    @overload
    def __init__(self, pos: Point, r: float) -> None: ...
    @overload
    def __init__(self, circle: _CircleLike) -> None: ...
    @overload
    def move(self, x: float, y: float, /) -> Circle: ...
    @overload
    def move(self, move_by: Point, /) -> Circle: ...
    @overload
    def move_ip(self, x: float, y: float, /) -> None: ...
    @overload
    def move_ip(self, move_by: Point, /) -> None: ...
    @overload
    def collidepoint(self, x: float, y: float, /) -> bool: ...
    @overload
    def collidepoint(self, point: Point, /) -> bool: ...
    @overload
    def collidecircle(self, circle: _CircleLike, /) -> bool: ...
    @overload
    def collidecircle(self, x: float, y: float, r: float, /) -> bool: ...
    @overload
    def collidecircle(self, center: Point, r: float, /) -> bool: ...
    @overload
    def colliderect(self, rect: RectLike, /) -> bool: ...
    @overload
    def colliderect(self, x: float, y: float, w: float, h: float, /) -> bool: ...
    @overload
    def colliderect(self, topleft: Point, size: Point, /) -> bool: ...
    def collideswith(self, other: _CanBeCollided, /) -> bool: ...
    def collidelist(self, colliders: SequenceLike[_CanBeCollided], /) -> int: ...
    def collidelistall(
        self, colliders: SequenceLike[_CanBeCollided], /
    ) -> list[int]: ...
    def intersect(self, other: _CanBeIntersected, /) -> list[tuple[float, float]]: ...
    def contains(self, shape: _CanBeCollided, /) -> bool: ...
    @overload
    def update(self, circle: _CircleLike, /) -> None: ...
    @overload
    def update(self, x: float, y: float, r: float, /) -> None: ...
    @overload
    def update(self, center: Point, r: float, /) -> None: ...
    @overload
    def rotate(self, angle: float, rotation_point: Point, /) -> Circle: ...
    @overload
    def rotate(self, angle: float, /) -> Circle: ...
    @overload
    def rotate_ip(self, angle: float, rotation_point: Point, /) -> None: ...
    @overload
    def rotate_ip(self, angle: float, /) -> None: ...
    def as_rect(self) -> Rect: ...
    def as_frect(self) -> FRect: ...
    def copy(self) -> Circle: ...
    def __copy__(self) -> Circle: ...

class Line:
    @property
    def ax(self) -> float: ...
    @ax.setter
    def ax(self, value: float) -> None: ...
    @property
    def ay(self) -> float: ...
    @ay.setter
    def ay(self, value: float) -> None: ...
    @property
    def bx(self) -> float: ...
    @bx.setter
    def bx(self, value: float) -> None: ...
    @property
    def by(self) -> float: ...
    @by.setter
    def by(self, value: float) -> None: ...
    @property
    def a(self) -> tuple[float, float]: ...
    @a.setter
    def a(self, value: Point) -> None: ...
    @property
    def b(self) -> tuple[float, float]: ...
    @b.setter
    def b(self, value: Point) -> None: ...
    @overload
    def __init__(self, ax: float, ay: float, bx: float, by: float) -> None: ...
    @overload
    def __init__(self, a: Point, b: Point) -> None: ...
    @overload
    def __init__(self, line: _LineLike) -> None: ...
    def __copy__(self) -> Line: ...
    def copy(self) -> Line: ...
