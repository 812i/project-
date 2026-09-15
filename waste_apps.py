import streamlit as st
import openai
import os

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="Trash to Art Gallery",
    page_icon="🎨",
    layout="centered"
)

# ⚠️ هام جداً: ضعي مفتاح الـ API الخاص بك هنا (مؤقتاً للتجربة، أو استخدمي ملف .env)
# يمكنك الحصول عليه من: https://platform.openai.com/
# إذا لم يكن لديك مفتاح، سيعمل التطبيق بدون ميزة الذكاء الاصطناعي.
openai.api_key = "Sk-proj-07xatW5KilQ1CH5QOSJf1pUbv-1bIvgTeaO4TqTYAKsFKpsJGPuqpcsDJduM2aRERL_ch7uultT3BlbkFJ18oX9CpdqTfrFrvqaXlpfGLrgjSAiRRWxGd7mMX_heGmFxhp9q5tZCCUhWbFXm70dNMblhqKUA "

# عنوان التطبيق والبانر
st.title("🎨 معرض الفن الرقمي للنفايات")
st.markdown("### تحويل المهملات إلى تحف فنية بمناسبة اليوم العالمي للتنظيف")
st.write("اختر نوعاً من النفايات الشائعة، وشاهد كيف يحولها الذكاء الاصطناعي إلى قطعة فنية فريدة!")

st.markdown("---")

# 1. اختيار المستخدم
st.subheader("🔍 اختر نوع النفايات لتحويلها:")
waste_item = st.selectbox("ما هي القطعة التي تريد رؤيتها كفن؟", [
    "قارورة بلاستيكية مهملة",
    "علبة مشروبات غازية فارغة",
    "إطار سيارة قديم",
    "مجموعة أكياس بلاستيكية",
    "أجهزة إلكترونية تالفة",
    "بقايا طعام مهدرة"
])

# قاموس لترجمة الوصف العربي إلى وصف إنجليزي دقيق لنموذج الذكاء الاصطناعي
art_prompts = {
    "قارورة بلاستيكية مهملة": "a detailed sculpture made entirely from recycled plastic bottles, glittering in sunlight, modern art style",
    "علبة مشروبات غازية فارغة": "a stunning mosaic mural created from crushed aluminum soda cans, colorful and reflective, urban art style",
    "إطار سيارة قديم": "a futuristic planter and seat made from old tires, covered in moss and flowers, sustainable design",
    "مجموعة أكياس بلاستيكية": "an avant-garde fashion dress created from fused and layered plastic bags, translucent and flowing, high fashion",
    "أجهزة إلكترونية تالفة": "an intricate steampunk sculpture assembled from discarded circuit boards, wires, and keyboards, detailed and complex",
    "بقايا طعام مهدرة": "a hyperrealistic painting depicting organic food waste transformed into fertile soil and sprouting plants, environmental message"
}

# 2. زر التنفيذ
if st.button("✨ حوّل النفايات إلى تحفة فنية!", type="primary"):
    if openai.api_key == "Sk-proj-07xatW5KilQ1CH5QOSJf1pUbv-1bIvgTeaO4TqTYAKsFKpsJGPuqpcsDJduM2aRERL_ch7uultT3BlbkFJ18oX9CpdqTfrFrvqaXlpfGLrgjSAiRRWxGd7mMX_heGmFxhp9q5tZCCUhWbFXm70dNMblhqKUA ":
        st.error("⚠️ لم يتم العثور على مفتاح OpenAI API. يرجى وضع مفتاحك في الكود لتفعيل ميزة الذكاء الاصطناعي.")
    else:
        with st.spinner(f"جاري تحويل {waste_item} إلى قطعة فنية مذهلة..."):
            try:
                # استدعاء نموذج DALL-E 2 لتوليد الصورة
                response = openai.Image.create(
                    prompt=f"A stunning professional photograph of {art_prompts[waste_item]}, clean background, studio lighting.",
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                
                # عرض النتيجة بشكل مبهر
                st.success("✅ تم إنجاز العمل الفني بنجاح!")
                st.image(image_url, caption=f"التحفة الفنية المستوحاة من: {waste_item}", use_column_width=True)
                st.balloons()
                
                st.markdown("---")
                st.info("💡 **رسالة اليوم العالمي للتنظيف:** كل قطعة نفايات يمكن أن تكون بداية جديدة إذا أعدنا تدويرها وفكرنا فيها بطريقة إبداعية. شاركنا في تنظيف كوكبنا!")
            
            except Exception as e:
                st.error(f"⚠️ حدث خطأ أثناء توليد الصورة: {e}")

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Trash-to-Art Gallery • AI Edition • 20 Sept</p>", unsafe_allow_html=True)
