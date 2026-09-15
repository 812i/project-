import streamlit as st

# إعداد صفحة التطبيق للجوال
st.set_page_config(
    page_title="World Cleanup Day",
    page_icon="🌿",
    layout="centered"
)

# تصميم العنوان المدمج والكامل
st.title("🌿 اليوم العالمي لتنظيف البيئة")
st.markdown("### حملة الرياض الخضراء - بادر وتعهد معنا!")
st.write("شاركنا في المبادرة لحماية بيئتنا وتنظيفها، وسجل تعهدك الشخصي لتكون جزءاً من التغيير.")

st.markdown("---")

# نموذج تسجيل المتطوع
st.subheader("📝 سجل تعهدك البيئي:")

name = st.text_input("اسمك الكريم (أو لقبك):")

pledge_type = st.selectbox("اختر تعهدك الأساسي لهذه المناسبة:", [
    "التطوع الميداني في حملات تنظيف الحدائق والأماكن العامة",
    "الامتناع عن استخدام البلاستيك أحادي الاستخدام لمدة شهر",
    "المساهمة في نشر الوعي البيئي وتنظيم حملات توعوية",
    "إعادة تدوير النفايات المنزلية بانتظام"
])

st.markdown("---")

if st.button("اعتمد تعهدي البيئي 🚀", type="primary"):
    if name.strip() == "":
        st.warning("⚠️ فضلاً أدخل اسمك لتأكيد التعهد.")
    else:
        st.success(f"🎉 شكراً لكِ يا {name}!")
        st.info("📅 التاريخ المستهدف: اليوم العالمي للتنظيف (20 سبتمبر)")
        
        # عرض بطاقة التعهد بشكل أنيق
        st.markdown("---")
        st.markdown("### 🏆 بطاقة سفير البيئة:")
        st.markdown(f"> **المتطوع/ة:** {name}")
        st.markdown(f"> **التعهد:** {pledge_type}")
        st.markdown(f"> *\"معاً لخلق بيئة أنظف وأكثر استدامة لأجل مستقبل أفضل.\"*")
        
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>World Cleanup Day • Mobile Edition (20 Sept)</p>", unsafe_allow_html=True)
