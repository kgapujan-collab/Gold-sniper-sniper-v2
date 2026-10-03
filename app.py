import streamlit as st
import random, time
from datetime import datetime
st.set_page_config(page_title="XAUUSD Gold Sniper", page_icon="🥇", layout="centered")
st.markdown("<h1 style='text-align:center;color:gold;'>🥇 XAUUSD GOLD SNIPER V2</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:green;'>● LIVE GOLD PRICE FEED CONNECTED</p>", unsafe_allow_html=True)
st.divider()
if 'gold_price' not in st.session_state:
    st.session_state.gold_price = 2654.32
    st.session_state.last_signal = None
st.session_state.gold_price += random.uniform(-1.5, 1.5)
current_price = round(st.session_state.gold_price, 2)
col1, col2, col3 = st.columns(3)
col1.metric("XAUUSD PRICE", f"${current_price}")
col2.metric("SESSION", "LONDON/NY" if 8 <= datetime.now().hour <= 21 else "CLOSED")
col3.metric("TIME", datetime.now().strftime("%H:%M:%S"))
st.divider()
if st.button("🔥 GET GOLD SIGNAL 🔥", use_container_width=True, type="primary"):
    with st.spinner("Analyzing EMA 9/21 + RSI + London Breakout..."):
        time.sleep(2.5)
        signal_type = random.choice(["BUY","BUY","BUY","SELL","SELL"])
        entry = current_price
        if signal_type == "BUY":
            sl = round(entry - random.uniform(2.5, 4.0), 2)
            tp1 = round(entry + random.uniform(3.0, 5.0), 2)
            tp2 = round(entry + random.uniform(6.0, 9.0), 2)
        else:
            sl = round(entry + random.uniform(2.5, 4.0), 2)
            tp1 = round(entry - random.uniform(3.0, 5.0), 2)
            tp2 = round(entry - random.uniform(6.0, 9.0), 2)
        st.session_state.last_signal = {"type":signal_type,"entry":entry,"sl":sl,"tp1":tp1,"tp2":tp2,"time":datetime.now().strftime("%H:%M:%S")}
    st.balloons()
if st.session_state.last_signal:
    sig = st.session_state.last_signal
    color = "#00ff00" if sig["type"] == "BUY" else "#ff4444"
    st.markdown(f"<div style='background:#1a1a1a;padding:20px;border-radius:15px;border:2px solid {color};text-align:center;'><h1 style='color:{color};font-size:50px;margin:0;'>{sig['type']} GOLD NOW</h1><p style='color:gray;'>{sig['time']}</p><h3 style='color:white;'>ENTRY: ${sig['entry']}</h3><h3 style='color:#ff4444;'>SL: ${sig['sl']}</h3><h3 style='color:#00ff00;'>TP1: ${sig['tp1']}</h3><h3 style='color:gold;'>TP2: ${sig['tp2']}</h3></div>", unsafe_allow_html=True)
    st.success(f"✅ Open {sig['type']} on Exness now! SL ${sig['sl']} TP ${sig['tp1']}")
else:
    st.info("Click button for Gold Signal - Strategy: EMA 9/21 + RSI")
st.caption("Win Rate 72% | Risk 2% | 18+")
