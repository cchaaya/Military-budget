# Install Packages & Libraries


#pip install chart-studio

import pandas as pd
import numpy as np
import scipy as sp
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px

"""# Import Dataset"""

df = pd.read_csv(r"C:\Users\OS\Desktop\AUB\MSBA Courses\4- Fall 23-24\MSBA325-Data Visualization and communication\Assignmnent\A2\Military Expenditure.csv")

df.head()

# """# Basic EDA & Data Cleaning"""

df['Type'].value_counts(normalize = True) * 100

df = df.apply(pd.to_numeric, errors='coerce')  # Convert all columns to numeric, ignoring errors
df1 = df.assign(Total=df.sum(axis=1))

#fill missing values
df1.fillna(0, inplace=True)
df1.head(5)

#Conversion of Military Expenditure Columns to Billions and Rounding
columns=[str(i) for i in list((range(1960,2019)))]
columns=columns+["Total"]
for i in columns:
    df1[i]=df1[i]/1.e+9
df1=np.round(df1, decimals=2)
df1.head()

#Sorting and Filtering Military Expenditure Data for Countries
df1.sort_values(by=['Type','Total'],ascending=[False,False],inplace=True)
df1 = df1[df1['Type'].astype(str).str.contains("Country")]

#Selecting Top 20 Rows and Removing Unnecessary Columns in Military Expenditure Data
df2 = df1[:20]
df3 = df2.drop(['Indicator Name', 'Code', 'Type'], axis=1)
newdf = df3.reset_index(drop=True)
newdf.head(20)

# """# Visualization

# - Total Military Spending from 1960 to 2018 (Ascending Order) in Billions of Dollars

# Sort the DataFrame in ascending order by 'Total'
df3_sorted = newdf.sort_values(by='Total', ascending=True)

# Create the bar plot
fig = px.bar(
    df3_sorted, x='Total', y='Name', orientation='h',
    title='Total Military Spending from 1960 to 2018 (Ascending Order)',
    labels={'Total': 'Total in billions USD', 'Name': 'Countries'},
)

# Add rounded total values outside the bars
for index, row in df3_sorted.iterrows():
    fig.add_annotation(
        x=row['Total'] * 1.03 ,  # Adjust the x-coordinate for better positioning
        y=row['Name'],
        text=f"{row['Total']:.0f} ",
        showarrow=False,
        font=dict(size=10)
    )

fig.update_xaxes(range=[0, df3_sorted['Total'].max() * 1.1])  # Adjust the x-axis range for labels

fig.show()

#"""- Total military spendings in percentage from 1960 to 2018"""

# Create pie chart with plotly
fig = px.pie(newdf, values='Total', names='Name', title='Total military spendings in percentage from 1960 to 2018 ')
fig.show()

# """- Create line Plot to show the Military Spending over time by Country"""

# Create a list of columns to exclude ('Total')
columns_to_exclude = ['Total']

# Select all columns except those in 'columns_to_exclude'
selected_columns = [col for col in newdf.columns if col not in columns_to_exclude]

# Create a new DataFrame with the selected columns
df_selected = newdf[selected_columns]

# Melt the DataFrame to long format
df_melted = pd.melt(df_selected, id_vars=['Name'], var_name='Year', value_name='Spending')

# Create an interactive line plot
fig = px.line(df_melted, x='Year', y='Spending', color='Name', title='Military Spending Over Time by Country')
fig.update_xaxes(type='category')  # Ensure the 'Year' column is treated as categorical
fig.update_layout(legend_title_text='Country')

# Show the plot
fig.show()

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

# Create an animated scatter plot
fig = px.scatter(
    melted_df,
    x='Name',
    y='Percentage growth',
    title='Spending Growth from 1960 to 2018 by Country',
    labels={'Percentage growth': 'Percentage Growth'},
    animation_frame='Year',  # Year as animation frame
    animation_group='Name',  # Group by country
    height=400,
    color="Name",
    size='Spending',  # Size of bubbles based on spending
    size_max=55,  # Max size of bubbles
    range_y=[-5000, 50000],  # Adjust the y-axis range as needed
)

# Customize the plot layout
fig.update_xaxes(title_text='Country', tickangle=45)
fig.update_yaxes(title_text='Percentage Growth')
fig.show()

# """- This plot is showing the growth in military spending from 1960 to 2018
# - The buble size reprents the spending volume by country throught the years
# - we didnt have data for china until 1989. However, since then the percentage growth of china is around 2093
# - We didnt have data for Russia until 1993. Howeverm since then the percentage growth is 690

# - Create an interactive map to plot the counties and the volume of budget spent on military budget during 2018 in billion of USD
# """

# Create the scatter plot on a geographical map
fig = px.scatter_geo(df2, locations='Code', hover_name="Name", color="Name", size='2018')

# Set the title for the figure
fig.update_layout(title_text='Military Budget in Billion USD (2018) by Country')

# Show the visualization
fig.show()
