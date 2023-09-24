# Install Packages & Libraries


#pip install chart-studio
# pip install streamlit-option-menu

import sys
import pandas as pd
import numpy as np
import scipy as sp
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import streamlit as st

#sys.path.insert(1, r"C:\Users\OS\AppData\Local\Programs\Python\Python310\Lib\site-packages")
from streamlit_option_menu import option_menu
#https://icons.getbootstrap.com/

# Menu bar
selected = option_menu(
    menu_title = None,
    options = [ "Data Overview", "Total Spending", "Spending Over Time", "Percent Growth", "Interactive Map"],
    menu_icon = "cast",
    icons = ['database-check', 'cash-coin', 'clock-history', 'graph-up-arrow', 'globe'],
    default_index = 0,
    orientation = "horizontal",
    styles = {"nav-link-selected":{"background-color":"red"}}
)

#import dataset:
df = pd.read_csv("Military Expenditure.csv")
# Add a sidebar
st.sidebar.title("Selector")

#-----------------------------------------------------------------------------#
# Component1: Data

if selected == "Data Overview":
    #"""# Import Dataset"""
    df = pd.read_csv("Military Expenditure.csv")
    st.subheader("Dataset: ")
    st.markdown('Data collected from 1960 to 2018 for 264 countries (in Billions of USD)')
    # st.write(df.head())

    # """# Basic EDA & Data Cleaning"""

    # df['Type'].value_counts(normalize = True) * 100

    #fill missing values
    df.fillna(0, inplace=True)
    # st.write(df.head(5))

    # assign total
    # Select only the numerical columns (assuming numeric columns are of type int or float)
    numerical_columns = df.select_dtypes(include=['int', 'float'])

    # Calculate the sum of numerical columns along axis 1
    df1 = df['Total'] = numerical_columns.sum(axis=1)
    # st.write(df.head(5))

    #Conversion of Military Expenditure Columns to Billions and Rounding
    columns=[str(i) for i in list((range(1960,2019)))]
    columns=columns+["Total"]
    for i in columns:
        df[i]=df[i]/1.e+9
    df1=np.round(df, decimals=2)
    st.write(df1.head())

    #Sorting and Filtering Military Expenditure Data for Countries
    df1.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
    df1 = df1[df1['Type'].astype(str).str.contains("Country")]


    #Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
    st.subheader("Subset Data: ")
    st.markdown('Selecting Top 20 Countries in Total Military Expenditure in Billions of USD')
    df2 = df1[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)
    st.write(newdf.head(20))
    st.markdown('Limitation: No data reported from China and Russian Federation until 1989 & 1993')

#-----------------------------------------------------------------------------#
# """# Visualization

# Component2: Total Spending
if selected == "Total Spending":
    #"""# Import Dataset"""
    df = pd.read_csv("Military Expenditure.csv")
    #fill missing values
    df.fillna(0, inplace=True)
    # assign total
    numerical_columns = df.select_dtypes(include=['int', 'float'])
    # Calculate the sum of numerical columns along axis 1
    df['Total'] = numerical_columns.sum(axis=1)
    #Conversion of Military Expenditure Columns to Billions and Rounding
    columns=[str(i) for i in list((range(1960,2019)))]
    columns=columns+["Total"]
    for i in columns:
        df[i]=df[i]/1.e+9
    df1=np.round(df, decimals=2)
    #Sorting and Filtering Military Expenditure Data for Countries
    df.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
    df = df[df['Type'].astype(str).str.contains("Country")]

    #Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
    df2 = df[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)

   # Sort the DataFrame in ascending order by 'Total'
    df3_sorted = newdf.sort_values(by='Total', ascending=True)

      # Create the bar plot using plotly.graph_objs
    fig = go.Figure()

    # Add horizontal bar trace
    fig.add_trace(go.Bar(
        x=df3_sorted['Total'],
        y=df3_sorted['Name'],
        orientation='h',
        text=df3_sorted['Total'].apply(lambda x: f"{x:.0f}"),
        textposition='outside',
    ))

    # Customize the layout
    fig.update_layout(
        title='Total Military Spending from 1960 to 2018',
        xaxis_title='Total in billions USD',
        yaxis_title='Countries',
        xaxis_range=[0, df3_sorted['Total'].max() * 1.1],  # Adjust the x-axis range for labels
    )

    # Show the figure within Streamlit
    st.plotly_chart(fig)

     # Create the pie chart using plotly.graph_objs
    fig = go.Figure()

    # Add a pie trace
    fig.add_trace(go.Pie(
        labels=newdf['Name'],
        values=newdf['Total'],
        textinfo='percent+label',
        textposition='inside',
    ))

    # Customize the layout
    fig.update_layout(
        title='Total Military Spendings in Percentage from 1960 to 2018',
    )

    # Show the figure within Streamlit
    st.plotly_chart(fig)
    st.subheader("Observation: ")
    st.markdown("*The highest spending country on Military since 1960 is USA with more than USD17 Trillion.") 
    st.markdown("*The total spending on Military in USA constitute almost half the spending of the Sum of the other 19 countries.")

#-----------------------------------------------------------------------------#
# Component3: Spending Over Time
if selected == "Spending Over Time":
    #"""# Import Dataset"""
    df = pd.read_csv("Military Expenditure.csv")
    #fill missing values
    df.fillna(0, inplace=True)
    # assign total
    numerical_columns = df.select_dtypes(include=['int', 'float'])
    # Calculate the sum of numerical columns along axis 1
    df['Total'] = numerical_columns.sum(axis=1)
    #Conversion of Military Expenditure Columns to Billions and Rounding
    columns=[str(i) for i in list((range(1960,2019)))]
    columns=columns+["Total"]
    for i in columns:
        df[i]=df[i]/1.e+9
    df=np.round(df, decimals=2)
    #Sorting and Filtering Military Expenditure Data for Countries
    df.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
    df = df[df['Type'].astype(str).str.contains("Country")]
    #Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
    df2 = df[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)

   # Sort the DataFrame in ascending order by 'Total'
    df3_sorted = newdf.sort_values(by='Total', ascending=True)

    # """- Create line Plot to show the Military Spending over time by Country"""
    # # Create a list of columns to exclude ('Total')
    columns_to_exclude = ['Total']

    ## Select all columns except those in 'columns_to_exclude'
    selected_columns = [col for col in newdf.columns if col not in columns_to_exclude]

    ## Create a new DataFrame with the selected columns
    df_selected = newdf[selected_columns]

    ## Melt the DataFrame to long format
    df_melted = pd.melt(df_selected, id_vars=['Name'], var_name='Year', value_name='Spending')
    
    # Start filter
    st.sidebar.subheader("Filter Data")
    # Define the list of years from 1960 to 2018
    years = [str(year) for year in range(1960, 2019)]

    # Create a range slider widget for selecting a range of years
    selected_years_range = st.sidebar.slider("Select Years Range", min_value=1960, max_value=2018, value=(1960, 2018), step=1)

    # Filter the data based on the selected years range
    filtered_data = df_melted[(df_melted['Year'].astype(int) >= selected_years_range[0]) & (df_melted['Year'].astype(int) <= selected_years_range[1])].reset_index(drop=True)


    unique_countries = filtered_data['Name'].unique()
    # Create a dictionary to store the state of each checkbox
    checkbox_states = {}
    # Create a checkbox to toggle the dropdown visibility
    show_dropdown = st.sidebar.checkbox("Countries List")
    # Only show the dropdown when the checkbox is selected
    if show_dropdown:
    # Loop through unique country names and create checkboxes
        for country in unique_countries:
            checkbox_states[country] = st.sidebar.checkbox(country, value=True, key=f"checkbox_{country}")
    
    else:
        # If the checkbox is not selected, set selected_countries to an empty list
        selected_countries = []

    # End filter

    # Create the interactive line chart using plotly.graph_objs
    fig = go.Figure()

    # Create lines for each country and highlight the highest point
    for country in filtered_data['Name'].unique():
        if country in checkbox_states and checkbox_states[country]:
            data_country = filtered_data[filtered_data['Name'] == country]
            highest_point = data_country[data_country['Spending'] == data_country['Spending'].max()]  # Find the highest point
            fig.add_trace(go.Scatter(
                x=data_country['Year'],
                y=data_country['Spending'],
                mode='lines',
                name=country,
            ))

            # Highlight the highest point with a marker without legend entry
            fig.add_trace(go.Scatter(
                x=highest_point['Year'],
                y=highest_point['Spending'],
                mode='markers',
                marker=dict(size=8, color='red'),
                name=country,
                showlegend=False,  # Do not include the highest point in the legend
            ))

    # Customize the layout
    fig.update_layout(
        title='Military Spending Over Time by Country',
        xaxis_title='Year',
        yaxis_title='Spending',
        xaxis_type='category',  # Ensure the 'Year' column is treated as categorical
        legend_title_text='Country',
    )

     # Show the figure within Streamlit
    st.plotly_chart(fig)
    # Highlights
    st.subheader("Observation: ")
    st.markdown("*The country with the highest military budget over the years is the USA. The budget started increasing significantly after the year 2000. The largest budget in the history of the USA was allocated in 2011, totaling approximately USD 711 billion.") 
    st.markdown("*China's budget began to increase significantly after the year 2000, reaching its peak in 2018 at approximately USD 250 billion.")
    st.markdown("*The next largest budgets were observed in Russia and Saudi Arabia in 2013 and 2015, each totaling around USD 88 billion.")
#-----------------------------------------------------------------------------#
# Component4: Percent Growth
if selected == "Percent Growth":
    #"""# Import Dataset"""
    df = pd.read_csv("Military Expenditure.csv")
    #fill missing values
    df.fillna(0, inplace=True)
    # assign total
    numerical_columns = df.select_dtypes(include=['int', 'float'])
    # Calculate the sum of numerical columns along axis 1
    df['Total'] = numerical_columns.sum(axis=1)
    #Conversion of Military Expenditure Columns to Billions and Rounding
    columns=[str(i) for i in list((range(1960,2019)))]
    columns=columns+["Total"]
    for i in columns:
        df[i]=df[i]/1.e+9
    df=np.round(df, decimals=2)
    #Sorting and Filtering Military Expenditure Data for Countries
    df.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
    df = df[df['Type'].astype(str).str.contains("Country")]
    #Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
    df2 = df[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)

   # Sort the DataFrame in ascending order by 'Total'
    df3_sorted = newdf.sort_values(by='Total', ascending=True)
   
    #   # Create the figure
    fig = go.Figure()

    # Calculate the percentage growth for each country in 10-year intervals
    interval_years = [str(year) for year in range(1968, 2019, 10)]

    # Create an empty dictionary to store checkbox states
    checkbox_states = {}

    # Create an empty list to store scatter traces
    scatter_traces = []

    # Initialize checkbox states
    for i in range(len(interval_years) - 1):
        start_year = int(interval_years[i])
        end_year = int(interval_years[i + 1])
        interval_name = f'Interval {start_year}-{end_year}'
        checkbox_states[interval_name] = True

    # Create a sidebar checkbox for each interval
    st.sidebar.header("Hide/Show Intervals")
    for interval_name in checkbox_states:
        checkbox_states[interval_name] = st.sidebar.checkbox(interval_name, value=True, key=f"checkbox_{interval_name}")

    # Create the scatter plot
    for i in range(len(interval_years) - 1):
        start_year = int(interval_years[i])
        end_year = int(interval_years[i + 1])
        interval_name = f'Interval {start_year}-{end_year}'

        # Select the relevant columns for the interval
        interval_columns = [str(year) for year in range(start_year, end_year + 1)]
        interval_columns.append('Name')
        data_interval = newdf[interval_columns]

        # Check if both start and end year columns exist
        if str(start_year) in data_interval.columns and str(end_year) in data_interval.columns:
            # Calculate the percentage growth
            data_interval['Percentage growth'] = ((data_interval[str(end_year)] - data_interval[str(start_year)]) / data_interval[str(start_year)]) * 100

            # Create a scatter trace for the current interval if not hidden
            if checkbox_states[interval_name]:
                scatter_trace = go.Scatter(
                    x=data_interval['Name'],
                    y=data_interval['Percentage growth'],
                    mode='markers',
                    name=interval_name,
                )

                scatter_traces.append(scatter_trace)

        else:
            st.write(f"Skipping interval {start_year}-{end_year} due to missing columns")

    # Create a Plotly figure for the scatter plot
    scatter_fig = go.Figure(data=scatter_traces)

    # Customize the layout
    scatter_fig.update_layout(
        title='Percentage Growth by Country (10-Year Intervals)',
        xaxis_title='Country',
        yaxis_title='Percentage Growth',
    )

    # Show the scatter plot within Streamlit
    st.plotly_chart(scatter_fig)
# Highlights
    st.subheader("Observation: ")
    st.markdown("*The highest percentage growth between 1968-1978 was Saudi Arabia.") 
    st.markdown("*The highest percentage growth between 1998-2008 was Russia.")
    st.markdown("*The highest percentage growth between 2008-2018 was China.")

#-----------------------------------------------------------------------------#
# Component5: Interactive Map
if selected == "Interactive Map":
    #"""# Import Dataset"""
    df = pd.read_csv("Military Expenditure.csv")
    #fill missing values
    df.fillna(0, inplace=True)
    # assign total
    numerical_columns = df.select_dtypes(include=['int', 'float'])
    # Calculate the sum of numerical columns along axis 1
    df1 = df['Total'] = numerical_columns.sum(axis=1)
    #Conversion of Military Expenditure Columns to Billions and Rounding
    columns=[str(i) for i in list((range(1960,2019)))]
    columns=columns+["Total"]
    for i in columns:
        df[i]=df[i]/1.e+9
    df1=np.round(df, decimals=2)
    #Sorting and Filtering Military Expenditure Data for Countries
    df1.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
    df1 = df1[df1['Type'].astype(str).str.contains("Country")]
    #Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
    df2 = df1[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)

   # Sort the DataFrame in ascending order by 'Total'
    df3_sorted = newdf.sort_values(by='Total', ascending=True)
    
    # Create the scatter plot on a geographical map with 'natural earth' projection
    fig = px.scatter_geo(df2, 
                        locations='Code', 
                        hover_name="Name", 
                        color="Name", 
                        size='2018', 
                        projection="natural earth")

    # Set the title for the figure
    fig.update_layout(title_text='Military Budget in Billion USD (2018) by Country')

    # Show the visualization
    st.plotly_chart(fig)
    st.subheader("Observation: ")
    st.markdown("*The circles on the map clearly represent the size of the military budget allocated in 2018 for both the USA and China.") 
    st.markdown("*The highest growth in the budget in 2018 is evident in Saudi Arabia, which now ranks third in the world after the USA and China.")
