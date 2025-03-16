import streamlit as st

# Title of the app
st.title("FarmSoil AI - Soil Analysis and Crop Suggestion")

# Input fields for soil data
st.header("Enter Soil Test Data")
ph = st.slider("pH Level", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
nitrogen = st.slider("Nitrogen (mg/kg)", min_value=0, max_value=100, value=20)
phosphorus = st.slider("Phosphorus (mg/kg)", min_value=0, max_value=100, value=15)
potassium = st.slider("Potassium (mg/kg)", min_value=0, max_value=100, value=25)

# Input field for land area
st.header("Enter Land Area")
area = st.number_input("Area (in hectares)", min_value=0.1, value=1.0, step=0.1)

# Crop selection
st.header("Select a Crop")
crop = st.selectbox("Choose a crop", ["Wheat", "Rice", "Corn", "Soybeans"])

# Ideal conditions for crops (hardcoded for prototype)
ideal_conditions = {
    "Wheat": {"pH": (6.0, 7.0), "N": 50, "P": 20, "K": 30},
    "Rice": {"pH": (5.0, 6.5), "N": 40, "P": 15, "K": 25},
    "Corn": {"pH": (5.8, 7.0), "N": 60, "P": 25, "K": 35},
    "Soybeans": {"pH": (6.0, 7.5), "N": 30, "P": 20, "K": 25},
}

# Analyze soil data
if st.button("Analyze Soil"):
    ideal = ideal_conditions[crop]
    feedback = []

    # Check pH
    if ph < ideal["pH"][0]:
        feedback.append(f"**Adjust pH to {ideal['pH'][0]}-{ideal['pH'][1]}:**\n"
                       f"The soil is too acidic (pH = {ph}). Apply 2-4 tons of agricultural lime per hectare. "
                       f"Mix the lime thoroughly into the top 6-8 inches of soil.")
    elif ph > ideal["pH"][1]:
        feedback.append(f"**Adjust pH to {ideal['pH'][0]}-{ideal['pH'][1]}:**\n"
                       f"The soil is too alkaline (pH = {ph}). Apply 1-2 tons of elemental sulfur per hectare. "
                       f"Mix the sulfur thoroughly into the top 6-8 inches of soil.")

    # Check Nitrogen
    if nitrogen < ideal["N"]:
        nitrogen_deficit = ideal["N"] - nitrogen
        total_nitrogen = nitrogen_deficit * area  # Total nitrogen needed in kg/ha
        feedback.append(f"**Add {total_nitrogen:.2f} kg of nitrogen-based fertilizer for {area} hectares:**\n"
                       f"Use urea, ammonium nitrate, or ammonium sulfate. Apply evenly across the field. "
                       f"Split the application into two doses: one at planting and the other during the growing season.")

    # Check Phosphorus
    if phosphorus < ideal["P"]:
        phosphorus_deficit = ideal["P"] - phosphorus
        total_phosphorus = phosphorus_deficit * area  # Total phosphorus needed in kg/ha
        feedback.append(f"**Add {total_phosphorus:.2f} kg of phosphorus-based fertilizer for {area} hectares:**\n"
                       f"Use single superphosphate (SSP) or diammonium phosphate (DAP). "
                       f"Apply at the time of planting and place near the seed for better uptake.")

    # Check Potassium
    if potassium < ideal["K"]:
        potassium_deficit = ideal["K"] - potassium
        total_potassium = potassium_deficit * area  # Total potassium needed in kg/ha
        feedback.append(f"**Add {total_potassium:.2f} kg of potassium-based fertilizer for {area} hectares:**\n"
                       f"Use muriate of potash (MOP) or sulfate of potash (SOP). "
                       f"Apply evenly across the field and incorporate into the soil before planting.")

    # Display feedback
    if feedback:
        st.success("Here's what you need to do:")
        for item in feedback:
            st.write(item)
    else:
        st.success("Your soil is ideal for growing " + crop + "!")
