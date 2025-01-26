import json
from typing import Any, Type, TypeVar
from dataclasses import dataclass, asdict
import tomlkit as toml
import yaml


__all__ = [
    "BaseConfig",
]

T = TypeVar("T", bound="BaseConfig")


@dataclass
class BaseConfig:
    def to_dict(self) -> dict[str, Any]:
        """Convert the dataclass instance to a dictionary.

        Returns:
            dict: A dictionary representation of the dataclass instance.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls: Type[T], data: dict[str, Any]) -> T:
        """Create a dataclass instance from a dictionary.

        Args:
            data (dict): A dictionary containing the data to populate the dataclass.

        Returns:
            BaseConfig: An instance of the dataclass.
        """
        return cls(**data)

    def to_toml(self) -> str:
        """Convert the dataclass instance to a TOML string.

        Returns:
            str: A TOML string representation of the dataclass instance.
        """
        return toml.dumps(self.to_dict())

    @classmethod
    def from_toml(cls: Type[T], toml_str: str) -> T:
        """Create a dataclass instance from a TOML string.

        Args:
            toml_str (str): A TOML string containing the data to populate the dataclass.

        Returns:
            BaseConfig: An instance of the dataclass.
        """
        data = toml.loads(toml_str)
        return cls.from_dict(data)

    def to_json(self) -> str:
        """Convert the dataclass instance to a JSON string.

        Returns:
            str: A JSON string representation of the dataclass instance.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        """Create a dataclass instance from a JSON string.

        Args:
            json_str (str): A JSON string containing the data to populate the dataclass.

        Returns:
            BaseConfig: An instance of the dataclass.
        """
        data = json.loads(json_str)
        return cls.from_dict(data)

    def to_yaml(self) -> str:
        """Convert the dataclass instance to a YAML string.

        Returns:
            str: A YAML string representation of the dataclass instance.
        """
        return yaml.dump(self.to_dict())

    @classmethod
    def from_yaml(cls: Type[T], yaml_str: str) -> T:
        """Create a dataclass instance from a YAML string.

        Args:
            yaml_str (str): A YAML string containing the data to populate the dataclass.

        Returns:
            BaseConfig: An instance of the dataclass.
        """
        data = yaml.safe_load(yaml_str)
        return cls.from_dict(data)
