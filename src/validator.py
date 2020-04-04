from fastjsonschema import compile as compile_schema


def validate_payload(payload):
    """ @throws JsonSchemaException """
    validate(payload)


validate = compile_schema({
    'type': 'object',
    'required': ['id', 'array'],
    'properties': {
        'id': {
            'type': 'string',
            'pattern': '^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$'
        },
        'array': {
            'type': 'array',
            'minItems': 1
        }
    }
})
