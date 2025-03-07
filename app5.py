import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Unit Converter", page_icon="📏")
st.title("🌟 Unit Converter App 🌟")

# Load and display an icon if available
try:
    icon = Image.open("unit_converter_icon.jpg")
    st.image(icon, width=200)
except FileNotFoundError:
    st.warning("Icon image not found! Make sure 'unit_converter_icon.png' is in the same directory.")

# Define constants to avoid duplication
VALUE_PROMPT = "Enter value:"
FROM_PROMPT = "From:"
TO_PROMPT = "To:"
CONVERT_BUTTON = "Convert"

# Conversion factors as constants
CONVERSION_FACTORS = {
    "Area 🌍": {
        "Square Meter": 1,
        "Square Kilometer": 1e6,
        "Hectare": 1e4,
        "Acre": 4046.86
    },
    "Bits & Bytes 💾": {
        "Bit": 1,
        "Byte": 8,
        "Kilobyte": 8 * 1024,
        "Megabyte": 8 * 1024**2
    },
    "Length 📏": {
        "Meter": 1,
        "Kilometer": 1e3,
        "Mile": 1609.34,
        "Yard": 0.9144
    },
    "Mass ⚖️": {
        "Gram": 1,
        "Kilogram": 1e3,
        "Pound": 453.592,
        "Ounce": 28.3495
    },
    "Speed 🚀": {
        "Meter/Second": 1,
        "Kilometer/Hour": 0.277778,
        "Mile/Hour": 0.44704
    },
    "Time ⏰": {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400
    },
    "Volume 🥤": {
        "Milliliter": 1,
        "Liter": 1e3,
        "Gallon": 3785.41,
        "Cubic Meter": 1e6
    },
    "Weight 🏋️": {
        "Gram": 1,
        "Kilogram": 1e3,
        "Pound": 453.592
    }
}

# Function for temperature conversion
def convert_temperature(value, unit, target_unit):
    if unit == target_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): lambda v: v * 9 / 5 + 32,
        ("Fahrenheit", "Celsius"): lambda v: (v - 32) * 5 / 9,
        ("Celsius", "Kelvin"): lambda v: v + 273.15,
        ("Kelvin", "Celsius"): lambda v: v - 273.15,
        ("Fahrenheit", "Kelvin"): lambda v: (v - 32) * 5 / 9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda v: (v - 273.15) * 9 / 5 + 32
    }
    return conversions.get((unit, target_unit), lambda v: v)(value)

# Function to handle standard conversions
def handle_standard_conversion(value, unit, target_unit, conversions):
    if unit == target_unit:
        return value
    return value * conversions[unit] / conversions[target_unit]

# Main function for unit conversion
def convert_units(category):
    value = st.number_input(VALUE_PROMPT, min_value=0.0, format="%.2f")

    if category in CONVERSION_FACTORS:
        conversions = CONVERSION_FACTORS[category]
        unit_options = list(conversions.keys())
        unit = st.selectbox(FROM_PROMPT, unit_options)
        target_unit = st.selectbox(TO_PROMPT, unit_options)
        if st.button(CONVERT_BUTTON):
            result = handle_standard_conversion(value, unit, target_unit, conversions)
            st.success(f"Result: {result:.2f} {target_unit}")

    elif category == "Temperature 🌡️":
        unit = st.selectbox(FROM_PROMPT, ["Celsius", "Fahrenheit", "Kelvin"])
        target_unit = st.selectbox(TO_PROMPT, ["Celsius", "Fahrenheit", "Kelvin"])
        if st.button(CONVERT_BUTTON):
            result = convert_temperature(value, unit, target_unit)
            st.success(f"Result: {result:.2f} {target_unit}")

# Sidebar for selecting category
st.sidebar.title("Choose a Category")
category = st.sidebar.selectbox("Category", [
    "Area 🌍",
    "Bits & Bytes 💾",
    "Length 📏",
    "Mass ⚖️",
    "Speed 🚀",
    "Temperature 🌡️",
    "Time ⏰",
    "Volume 🥤",
    "Weight 🏋️"
])

# Perform unit conversion based on selected category
convert_units(category)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Your Name")

