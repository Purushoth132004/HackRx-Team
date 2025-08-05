from app.query_parser import parse_health_query

query = "62-year-old man, cataract surgery in Delhi, 10-month-old policy"

result = parse_health_query(query)

print("🎯 Parsed Result:", result)
