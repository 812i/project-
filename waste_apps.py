import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

# إعداد صفحة Streamlit
st.set_page_config(
    page_title="AI Waste Sorter",
    page_icon="♻️",
    layout="centered"
)

# تحميل نموذج الذكاء الاصطناعي الخفيف (يتم تخزين مؤقت لسرعة التشغيل)
@st.cache_resource
def load_ai_model():
    return MobileNetV2(weights='imagenet')

with st.spinner("جاري تهيئة نموذج الذكاء الاصطناعي للرؤية الحاسوبية..."):
    model = load_ai_model()

# --- تصميم واجهة المستخدم ---
st.title("AI Waste Sorter ♻️")
st.write(
    "تطبيق ذكاء اصطناعي حقيقي مخصص للجوال لتحليل الصور تلقائياً "
    "وتصنيف النفايات لمكانها الصحيح."
)

st.markdown("---")

# رفع الصورة من الجوال
uploaded_file = st.file_uploader(
    "اختر صورة لقطعة النفايات من جوالك...", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        # قراءة الصورة وتجهيزها
        pil_image = Image.open(uploaded_file)
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        st.subheader("الصورة المرفوعة")
        st.image(pil_image, caption="قطعة النفايات قيد التحليل", use_container_width=True)
        
        # زر التحليل بالذكاء الاصطناعي
        if st.button("تحليل وتصنيف بالذكاء الاصطناعي (Classify)", type="primary"):
            with st.spinner("الذكاء الاصطناعي يحلل تفاصيل الصورة..."):
                
                # 1. تجهيز الصورة بمقاسات نموذج MobileNetV2 (224x224)
                img_resized = pil_image.resize((224, 224))
                img_array = np.array(img_resized)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)
                
                # 2. التنبؤ عبر النموذج
                preds = model.predict(img_array)
                decoded_preds = decode_predictions(preds, top=3)[0] # أعلى 3 احتمالات
                
                # تحليل الناتج وتوجيهه لتصنيفات النفايات
                top_pred_name = decoded_preds[0][1].lower()
                top_pred_confidence = float(decoded_preds[0][2]) * 100
                
                # مطابقة الكلمات المفتاحية لتحديد نوع النفايات بناءً على رؤية الذكاء الاصطناعي
                if any(k in top_pred_name for k in ['can', 'tin', 'metal', 'steel', 'aluminum', 'bottle_cap', 'nail']):
                    category = "Metal"
                    emoji = "🥫"
                    rec = "Place it in the metal recycling bin. (علبة معدنية/تنسيق معادن -> حاوية المعادن)"
                elif any(k in top_pred_name for k in ['plastic', 'cup', 'bag', 'jug', 'carton', 'wrapper', 'container']):
                    category = "Plastic"
                    emoji = "♻️"
                    rec = "Place it in the plastic/recycling bin. (مادة بلاستيكية -> حاوية إعادة تدوير البلاستيك)"
                elif any(k in top_pred_name for k in ['paper', 'envelope', 'book', 'cardboard', 'box', 'newspaper', 'magazine']):
                    category = "Paper"
                    emoji = "📄"
                    rec = "Place it in the paper recycling bin. (مادة ورقية/كرتون -> حاوية الورق)"
                else:
                    # افتراضي في حال كانت قطعة طعام أو نبات أو شيء آخر
                    category = "Organic Waste"
                    emoji = "🍎"
                    rec = "Place it in the organic waste bin. (نفايات عضوية أو طعام -> حاوية النفايات العضوية)"

            # عرض النتائج الاحترافية الحقيقية
            st.markdown("### 📊 نتيجة التحليل الذكي")
            
            result_container = st.container()
            with result_container:
                st.metric(label="التصنيف المكتشف بالذكاء الاصطناعي", value=f"{emoji} {category}")
                st.progress(int(top_pred_confidence), text=f"نسبة الثقة التقريبية: {top_pred_confidence:.1f}% (AI Detected: {decoded_preds[0][1]})")
                
                st.success(f"**توجيهات التخلص من النفايات:**\n\n{emoji} {rec}")
                
                # عرض التفاصيل التقنية لما رأه الذكاء الاصطناعي (لكي تري أنه مساعد حقيقي وذكي)
                with st.expander("🔍 عرض تفاصيل تحليل النموذج (AI Insights)"):
                    st.write("أبرز ما تم التعرف عليه في الصورة:")
                    for i, (p_id, p_label, p_score) in enumerate(decoded_preds, 1):
                        st.write(f"{i}. **{p_label}** (الثقة: {float(p_score)*100:.1f}%)")

    except Exception as e:
        st.error(f"حدث خطأ أثناء تحليل الصورة بالذكاء الاصطناعي. (التفاصيل: {e})")
else:
    st.info("👆 اضغط على زر رفع الملفات بالأعلى لاختيار صورة من هاتفك ليقوم الذكاء الاصطناعي بقراءتها.")

# ذيل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>AI Waste Sorter Mobile Edition • Streamlit & TensorFlow</p>", unsafe_allow_html=True)
