import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("🔋 Smart Battery Management System Dashboard")

# -------------------------
# User Inputs
# -------------------------
capacity = st.slider("Battery Capacity (Ah)", 50, 200, 100)
voltage = st.slider("Voltage (V)", 2.5, 4.2, 3.7)
current = st.slider("Current (A)", -50, 50, 10)
temperature = st.slider("Temperature (°C)", 20, 80, 30)

# -------------------------
# Calculations
# -------------------------
soc = (voltage - 2.5) / (4.2 - 2.5) * 100
power = voltage * current
efficiency = max(0, 100 - abs(current)*0.5)

# -------------------------
# Display Metrics
# -------------------------
st.subheader("📊 Battery Status")

st.metric("State of Charge (%)", f"{soc:.2f}")
st.metric("Power (W)", f"{power:.2f}")
st.metric("Efficiency (%)", f"{efficiency:.2f}")

# -------------------------
# Alerts
# -------------------------
st.subheader("⚠️ Alerts")

if voltage > 4.1:
    st.error("Overvoltage detected!")
elif voltage < 2.7:
    st.warning("Undervoltage condition!")
else:
    st.success("Voltage Normal")

if temperature > 60:
    st.error("High Temperature!")
else:
    st.success("Temperature Normal")

# -------------------------
# Simulation Graph
# -------------------------
st.subheader("📈 Battery Trends")

time = np.arange(0, 50)
voltage_data = 3.7 + 0.1*np.sin(time/5)
temp_data = 30 + 5*np.sin(time/10)

df = pd.DataFrame({
    "Time": time,
    "Voltage": voltage_data,
    "Temperature": temp_data
})

st.line_chart(df.set_index("Time"))
