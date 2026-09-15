import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="Eco-Hero Waste Game",
    page_icon="🌍",
    layout="centered"
)

# تخزين النقاط في الجلسة
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🌍 Eco-Hero: تحدي الفرز الذكي")
st.write(
    "لعبتك البيئية الممتعة لتصنيف النفايات، كسب النقاط الخضراء، "
    "ومعرفة أثرها الحقيقي على البيئة بكل سهولة من جوالك!"
)

st.markdown("---")

# لوحة النتائج المصغرة
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🌟 نقاطك الخضراء", value=f"{st.session_state.score} نقطة")
with col2:
    st.metric(label="♻️ مستوى الوعي", value="مبتدئ بيئي" if st.session_state.score < 20 else "بطل البيئة!")

st.markdown("---")
st.subheader("🗑️ اختر نوع النفايات لمعرفة طريقة التخلص الصحيحة:")

# خيارات النفايات ببطء تفاعلي نظيف
waste_options = {
    "قشرة تفاح / طعام (Organic)": {
        "type": "Organic Waste",
        "emoji": "🍎",
        "bin": "حاوية النفايات العضوية (Green Bin)",
        "tip": "تتحلل طبيعياً وتتحول إلى سماد مفيد للتربة!",
        "points": 10
    },
    "علبة مياه بلاستيكية (Plastic)": {
        "type": "Plastic",
        "emoji": "♻️",
        "bin": "حاوية إعادة تدوير البلاستيك (Yellow Bin)",
        "tip": "إعادة تدوير 10 قوارير يوفر طاقة تشغيل لابتوب لمدة 25 ساعة!",
        "points": 15
    },
    "علبة معدنية / صودا (Metal)": {
        "type": "Metal",
        "emoji": "🥫",
        "bin": "حاوية المعادن (Blue Bin)",
        "tip": "الألمنيوم قابل لإعادة التدوير بنسبة 100% وللا مالئ لهدايا المستقبل!",
        "points": 20
    },
    "صندوق كرتون أو ورق (Paper)": {
        "type": "Paper",
        "emoji": "📄",
        "bin": "حاوية الورق (Brown Bin)",
        "tip": "إعادة تدوير الورق يحمِ الأشجار ويقلل انبعاثات الكربون.",
        "points": 10
    }
}

selected_item = st.selectbox("اختر القطعة الموجودة أمامك:", options=list(waste_options.keys()))

if st.button("تحقق من مكان الرمي واربح النقاط!", type="primary"):
    item_info = waste_options[selected_item]
    
    # إضافة النقاط
    st.session_state.score += item_info['points']
    
    # عرض النتيجة بشكل مرتب وجميل
    st.success(f"### النتيجة صحيحة 100%!")
    st.markdown(f"**{item_info['emoji']} التصنيف:** {item_info['type']}")
    st.markdown(f"📍 **مكان التخلص الصحيح:** `{item_info['bin']}`")
    st.info(f"💡 **معلومة بيئية ذكية:** {item_info['tip']}")
    st.balloons() # تأثير احتفالي ممتع على الجوال!

st.markdown("---")
if st.button("🔄 إعادة ضبط النقاط"):
    st.session_state.score = 0
    st.rerun()

# ذيل الصفحة
fn_text = "Eco-Hero Game • Mobile Edition"
st.markdown(f"<p style='text-align: center; color: gray;'>{fn_text}</p>", unsafe_allow_html=True)
