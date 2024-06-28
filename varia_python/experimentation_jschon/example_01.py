
#
# from example on https://jschon.readthedocs.io/en/latest/
#
import json
from jschon import create_catalog, JSON, JSONSchema

create_catalog('2020-12')

demo_schema = JSONSchema({
    "$id": "https://example.com/demo",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "array",
    "items": {
        "anyOf": [
            {
                "type": "string",
                "description": "Cool! We got a string here!"
            },
            {
                "type": "integer",
                "description": "Hey! We got an integer here!"
            }
        ]
    }
})

result = demo_schema.evaluate(
    JSON([12, "Monkeys"])
)

generated = result.output('basic')
{
    "valid": True,
    "annotations": [
        {
            "instanceLocation": "",
            "keywordLocation": "/items",
            "absoluteKeywordLocation": "https://example.com/demo#/items",
            "annotation": True
        },
        {
            "instanceLocation": "/0",
            "keywordLocation": "/items/anyOf/1/description",
            "absoluteKeywordLocation": "https://example.com/demo#/items/anyOf/1/description",
            "annotation": "Hey! We got an integer here!"
        },
        {
            "instanceLocation": "/1",
            "keywordLocation": "/items/anyOf/0/description",
            "absoluteKeywordLocation": "https://example.com/demo#/items/anyOf/0/description",
            "annotation": "Cool! We got a string here!"
        }
    ]
}

print(json.dumps(generated,indent=4))
