import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div
from PIL import Image

st.set_page_config(layout='centered', initial_sidebar_state='expanded')
st. sidebar.image('Data/App_icon.png')

California = pd.read_csv('Data/California/California.csv', sep=',')
California["Location"] = California["Street Address"] +', '+ California["Location"]
California = California.drop(['Street Address',], axis=1)

New_York = pd.read_csv('Data/New York/New_York.csv', sep=',')
New_York["Location"] = New_York["Street Address"] +', '+ New_York["Location"]
New_York = New_York.drop(['Street Address', ], axis=1)



New_Jersey = pd.read_csv('Data/New Jersey/New_Jersey.csv', sep=',')
New_Jersey["Location"] = New_Jersey["Street Address"] +', '+ New_Jersey["Location"]
New_Jersey  = New_Jersey.drop(['Street Address', ], axis=1)



Texas = pd.read_csv('Data/Texas/Texas.csv', sep=',')
Texas["Location"] = Texas["Street Address"] +', '+ Texas["Location"]
Texas = Texas.drop(['Street Address', ],axis=1)



Washington = pd.read_csv('Data/Washington/Washington.csv', sep=',')
Washington["Location"] = Washington["Street Address"] +', '+ Washington["Location"]
Washington = Washington.drop(['Street Address', ], axis=1)


option = st.selectbox('Select Your State', ('New Jersey','New York','California', 'Texas', 'Washington'))


#Details of every resturant
def details(dataframe):

    dataframe = dataframe.drop(["Unnamed: 0", "Trip_advisor Url", "Menu"], axis=1)
    data_new = dataframe

    split_data = dataframe["Type"].str.split(",").str[0]
    data1 = split_data.to_list()
    data_new["Cost_Range"] = data1[0]

    split_data = dataframe["Type"].str.split(",").str[1:]
    data2 = split_data.to_list()
    new_df1 = pd.DataFrame(data2)
    new_df1["Type"] = new_df1[0].fillna('') + new_df1[1].fillna('') + new_df1[2].fillna('')
    new_df1["Type"] = new_df1["Type"].str.replace(" ", ",").str[1:]
    data_new["Type"] = new_df1["Type"]
    data_new["Type"] = data_new["Type"].str.replace(",", ", ")

    data_new['Type'].value_counts().sort_values(ascending=False).head(10)

    data_new['Reviews'] = data_new["Reviews"].str.split(" ").str[0]
    i = data_new[((data_new.Reviews == 'No'))].index
    data_new = data_new.drop(i)
    data_new["Reviews"] = data_new["Reviews"].astype(float)
    data_new = data_new.reset_index()
    data_new = data_new.drop(['index'], axis=1)

    data_new["No of Reviews"] = data_new["No of Reviews"].str.replace(",", "")
    split_data = data_new["No of Reviews"].str.split(" ").str[0]
    data1 = split_data.to_list()
    new_df = pd.DataFrame(data1)
    data_new["No of Reviews"] = new_df[0]
    data_new["No of Reviews"] = data_new["No of Reviews"].astype(float)

    title = st.selectbox('Select Your Restaurant', (list(dataframe['Name'])))

    if title in dataframe['Name'].values:
        Reviews = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Reviews'])
        st.markdown("### Restaurant Rating:-")

        #REVIEWS
        if Reviews == '4.5':
            image = Image.open('Data/Ratings/Img4.5.jpg')
            st.image(image, use_container_width=True)


        elif Reviews == '4':
            image = Image.open('Data/Ratings/Img4.0.jpg')
            st.image(image, use_container_width=True)


        elif Reviews == '5':
            image = Image.open('Data/Ratings/Img5.0.png')
            st.image(image, use_container_width=True)

        else:
            pass

        if 'Comments' not in dataframe.columns:
            pass
        else:
            comment = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Comments'])
            if comment != "No Comments":
                st.markdown("### Comments:-")
                st.warning(comment)
            else:
                pass

        #TYPE OF RESTURANT
        Type = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Type'])
        st.markdown("### Restaurant Category:-")
        st.error(Type)

        #LOCATION
        Location = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Location'])
        st.markdown("### The Address:-")
        st.success(Location)

        #CONTACT DETAILS
        contact_no = (dataframe.at[dataframe['Name'].eq(title).idxmax(), 'Contact Number'])
        if contact_no == "Not Available":
            pass

        else:
            st.markdown("### Contact Details:-")
            st.info('Phone:- '+ contact_no)

        #URL
        url = (New_Jersey.at[New_Jersey['Name'].eq(title).idxmax(), 'Trip_advisor Url'])
        st.markdown("### The Website:-")
        if st.button("Tripadvisor Website"):
            #js = "window.open" + "('" + url + "')"  # New tab
            js = "window.location.href" + " = " + "'" + url + "'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

        
    st.text("")
    image = Image.open('Data/happy_eating.jpg')
    st.image(image, use_container_width=True)



if option == 'New Jersey':
    image = Image.open('Data/New Jersey/nj.png')
    st.image(image, use_container_width=True)
    details(New_Jersey)


elif option == 'New York':
    image = Image.open('Data/New York/ny.jpg')
    st.image(image, use_container_width=True)
    details(New_York)

elif option == 'California':
    image = Image.open('Data/California/cali.jpg')
    st.image(image, use_container_width=True)
    details(California)

elif option == 'Texas':
    image = Image.open('Data/Texas/Texas.jpg')
    st.image(image, use_container_width=True)
    details(Texas)

elif option == 'Washington':
    image = Image.open('Data/Washington/washington.jpg')
    st.image(image, use_container_width=True)
    details(Washington)




