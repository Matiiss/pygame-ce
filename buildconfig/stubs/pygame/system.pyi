from typing import Optional, TypedDict

from pygame._data_classes import PowerState

class _InstructionSets(TypedDict):
    ALTIVEC: bool
    MMX: bool
    SSE: bool
    SSE2: bool
    SSE3: bool
    SSE41: bool
    SSE42: bool
    AVX: bool
    AVX2: bool
    AVX512F: bool
    NEON: bool
    ARMSIMD: bool
    LSX: bool
    LASX: bool

class _Locale(TypedDict):
    language: str
    country: Optional[str]

def get_cpu_instruction_sets() -> _InstructionSets: ...
def get_total_ram() -> int: ...
def get_pref_path(org: str, app: str) -> str: ...
def get_pref_locales() -> list[_Locale]: ...
def get_power_state() -> Optional[PowerState]: ...
