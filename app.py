import streamlit as st
from calculator import calculate_monthly, calculate_profit

st.set_page_config(page_title="Etsy Profit Calculator",page_icon="🛍️")

st.title(" 🛍️ Etsy Profit Calcualtor 🛍️")
st.caption("Know your real profit before you price your listing.")
with st.sidebar:
    st.header("How to use")
    st.write("1. Enter your product's selling price")
    st.write("2. Enter your costs (materials + shipping)")
    st.write("3. See your real profit instantly")
    st.write("4. Adjust until you hit a healthy margin (20%+)")
st.divider()

col1 , col2 = st.columns(2)
 
with col1:
    selling_price = st.number_input("Selling Price ($)", min_value=0.0, value=25.0, step=0.5)
    material_cost = st.number_input("Material Cost ($)", min_value=0.0, value=5.0, step=0.5)
    
with col2:
    shipping_charged = st.number_input("Shipping Charged to buyer ($)", min_value = 0.0, value = 5.0, step = 0.5)
    actual_shipping = st.number_input("Actual Shipping Cost ($)", min_value= 0.0, value = 4.0, step = 0.5)     
    
units = st.slider("Units sold per month", min_value=0, max_value=500, value=25)

include_ads = st.toggle("Include Offsite Ads fee (15%)?", value=False)
st.divider()

result = calculate_profit(selling_price, material_cost , shipping_charged , actual_shipping , include_ads)
monthly = calculate_monthly(result , selling_price , units)

st.subheader("📊 Results")
col3, col4, col5 = st.columns(3)
col3.metric("Net Profit per Sale", f"${result['net_profit']}")
col4.metric("Profit Margin", f"{result['profit_margin']}%")
col5.metric("Break-even Price", f"${result['break_even_price']}")

st.info(f"Total costs per sale (fees + materials + shipping): **${result['total_costs']}**")

st.subheader("💸 Etsy Fee Breakdown")
fee1, fee2, fee3 = st.columns(3)
fee1.metric("Transaction Fee (6.5%)", f"${result['transaction_fee']}")
fee2.metric("Payment Processing", f"${result['payment_processing_fee']}")
fee3.metric("Listing Fee", "$0.20")

st.info(f"Total Etsy Fees per sale: **${result['total_etsy_fees']}**")

st.subheader("📅 Monthly Projection")
m1, m2, m3 = st.columns(3)
m1.metric("Monthly Revenue", f"${monthly['monthly_revenue']}")
m2.metric("Monthly Fees", f"${monthly['monthly_fees']}")
m3.metric("Monthly Profit", f"${monthly['monthly_profit']}")

st.divider()
if result['net_profit'] < 0:
    st.error("⚠️ You are losing money at this price!")
elif result['profit_margin'] < 20:
    st.warning("Low margin — consider raising your price.")
else:
    st.success(f"Healthy profit! You make ${result['net_profit']} per sale.")    
    
st.divider()
st.subheader("💡 Pricing Tip")
recommended = round(result['break_even_price'] * 1.4, 2)
st.write(f"To hit a healthy 30% margin, we recommend pricing at: **${recommended}**")    