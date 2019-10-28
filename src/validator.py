from fastjsonschema import compile as compile_schema


def validate_payload(payload):
    """ @throws JsonSchemaException """
    validate(payload)


validate = compile_schema({
    'type': 'object',
    'required': ['rdi', 'vb'],
    'properties': {
        'rdi': {
            'type': 'string',
            'pattern': '^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$'
        },
        'vb': {
            'type': 'array',
            'minItems': 1
        }
    }
})
