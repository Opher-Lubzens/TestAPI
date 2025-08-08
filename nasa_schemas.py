APOD_SINGLE_SCHEMA = {
    "type": "object",
    "properties": {
        "date": {"type": "string", "format": "date-time"},
        "explanation": {"type": "string"},
        "hdurl": {"type": "string"},
        "media_type": {"type": "string"},
        "service_version": {"type": "string"},
        "title": {"type": "string"},
        "url": {"type": "string"}
    }
}

APOD_MULTI_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
                "date": {"type": "string", "format": "date-time"},
                "explanation": {"type": "string"},
                "hdurl": {"type": "string"},
                "media_type": {"type": "string"},
                "service_version": {"type": "string"},
                "title": {"type": "string"},
                "url": {"type": "string"}
        }
    }
}