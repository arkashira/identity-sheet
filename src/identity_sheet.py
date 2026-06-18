import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Identity:
    id: int
    name: str

class IdentitySheet:
    def __init__(self):
        self.identities: Dict[int, Identity] = {}
        self.spreadsheet: Dict[int, List[int]] = {}

    def create_identity(self, id: int, name: str) -> Identity:
        if id in self.identities:
            raise ValueError("Identity already exists")
        identity = Identity(id, name)
        self.identities[id] = identity
        return identity

    def reference_identity(self, id: int, spreadsheet_id: int) -> None:
        if id not in self.identities:
            raise ValueError("Identity does not exist")
        if spreadsheet_id not in self.spreadsheet:
            self.spreadsheet[spreadsheet_id] = []
        self.spreadsheet[spreadsheet_id].append(id)

    def update_spreadsheet(self, spreadsheet_id: int, new_references: List[int]) -> None:
        if spreadsheet_id not in self.spreadsheet:
            raise ValueError("Spreadsheet does not exist")
        self.spreadsheet[spreadsheet_id] = new_references

    def get_references(self, spreadsheet_id: int) -> List[Identity]:
        if spreadsheet_id not in self.spreadsheet:
            raise ValueError("Spreadsheet does not exist")
        return [self.identities[id] for id in self.spreadsheet[spreadsheet_id]]

    def to_json(self) -> str:
        data = {
            "identities": [{"id": id, "name": identity.name} for id, identity in self.identities.items()],
            "spreadsheet": {str(spreadsheet_id): references for spreadsheet_id, references in self.spreadsheet.items()}
        }
        return json.dumps(data)
