import streamlit as st

# إعداد صفحة التطبيق للجوال
st.set_page_config(
    page_title="Eco Calculator",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 حاسبة البصمة البيئية والتدوير")
st.write("حساب بسيط وسريع لمعرفة أثر نفاياتك اليومية وكيفية تقليلها من جوالك!")

st.markdown("---")

# إدخال المستخدم
st.subheader("📊 أدخل معدل استخدامك اليومي:")

plastic_bottles = st.slider("كم عدد قوارير البلاستيك التي تستخدمها يومياً؟", 0, 10, 2)
paper_bags = st.slider("كم عدد الأكياس أو الأوراق المهدرة أسبوعياً؟", 0, 20, 5)
organic_food = st.selectbox("هل تتخلص من بقايا الطعام بشكل مستمر؟", ["نعم", "أحياناً", "لا تقريباً"])

st.markdown("---")

if st.button("احسب أثرك البيئي الآن", type="primary"):
    # حسابات تقريبية بسيطة وممتعة
    plastic_yearly = plastic_bottles * 365
    co2_saved = plastic_yearly * 0.08  # كيلو غرام من الكربون الموفر بالتدوير
    
    st.success("### 📈 تقرير أثرك البيئي:")
    st.markdown(f"🔹 **استهلاكك السنوي من البلاستيك:** تقريباً `{plastic_yearly}` قارورة.")
    st.markdown(f"🌍 **ما يمكنك توفيره بالتدوير:** تدوير هذه الكمية يمنع انبعاث نحو `{co2_stored:.1f}` كجم من ثاني أكسيد الكربون سنوياً!")
    
    if organic_food == "نعم":
        st.warning("💡 **نصيحة ذكية:** محاولة تحويل الفائض الغذائي إلى سماد منزلي يقلل نفاياتك بنسبة 30%!")
    else:
        st.info("🌟 **رائع جداً!** وعيك البيئي ممتاز ويساهم في حماية الكوكب.")
        
    st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Eco-Calculator • Mobile Edition</p>", unsafe_allow_html=True)
