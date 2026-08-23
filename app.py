import streamlit as st
import pandas as pd
import joblib


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="RecoverAI",
    page_icon="💰",
    layout="wide"
)


# -------------------------------------------------
# LOAD MODEL AND DATA
# -------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("recovery_model.pkl")


@st.cache_data
def load_data():
    return pd.read_csv("payment_failures.csv")


model = load_model()
data = load_data()


# -------------------------------------------------
# RECOMMENDATION FUNCTION
# -------------------------------------------------

def recommend_action(row):
    probability = row["predicted_recovery_probability"]
    failure_reason = row["failure_reason"]
    attempts = row["customer_attempts"]

    if probability >= 0.75:
        if failure_reason == "Network Error":
            return "Retry payment automatically in 15 minutes"

        elif failure_reason == "Authentication Failed":
            return "Send instant payment reminder with secure payment link"

        elif failure_reason == "Bank Declined":
            return "Ask customer to retry using an alternate payment method"

        else:
            return "Send instant payment reminder with secure payment link"

    elif probability >= 0.50:

        if attempts < 3:
            return "Send personalized recovery reminder"

        else:
            return "Retry once and monitor payment status"

    else:
        return "Monitor customer and avoid repeated payment retries"


# -------------------------------------------------
# CREATE PREDICTIONS FOR DASHBOARD
# -------------------------------------------------

features = [
    "amount",
    "payment_method",
    "failure_reason",
    "customer_attempts",
    "hour"
]


@st.cache_data
def prepare_dashboard_data(data):
    dashboard_data = data.copy()

    dashboard_data["predicted_recovery_probability"] = (
        model.predict_proba(dashboard_data[features])[:, 1]
    )

    dashboard_data["expected_recovery_value"] = (
        dashboard_data["amount"]
        * dashboard_data["predicted_recovery_probability"]
    )

    dashboard_data["recommended_action"] = dashboard_data.apply(
        recommend_action,
        axis=1
    )

    return dashboard_data


dashboard_data = prepare_dashboard_data(data)


# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("💰 RecoverAI")

st.subheader("Autonomous AI Revenue Recovery Agent")

st.write(
    "Identify high-value failed payments, predict recovery potential, "
    "and recommend the best action to recover lost revenue."
)


# -------------------------------------------------
# METRICS
# -------------------------------------------------

total_failed = len(dashboard_data)

total_revenue_at_risk = dashboard_data["amount"].sum()

total_expected_recovery = (
    dashboard_data["expected_recovery_value"].sum()
)

high_priority_cases = len(
    dashboard_data[
        dashboard_data["predicted_recovery_probability"] >= 0.75
    ]
)


metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Failed Transactions",
    f"{total_failed:,}"
)

metric2.metric(
    "Revenue at Risk",
    f"₹{total_revenue_at_risk:,.0f}"
)

metric3.metric(
    "Expected Recovery",
    f"₹{total_expected_recovery:,.0f}"
)

metric4.metric(
    "High Priority Cases",
    f"{high_priority_cases:,}"
)


st.divider()


# -------------------------------------------------
# TABS
# -------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "📊 Recovery Dashboard",
        "🎯 Priority Queue",
        "🤖 AI Recovery Agent"
    ]
)


# =================================================
# TAB 1 - RECOVERY DASHBOARD
# =================================================
# =================================================
# TAB 1 - RECOVERY DASHBOARD
# =================================================

with tab1:

    st.subheader("Revenue Recovery Overview")

    # -------------------------------------------------
    # Expected Recovery by Failure Reason
    # -------------------------------------------------

    chart_data = (
        dashboard_data
        .groupby("failure_reason")["expected_recovery_value"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(chart_data)


    # -------------------------------------------------
    # Expected Recovery by Payment Method
    # -------------------------------------------------

    st.subheader("Expected Recovery by Payment Method")

    payment_method_data = (
        dashboard_data
        .groupby("payment_method")["expected_recovery_value"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(payment_method_data)


    # -------------------------------------------------
    # Recovery Probability Distribution
    # -------------------------------------------------

    st.subheader("Recovery Probability Distribution")

    probability_bins = pd.cut(
        dashboard_data["predicted_recovery_probability"],
        bins=[0, 0.25, 0.50, 0.75, 1.0],
        labels=[
            "Low (0-25%)",
            "Moderate (25-50%)",
            "High (50-75%)",
            "Very High (75-100%)"
        ],
        include_lowest=True
    )

    probability_distribution = (
        probability_bins
        .value_counts()
        .sort_index()
    )

    st.bar_chart(probability_distribution)


    # -------------------------------------------------
    # Priority Distribution
    # -------------------------------------------------

    st.subheader("Recovery Priority Distribution")

    def get_priority(probability):

        if probability >= 0.75:
            return "High Priority"

        elif probability >= 0.50:
            return "Medium Priority"

        else:
            return "Low Priority"


    priority_distribution = (
        dashboard_data["predicted_recovery_probability"]
        .apply(get_priority)
        .value_counts()
    )

    priority_order = [
        "High Priority",
        "Medium Priority",
        "Low Priority"
    ]

    priority_distribution = (
        priority_distribution
        .reindex(priority_order, fill_value=0)
    )

    st.bar_chart(priority_distribution)


# =================================================
# TAB 2 - PRIORITY QUEUE
# =================================================

with tab2:

    st.subheader("High-Value Recovery Opportunities")

    priority_data = dashboard_data[
        dashboard_data["predicted_recovery_probability"] >= 0.75
    ].copy()

    priority_data = priority_data.sort_values(
        by="expected_recovery_value",
        ascending=False
    )

    display_columns = [
        "transaction_id",
        "amount",
        "payment_method",
        "failure_reason",
        "customer_attempts",
        "predicted_recovery_probability",
        "expected_recovery_value",
        "recommended_action"
    ]

    st.dataframe(
        priority_data[display_columns].head(50)
    )


# =================================================
# TAB 3 - AI RECOVERY AGENT
# =================================================

with tab3:

    st.subheader("Analyze a Failed Payment")

    col1, col2 = st.columns(2)


    # ---------------------------------------------
    # LEFT COLUMN
    # ---------------------------------------------

    with col1:

        amount = st.number_input(
            "Transaction Amount (₹)",
            min_value=100,
            max_value=100000,
            value=45000,
            step=100
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "UPI",
                "Card",
                "Netbanking",
                "Wallet"
            ]
        )

        failure_reason = st.selectbox(
            "Failure Reason",
            [
                "Insufficient Funds",
                "Bank Declined",
                "Network Error",
                "Timeout",
                "Authentication Failed"
            ]
        )


    # ---------------------------------------------
    # RIGHT COLUMN
    # ---------------------------------------------

    with col2:

        customer_attempts = st.slider(
            "Previous Attempts",
            min_value=1,
            max_value=5,
            value=2
        )

        hour = st.slider(
            "Hour of Failure",
            min_value=0,
            max_value=23,
            value=12
        )


    # ---------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------

    if st.button(
        "🤖 Analyze Recovery Opportunity",
        type="primary"
    ):

        # Create input dataframe
        input_data = pd.DataFrame({
            "amount": [amount],
            "payment_method": [payment_method],
            "failure_reason": [failure_reason],
            "customer_attempts": [customer_attempts],
            "hour": [hour]
        })


        # Predict recovery probability
        probability = model.predict_proba(
            input_data[features]
        )[0][1]


        # Calculate expected recovery
        expected_value = amount * probability


        # Create result dataframe
        result = input_data.copy()

        result["predicted_recovery_probability"] = probability


        # Get recommended action
        action = recommend_action(
            result.iloc[0]
        )


        # -----------------------------------------
        # DISPLAY RESULTS
        # -----------------------------------------

        st.divider()

        metric1, metric2 = st.columns(2)


        metric1.metric(
            "Recovery Probability",
            f"{probability:.1%}"
        )


        metric2.metric(
            "Potential Recoverable Revenue",
            f"₹{expected_value:,.0f}"
        )


        st.success(
            f"Recommended Action: {action}"
        )


        # -----------------------------------------
        # AI AGENT DECISION
        # -----------------------------------------

        if probability >= 0.75:

            st.success(
                f"""
### 🤖 AI Agent Decision: HIGH PRIORITY

**Recommended Action:** {action}

This payment has a **high probability of recovery**.

The RecoverAI agent recommends taking immediate action to maximize the chance of recovering **₹{expected_value:,.0f}**.
"""
            )


        elif probability >= 0.50:

            st.warning(
                f"""
### 🤖 AI Agent Decision: MEDIUM PRIORITY

**Recommended Action:** {action}

This payment has a moderate probability of recovery.

The RecoverAI agent recommends a controlled recovery attempt.
"""
            )


        else:

            st.info(
                f"""
### 🤖 AI Agent Decision: LOW PRIORITY

**Recommended Action:** {action}

This payment currently has a low probability of recovery.

Avoid excessive retries and continue monitoring the customer.
"""
            )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "RecoverAI • AI-powered failed payment prioritization "
    "and revenue recovery prototype"
)