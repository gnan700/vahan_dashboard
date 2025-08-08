def top_qoq_growth(df, latest_quarter):
    latest_df = df[df['Quarter'] == latest_quarter]
    top = latest_df.sort_values("QoQ Growth (%)", ascending=False).head(1)
    if not top.empty:
        return {
            "manufacturer": top["Manufacturer"].values[0],
            "vehicle_type": top["VehicleType"].values[0],
            "qoq_growth": round(top["QoQ Growth (%)"].values[0], 2)
        }
    return None

def yoy_vs_qoq_summary(df, latest_quarter):
    latest_df = df[df["Quarter"] == latest_quarter]
    summary = latest_df.groupby("VehicleType")[["QoQ Growth (%)", "YoY Growth (%)"]].mean().reset_index()
    return summary.round(2)