import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data/vahan_data.csv")

# Convert 'Year' column to int
df["Year"] = df["Year"].astype(int)

# Sidebar: vehicle selection
vehicle_types = st.sidebar.multiselect(
    "Select Vehicle Types",
    options=df.columns[1:],  # exclude 'Year'
    default=list(df.columns[1:])
)

# Sidebar: year range filter
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max()))
)

# Filter data
filtered_df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

st.title("📊 Vahan Vehicle Registration Dashboard")
st.write("Showing Year-over-Year growth and trends by vehicle type.")

# Plot each selected vehicle type
for vehicle in vehicle_types:
    st.subheader(f"{vehicle}")

    # Plot line chart
    fig, ax = plt.subplots()
    ax.plot(filtered_df["Year"], filtered_df[vehicle], marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Registrations")
    ax.set_title(f"{vehicle} over Years")
    st.pyplot(fig)

    # Calculate and show YoY growth
    growth = filtered_df[["Year", vehicle]].copy()
    growth["YoY Growth (%)"] = growth[vehicle].pct_change() * 100
    st.dataframe(growth.round(2))

