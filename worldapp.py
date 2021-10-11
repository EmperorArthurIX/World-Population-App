from numpy import dtype
import streamlit as st
from streamlit_folium import folium_static

year = st.sidebar.slider("Population for Year:", 1950, 2020)
# THE COUNTRIES LIST IS HARDCODED. PLEASE BE CAREFUL
countries = ['Afghanistan',
 'Albania',
 'Algeria',
 'American Samoa',
 'Andorra',
 'Angola',
 'Anguilla',
 'Antigua and Barbuda',
 'Argentina',
 'Armenia',
 'Aruba',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas',
 'Bahrain',
 'Bangladesh',
 'Barbados',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bermuda',
 'Bhutan',
 'Bosnia and Herzegovina',
 'Botswana',
 'Brazil',
 'British Virgin Islands',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Cayman Islands',
 'Central African Republic',
 'Chad',
 'Chile',
 'China',
 'Colombia',
 'Comoros',
 'Cook Islands',
 'Costa Rica',
 'Croatia',
 'Cuba',
 'Cyprus',
 "Côte d'Ivoire",
 'Denmark',
 'Djibouti',
 'Dominica',
 'Dominican Republic',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Ethiopia',
 'Faroe Islands',
 'Fiji',
 'Finland',
 'France',
 'French Guiana',
 'French Polynesia',
 'Gabon',
 'Gambia',
 'Georgia',
 'Germany',
 'Ghana',
 'Gibraltar',
 'Greece',
 'Greenland',
 'Grenada',
 'Guadeloupe',
 'Guam',
 'Guatemala',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hungary',
 'Iceland',
 'India',
 'Indonesia',
 'Iraq',
 'Ireland',
 'Isle of Man',
 'Israel',
 'Italy',
 'Jamaica',
 'Japan',
 'Jordan',
 'Kazakhstan',
 'Kenya',
 'Kiribati',
 'Kuwait',
 'Kyrgyzstan',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Liechtenstein',
 'Lithuania',
 'Luxembourg',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Maldives',
 'Mali',
 'Malta',
 'Marshall Islands',
 'Martinique',
 'Mauritania',
 'Mauritius',
 'Mayotte',
 'Mexico',
 'Micronesia',
 'Monaco',
 'Mongolia',
 'Montenegro',
 'Montserrat',
 'Morocco',
 'Mozambique',
 'Namibia',
 'Nauru',
 'Nepal',
 'Netherlands',
 'New Caledonia',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'Niue',
 'Northern Mariana Islands',
 'Norway',
 'Oman',
 'Pakistan',
 'Palau',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Philippines',
 'Poland',
 'Portugal',
 'Puerto Rico',
 'Qatar',
 'Romania',
 'Rwanda',
 'Réunion',
 'Saint Helena',
 'Saint Kitts and Nevis',
 'Saint Lucia',
 'Saint Pierre and Miquelon',
 'Saint Vincent and the Grenadines',
 'Samoa',
 'San Marino',
 'Saudi Arabia',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Sierra Leone',
 'Singapore',
 'Slovakia',
 'Slovenia',
 'Solomon Islands',
 'Somalia',
 'South Africa',
 'Spain',
 'Sri Lanka',
 'Sudan',
 'Suriname',
 'Sweden',
 'Switzerland',
 'Tajikistan',
 'Thailand',
 'Timor-Leste',
 'Togo',
 'Tokelau',
 'Tonga',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Turkmenistan',
 'Turks and Caicos Islands',
 'Tuvalu',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Kingdom',
 'Uruguay',
 'Uzbekistan',
 'Vanuatu',
 'Western Sahara',
 'Yemen',
 'Zambia',
 'Zimbabwe']
country = st.sidebar.selectbox("Country:", countries)

st.title("World Population over the years")

if st.button("Let's begin!"):
    import folium
    from folium import plugins
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv('D:\Data Science\WPP2019_TotalPopulationBySex.csv')
    df = df[["Location", "Time", "PopTotal", "PopDensity"]]
    df = df[df["Time"] < 2021]
    df = df.drop_duplicates()
    df['PopTotal'] = df['PopTotal'].astype(int)
    df['PopTotal'] = df['PopTotal']*1000
    df_year = df[df["Time"] == year]
    df_year = df_year.set_index(pd.RangeIndex(df_year.shape[0]))


    df_locs = pd.read_csv('D:\Data Science\WorldCountryCoordinates.csv')
    df_locs = df_locs.rename(columns = {"name" : "Location"})


    work_df = pd.merge(left = df_locs, right = df_year, left_on="Location", right_on="Location", how = "inner")


    def get_country_location():
        ind = countries.index(country)
        data =  work_df[work_df['Location'] == countries[ind]]
        lati = list(data['latitude'])
        longi = list(data['longitude'])
        lati.extend(longi)
        return lati
    world_map = folium.Map(location = get_country_location(),tiles = "Stamen Terrain", zoom_start = 4)
    pops = plugins.MarkerCluster().add_to(world_map)

    for lat, long, label in zip(work_df["latitude"], work_df["longitude"], work_df["PopTotal"].astype(str)):
        folium.Marker(
            location = [lat,long],
            icon = None,
            popup = label + " Citizens"
        ).add_to(pops)

    folium_static(world_map)

if st.button("Exit"):
    st.write("Thanks a tonne for visiting!")