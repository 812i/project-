import streamlit as st
from datetime import date

# إعداد صفحة التطبيق للجوال
st.set_page_config(
    page_title="World Cleanup Day 2026",
    page_icon="🌿",
    layout="centered"
)

# تصميم العنوان والبانر
st.title("🌿 اليوم العالمي للتنظيف")
st.markdown("### حملة الرياض الخضراء - بادر وتعهد معنا!")
st.write("شاركنا في المبادرة الوطنية لحماية بيئتنا وتنظيفها، وسجل تعهدك الشخصي لتكون جزءاً من التغيير.")

st.markdown("---")

# نموذج تسجيل المتطوع / المشارك
st.subheader("📝 سجل تعهدك البيئي:")

name = st.text_input("اسمك الكريم (أو لقبك):")

pledge_type = st.selectbox("اختر تعهدك الأساسي لهذه المناسبة:", [
    "التطوع الميداني في حملات تنظيف الشواطئ أو الحدائق",
    "الامتناع عن استخدام البلاستيك أحادي الاستخدام لمدة شهر",
    "المساهمة في نشر الوعي البيئي وتنظيم حملات توعوية",
    "إعادة تدوير النفايات المنزلية بانتظام"
])

city = st.selectbox("المدينة:", ["الرياض", "الجدة", "الشرقية", "أبها", "مناطق أخرى"])

st.markdown("---")

if st.button("اعتمد تعهدي البيئي 🚀", type="primary"):
    if name.strip() == "":
        st.warning("⚠️ فضلاً أدخل اسمك لتأكيد التعهد.")
    else:
        st.success(f"🎉 شكراً لكِ يا **{name}**!")
        st.info(f"📍 **الموقع:** {city} | 📅 **التاريخ المستهدف:** اليوم العالمي للتنظيف (20 سبتمبر)")
        
        # عرض بطاقة التعهد بشكل أنيق
        st.markdown("---")
        st.markdown("### 🏆 بطاقة سفير البيئة:")
        st.markdown(f"> **المتطوع/ة:** {name}")
        st.markdown(f"> **التعهد:** {pledge_type}")
        st.markdown(f"> *\"معاً لخلق بيئة أنظف وأكثر استدامة لأجل مستقبل أفضل.\"*")
        
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>World Cleanup Day Initiative • Mobile Edition</p>", unsafe_allow_html=True)
