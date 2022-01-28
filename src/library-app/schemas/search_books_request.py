from validate_json_schema import validate

schema = {
	"type": "object",
	"properties": {
		"title": {"type": "string"},
		"fields": {
			"type": "array",
			"items": {"type": "string"}
		}
	},
	"required": ["title", "fields"]
}

valid = {
	"title": "habit",
	"fields": ["title", "weight", "number_of_pages"]
}

invalid = {
	"tilte": "habit",
	"fields": ["title", "weight", "number_of_pages"]
}

validate(schema, valid)
#validate(schema, invalid)
