import streamlit as st
import pandas as pd

rfm_file = "result_rfm_quintile.csv"
customer_transaction = 'data_customer_transaction.csv'
RFM_segmentation_description = """
            - **Champions**: Bought recently, buy often and spend the most!
            - **Loyal Customers**: Spend good money with us often. Responsive to promotions. 
            - **Potential Loyalist**: Recent customers, but spent a good amount and bought more than once. 
            - **Recent Customers**: Bought most recently, but not often. 
            - **Promising**: Recent shoppers, but haven’t spent much. 
            - **Customers Needing Attention**: Above average recency, frequency and monetary values. May not have bought very recently though.
            - **About To Sleep**: Below average recency, frequency and monetary values. Will lose them if not reactivated. 
            - **At Risk**: Spent big money and purchased often. But long time ago. 
            - **Can’t Lose Them**: Made biggest purchases, and often. But haven’t returned for a long time.
            - **Hibernating**: Last purchase was long back, low spenders and low number of orders. 
            - **Lost**: Lowest recency, frequency and monetary scores.       
            """
def FMscore(x,p,d):
    if x <= d[p][0.2]:
        return 1
    elif x <= d[p][0.4]:
        return 2
    elif x <= d[p][0.6]:
        return 3
    elif x <= d[p][0.8]:
        return 4
    else:
        return 5
    
def Rscore(x,p,d):
    if x <= d[p][0.2]:
        return 5
    elif x <= d[p][0.4]:
        return 4
    elif x <= d[p][0.6]:
        return 3
    elif x <= d[p][0.8]:
        return 4
    else:
        return 1

def split_rfm_seg(x):
    Champions=[555, 554, 544, 545, 454, 455, 445]
    LoyalCustomers=[543, 444, 435, 355, 354, 345, 344, 335]
    PotentialLoyalist=[553, 551,552, 541, 542, 533, 532, 531, 452, 451, 442, 441, 431, 453, 433, 432, 423, 353, 352, 351, 342, 341, 333, 323]
    RecentCustomers=[512, 511, 422, 421, 412, 411, 311]
    Promising=[525, 524, 523, 522, 521, 515, 514, 513, 425, 424, 413,414, 415, 315, 314, 313]
    CustomersNeedingAttention=[535, 534, 443, 434, 343, 334, 325, 324]
    AboutToSleep=[331, 321, 312, 221, 213]
    AtRisk=[255, 254, 245, 244, 253, 252, 243, 242, 235, 234, 225, 224, 153, 152, 145, 143, 142, 135, 134, 133, 125, 124]
    CantLoseThem=[155, 154, 144, 214,215,115, 114, 113]
    Hibernating=[332, 322, 231, 241, 251, 233, 232, 223, 222, 132, 123, 122, 212, 211]
    Lost=[111, 112, 121, 131,141,151]
    
    if x in Champions:
        return 'Champions'
    elif x in LoyalCustomers:
        return 'Loyal Customers'
    elif x in PotentialLoyalist:
        return 'Potential Loyalist'
    elif x in RecentCustomers:
        return 'Recent Customers'
    elif x in Promising:
        return 'Promising'
    elif x in CustomersNeedingAttention:
        return 'Customers Needing Attention'
    elif x in AboutToSleep:
        return 'About To Sleep'
    elif x in AtRisk:
        return 'At Risk'
    elif x in CantLoseThem:
        return 'Cant Lose Them'
    elif x in Hibernating:
        return 'Hibernating'
    elif x in Lost:
        return 'Lost'
    else:
        return 'No activity'

def main():
    pd00 = pd.read_csv(rfm_file)
    pd01 = pd.read_csv(customer_transaction, dtype={'InvoiceNo': str})
    #pd00['CustomerID'] = pd00['CustomerID'].str.replace(r'\.0$', '')

    limit_recency = 365
    limit_frequency = 1000
    limit_monetary = 1000000 
    
    title = "👨‍👨‍👧‍👦 CUSTOMER SEGMENTATION"
    st.set_page_config(page_title=title,layout="wide")
    st.title(title) 

    menu = ["📚 Business Objective", "🎓️ Data Insights", "🎯 Customer Segmentation"]
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == '📚 Business Objective':
        st.image("customer-segmentation.jpg", width=600)  
        st.subheader ("🎯 Why is it necessary for customer segmentation?")
        st.write("""
                - Build better marketing campaigns
                - Improve products and services => improve customer satisfaction
                - Promote expanding new products and services suitable for the business's target audience.
                - Price optimization
                - Increase revenue and profits as well as reduce sales costs  
        """)
                
        st.subheader ("👨‍💼 Customer Segmentation with RFM")        
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
        
        st.subheader ("📃 About Dataset")
            
        st.write("""
                    The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.
                    
                    This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.
                    
                    Dataset Information: [Click here](https://archive.ics.uci.edu/dataset/352/online+retail)
                 """)
        st.subheader ("👭 Team members")
        st.write("""
        Le Yen Ha
        
        Nguyen Yen Nhi
        """)
        
    if choice == '🎓️ Data Insights':
        st.write("""There are 5766 customers with transactional data""")
        
        st.subheader ("Number of orders over the year")
        image = 'rfm_year_month_order.png'
        st.image(image, width=800)
        st.write("""
        - From October 2010 to August 2011, the number of orders placed online did not differ much.
        - Starting from September 2011 to November 2011, the number of orders placed increased significantly.
        - Especially in November 2011, there was the highest number of orders, reaching about 83,635 orders.
        - However, at the end of 2011, the number of orders decreased sharply to only 25,165 orders. (The explanation for the suddenly lower number of orders in December 2011 is that the dataset was only collected until December 9, 2011)
        """)
        st.subheader ("Number of customers in different country")
        image = 'rfm_country.png'
        st.image(image, width=800)
        st.write("""
                    - The main customers of the business are mostly from the United Kingdom
                    - Customers from other regions account for an insignificant amount
                    
                    **Solutions:**
                    - Businesses should focus on analyzing the United Kingdom market specifically to retain customers in this area
                    - At the same time, businesses can focus on analyzing market trends in other regions to come up with policies to expand their market, as well as boost revenue from many regions.
                 """)
        st.subheader ("Distribution of Receny, Frequency, Monetary value")
        image = 'rfm_distribution.png'
        st.image(image, width=800)
        
        image = 'rfm_quantile.png'
        st.image(image, width=800)
        st.write("""
                    - The average number of orders is 3.46, with a wide range (1 to 209).
                    - On average, customers made purchases over 3.15 days, with a similar wide range (1 to 132).
                    - The average purchase amount is 1849.93, with a high standard deviation of 7919.03. This indicates a wide distribution of purchase values.
                    - The average DayDiff of 117.07 with a standard deviation of 111.33 highlights the irregularity in customer purchase intervals.
                 """)
        
        
        # Segmentation description
        st.subheader ("There are 11 RFM segments with following description:")
        with st.expander("Customer Segmentation Description", expanded=False):
            st.write(RFM_segmentation_description)
            st.write("")
        image = 'rfm_squarify.png'
        st.image(image, width=800)
            
    if choice == '🎯 Customer Segmentation':    
        st.subheader ("Input customer information")
        choice_input = st.radio("Please choose", options=["1. Input customerID", "2. Search customerID", "3. Input new customer information"])

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
                st.info("CustomerID: 12346")

            if customer_id:
                if st.button("Get segmentation"):
                    if customer_id in pd00['CustomerID'].values:
                        st.dataframe(pd00[pd00['CustomerID'] == customer_id][['CustomerID','Country','Recency','Frequency','Monetary','Segment']].reset_index(drop=True), width=1000)
                        st.markdown("Detail transaction:")  
                        st.dataframe(pd01[pd01['CustomerID'] == customer_id][['Date','InvoiceDate','InvoiceNo','StockCode','Description','Quantity','UnitPrice']].sort_values('Date').reset_index(drop=True), width=1000)
                    else:
                        st.error(f"CustomerID {customer_id} does not exist")
            else:
                st.button("Get segmentation", disabled=True) 
                    
        elif choice_input == "2. Search customerID":
            # 2.2 search ID khách hàng để tìm RFM segmentation
            st.write("##### 2. Search customerID")
            
            list_dropdown = sorted(list(pd00['CustomerID'].unique()))
            option = st.selectbox("Filter customerID", index=0, options=['<Choose one>']+list_dropdown) 
            st.write('You selected:', option)
            
            if option == '<Choose one>':
                st.dataframe(pd.DataFrame(),width=1000)
            else:
                st.dataframe(pd00[pd00['CustomerID'] == option][['CustomerID','Country','Recency','Frequency','Monetary','Segment']].reset_index(drop=True), 
                         width=1000)
                st.markdown("Detail transaction:")  
                st.dataframe(pd01[pd01['CustomerID'] == option][['Date','InvoiceDate','InvoiceNo','StockCode','Description','Quantity','UnitPrice']].sort_values('Date').reset_index(drop=True), width=1000)

        else:
            # 2.3.1 Input thông tin mới khách hàng
            st.write("##### 2.1 Input new customer information")
            st.write("Input RFM information of **maximum 5 customers**. Input value must be number.")
            
            row1_spacer1, row1_1, row1_spacer2 = st.columns((0.0001, 4, 2))
            with row1_1:
                code = f"""
                Recency value range from 0 to {limit_recency} (days).
                
                Frequency value range from 0 to {limit_frequency} (orders).
                
                Monetary value range from 0 to {limit_monetary} (VND).
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
                new_data = {"Recency": recency, "Frequency": frequency, "Monetary": monetary}
                df_customer = pd.concat([df_customer, pd.DataFrame([new_data], columns=new_data.keys())], ignore_index=True)
                if i < 5 and not st.checkbox(f"Input new customer", key=f"add_new_{i}"):
                    break   
            
            # 2.3.2 Summit để phân cụm khách hàng
            if recency and frequency and monetary:
                if st.button("Get segmentation"):
                    try:
                        df_customer['Recency'] = df_customer['Recency'].astype(int)
                        df_customer['Frequency'] = df_customer['Frequency'].astype(int)
                        df_customer['Monetary'] = df_customer['Monetary'].astype(int)

                        if int(recency)<=limit_recency and int(frequency)<=limit_frequency and int(monetary)<=limit_monetary:
                            st.write("##### 2.2 Segment new customer")
                            
                            quintiles = {'Recency': {0.2: 17.0, 0.4: 49.0, 0.6: 113.0, 0.8: 234.0},
                                         'Frequency': {0.2: 1.0, 0.4: 1.0, 0.6: 2.0, 0.8: 4.0},
                                         'Monetary': {0.2: 181.09, 0.4: 437.7, 0.6: 914.93, 0.8: 2000.86}}
                            df_customer['R_quintile'] = df_customer['Recency'].apply(Rscore, args=('Recency',quintiles))
                            df_customer['F_quintile'] = df_customer['Frequency'].apply(FMscore, args=('Frequency',quintiles))
                            df_customer['M_quintile'] = df_customer['Monetary'].apply(FMscore, args=('Monetary',quintiles))                            
                            df_customer['RFM_Segment'] = (df_customer['R_quintile'].astype(str) 
                                                          + df_customer['F_quintile'].astype(str) 
                                                          + df_customer['F_quintile'].astype(str))
                            df_customer['RFM_Segment'] = df_customer['RFM_Segment'].astype(int)
                            df_customer['RFM_Name'] = df_customer['RFM_Segment'].apply(split_rfm_seg)
                            
                            df_customer_show = df_customer[['Recency','Frequency','Monetary','RFM_Name']].rename(columns={'RFM_Name':'Segmentation'})
                            st.dataframe(df_customer_show, width=1000)
                            
                            st.download_button("Download customer segmentation as CSV file", 
                                               df_customer_show.to_csv(index=False).encode('utf-8'), 
                                               "rfm_segmentation.csv", "csv", key='download-csv')
                            
                        else:
                            st.error('Invalid input value. Please check carefully and try again.')
                    except Exception as e:
                        print(e)
                        st.error(e)
                        st.error('Please input only number (no special characters, no comma, no dot).')
            else:
                st.button("Get segmentation", disabled=True)  
                
if __name__ == '__main__':
    main()