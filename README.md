# ⚖️ Hệ thống Trợ lý Tư vấn Pháp Luật

Ứng dụng web Streamlit để tư vấn pháp luật sử dụng LangFlow API.

## 🚀 Deploy lên Render

### Bước 1: Chuẩn bị code
- Đảm bảo có file `app.py` và `requirements.txt`
- Code đã được cấu hình để sử dụng biến môi trường

### Bước 2: Tạo tài khoản Render
1. Truy cập [render.com](https://render.com)
2. Đăng ký/Đăng nhập tài khoản (có thể dùng GitHub)

### Bước 3: Deploy ứng dụng
1. **Tạo Web Service mới:**
   - Vào Dashboard > New > Web Service
   - Kết nối repository GitHub của bạn (hoặc deploy từ Git)
   - Hoặc chọn "Deploy existing project" và upload code

2. **Cấu hình:**
   - **Name:** Tên ứng dụng (ví dụ: `tro-ly-luat`)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - **Plan:** Chọn Free plan (hoặc paid nếu cần)

3. **Thiết lập Environment Variables:**
   - Vào tab "Environment"
   - Thêm các biến sau:
     ```
     LANGFLOW_TOKEN=sk-xfhoXgssl89tL0EjCEQyK8S2MXkv6S2MXkv6SfM_tYgqOhVjgg
     API_URL=https://3e16b6762593.ngrok-free.app/api/v1/run/cf9aed3c-a624-4235-8f0a-234970a9afe2
     ```

4. **Deploy:**
   - Click "Create Web Service"
   - Render sẽ tự động build và deploy
   - Đợi vài phút để hoàn tất

### Bước 4: Truy cập ứng dụng
- Sau khi deploy thành công, bạn sẽ nhận được URL công khai
- Ví dụ: `https://tro-ly-luat.onrender.com`

## 📝 Lưu ý quan trọng

### Về ngrok URL:
- URL ngrok có thể thay đổi khi restart
- Nếu ngrok URL thay đổi, cập nhật lại biến môi trường `API_URL` trên Render
- Hoặc cân nhắc sử dụng domain cố định cho LangFlow server

### Bảo mật:
- ✅ API Key được lưu trong Environment Variables (an toàn)
- ✅ Không hardcode credentials trong code
- ⚠️ Đảm bảo LangFlow server có cấu hình bảo mật phù hợp

### Giới hạn Free Plan:
- Render Free plan có thể sleep sau 15 phút không hoạt động
- Lần đầu truy cập sau khi sleep có thể mất vài giây để wake up
- Nếu cần performance tốt hơn, cân nhắc upgrade lên paid plan

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

