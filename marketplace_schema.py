EOD_SCHEMA = {
    "type": "object",
    "required": ["pagination", "data"],
    "properties": {
        "pagination": {
            "type": "object",
            "required": ["limit", "offset", "count", "total"],
            "properties": {
                "limit":   {"type": "integer", "minimum": 0},
                "offset":  {"type": "integer", "minimum": 0},
                "count":   {"type": "integer", "minimum": 0},
                "total":   {"type": "integer", "minimum": 0}
            },
            "additionalProperties": False
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "date", "symbol", "exchange", "open", "high", "low",
                    "close", "volume", "adj_open", "adj_high", "adj_low",
                    "adj_close", "adj_volume", "split_factor", "dividend",
                    "name", "exchange_code", "asset_type", "price_currency"
                ],
                "properties": {
                    "date": {"type": "string", "format": "date-time"},
                    "symbol": {"type": "string"},
                    "exchange": {"type": "string"},
                    "exchange_code": {"type": "string"},
                    "name": {"type": "string"},
                    "asset_type": {"type": "string"},
                    "price_currency": {"type": "string"},
                    "open": {"type": "number"},
                    "high": {"type": "number"},
                    "low": {"type": "number"},
                    "close": {"type": "number"},
                    "volume": {"type": "number"},
                    "adj_open": {"type": "number"},
                    "adj_high": {"type": "number"},
                    "adj_low": {"type": "number"},
                    "adj_close": {"type": "number"},
                    "adj_volume": {"type": "number"},
                    "split_factor": {"type": "number"},
                    "dividend": {"type": "number"}
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}