import streamlit as st

# 1. إعدادات الصفحة لتناسب الجوال بشكل تلقائي
st.set_page_config(
    page_title="تحدي الـ 7 أيام البيئي",
    page_icon="🌱",
    layout="centered" # يضمن بقاء المحتوى في المنتصف ومناسباً للشاشات الصغيرة
)

# تصميم مخصص لتحسين الخطوط والأزرار على الجوال
st.markdown("""
    <style>
    .big-title { font-size: 1.8rem !important; font-weight: bold; text-align: center; color: #2E7D32; }
    .subtitle { font-size: 1.1rem; text-align: center; color: #555; margin-bottom: 20px; }
    div[data-testid="stCheckbox"] { padding: 8px; background-color: #f9f9f9; border-radius: 8px; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<p class="big-title">🌱 تحدي الـ 7 أيام البيئي</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">بمناسبة اليوم العالمي للنظافة - أنجز المهام يومياً لجعل كوكبنا أفضل!</p>', unsafe_allow_html=True)

# 2. قائمة المهام اليومية
tasks = [
    "📅 اليوم 1: استبدل الأكياس البلاستيكية بأكياس قماشية مستدامة.",
    "📅 اليوم 2: تجنب شراء أي قوارير ماء بلاستيكية واستخدم مطرتك الخاصة.",
    "📅 اليوم 3: افصل النفايات في منزلك (بلاستيك، ورق، بقايا طعام).",
    "📅 اليوم 4: قلل هدر الطعام (تناول وجبة كاملة دون مخلفات).",
    "📅 اليوم 5: اجمع 5 قطع من النفايات البلاستيكية من محيطك أو الشارع ووفرها للحاويات المخصصة.",
    "📅 اليوم 6: أغلق الأجهزة غير المستخدمة ووفر الطاقة.",
    "📅 اليوم 7: انشر الوعي! شارك لقطة شاشة لإنجازك مع صديق ليدخل التحدي."
]

# 3. تتبع حالة المهام
completed_tasks = 0

st.subheader("📋 مهامك اليومية:")
for task in tasks:
    # الحالات المحددة يتم حفظها تفاعلياً
    if st.checkbox(task):
        completed_tasks += 1

# 4. حساب النسبة المئوية للإنجاز
total_tasks = len(tasks)
progress_percentage = completed_tasks / total_tasks

# 5. عرض شريط التقدم (Progress Bar)
st.write("---")
st.write(f"📊 **نسبة إنجاز التحدي:** {int(progress_percentage * 100)}%")
st.progress(progress_percentage)

# 6. مكافأة النجاح عند إتمام التحدي بالكامل
if completed_tasks == total_tasks:
    st.balloons() # تأثير بالونات احتفالية يظهر بشكل رائع على الجوال
    st.success("🎉 كفو! لقد أتممت تحدي الـ 7 أيام بنجاح وساهمت في حماية بيئتك!")
elif completed_tasks > 0:
    st.info(f"💪 ممتاز! لقد أنجزت {completed_tasks} من أصل {total_tasks} مهام. استمر!")
else:
    st.warning("👋 ابدأ التحدي الآن بالضغط على المهام التي قمت بها اليوم!")
