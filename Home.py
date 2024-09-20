import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate App",
    page_icon="🏙️",
)

# Main header
st.write("# Welcome to the Gurgaon Real Estate Price Prediction, Analytics and Recommendation Application! 🏙️")

# Display the image
st.image("https://energyfactor.exxonmobil.asia/wp-content/uploads/2020/07/alok-sharma-peU-vKVCOZQ-unsplash-scaled-1500x1530.jpg", caption="Gurgaon Cityscape", use_column_width=True)

# Sidebar message
st.sidebar.success("Select an option above.")

# App description
st.markdown("""
## About Gurgaon

Gurgaon, officially known as Gurugram, is a rapidly growing city in the northern Indian state of Haryana. Located just southwest of New Delhi, Gurgaon has emerged as a major satellite city of the Indian capital, with an extraordinary transformation over the last few decades. The city's skyline is dotted with modern high-rise buildings, luxury apartments, and sprawling office complexes.

### A Hub of Urban Development

Gurgaon is known for its well-planned infrastructure, booming service sector, and state-of-the-art facilities. It houses the headquarters of many multinational corporations, making it one of India's most important financial and industrial hubs. The city also boasts a vibrant lifestyle, with numerous shopping malls, restaurants, and entertainment venues.

### Real Estate in Gurgaon

Gurgaon's real estate market is one of the most dynamic and sought-after in India. The city's growth has been fueled by its proximity to New Delhi, excellent connectivity, and the presence of a high-income population. As a result, Gurgaon offers a diverse range of residential and commercial properties, catering to different budget ranges and preferences.

#### Key Areas in Gurgaon's Real Estate Market

- **DLF Cyber City**: Known as the "Silicon Valley of India," DLF Cyber City is a prime location for corporate offices. It's also a preferred residential area for professionals due to its proximity to metro stations and business hubs.

- **Golf Course Road**: This area is synonymous with luxury, offering high-end residential complexes, premium apartments, and villas. Golf Course Road is also home to some of the city's top retail outlets and fine dining restaurants.

- **Sohna Road**: An emerging real estate corridor, Sohna Road is gaining popularity for its relatively affordable housing options. The area is well-connected to major parts of the city and offers a mix of residential and commercial properties.

- **MG Road**: One of the oldest and most prominent areas in Gurgaon, MG Road is a bustling commercial and residential zone. It is well-known for its shopping malls, such as MGF Metropolitan and DLF City Centre, and offers easy access to the metro.

- **Sector 49**: A rapidly developing sector, Sector 49 offers a range of residential options, from high-rise apartments to independent houses. The area is attracting attention due to its modern infrastructure and availability of amenities.

### Current Trends in Gurgaon's Real Estate Market

- **Price Appreciation**: Over the years, property prices in Gurgaon have seen significant appreciation, driven by high demand from both investors and end-users. The influx of professionals working in the nearby business districts has further fueled this trend.

- **Luxury Segment**: Gurgaon has established itself as a hotspot for luxury real estate. High-net-worth individuals are drawn to the city’s upscale residential projects, which offer world-class amenities, security, and proximity to key locations.

- **Affordable Housing**: Despite its reputation for luxury, Gurgaon also offers a growing segment of affordable housing. Areas like Sohna Road and sectors along the Dwarka Expressway are seeing a surge in affordable and mid-segment housing projects.

- **Commercial Real Estate**: The commercial real estate sector in Gurgaon is thriving, with high demand for office spaces, retail outlets, and co-working spaces. DLF Cyber City and Golf Course Extension Road are among the top choices for businesses.

- **Infrastructure Development**: Ongoing infrastructure projects, such as the extension of metro lines, construction of underpasses, and development of expressways, are enhancing Gurgaon's connectivity and boosting its real estate appeal.

### What This App Offers

This app provides a comprehensive analysis of the real estate market in Gurgaon, including:

- **Price Predictions**: Using advanced machine learning models to predict property prices based on various features.
- **Analytics**: In-depth analysis of real estate trends, property types, and area-wise pricing.
- **Recommendations**: Personalized property recommendations based on user preferences and market trends.

Explore the app to gain insights and make informed decisions in Gurgaon's real estate market!
""")
