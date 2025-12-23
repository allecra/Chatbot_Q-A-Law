# ⚖️ Hệ thống Trợ lý Tư vấn Pháp Luật

Ứng dụng web Streamlit để tư vấn pháp luật sử dụng LangFlow API.

## 🚀 Deploy lên Streamlit Cloud (Qua GitHub)

### Cách 1: Streamlit Cloud (Khuyến nghị - Miễn phí)

1. **Push code lên GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy trên Streamlit Cloud:**
   - Truy cập https://share.streamlit.io/
   - Đăng nhập bằng GitHub
   - Click "New app"
   - Chọn repository: `allecra/Chatbot_Q-A-Law`
   - Main file: `app.py`
   - Thêm Secrets trong Advanced settings:
     ```
     LANGFLOW_TOKEN=sk-xfhoXgssl89tL0EjCEQyK8S2MXkv6SfM_tYgqOhVjgg
     API_URL=https://3e16b6762593.ngrok-free.app/api/v1/run/cf9aed3c-a624-4235-8f0a-234970a9afe2
     ```
   - Click "Deploy!"

3. **Truy cập app:** URL sẽ có dạng `https://your-app-name.streamlit.app`

**Ưu điểm:**
- ✅ Miễn phí hoàn toàn
- ✅ Tự động deploy khi push code mới
- ✅ Không bị sleep
- ✅ Tích hợp tốt với GitHub

Xem hướng dẫn chi tiết trong file `DEPLOY_GITHUB.md`

### Cách 2: Render (Alternative)

Xem hướng dẫn trong file `DEPLOY.md`

## 🔧 Chạy local

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py
```

Truy cập tại: http://localhost:8501

## 📦 Dependencies

- `streamlit>=1.28.0` - Framework web app
- `requests>=2.31.0` - HTTP requests đến LangFlow API

## 🔐 Bảo mật

- API Key được lưu trong Secrets/Environment Variables
- Không hardcode credentials trong code
- Sử dụng biến môi trường để bảo mật

## 📝 Lưu ý

- Ngrok URL có thể thay đổi khi restart - cần cập nhật lại trong Secrets
- Đảm bảo LangFlow server đang chạy và có thể truy cập
