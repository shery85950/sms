"""
Quick test script to verify the monitoring system locally
"""
import json

# Load river data
with open('river_data.json', 'r') as f:
    data = json.load(f)

# Get latest entry
latest_entry = None
for entry in data:
    if entry.get('stations'):
        latest_entry = entry
        break

if latest_entry:
    print(f"📊 Checking data for date: {latest_entry.get('date')}")
    stations = latest_entry.get('stations', {})
    
    THRESHOLD = 100000
    
    for station_name, metrics in stations.items():
        discharge_vals = []
        for k, v in metrics.items():
            if "DISCHARGE" in k and isinstance(v, (int, float)):
                discharge_vals.append(v)
        
        max_discharge = max(discharge_vals) if discharge_vals else 0
        
        if max_discharge > THRESHOLD:
            print(f"⚠️  HIGH DISCHARGE at {station_name}: {max_discharge} cusecs - ALERT WOULD BE SENT!")
        else:
            print(f"✓ {station_name}: {max_discharge} cusecs (Normal)")
else:
    print("❌ No station data found")
