
from jschon import create_catalog, JSON, JSONSchema, URI


def validate(schema, data, verbose=True):

	create_catalog('2020-12')

	json_schema = JSONSchema(schema, metaschema_uri=URI("https://json-schema.org/draft/2020-12/schema"))
	json = JSON(data)

	result = json_schema.evaluate(json)

	if verbose:
		print(result.output('basic'))

	return result
