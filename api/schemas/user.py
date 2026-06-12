USER_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string", "format": "uri"},
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"],
}

SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": USER_DATA_SCHEMA,
    },
    "required": ["data"],
}

USERS_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": USER_DATA_SCHEMA,
        },
    },
    "required": ["page", "per_page", "total", "total_pages", "data"],
}

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["name", "job", "id", "createdAt"],
}

NOT_FOUND_SCHEMA = {
    "type": "object",
    "properties": {},
    "additionalProperties": False,
}
