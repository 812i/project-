import streamlit as st

# إعداد صفحة التطبيق للجوال
st.set_page_config(
    page_title="Eco-Clean Mission",
    page_icon="🧹",
    layout="centered"
)

# تهيئة النقاط وحالة المناطق في الذاكرة المؤقتة للجلسة
if 'cleaned_score' not in st.session_state:
    st.session_state.cleaned_score = 0
if 'zones' not in st.session_state:
    st.session_state.zones = {
        "منطقة الألعاب للأطفال 🛝": False,
        "مسار المشاة الرئيسي 🚶‍♂️": False,
        "المنطقة الخضراء تحت الأشجار 🌳": False,
        "محيط الطاولات والمقاعد 🪑": False
    }

st.title("🧹 مهمة تنظيف الحديقة")
st.markdown("### تحدي اليوم العالمي لتنظيف البيئة")
st.write("الحديقة ملوثة! اضغطي على المناطق أدناه لتنظيفها، جمع النفايات، وإعادة البريق للجمال الطبيعي.")

st.markdown("---")

# عرض لوحة النتائج
st.metric(label="🌟 نقاط النظافة المكتسبة", value=f"{st.session_state.cleaned_score} / 100 نقطة")

st.markdown("### 🗺️ خريطة مواقع الحديقة:")
st.write("اختر منطقة لبدء حملة التنظيف الفوري:")

# تفاعل الأزرار لكل منطقة
for zone_name, is_cleaned in st.session_state.zones.items():
    col1, col2 = st.columns([3, 1])
    with col1:
        if is_cleaned:
            st.success(f"✅ {zone_name} (تم تنظيفها بنجاح!)")
        else:
            st.warning(f"⚠️ {zone_name} (بحاجة للتنظيف)")
    with col2:
        if not is_cleaned:
            if st.button("تنظيف 🗑️", key=f"btn_{zone_name}"):
                st.session_state.zones[zone_name] = True
                st.session_state.cleaned_score += 25
                st.rerun()

st.markdown("---")

# إذا تم إنجاز تنظيف الحديقة بالكامل
if st.session_state.cleaned_score == 100:
    st.balloons()
    st.success("🏆 **مبروك! أتممتِ المهمة بنجاح وأصبحت الحديقة نظيفة 100% لخلق بيئة صحية وآمنة للجميع!**")

# زر إعادة ضبط اللعبة
if st.button("🔄 إعادة تعيين الحديقة من جديد"):
    st.session_state.cleaned_score = 0
    for key in st.session_state.zones:
        st.session_state.zones[key] = False
    st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Eco-Clean Mission • Mobile Edition</p>", unsafe_allow_html=True)
