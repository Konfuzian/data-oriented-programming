from jsonschema import validate as validate_schema
#from jschon import create_catalog, JSON, JSONSchema, URI


def validate(schema, data):
	# raises an exception if the data is invalid
	validate_schema(instance=data, schema=schema)


#def validate(schema, data, verbose=True):
#	create_catalog('2020-12')
#	json_schema = JSONSchema(schema, metaschema_uri=URI("https://json-schema.org/draft/2020-12/schema"))
#	result = json_schema.evaluate(JSON(data))
#	if verbose:
#		print(result.output('basic'))
#	return result
