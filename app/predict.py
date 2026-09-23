import pandas as pd
import joblib

# Load saved model files
model = joblib.load(
    "/home/sankar/Documents/Flight-delay-prediction/models/flight_delay_xgboost.pkl"
)

threshold = joblib.load(
    "/home/sankar/Documents/Flight-delay-prediction/models/threshold.pkl"
)

category_mappings = joblib.load(
    "/home/sankar/Documents/Flight-delay-prediction/models/category_mappings.pkl"
)


def predict_flight_delay(
    airline,
    origin_airport,
    destination_airport,
    month,
    day,
    day_of_week,
    departure_hour,
    scheduled_time,
    distance,
    is_weekend
):

    # Check whether airline exists
    if airline not in category_mappings["AIRLINE"]:
        return f"Unknown airline: {airline}"

    # Check whether origin airport exists
    if origin_airport not in category_mappings["ORIGIN_AIRPORT"]:
        return f"Unknown origin airport: {origin_airport}"

    # Check whether destination airport exists
    if destination_airport not in category_mappings["DESTINATION_AIRPORT"]:
        return f"Unknown destination airport: {destination_airport}"

    # Convert categorical values to training codes
    airline_code = category_mappings["AIRLINE"].index(airline)

    origin_code = category_mappings["ORIGIN_AIRPORT"].index(
        origin_airport
    )

    destination_code = category_mappings["DESTINATION_AIRPORT"].index(
        destination_airport
    )

    # Create input data
    input_data = pd.DataFrame([{
        "AIRLINE": airline_code,
        "ORIGIN_AIRPORT": origin_code,
        "DESTINATION_AIRPORT": destination_code,
        "MONTH": month,
        "DAY": day,
        "DAY_OF_WEEK": day_of_week,
        "DEPARTURE_HOUR": departure_hour,
        "SCHEDULED_TIME": scheduled_time,
        "DISTANCE": distance,
        "IS_WEEKEND": is_weekend
    }])

    # Get delay probability
    probability = model.predict_proba(input_data)[0][1]

    # Apply threshold
    prediction = int(probability >= threshold)

    if prediction == 1:
        result = "DELAYED"
    else:
        result = "NOT DELAYED"

    return {
        "prediction": result,
        "delay_probability": round(float(probability) * 100, 2),
        "threshold": threshold
    }