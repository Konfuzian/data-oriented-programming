from validate_json_schema import validate

book_info_schema = {
	"type": "object",
	"required": ["title", "available"],
	"properties": {
		"title": {"type": "string"},
		"available": {"type": "boolean"},
		"subtitle": {"type": "string"},
		"number_of_pages": {"type": "integer"},
		"subjects": {
			"type": "array",
			"items": {"type": "string"}
		},
		"isbn": {"type": "string"},
		"isbn_13": {"type": "string"}
	}
}

schema = {
	"type": "array",
	"items": book_info_schema
}

valid = [
	{
		"title": "7 Habits of Highly Effective People",
		"available": True,
		"isbn": "978-0812981605",
		"subtitle": "Powerful Lessons in Personal Change",
		"number_of_pages": 432
	},
	{
		"title": "The Power of Habit",
		"available": False,
		"isbn_13": "978-1982137274",
		"subtitle": "Why We Do What We Do in Life and Business",
		"subjects": [
			"Social aspects",
			"Habit",
			"Change (Psychology)"
		]
	}
]

invalid = {}

validate(schema, valid)
#validate(schema, invalid)
