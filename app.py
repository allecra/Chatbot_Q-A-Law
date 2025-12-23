import streamlit as st
import requests

# --- CẤU HÌNH THÔNG TIN ---
# Sử dụng biến môi trường để bảo mật (khuyến nghị cho production)
# Trên Streamlit Cloud: Settings > Secrets
# Trên Render: Settings > Environment Variables
import os

LANGFLOW_TOKEN = os.getenv("LANGFLOW_TOKEN", "sk-xfhoXgssl89tL0EjCEQyK8S2MXkv6SfM_tYgqOhVjgg")
API_URL = os.getenv("API_URL", "https://3e16b6762593.ngrok-free.app/api/v1/run/cf9aed3c-a624-4235-8f0a-234970a9afe2")
# Timeout cho API request (giây) - tăng lên để đợi RAG xử lý lâu hơn
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "120"))  # Mặc định 120 giây (2 phút)

# LangFlow API v1.5+ có thể yêu cầu x-api-key header thay vì Authorization Bearer
HEADERS = {
    "x-api-key": LANGFLOW_TOKEN,  # Format cho LangFlow v1.5+
    "Content-Type": "application/json",
    "ngrok-skip-browser-warning": "true", # Sửa lỗi 403 từ ngrok
    "Accept": "application/json"
}

st.set_page_config(page_title="Hệ thống Trợ lý Luật", page_icon="⚖️", layout="wide")

# --- SIDEBAR: TẢI TÀI LIỆU & CAMERA ---
with st.sidebar:
    st.header("📂 Công cụ hỗ trợ")
    
    # Nút tải tài liệu (Ảnh 2 đã có UI này)
    uploaded_file = st.file_uploader("Tải lên file luật (PDF, Docx)", type=['pdf', 'docx', 'txt'])
    if uploaded_file:
        st.success(f"✅ Đã nhận: {uploaded_file.name}")
    
    st.divider()
    
    # Nút chụp ảnh văn bản
    st.write("📸 Chụp ảnh văn bản cần kiểm tra")
    img_file = st.camera_input("Camera", label_visibility="hidden") # Ẩn label để gọn giao diện
    if img_file:
        st.image(img_file, caption="Ảnh đã chụp", use_container_width=True)

    st.divider()
    if st.button("🗑️ Xóa lịch sử phiên"):
        st.session_state.messages = []
        st.rerun()

# --- GIAO DIỆN CHÍNH ---
st.title("⚖️ Trợ Lý Tư Vấn Pháp Luật")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Xử lý nhập liệu
if prompt := st.chat_input("Nhập câu hỏi hoặc nội dung cần kiểm tra luật..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🔍 **Đang xử lý:** Hệ thống RAG đang phân tích câu hỏi và tìm kiếm trong cơ sở dữ liệu pháp luật. Vui lòng đợi...")
        
        # Hiển thị spinner trong khi đợi API response
        with st.spinner("⏳ Đang xử lý... (có thể mất vài phút cho câu hỏi phức tạp)"):
            try:
                payload = {
                    "input_value": prompt,
                    "output_type": "chat",
                    "input_type": "chat"
                }
                
                # Thử với headers hiện tại (x-api-key)
                # Sử dụng timeout dài hơn để đợi RAG xử lý
                response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=API_TIMEOUT)
                
                # Nếu gặp lỗi 403, thử với Authorization Bearer header
                if response.status_code == 403:
                    fallback_headers = {
                        "Authorization": f"Bearer {LANGFLOW_TOKEN}",
                        "Content-Type": "application/json",
                        "ngrok-skip-browser-warning": "true",
                        "Accept": "application/json"
                    }
                    response = requests.post(API_URL, json=payload, headers=fallback_headers, timeout=API_TIMEOUT)
                
                if response.status_code == 200:
                    try:
                        result = response.json()
                        # Xử lý an toàn với nhiều cấu trúc response có thể có
                        answer = None
                        
                        # Thử các cấu trúc response khác nhau
                        if 'outputs' in result and len(result['outputs']) > 0:
                            if 'outputs' in result['outputs'][0] and len(result['outputs'][0]['outputs']) > 0:
                                if 'results' in result['outputs'][0]['outputs'][0]:
                                    if 'message' in result['outputs'][0]['outputs'][0]['results']:
                                        if 'text' in result['outputs'][0]['outputs'][0]['results']['message']:
                                            answer = result['outputs'][0]['outputs'][0]['results']['message']['text']
                        
                        # Nếu không tìm thấy theo cấu trúc trên, thử các cấu trúc khác
                        if answer is None:
                            if 'output' in result:
                                answer = result['output']
                            elif 'text' in result:
                                answer = result['text']
                            elif 'message' in result:
                                answer = result['message']
                            elif 'result' in result:
                                answer = str(result['result'])
                        
                        if answer:
                            message_placeholder.markdown(answer)
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                        else:
                            # Hiển thị toàn bộ response để debug
                            st.error(f"Cấu trúc response không nhận dạng được. Response: {result}")
                            message_placeholder.markdown("⚠️ Không thể đọc được phản hồi từ API.")
                            
                    except ValueError as json_error:
                        st.error(f"Lỗi parse JSON: {str(json_error)}")
                        st.error(f"Response text: {response.text[:500]}")
                        message_placeholder.markdown("⚠️ Phản hồi từ API không phải định dạng JSON hợp lệ.")
                elif response.status_code == 403:
                    # Xử lý riêng cho lỗi authentication
                    try:
                        error_detail = response.json()
                        error_msg = error_detail.get('detail', response.text[:500])
                    except:
                        error_msg = response.text[:500] if response.text else "Lỗi xác thực"
                    
                    st.error(f"🔐 Lỗi xác thực API (403): {error_msg}")
                    st.warning("💡 **Đã thử cả hai phương thức xác thực:** `x-api-key` và `Authorization Bearer`")
                    with st.expander("📝 Hướng dẫn khắc phục"):
                        st.markdown("""
                        1. **Kiểm tra API Key:** Đảm bảo API Key đúng và còn hiệu lực
                        2. **Kiểm tra LangFlow server:** Xác nhận server đang chạy và có thể truy cập
                        3. **Cấu hình server:** Nếu tự host LangFlow, thử set biến môi trường:
                           ```bash
                           LANGFLOW_SKIP_AUTH_AUTO_LOGIN=true
                           ```
                        4. **Kiểm tra URL:** Xác nhận API URL và endpoint ID đúng
                        """)
                    message_placeholder.markdown("⚠️ Không thể xác thực với LangFlow API sau khi thử cả hai phương thức.")
                else:
                    # Hiển thị lỗi chi tiết để debug
                    error_text = response.text[:500] if response.text else "Không có thông tin lỗi"
                    st.error(f"Lỗi API ({response.status_code}): {error_text}")
                    message_placeholder.markdown("⚠️ Đã xảy ra lỗi khi kết nối với LangFlow.")
                    
            except requests.exceptions.Timeout:
                st.error(f"⏱️ Yêu cầu quá thời gian chờ ({API_TIMEOUT} giây). RAG có thể đang xử lý câu hỏi phức tạp.")
                st.info("💡 **Gợi ý:** Câu hỏi của bạn có thể cần thời gian xử lý lâu hơn. Vui lòng thử lại hoặc đơn giản hóa câu hỏi.")
                message_placeholder.markdown("⚠️ Kết nối với API mất quá nhiều thời gian. RAG có thể đang phân tích dữ liệu lớn.")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Không thể kết nối đến API. Vui lòng kiểm tra kết nối mạng.")
                message_placeholder.markdown("⚠️ Không thể kết nối với LangFlow.")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {str(e)}")
                message_placeholder.markdown("⚠️ Đã xảy ra lỗi không mong đợi.")