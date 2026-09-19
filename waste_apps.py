import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Eco-Cleanliness Challenge", page_icon="🌱", layout="centered")

# تنسيق CSS بسيط لتحسين المظهر العام
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    .badge-card {
        background: linear-gradient(135deg, #1b5e20, #4caf50);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 World Environment Cleanliness Challenge")
st.write("Complete your daily eco-friendly tasks and protect our planet to earn your badge!")

# قائمة المهام المختارة
tasks = [
    "قراءة مقال قصير أو معلومة عن أهمية الحفاظ على النظافة البيئية والتنوع البيولوجي 📚",
    "فصل الأجهزة الكهربائية (الشواحن، التلفزيون) عن المقبس عند عدم استخدامها 🔌",
    "إعادة استخدام علبة بلاستيكية أو زجاجية قديمة كحوض لزرع نبتة صغيرة 🪴",
    "استخدام كيس تسوق قماشي بدلاً من الأكياس البلاستيكية لمرة واحدة 🛍️",
    "تجميع الورق والكرتون القديم في المنزل وتسليمه لمراكز إعادة التدوير 📦",
    "الامتناع عن استخدام الأكواب أو المصاصات البلاستيكية طوال اليوم 🥤",
    "فرز العلب المعدنية والعلب الزجاجية عن بقية النفايات المنزلية ♻️"
]

st.markdown("---")
st.subheader("📋 Your Daily Tasks:")

# تتبع حالة المهام
completed_tasks = []
for i, task in enumerate(tasks):
    is_checked = st.checkbox(task, key=f"task_{i}")
    if is_checked:
        completed_tasks.append(task)

# حساب نسبة الإنجاز
total_tasks = len(tasks)
progress = len(completed_tasks) / total_tasks
percentage = int(progress * 100)

st.markdown("---")
st.write(f"📊 **Challenge Progress:** {percentage}%")
st.progress(progress)

# متغير لحفظ حالة البالونات عشان ما تطلع مع كل ريفريش بسيط
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False

# إدخال الاسم والحصول على الشارة عند اكتمال المهام (100%)
if percentage == 100:
    if not st.session_state.balloons_shown:
        st.balloons()  # إطلاق البالونات عند إتمام المهام
        st.session_state.balloons_shown = True
        
    st.success("🎉 Amazing! You have successfully completed all eco-friendly tasks!")
    
    st.markdown("### 🏆 Get Your Eco-Hero Badge:")
    user_name = st.text_input("Enter your name to display on the badge:")
    
    if user_name:
        st.markdown(f"""
            <div class="badge-card">
                <h2>🌟 ECO-HERO BADGE 🌟</h2>
                <p>This is proudly presented to:</p>
                <h1 style="color: #ffeb3b; margin: 10px 0;">{user_name}</h1>
                <p>For successfully completing the Cleanliness Challenge and contributing to a <b>Green Riyadh</b> and a sustainable future! 🌍💚</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 Take a screenshot to save your badge and share it with friends!")
else:
    st.session_state.balloons_shown = False
    st.warning("⚠️ Complete all tasks above to unlock your achievement badge!")
