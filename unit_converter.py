import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()

# Set up the Streamlit app
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")
st.write("Convert between different units easily!")

# Dropdown to select conversion type
conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Define units based on conversion type
if conversion_type == "Length":
    units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "foot", "inch"]
elif conversion_type == "Weight":
    units = ["gram", "kilogram", "milligram", "pound", "ounce"]
elif conversion_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]

# Input fields
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value", min_value=0.0, value=1.0)
    to_unit = st.selectbox("To Unit", units)

with col2:
    from_unit = st.selectbox("From Unit", units)

# Perform conversion
if st.button("Convert"):
    try:
        # Create Quantity objects
        quantity = value * ureg(from_unit)
        converted_quantity = quantity.to(to_unit)

        # Display result
        st.success(f"**Result:** {value} {from_unit} = {converted_quantity.magnitude:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")

# Adding Personal Info in the Sidebar
st.sidebar.markdown("---")
st.sidebar.write("**Developed By:** Owais Mukhtar Khan")
st.sidebar.write("**Contact:** owaismukhtarkhan@gmail.com")
st.sidebar.write("**GitHub:** [GitHub Profile](https://github.com/owaismukhtarkhan)")

# to run program type - streamlit run unit_converter.py