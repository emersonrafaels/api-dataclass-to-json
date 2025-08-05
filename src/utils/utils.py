import json
from dataclasses import asdict
from typing import Any

def to_json(obj: Any, ensure_ascii: bool = False, indent: int = 2) -> str:
    """
    Converte um objeto ou lista de objetos (dataclass) para uma string JSON formatada.
    Se o objeto não for dataclass, tenta converter diretamente.
    """
    if isinstance(obj, list):
        obj_dict = [asdict(o) if hasattr(o, '__dataclass_fields__') else o for o in obj]
    elif hasattr(obj, '__dataclass_fields__'):
        obj_dict = asdict(obj)
    else:
        obj_dict = obj
    return json.dumps(obj_dict, ensure_ascii=ensure_ascii, indent=indent)

def is_json(s: str) -> bool:
    """
    Valida se uma string é um JSON válido.
    Retorna True se válido, False caso contrário.
    """
    try:
        json.loads(s)
        return True
    except (ValueError, TypeError):
        return False
