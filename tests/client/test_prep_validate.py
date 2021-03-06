import json
from pyapacheatlas.core import AtlasClient, AtlasEntity

sample_entity = {
      "typeName": "hive_column",
      "attributes": {
        "owner": "admin",
        "replicatedTo": [],
        "replicatedFrom": [],
        "qualifiedName": "hivedbtest.point_derived.y_value@primary",
        "name": "y_value",
        "description": None,
        "comment": None,
        "position": 1,
        "type": "int",
        "table": {
          "guid": "79e5659a-70c9-4ac9-bced-d28ac86a60cd",
          "typeName": "hive_table"
        }
      },
      "guid": "95f5da92-545b-44ac-8393-427f706cc7bb",
      "relationshipAttributes": {
        "inputToProcesses": [],
        "schema": [],
        "attachedSchema": [],
        "meanings": [],
        "table": {
          "guid": "79e5659a-70c9-4ac9-bced-d28ac86a60cd",
          "typeName": "hive_table",
          "entityStatus": "ACTIVE",
          "displayText": "point_derived",
          "relationshipType": "hive_table_columns",
          "relationshipGuid": "1dc9aed8-011e-4c0f-b879-90ba3c59ef78",
          "relationshipStatus": "ACTIVE",
          "relationshipAttributes": {
            "typeName": "hive_table_columns"
          }
        }
    }
}


def test_prepare_bulk_entity_from_list():
    results = AtlasClient._prepare_entity_upload([sample_entity])

    expected = {"entities": [sample_entity]}

    assert(results == expected)

def test_prepare_bulk_entity_from_dict():
    results = AtlasClient._prepare_entity_upload({"entities":[sample_entity]})

    expected = {"entities": [sample_entity]}

    assert(results == expected)

def test_prepare_bulk_entity_from_atlas_entity():

    class_entity = AtlasEntity(
        name=sample_entity["attributes"]["name"], 
        typeName=sample_entity["typeName"], 
        qualified_name=sample_entity["attributes"]["qualifiedName"],
        attributes=sample_entity["attributes"],
        guid=sample_entity["guid"],
        relationshipAttributes= sample_entity["relationshipAttributes"]
    )

    results = AtlasClient._prepare_entity_upload(class_entity)

    expected = {"entities": [sample_entity]}

    assert(results == expected)