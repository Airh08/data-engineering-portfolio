from dataclasses import asdict, dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any


def json_file_path(filename: str = "info.json") -> Path:
    """Build a path inside the directory used by JSON examples."""
    base_dir = Path(__file__).resolve().parent.parent
    return base_dir / "src" / filename


def search_json_files(filename: str = "info.json") -> Path:
    """Return an existing JSON file or raise a clear error."""
    file_path = json_file_path(filename)
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")
    return file_path


def write_json_file(data: object, filename: str = "example_dump.json") -> Path:
    """Write JSON to a new or existing file using readable UTF-8 output."""
    file_path = json_file_path(filename)
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    return file_path


def read_json_file(filename: str = "info.json") -> Any:
    """Read an existing JSON file with explicit UTF-8 decoding."""
    file_path = search_json_files(filename)
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def parse_json_text(json_text: str) -> Any:
    """Parse JSON text and let JSONDecodeError reach the caller."""
    return json.loads(json_text)


def nested_json_example() -> dict[str, Any]:
    """Create and parse a nested JSON object in memory."""
    data = {"id": 1, "name": "order", "metadata": {"source": "api"}}
    return parse_json_text(json.dumps(data))


@dataclass
class UserProfile:
    first_name: str
    last_name: str
    country: str


@dataclass
class UserRecord:
    id: int
    uuid: str
    username: str
    is_active: bool
    score: float
    roles: list[str]
    profile: UserProfile
    last_login: datetime


def validate_info_payload(data: object) -> dict[str, Any]:
    """Validate required top-level fields before creating a dataclass."""
    if not isinstance(data, dict):
        raise TypeError("The JSON root must be an object")
    required_fields = {
        "id", "uuid", "username", "isActive", "score", "roles", "profile", "lastLogin"
    }
    missing_fields = required_fields - data.keys()
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Missing required fields: {missing}")
    if not isinstance(data["profile"], dict):
        raise TypeError("The profile field must be an object")
    return data


def iso_to_datetime(value: str) -> datetime:
    """Convert a JSON ISO timestamp with Z into a datetime."""
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    return datetime.fromisoformat(normalized)


def info_to_dataclass(data: object) -> UserRecord:
    """Convert validated info.json data into nested dataclasses."""
    payload = validate_info_payload(data)
    profile = payload["profile"]
    return UserRecord(
        id=payload["id"],
        uuid=payload["uuid"],
        username=payload["username"],
        is_active=payload["isActive"],
        score=payload["score"],
        roles=payload["roles"],
        profile=UserProfile(
            first_name=profile["firstName"],
            last_name=profile["lastName"],
            country=profile["country"],
        ),
        last_login=iso_to_datetime(payload["lastLogin"]),
    )


def dataclass_to_json(user: UserRecord) -> str:
    """Convert a dataclass to JSON while preserving the input field names."""
    data = asdict(user)
    data["isActive"] = data.pop("is_active")
    data["lastLogin"] = data.pop("last_login").isoformat().replace("+00:00", "Z")
    profile = data["profile"]
    data["profile"] = {
        "firstName": profile["first_name"],
        "lastName": profile["last_name"],
        "country": profile["country"],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    print("Writing JSON")
    print(write_json_file({"message": "Hola", "values": [1, 2, 3]}))
    print("Reading real info.json")
    info_data = read_json_file()
    print(info_data)
    user = info_to_dataclass(info_data)
    print(f"Dataclass: {user}")
    print(f"Dataclass to JSON:\n{dataclass_to_json(user)}")
    print(f"Nested JSON: {nested_json_example()}")

    try:
        parse_json_text("not-json")
    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error.msg}")

    try:
        validate_info_payload({"id": 1})
    except ValueError as error:
        print(f"Invalid structure: {error}")