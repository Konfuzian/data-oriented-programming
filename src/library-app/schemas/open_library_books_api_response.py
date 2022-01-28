from validate_json_schema import validate


basic_book_info_schema = {
  "type": "object",
  "required": ["title"],
  "properties": {
    "title": {"type": "string"},
    "publishers": {
      "type": "array",
      "items": {"type": "string"}
    },
    "number_of_pages": {"type": "integer"},
    "weight": {"type": "string"},
    "physical_format": {"type": "string"},
    "subjects": {
      "type": "array",
      "items": {"type": "string"}
    },
    "isbn_13": {
      "type": "array",
      "items": {"type": "string"}
    },
    "isbn_10": {
      "type": "array",
      "items": {"type": "string"}
    },
    "publish_date": {"type": "string"},
    "physical_dimensions": {"type": "string"}
  }
}

mandatory_isbn_13_schema = {
  "type": "object",
  "required": ["isbn_13"]
}

mandatory_isbn_10_schema = {
  "type": "object",
  "required": ["isbn_10"]
}

schema = {
  "allOf": [
    basic_book_info_schema,
    {
      "anyOf": [mandatory_isbn_13_schema, mandatory_isbn_10_schema]
    }
  ]
}

valid = {
	"publishers": [
		"DC Comics"
	],
	"number_of_pages": 334,
	"weight": "1.4 pounds",
	"physical_format": "Paperback",
	"subjects": [
		"Graphic Novels",
		"Comics & Graphic Novels",
		"Fiction",
		"Fantastic fiction"
	],
	"isbn_13": [
		"9780930289232"
	],
	"title": "Watchmen",
	"isbn_10": [
		"0930289234"
	],
	"publish_date": "April 1, 1995",
	"physical_dimensions": "10.1 x 6.6 x 0.8 inches"
}

invalid = {
	"publishers": [
		"DC Comics"
	],
	"number_of_pages": 334,
	"weight": "1.4 pounds",
	"physical_format": "Paperback",
	"subjects": [
		"Graphic Novels",
		"Comics & Graphic Novels",
		"Fiction",
		"Fantastic fiction"
	],
	"title": "Watchmen",
	"publish_date": "April 1, 1995",
	"physical_dimensions": "10.1 x 6.6 x 0.8 inches"
}

validate(schema, valid)
#validate(schema, invalid)
