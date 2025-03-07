# app.py
import streamlit as st

# Constants
BITS_BYTES = "Bits & Bytes"

# Set page title and icon
st.set_page_config(page_title="UNIT CONVERTER", page_icon="📏", layout="wide")

# Add some color and styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stSelectbox>div>div>select {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 5px;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 5px;
    }
    .stMarkdown {
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("📏 UNIT CONVERTER")
st.markdown("**Convert units easily for area, bits & bytes, length, mass, speed, time, volume, temperature, and weight.**")

# Author
st.markdown("---")
st.markdown("**Author: Azmat Ali**")

# Conversion functions
def convert_area(value, from_unit, to_unit):
    area_units = {
        "Square Meter": 1,
        "Square Kilometer": 1e-6,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550,
        "Hectare": 1e-4,
        "Acre": 0.000247105,
    }
    return value * (area_units[to_unit] / area_units[from_unit])

def convert_bits_bytes(value, from_unit, to_unit):
    bits_bytes_units = {
        "Bit": 1,
        "Byte": 8,
        "Kilobit": 1e3,
        "Kilobyte": 8e3,
        "Megabit": 1e6,
        "Megabyte": 8e6,
        "Gigabit": 1e9,
        "Gigabyte": 8e9,
    }
    return value * (bits_bytes_units[to_unit] / bits_bytes_units[from_unit])

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 1e-3,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Metric Ton": 1e-3,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    return value * (mass_units[to_unit] / mass_units[from_unit])

def convert_speed(value, from_unit, to_unit):
    speed_units = {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,
        "Miles/Hour": 2.23694,
        "Knot": 1.94384,
    }
    return value * (speed_units[to_unit] / speed_units[from_unit])

def convert_time(value, from_unit, to_unit):
    time_units = {
        "Second": 1,
        "Minute": 1 / 60,
        "Hour": 1 / 3600,
        "Day": 1 / 86400,
        "Week": 1 / 604800,
        "Year": 1 / 3.154e7,
    }
    return value * (time_units[to_unit] / time_units[from_unit])

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic Meter": 1e-3,
        "Cubic Centimeter": 1e3,
        "Gallon": 0.264172,
        "Quart": 1.05669,
        "Pint": 2.11338,
        "Cup": 4.22675,
    }
    return value * (volume_units[to_unit] / volume_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9 / 5 + 32
    return value

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

# Sidebar for unit selection
st.sidebar.title("🔧 Select Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type:",
    [
        "Area",
        BITS_BYTES,
        "Length",
        "Mass",
        "Speed",
        "Time",
        "Volume",
        "Temperature",
        "Weight",
    ],
)

# Main conversion logic
st.header(f"🔨 {conversion_type} Conversion")

if conversion_type == "Area":
    units = ["Square Meter", "Square Kilometer", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Hectare", "Acre"]
elif conversion_type == BITS_BYTES:
    units = ["Bit", "Byte", "Kilobit", "Kilobyte", "Megabit", "Megabyte", "Gigabit", "Gigabyte"]
elif conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
elif conversion_type == "Mass":
    units = ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce"]
elif conversion_type == "Speed":
    units = ["Meters/Second", "Kilometers/Hour", "Miles/Hour", "Knot"]
elif conversion_type == "Time":
    units = ["Second", "Minute", "Hour", "Day", "Week", "Year"]
elif conversion_type == "Volume":
    units = ["Liter", "Milliliter", "Cubic Meter", "Cubic Centimeter", "Gallon", "Quart", "Pint", "Cup"]
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]

# Input and output units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

# Input value
value = st.number_input("Enter value to convert:", value=1.0)

# Perform conversion
if conversion_type == "Area":
    result = convert_area(value, from_unit, to_unit)
elif conversion_type == BITS_BYTES:
    result = convert_bits_bytes(value, from_unit, to_unit)
elif conversion_type == "Length":
    result = convert_length(value, from_unit, to_unit)
elif conversion_type == "Mass":
    result = convert_mass(value, from_unit, to_unit)
elif conversion_type == "Speed":
    result = convert_speed(value, from_unit, to_unit)
elif conversion_type == "Time":
    result = convert_time(value, from_unit, to_unit)
elif conversion_type == "Volume":
    result = convert_volume(value, from_unit, to_unit)
elif conversion_type == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)
elif conversion_type == "Weight":
    result = convert_weight(value, from_unit, to_unit)

# Display result
st.success(f"✅ **Converted Value:** {result:.4f} {to_unit}")