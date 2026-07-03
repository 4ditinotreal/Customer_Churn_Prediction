import streamlit as st
import plotly.express as px
from utils import load_data
from logger import setup_logger

logger = setup_logger("Analytics Dashboard")

st.set_page_config(page_title="Analytics",layout="wide")
# title of the project
st.title("📊 Customer Churn Analytics Dashboard")

try:
    df = load_data()
    logger.info("data has been loaded")
    
    total_customers = df.shape[0]
    churned_customers = df[df['Churn'] == "Yes"].shape[0]
    active_customers = total_customers - churned_customers
    churn_rate = round( (churned_customers / total_customers) * 100,2)
    logger.info(f"{total_customers} - {churned_customers} - {active_customers}")
    col1, col2,col3 = st.columns(3)
    
    col1.metric("👥 Total Customers",value=total_customers)
    col2.metric("💔 Churned Customers",value=churned_customers,delta=f"{churn_rate}%"   )
    col3.metric("🟢 Active Customers",value=active_customers)
    logger.info("Cards created")

    st.markdown("-----")
    #creating the filter section
    
    with st.expander("🔍 Filter Data"):
        filter_gender = st.multiselect("Filter by Gender",
                                       options= df["gender"].unique(),
                                       default= df["gender"].unique())
        filter_contract = st.multiselect("Filter by Contract Type",
                                       options= df["Contract"].unique(),
                                       default= df["Contract"].unique())

        df = df[df["gender"].isin(filter_gender) | df["Contract"].isin(filter_contract)]
    
    col4, col5 = st.columns(2)
    with col4:
        fig1 = px.histogram(df, x="MonthlyCharges", nbins=30, title="📈 Monthly Charges Distribution", color="Churn")
        st.plotly_chart(fig1, use_container_width=True)
        logger.info("histogram has been loaded")
    
    with col5:
        fig2 = px.pie(df[df['Contract'].isin(filter_contract)], names="Contract", title="📋 Contract Type Distribution", hole=0.0)
        st.plotly_chart(fig2, use_container_width=True)
        logger.info("Pie has been loaded")
    
    col6,col7 = st.columns(2)
    with col6:
        fig2 = px.pie(df[df['gender'].isin(filter_gender)], names="gender", title="🙎‍♂️ Gender Type Distribution 🙎‍♀️", hole=0.0)
        st.plotly_chart(fig2, use_container_width=True)
        logger.info("Pie has been loaded")

    with col7:
        fig7 = px.box(df,x="Churn",y="MonthlyCharges",title = "💰 Churn vs Charges",color= "Churn")
        st.plotly_chart(fig7,use_container_width=True)
        logger.info("Box has been created")
        
except Exception as e:
    logger.error("Error has occurred")
    logger.error(e)