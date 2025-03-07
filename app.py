import streamlit as st
import pandas as pd
import math

# Add these constants at the top of the file, after the imports but before any other code
# Define category name constants to avoid string duplication
CATEGORY_LENGTH = "Length"
CATEGORY_AREA = "Area"
CATEGORY_VOLUME = "Volume"
CATEGORY_MASS = "Mass"
CATEGORY_TEMPERATURE = "Temperature"
CATEGORY_TIME = "Time"
CATEGORY_SPEED = "Speed"
CATEGORY_BITS_BYTES = "Bits & Bytes"
CATEGORY_WEIGHT = "Weight"

# Set page config - this must be the first Streamlit command
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    body {
    background-color: #050505 !important;
            }
    /* Main container */
    .main {
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        background-attachment: fixed !important;
        color: white !important;
    }
    
    /* App title */
    .app-title {
        color: #f8f9fa;
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fad0c4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* App subtitle */
    .app-subtitle {
        color: #0574fc;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Category cards */
    .category-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .category-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Category title */
    .category-title {
        color: #fcb605;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    
    .category-title i {
        margin-right: 10px;
        font-size: 2rem;
    }
    
    /* Input/output fields */
    .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    
    .stSelectbox {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e3c72, #2a5298) !important;
    }
    
    .css-1d391kg .sidebar-content {
        background-color: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Sidebar title */
    .sidebar-title {
        color: #f8f9fa;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fad0c4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    div[data-baseweb="radio"] label {
        color: #02c42c;        /* Green text color */
        font-size: 18px;       /* Bigger text size */
        font-weight: bold;     /* Bold text */
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #022bf7;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        padding: 1rem;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    
    /* Icons */
    .icon {
        font-size: 2rem;
        margin-right: 10px;
        vertical-align: middle;
    }
    
    /* Result display */
    .result-display {
        background: rgba(255, 255, 255, 0.1);
        color: #f70505;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Category icons */
    .category-icon {
        
        font-size: 2.5rem;
        font-weight: bold;
        margin-right: 15px;
        display: inline-block;
    }
    .custom-markdown1 {
    color: #ec05fc;
    font-weight: bold;
            font-size: 1.5rem;
            }
    .custom-markdown2 {
    color: #02c42c;
    font-weight: bold;
            font-size: 1.5rem;
            }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .app-title {
            font-size: 2.5rem;
        }
        
        .category-title {
            font-size: 1.5rem;
        }
        
        .category-icon {
            font-size: 2rem;
        }
        
</style>
""", unsafe_allow_html=True)

# Font Awesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="app-title">Unit Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Convert between different units of measurement</div>', unsafe_allow_html=True)

# Sidebar for category selection
st.sidebar.markdown('<div class="sidebar-title">Categories</div>', unsafe_allow_html=True)

# Define conversion categories with their respective icons
categories = {
    CATEGORY_LENGTH: "📏",
    CATEGORY_AREA: "📐",
    CATEGORY_VOLUME: "🧊",
    CATEGORY_MASS: "⚖️",
    CATEGORY_TEMPERATURE: "🌡️",
    CATEGORY_TIME: "⏱️",
    CATEGORY_SPEED: "🚀",
    CATEGORY_BITS_BYTES: "💾",
    CATEGORY_WEIGHT: "🏋️"
}

# Create sidebar buttons for each category
# Styled title for radio buttons
st.sidebar.markdown("<h3 style='color: #fab405; font-size: 25px; font-weight: bold;'>Category Selection</h3>", unsafe_allow_html=True)

# Plain radio buttons (cannot style options directly)
selected_category = st.sidebar.radio(
    "Select a category",  # Non-empty label
    options=list(categories.keys()),
    format_func=lambda x: f"{categories[x]} {x}",
    label_visibility="visible"
)

# Define conversion units for each category
conversion_units = {
    CATEGORY_LENGTH: ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    CATEGORY_AREA: ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Hectare", "Acre"],
    CATEGORY_VOLUME: ["Cubic Meter", "Cubic Centimeter", "Liter", "Milliliter", "Gallon (US)", "Quart (US)", "Pint (US)", "Cup (US)", "Fluid Ounce (US)", "Tablespoon (US)", "Teaspoon (US)"],
    CATEGORY_MASS: ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce", "Stone"],
    CATEGORY_TEMPERATURE: ["Celsius", "Fahrenheit", "Kelvin"],
    CATEGORY_TIME: ["Second", "Millisecond", "Microsecond", "Nanosecond", "Minute", "Hour", "Day", "Week", "Month", "Year"],
    CATEGORY_SPEED: ["Meter per Second", "Kilometer per Hour", "Mile per Hour", "Knot", "Foot per Second"],
    CATEGORY_BITS_BYTES: ["Bit", "Byte", "Kilobit", "Kilobyte", "Megabit", "Megabyte", "Gigabit", "Gigabyte", "Terabit", "Terabyte", "Petabit", "Petabyte"],
    CATEGORY_WEIGHT: ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Stone", "Ton"]
}

# Conversion functions for each category
def convert_length(value, from_unit, to_unit):
    # Base unit: Meter
    conversion_to_base = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    
    # Convert to base unit (meter)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_area(value, from_unit, to_unit):
    # Base unit: Square Meter
    conversion_to_base = {
        "Square Meter": 1,
        "Square Kilometer": 1000000,
        "Square Centimeter": 0.0001,
        "Square Millimeter": 0.000001,
        "Square Mile": 2589988.11,
        "Square Yard": 0.83612736,
        "Square Foot": 0.09290304,
        "Square Inch": 0.00064516,
        "Hectare": 10000,
        "Acre": 4046.86
    }
    
    # Convert to base unit (square meter)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_volume(value, from_unit, to_unit):
    # Base unit: Cubic Meter
    conversion_to_base = {
        "Cubic Meter": 1,
        "Cubic Centimeter": 0.000001,
        "Liter": 0.001,
        "Milliliter": 0.000001,
        "Gallon (US)": 0.00378541,
        "Quart (US)": 0.000946353,
        "Pint (US)": 0.000473176,
        "Cup (US)": 0.000236588,
        "Fluid Ounce (US)": 0.0000295735,
        "Tablespoon (US)": 0.0000147868,
        "Teaspoon (US)": 0.00000492892
    }
    
    # Convert to base unit (cubic meter)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_mass(value, from_unit, to_unit):
    # Base unit: Kilogram
    conversion_to_base = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Metric Ton": 1000,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029
    }
    
    # Convert to base unit (kilogram)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Special case for temperature
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit

def convert_time(value, from_unit, to_unit):
    # Base unit: Second
    conversion_to_base = {
        "Second": 1,
        "Millisecond": 0.001,
        "Microsecond": 0.000001,
        "Nanosecond": 0.000000001,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2592000,  # Assuming 30 days per month
        "Year": 31536000  # Assuming 365 days per year
    }
    
    # Convert to base unit (second)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_speed(value, from_unit, to_unit):
    # Base unit: Meter per Second
    conversion_to_base = {
        "Meter per Second": 1,
        "Kilometer per Hour": 0.277778,
        "Mile per Hour": 0.44704,
        "Knot": 0.514444,
        "Foot per Second": 0.3048
    }
    
    # Convert to base unit (meter per second)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_bits_bytes(value, from_unit, to_unit):
    # Base unit: Bit
    conversion_to_base = {
        "Bit": 1,
        "Byte": 8,
        "Kilobit": 1000,
        "Kilobyte": 8000,
        "Megabit": 1000000,
        "Megabyte": 8000000,
        "Gigabit": 1000000000,
        "Gigabyte": 8000000000,
        "Terabit": 1000000000000,
        "Terabyte": 8000000000000,
        "Petabit": 1000000000000000,
        "Petabyte": 8000000000000000
    }
    
    # Convert to base unit (bit)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Base unit: Kilogram
    conversion_to_base = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029,
        "Ton": 1000
    }
    
    # Convert to base unit (kilogram)
    base_value = value * conversion_to_base[from_unit]
    
    # Convert from base unit to target unit
    return base_value / conversion_to_base[to_unit]

# Map categories to conversion functions
conversion_functions = {
    CATEGORY_LENGTH: convert_length,
    CATEGORY_AREA: convert_area,
    CATEGORY_VOLUME: convert_volume,
    CATEGORY_MASS: convert_mass,
    CATEGORY_TEMPERATURE: convert_temperature,
    CATEGORY_TIME: convert_time,
    CATEGORY_SPEED: convert_speed,
    CATEGORY_BITS_BYTES: convert_bits_bytes,
    CATEGORY_WEIGHT: convert_weight
}

# Main content

st.markdown(f'<div class="category-title"><span class="category-icon">{categories[selected_category]}</span>{selected_category}</div>', unsafe_allow_html=True)

# Input and output columns
col1, col2 = st.columns(2)

with col1:
    # Inline CSS for the heading
    st.markdown('<h3 style="color: #02c42c;">From</h3>', unsafe_allow_html=True)
    
    # Updated selectbox with a non-empty label
    from_unit = st.selectbox(
        "From Unit",  # Non-empty label
        conversion_units[selected_category], 
        key="from_unit",
        label_visibility="visible"
    )
    
    # Updated number input with a non-empty label
    input_value = st.number_input(
        "Enter value",  # Non-empty label
        value=1.0, 
        step=0.01, 
        key="input_value",
        label_visibility="visible"
    )

with col2:
    # Inline CSS for the heading
    st.markdown('<h3 style="color: #fc2e2b;">To</h3>', unsafe_allow_html=True)
    
    # Updated selectbox with a non-empty label
    to_unit = st.selectbox(
        "To Unit",  # Non-empty label
        conversion_units[selected_category], 
        key="to_unit",
        label_visibility="visible"
    )
    
    # Perform conversion
    if input_value is not None:
        result = conversion_functions[selected_category](input_value, from_unit, to_unit)
        
        # Format result based on magnitude
        if abs(result) >= 1e6 or abs(result) <= 1e-6 and abs(result) > 0:
            result_str = f"{result:.6e}"
        else:
            result_str = f"{result:.6f}".rstrip('0').rstrip('.') if '.' in f"{result:.6f}" else f"{result:.6f}"
        
        st.markdown(f'<div class="result-display">{result_str}</div>', unsafe_allow_html=True)

# Conversion formulas and information

st.markdown('<div class="category-title"><i class="fas fa-info-circle"></i>Conversion Information</div>', unsafe_allow_html=True)

# Display different information based on selected category
if selected_category == CATEGORY_LENGTH:
    st.markdown("""
    <div class="custom-markdown1">
    Common Length Conversions:
    <br>
    - 1 meter = 100 centimeters
    - 1 meter = 1000 millimeters
    - 1 kilometer = 1000 meters
    - 1 mile = 1.60934 kilometers
    - 1 foot = 12 inches
    - 1 yard = 3 feet
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-markdown2">
    Formula:
    To convert from one unit to another, we first convert to the base unit (meter) and then to the target unit.
    </div>
    """, unsafe_allow_html=True)
    
elif selected_category == CATEGORY_AREA:
    st.markdown("""
    <div class="custom-markdown1">
    Common Area Conversions:
    <br>
    - 1 square meter = 10.7639 square feet
    - 1 square kilometer = 0.386102 square miles
    - 1 hectare = 10,000 square meters
    - 1 acre = 4,046.86 square meters
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-markdown2">
    Formula:
    Area conversions involve squared units, so the conversion factors are squared compared to length conversions.
    </div>
    """, unsafe_allow_html=True)
    
# Continue with other categories similarly...

# Footer with author information
st.markdown('<div class="footer">Author: Azmat Ali</div>', unsafe_allow_html=True)

