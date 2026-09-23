import streamlit as st
from predict import predict_flight_delay

# --------------------------------------------------
# Reset Function
# --------------------------------------------------

def reset_fields():
    st.session_state.airline = "AA"
    st.session_state.origin = sorted(
        predict_flight_delay.__globals__["category_mappings"]["ORIGIN_AIRPORT"]
    )[0]
    st.session_state.destination = sorted(
        predict_flight_delay.__globals__["category_mappings"]["DESTINATION_AIRPORT"]
    )[0]
    st.session_state.month = 1
    st.session_state.day = 1
    st.session_state.day_of_week = 0
    st.session_state.departure_hour = 10
    st.session_state.scheduled_time = 120
    st.session_state.distance = 500
    st.session_state.is_weekend = 0


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="centered"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("✈️ About the Project")

    st.write("Flight Delay Prediction System")
    st.write("Machine Learning Model: XGBoost")
    st.write("Prediction: Delayed / Not Delayed")
    st.write("Decision Threshold: 55%")

    st.divider()

    st.subheader("📈 Model Performance")

    st.write("Accuracy: 71.56%")
    st.write("Precision: 33.70%")
    st.write("Recall: 55.96%")
    st.write("F1 Score: 42.07%")
    st.write("ROC-AUC: 71.75%")


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("✈️ Flight Delay Prediction System")

st.caption(
    "Predicting flight delays using Machine Learning and XGBoost"
)

st.markdown(
    """
    **Flight Delay Prediction System** uses an XGBoost machine
    learning model to estimate the probability of a flight delay.

    Enter the flight details below and click **Predict Flight Delay**
    to get the prediction.
    """
)

st.divider()


# --------------------------------------------------
# Flight Information
# --------------------------------------------------

st.header("🛫 Flight Information")

col1, col2 = st.columns(2)


# --------------------------------------------------
# Column 1
# --------------------------------------------------

with col1:

    airline = st.selectbox(
        "Airline Code",
        options=[
            "AA", "AS", "B6", "DL", "EV", "F9",
            "HA", "MQ", "NK", "OO", "UA", "US",
            "VX", "WN"
        ],
        key="airline"
    )

    origin = st.selectbox(
        "Origin Airport",
        options=sorted(
            predict_flight_delay.__globals__["category_mappings"]["ORIGIN_AIRPORT"]
        ),
        key="origin"
    )

    destination = st.selectbox(
        "Destination Airport",
        options=sorted(
            predict_flight_delay.__globals__["category_mappings"]["DESTINATION_AIRPORT"]
        ),
        key="destination"
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1,
        key="month"
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1,
        key="day"
    )


# --------------------------------------------------
# Column 2
# --------------------------------------------------

with col2:

    day_of_week = st.number_input(
        "Day of Week",
        min_value=0,
        max_value=6,
        value=0,
        help="0 = Monday, 6 = Sunday",
        key="day_of_week"
    )

    departure_hour = st.number_input(
        "Departure Hour",
        min_value=0,
        max_value=23,
        value=10,
        key="departure_hour"
    )

    scheduled_time = st.number_input(
        "Scheduled Time (minutes)",
        min_value=1,
        value=120,
        key="scheduled_time"
    )

    distance = st.number_input(
        "Distance (miles)",
        min_value=1,
        value=500,
        key="distance"
    )

    is_weekend = st.selectbox(
        "Is it Weekend?",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No",
        key="is_weekend"
    )


st.divider()


# --------------------------------------------------
# Buttons
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    predict_button = st.button(
        "🔮 Predict Flight Delay",
        use_container_width=True
    )


with col2:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True,
        on_click=reset_fields
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    result = predict_flight_delay(
        airline=airline.upper(),
        origin_airport=origin.upper(),
        destination_airport=destination.upper(),
        month=month,
        day=day,
        day_of_week=day_of_week,
        departure_hour=departure_hour,
        scheduled_time=scheduled_time,
        distance=distance,
        is_weekend=is_weekend
    )


    # --------------------------------------------------
    # Prediction Result
    # --------------------------------------------------

    st.header("📊 Prediction Result")


    if isinstance(result, str):

        st.error(f"❌ {result}")


    else:

        prediction = result["prediction"]
        probability = result["delay_probability"]


        if prediction == "DELAYED":

            st.error(
                "🔴 FLIGHT IS PREDICTED TO BE DELAYED"
            )

        else:

            st.success(
                "🟢 FLIGHT IS PREDICTED NOT TO BE DELAYED"
            )


        st.metric(
            label="Delay Probability",
            value=f"{probability}%"
        )


        st.caption(
            "This percentage represents the model's estimated probability "
            "that the flight will be delayed."
        )


        st.progress(
            min(probability / 100, 1.0)
        )


        if probability >= 75:

            st.warning(
                "⚠️ High risk of flight delay"
            )

        elif probability >= 55:

            st.info(
                "ℹ️ Moderate risk of flight delay"
            )

        else:

            st.success(
                "✅ Low risk of flight delay"
            )


        st.info(
            f"Decision Threshold: "
            f"{result['threshold'] * 100:.0f}%"
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Flight Delay Prediction System"
)


# --------------------------------------------------
# About the Model
# --------------------------------------------------

st.markdown(
    """
    ### About the Model

    - **Algorithm:** XGBoost Classifier
    - **Prediction:** Delayed / Not Delayed
    - **Decision Threshold:** 55%
    - **Input Features:** 10
    - **Model Type:** Supervised Machine Learning
    """
)


# --------------------------------------------------
# How It Works
# --------------------------------------------------

st.divider()

st.header("⚙️ How It Works")

st.write(
    "1️⃣ Enter the flight details."
)

st.write(
    "2️⃣ The XGBoost model processes the input data."
)

st.write(
    "3️⃣ The model calculates the probability of a flight delay."
)

st.write(
    "4️⃣ A 55% decision threshold is used to classify the flight."
)

st.write(
    "5️⃣ The system displays the final prediction and delay probability."
)
