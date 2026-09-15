import streamlit as st
import base64
from pathlib import Path

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="Trash to Art Gallery",
    page_icon="🎨",
    layout="centered"
)

# --- وظيفة مساعدة لتحميل الصور المحلية وتحويلها إلى Base64 لعرضها في التطبيق ---
def get_img_as_base64(file_path):
    if not Path(file_path).exists():
        return None
    with open(file_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

# --- تعريف مسارات الصور الجاهزة ---
# ملاحظة: يجب أن تكون الصور موجودة في نفس مجلد ملف الكود (أو في مجلد images/ وتعديل المسار)
# لتجربة فورية، تم استخدام روابط صور خارجية عامة كمثال (ويمكن استبدالها بصورك الخاصة لاحقاً)
art_images = {
    "قارورة بلاستيكية مهملة": "https://i.ibb.co/qN96L5Y/art-plastic-bottles.jpg", # مثال فني لزجاجات بلاستيكية
    "علبة مشروبات غازية فارغة": "https://i.ibb.co/7gL2JvT/art-aluminum-cans.jpg", # مثال فني لعلب ألمنيوم
    "إطار سيارة قديم": "https://i.ibb.co/j6w8T5X/art-tires-planter.jpg",   # مثال فني لإطارات معاد تدويرها
    "مجموعة أكياس بلاستيكية": "https://i.ibb.co/x1N3q0Y/art-plastic-bags-dress.jpg", # مثال فني لفساتين من الأكياس
    "أجهزة إلكترونية تالفة": "https://i.ibb.co/hZ41Q1D/art-circuit-board-sculpture.jpg", # مثال فني من لوحات إلكترونية
    "بقايا طعام مهدرة": "https://i.ibb.co/bWHx2Fp/art-food-waste-compost.jpg" # مثال فني بيئي للطعام والسماد
}

# عنوان التطبيق والبانر
st.title("🎨 معرض الفن الرقمي للنفايات")
st.markdown("### تحويل المهملات إلى تحف فنية بمناسبة اليوم العالمي للتنظيف")
st.write("اختر نوعاً من النفايات الشائعة، وشاهد كيف يمكن تحويلها إلى قطعة فنية فريدة!")

st.markdown("---")

# 1. اختيار المستخدم
st.subheader("🔍 اختر نوع النفايات لتحويلها:")
waste_item = st.selectbox("ما هي القطعة التي تريد رؤيتها كفن؟", list(art_images.keys()))

# 2. زر التنفيذ
if st.button("✨ اعرض التحفة الفنية!", type="primary"):
    with st.spinner(f"جاري تحميل التحفة الفنية المستوحاة من: {waste_item}..."):
        try:
            # جلب رابط الصورة
            image_url = art_images[waste_item]
            
            # عرض النتيجة بشكل مبهر
            st.success("✅ تم إنجاز العمل الفني!")
            # عرض الصورة باستخدام الرابط المباشر (أسرع وأضمن)
            st.image(image_url, caption=f"التحفة الفنية المستوحاة من: {waste_item}", use_column_width=True)
            st.balloons()
            
            st.markdown("---")
            st.info("💡 **رسالة اليوم العالمي للتنظيف:** كل قطعة نفايات يمكن أن تكون بداية جديدة إذا أعدنا تدويرها وفكرنا فيها بطريقة إبداعية. شاركنا في تنظيف كوكبنا!")
        
        except Exception as e:
            st.error(f"⚠️ حدث خطأ أثناء تحميل الصورة: {e}")

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Trash-to-Art Gallery • Creative Edition • 20 Sept</p>", unsafe_allow_html=True)
