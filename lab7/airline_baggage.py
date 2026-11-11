def parse_booking(code):
    if not code or not isinstance(code, str):
        return None
    parts = code.strip().split('-')
    if len(parts) != 3:
        return None
    airline, flight, seat = parts
    if not airline or not flight.isdigit() or not seat:
        return None
    return airline.upper(), int(flight), seat[-1].upper()

def total_weight(weights_csv):
    if not weights_csv or not isinstance(weights_csv, str):
        return 0.0
    total = 0.0
    for w in weights_csv.split(','):
        cleaned = w.strip()
        if cleaned:
            try:
                total += float(cleaned)
            except ValueError:
                pass
    return round(total, 2)

def tag_label(name):
    if not name or not isinstance(name, str):
        return ""
    parts = name.strip().split()
    if len(parts) == 0:
        return ""
    elif len(parts) == 1:
        return parts[0].upper()
    return parts[0][0].upper() + '. ' + parts[1].upper()

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)

if __name__ == "__main__":
    main()
