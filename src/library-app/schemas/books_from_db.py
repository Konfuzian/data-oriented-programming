from validate_json_schema import validate

schema = {
	"type": "array",
	"items": {
		"type": "object",
		"required": ["title", "isbn", "available"],
		"additionalProperties": False,
		"properties": {
			"title": {"type": "string"},
			"available": {"type": "boolean"},
			"isbn": {"type": "string"}
		}
	}
}

valid = [
	{
		"title": "7 Habits of Highly Effective People",
		"available": True,
		"isbn": "978-0812981605"
	},
	{
		"title": "The Power of Habit",
		"available": False,
		"isbn": "978-1982137274"
	}
]

invalid = [
	{
		"title": "7 Habits of Highly Effective People",
		"available": True,
		"isbn": "978-0812981605",
		"dummy_property": 42
	},
	{
		"title": "The Power of Habit",
		"available": False,
		"isbn": "978-1982137274",
		"dummy_property": 45
	}
]

validate(schema, valid)
validate(schema, invalid)
