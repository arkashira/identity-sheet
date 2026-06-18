import json
from identity_sheet import IdentitySheet, Identity

def test_create_identity():
    sheet = IdentitySheet()
    identity = sheet.create_identity(1, "John Doe")
    assert identity.id == 1
    assert identity.name == "John Doe"

def test_create_duplicate_identity():
    sheet = IdentitySheet()
    sheet.create_identity(1, "John Doe")
    try:
        sheet.create_identity(1, "Jane Doe")
        assert False
    except ValueError as e:
        assert str(e) == "Identity already exists"

def test_reference_identity():
    sheet = IdentitySheet()
    sheet.create_identity(1, "John Doe")
    sheet.reference_identity(1, 1)
    assert sheet.spreadsheet[1] == [1]

def test_reference_nonexistent_identity():
    sheet = IdentitySheet()
    try:
        sheet.reference_identity(1, 1)
        assert False
    except ValueError as e:
        assert str(e) == "Identity does not exist"

def test_update_spreadsheet():
    sheet = IdentitySheet()
    sheet.create_identity(1, "John Doe")
    sheet.create_identity(2, "Jane Doe")
    sheet.reference_identity(1, 1)
    sheet.update_spreadsheet(1, [2])
    assert sheet.spreadsheet[1] == [2]

def test_get_references():
    sheet = IdentitySheet()
    sheet.create_identity(1, "John Doe")
    sheet.create_identity(2, "Jane Doe")
    sheet.reference_identity(1, 1)
    sheet.reference_identity(2, 1)
    references = sheet.get_references(1)
    assert len(references) == 2
    assert references[0].id == 1
    assert references[1].id == 2

def test_to_json():
    sheet = IdentitySheet()
    sheet.create_identity(1, "John Doe")
    sheet.create_identity(2, "Jane Doe")
    sheet.reference_identity(1, 1)
    sheet.reference_identity(2, 1)
    json_data = sheet.to_json()
    data = json.loads(json_data)
    assert len(data["identities"]) == 2
    assert len(data["spreadsheet"]) == 1
    assert data["spreadsheet"]["1"] == [1, 2]
