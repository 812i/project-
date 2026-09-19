import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="تحدي النظافة البيئية", page_icon="🌱", layout="centered")

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

st.title("🌱 تحدي اليوم العالمي للنظافة البيئية")
st.write("أتمم مهامك البيئية اليومية، وساهم في حماية كوكبنا للحصول على شارة التميز الخاصة بك!")

# قائمة المهام البيئية
tasks = [
    "استخدام علبة ماء أو كوب قهوة قابل لإعادة الاستخدام 🥤",
    "جمع زجاجات بلاستيكية ووضعها في مخصص إعادة التدوير ♻️",
    "التقاط 3 مخلفات وإلقاؤها في حاوية القمامة أثناء المشي 🗑️",
    "إغلاق صنبور الماء أثناء تنظيف الأسنان لترشيد الاستهلاك 💧",
    "إطفاء الأضواء والأجهزة غير المستخدمة لتوفير الطاقة 💡"
]

st.markdown("---")
st.subheader("📋 مهامك اليومية:")

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
st.write(f"📊 **نسبة إنجاز التحدي:** {percentage}%")
st.progress(progress)

# إدخال الاسم والحصول على الشارة عند اكتمال المهام (100%)
if percentage == 100:
    st.success("🎉 كفو! لقد أتممت جميع المهام البيئية بنجاح وحافظت على بيئتك!")
    
    st.markdown("### 🏆 احصل على شارة حامي البيئة الخاصة بك:")
    user_name = st.text_input("أدخل اسمك الكريم لعرضه على الشارة:")
    
    if user_name:
        st.markdown(f"""
            <div class="badge-card">
                <h2>🌟 وسام حامي البيئة 🌟</h2>
                <p>تشهد هذه الشارة بأن البطل/ـة:</p>
                <h1 style="color: #ffeb3b; margin: 10px 0;">{user_name}</h1>
                <p>قد أتم بنجاح تحدي النظافة البيئية وساهم في جعل العالم مكاناً أنظف وأفضل! 🌍💚</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 يمكنك التقاط صورة الشاشة (Screenshot) لحفظ الشارة ومشاركتها مع أصدقائك!")
else:
    st.warning("⚠️ أتمم جميع المهام أعلاه لتظهر لك شارة الإنجاز الخاصة بك!")
