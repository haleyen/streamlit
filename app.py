import streamlit as st
import pandas as pd

RFM_FILE = "result_rfm_quartile.csv"

RFM_segmentation_description = """
            - **Loyal Customers**: khách hàng này mua hàng thường xuyên và có giá trị cao.
            - **Potential Loyalist**: khách hàng có tiềm năng trở thành loyal customers, họ đã mua hàng nhiều lần và có giá trị.
            - **Recent Customers**: khách hàng mới mua hàng và có thể trở thành loyal customers nếu được quản lý một cách hiệu quả.
            - **Promising**: khách hàng có tiềm năng, họ có thể đã mua hàng nhiều lần nhưng không có giá trị lớn.
            - **Customers Needing Attention**: khách hàng đã mua hàng thường xuyên và có giá trị cao trước đây, nhưng hiện tại đã giảm sút hoạt động mua hàng.
            - **About To Sleep**: khách hàng mua hàng thường xuyên nhưng không có giá trị lớn, và hiện tại đang giảm sút hoạt động mua hàng.
            - **At Risk**: khách hàng đã mua hàng thường xuyên và có giá trị, nhưng hiện tại đã giảm sút hoạt động mua hàng.
            - **Cant Lose Them**: khách hàng đã mua hàng thường xuyên và có giá trị lớn, nhưng hiện tại đã giảm sút hoạt động mua hàng.
            - **Hibernating**: khách hàng chỉ mua hàng ít lần và không có giá trị lớn.
            - **Lost**: khách hàng đã từng mua hàng nhưng không còn hoạt động mua hàng nữa.
            - **No activity**: khách hàng chưa có hoạt động mua hàng.            
            """

def FMscore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]:
        return 3
    else:
        return 4
    
def Rscore(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]:
        return 2
    else:
        return 1

def split_rfm_seg_quartile(x):
    if x == 3:
        return 'Loyal Customers'
    elif x == 4:
        return 'Potential Loyalist'
    elif x == 5:
        return 'Recent Customers'
    elif x == 6:
        return 'Promising'
    elif x == 7:
        return 'Customers Needing Attention'
    elif x == 8:
        return 'About To Sleep'
    elif x == 9:
        return 'At Risk'
    elif x == 10:
        return 'Cant Lose Them'
    elif x == 11:
        return 'Hibernating'
    elif x == 12:
        return 'Lost'
    else:
        return 'No activity'

def main():
    pd00 = pd.read_csv(RFM_FILE)
    pd00['CustomerID'] = pd00['CustomerID'].str.replace(r'\.0$', '')

    limit_recency = 365
    limit_frequency = 1000
    limit_monetary = 1000000 
    
    title = "👨‍👨‍👧‍👦 CUSTOMER SEGMENTATION"
    st.set_page_config(page_title=title,layout="wide")
    st.title(title) 

    menu = ["📚 Business Objective", "🎓️ Data Insights", "🎯 Customer Segmentation"]
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == '📚 Business Objective':
        image = 'rfm_image.jpeg'
        st.image(image, caption='RFM Analysis', width=800)
        
        st.subheader ("📙 What is RFM Segmentation?")
        st.write("""
                RFM segmentation is a marketing analysis method that involves analyzing customer behavior based on three key factors: recency, frequency, and monetary value. This RFM analysis helps businesses categorize customers into segments, enabling targeted and personalized marketing strategies.  

                This RFM methodology helps businesses categorize customers into distinct segments, allowing for more effective and targeted marketing strategies tailored to their specific engagement and spending patterns. """
                )
        st.subheader ("📘 Recency, Frequency and Monetary Explained")
        st.write("""
                Underlying the RFM segmentation technique is the idea that marketers can gain an extensive understanding of their customers by analyzing these three quantifiable factors:

                - **Recency**: How much time has elapsed since a customer’s last activity or transaction with the brand? Activity is usually a purchase, although variations are sometimes used, e.g., the last visit to a website or use of a mobile app. In most cases, the more recently a customer has interacted or transacted with a brand, the more likely that customer will be responsive to communications from the brand. 
                - **Frequency**: How often has a customer transacted or interacted with the brand during a particular period of time? Clearly, customers with frequent activities are more engaged, and probably more loyal, than customers who rarely do so. And one-time-only customers are in a class of their own. 
                - **Monetary**: Also referred to as “monetary value,” this factor reflects how much a customer has spent with the brand during a particular period of time. Big spenders should usually be treated differently than customers who spend little. Looking at monetary divided by frequency indicates the average purchase amount – an important secondary factor to consider when segmenting customers. """)
        st.subheader ("👭 Team members")
        st.write("""
        Le Yen Ha
        
        Nguyen Yen Nhi
        """)
        
    if choice == '🎓️ Data Insights':
        st.write("""There are 5766 customers with transactional data""")
        
        st.subheader ("Number order over the year")
        image = 'rfm_year_month_order.png'
        st.image(image, width=800)
        
        st.subheader ("Number of customer in different country")
        image = 'rfm_country.png'
        st.image(image, width=800)
        
        st.subheader ("Distribution of Receny, Frequency, Monetary value")
        image = 'rfm_distribution.png'
        st.image(image, width=800)
        
        
        # Segmentation description
        st.subheader ("There are 11 RFM segments with following description:")
        with st.expander("Thông tin các nhóm khách hàng", expanded=False):
            st.write(RFM_segmentation_description)
            st.write("")
        image = 'rfm_squarify.png'
        st.image(image, width=800)
            
    if choice == '🎯 Customer Segmentation':    
        st.subheader ("Input customer information")
        choice_input = st.radio("Please choose", options=["1. Input customerID", "2. Input new customer information"])

        # Segmentation description
        with st.expander("Customer Segmentation Description", expanded=False):
            st.write(f"""{RFM_segmentation_description}
            
            **Average Recency (days), Frequency (number of orders), Monetary (VND) for each group**
            """)
            st.write("")
            rfm_mean_image = 'rfm_mean.jpeg'
            st.image(rfm_mean_image, width=600)
            st.write("")
    
        if choice_input == "1. Input customerID":
            # 2.1 nhập ID khách hàng để tìm RFM segmentation
            st.write("##### 1. Input customerID")
            customer_id = st.text_input("Input customerID (only 1 ID each time)")
            
            #example
            col1,col2 = st.columns([1,1])
            with col1:
                st.markdown("Example:")  
                st.info("CustomerID: 12346, 12374")

            st.write("CustomerID:", customer_id) 

            if customer_id: 
                if customer_id in pd00['CustomerID'].values:
                    st.dataframe(pd00[pd00['CustomerID'] == customer_id][['CustomerID','Recency','Frequency','Monetary','RFM_Name']],
                                 hide_index=True,width=1000)
                else:
                    st.error(f"CustomerID {customer_id} does not exist")      
        else:
            # 2.2.1 Input thông tin mới khách hàng
            st.write("##### 2.1 Input new customer information")
            st.write("Input RFM information of maximum 5 customers. Input value must be number")
            
            row1_spacer1, row1_1, row1_spacer2 = st.columns((0.0001, 4, 2))
            with row1_1:
                code = f"""
                Recency value range from 0 to {limit_recency} (days)
                Frequency value range from 0 to {limit_frequency} (orders)
                Monetary value range from 0 to {limit_monetary} (VND)
                """
                st.code(code, language='python')

            col1,col2 = st.columns([1,1])
            with col1:
                st.markdown("Example:")  
                text = '''
                    Recency = 0, Frequency = 23, Monetary = 250000
                    
                    Recency = 20, Frequency = 3, Monetary = 5000
                       '''
                st.info(text)
                
            df_customer = pd.DataFrame(columns=["Recency", "Frequency", "Monetary"])
            for i in range(1, 6):
                st.write(f"{i}. Customer {i}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    recency = st.text_input(f"Recency {i}", key=f"recency_{i}")
                with col2:
                    frequency = st.text_input(f"Frequency {i}", key=f"frequency_{i}")
                with col3:
                    monetary = st.text_input(f"Monetary {i}", key=f"monetary_{i}")
                df_customer = df_customer.append({"Recency": recency, "Frequency": frequency, "Monetary": monetary}, ignore_index=True)
                if i < 5 and not st.checkbox(f"Input new customer", key=f"add_new_{i}"):
                    break   
            
            # 2.2.2 Summit để phân cụm khách hàng
            if recency and frequency and monetary:
                if st.button("Get segmentation"):
                    try:
                        df_customer['Recency'] = df_customer['Recency'].astype(int)
                        df_customer['Frequency'] = df_customer['Frequency'].astype(int)
                        df_customer['Monetary'] = df_customer['Monetary'].astype(int)

                        if int(recency)<=limit_recency and int(frequency)<=limit_frequency and int(monetary)<=limit_monetary:
                            st.write("##### 2.2 Segment new customer")
                            quantiles = {'Recency': {0.25: 23.0, 0.5: 72.0, 0.75: 199.0},
                                         'Frequency': {0.25: 1.0, 0.5: 1.0, 0.75: 4.0},
                                         'Monetary': {0.25: 240.775, 0.5: 632.4749999999999, 0.75: 1642.825}}
                            df_customer['R_quartile'] = df_customer['Recency'].apply(Rscore, args=('Recency',quantiles))
                            df_customer['F_quartile'] = df_customer['Frequency'].apply(FMscore, args=('Frequency',quantiles))
                            df_customer['M_quartile'] = df_customer['Monetary'].apply(FMscore, args=('Monetary',quantiles))
                            df_customer['RFM_Segment'] = (df_customer.R_quartile.map(str)+df_customer.F_quartile.map(str)+df_customer.M_quartile.map(str))
                            df_customer['RFM_Score'] = df_customer[['R_quartile','F_quartile','M_quartile']].sum(axis=1)
                            df_customer['RFM_Name'] = df_customer['RFM_Score'].apply(split_rfm_seg_quartile)
                            df_customer_show = df_customer[['Recency','Frequency','Monetary','RFM_Name']].rename(columns={'RFM_Name':'Segmentation'})
                            st.dataframe(df_customer_show, width=1000)
                            
                            st.download_button("Download customer segmentation as CSV file", 
                                               df_customer_show.to_csv(index=False).encode('utf-8'), 
                                               "rfm_segmentation.csv", "csv", key='download-csv')
                            # st.success("Download successful!", icon="✅")                           
                            
                        else:
                            st.error('Invalid input value. Please check carefully and try again.')
                    except Exception as e:
                        st.error('Please input only number (no special characters, no comma, no dot).')
            else:
                st.button("Get segmentation", disabled=True)  
                
if __name__ == '__main__':
    main()