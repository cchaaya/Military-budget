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

sys.path.insert(1, r"C:\Users\OS\AppData\Local\Programs\Python\Python310\Lib\site-packages")
from streamlit_option_menu import option_menu
#https://icons.getbootstrap.com/

# Menu bar
selected = option_menu(
    menu_title = None,
    options = [ "Data", "Total Spending", "Spending Over Time", "Percent Growth", "Interactive Map"],
    menu_icon = "cast",
    icons = ['database-check', 'cash-coin', 'clock-history', 'graph-up-arrow', 'globe'],
    default_index = 0,
    orientation = "horizontal",
    styles = {"nav-link-selected":{"background-color":"red"}}
)
#-----------------------------------------------------------------------------#
# Component1: Data

if selected == "Data":
    #"""# Import Dataset"""
    df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")
    st.subheader("Dataset: ")
    st.markdown('Countries data collected from 1960 to 2018 in Billions of USD')
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
    st.markdown('Selecting Top 20 Countries in Total Military Expenditure in Billions of USD')
    df2 = df1[:20]
    df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
    newdf = df3.reset_index(drop=True)
    st.write(newdf.head(20))


#-----------------------------------------------------------------------------#
# """# Visualization
# Component2: Total Spending
if selected == "Total Spending":
    #"""# Import Dataset"""
    df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")
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
        title='Total Military Spending from 1960 to 2018 (Ascending Order)',
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

#-----------------------------------------------------------------------------#
# Component3: Spending Over Time
if selected == "Spending Over Time":
    #"""# Import Dataset"""
    df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")
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


    # """- Create line Plot to show the Military Spending over time by Country"""

    # # Create a list of columns to exclude ('Total')
    columns_to_exclude = ['Total']

    # # Select all columns except those in 'columns_to_exclude'
    selected_columns = [col for col in newdf.columns if col not in columns_to_exclude]

    # # Create a new DataFrame with the selected columns
    df_selected = newdf[selected_columns]

    # # Melt the DataFrame to long format
    df_melted = pd.melt(df_selected, id_vars=['Name'], var_name='Year', value_name='Spending')

    # Create the interactive line chart using plotly.graph_objs
    fig = go.Figure()

    # Create lines for each country
    for country in df_melted['Name'].unique():
        data_country = df_melted[df_melted['Name'] == country]
        fig.add_trace(go.Scatter(
            x=data_country['Year'],
            y=data_country['Spending'],
            mode='lines',
            name=country,
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

#-----------------------------------------------------------------------------#
#"""- Total military spendings in percentage from 1960 to 2018"""
# Component4: Percent Growth
if selected == "Percent Growth":
    #"""# Import Dataset"""
    df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")
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

    # """- Create an animated scatter plot to show the percentage growth of spending on military budget by country over the years"""

    # Calculate the percentage growth
    newdf['Percentage growth'] = ((newdf['2018'] - newdf['1960']) / newdf['1960']) * 100

    # Reshape the data
    melted_df = pd.melt(
        newdf,
        id_vars=['Name', 'Percentage growth'],
        value_vars=[str(year) for year in range(1960, 2019)],
        var_name='Year',
        value_name='Spending',
    )
 
    import plotly.graph_objs as go

    # ...

    # Create the figure
    fig = go.Figure()

    # Add scatter points for each year
    for year in melted_df['Year'].unique():
        data_year = melted_df[melted_df['Year'] == year]
        scatter_trace = go.Scatter(
            x=data_year['Name'],
            y=data_year['Percentage growth'],
            mode='markers',
            name=str(year),
            marker=dict(
                size=data_year['Spending'],  # Size of markers based on spending
                sizemode='diameter',
                sizeref=0.1,
                opacity=0.7,
            ),
        )
        fig.add_trace(scatter_trace)

    # Customize the layout
    fig.update_layout(
        title='Spending Growth from 1960 to 2018 by Country',
        xaxis=dict(title='Country', tickangle=45, type='category'),  # Ensure the 'Name' column is treated as categorical
        yaxis=dict(title='Percentage Growth'),
        showlegend=True,
    )

    # Add animation frames
    frames = [go.Frame(data=[go.Scatter(x=data_year['Name'], y=data_year['Percentage growth'])], name=str(year)) for year, data_year in melted_df.groupby('Year')]
    fig.frames = frames

    # Add animation slider
    fig.update_layout(
        updatemenus=[
            {
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 1000, 'redraw': True}, 'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate',
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate',
                    },
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'right',
                'y': 0,
                'yanchor': 'top',
            }
        ],
    )

    # Show the figure within Streamlit
    st.plotly_chart(fig)

    # # """- This plot is showing the growth in military spending from 1960 to 2018
    # # - The buble size reprents the spending volume by country throught the years
    # # - we didnt have data for china until 1989. However, since then the percentage growth of china is around 2093
    # # - We didnt have data for Russia until 1993. Howeverm since then the percentage growth is 690
#-----------------------------------------------------------------------------#
#"""- Total military spendings in percentage from 1960 to 2018"""
# Component5: Interactive Map
if selected == "Interactive Map":
    #"""# Import Dataset"""
    df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")
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
