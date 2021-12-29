from pathlib import Path

def resolve_relative_path(caller, file_path) -> str:
    base_path = Path(caller).parent
    target_path = (base_path / file_path).resolve()
    print(target_path)
    return str(target_path)