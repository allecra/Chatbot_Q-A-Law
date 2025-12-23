# 🚀 Hướng dẫn Deploy lên Render

## Bước 1: Khởi tạo Git và Push lên GitHub

Chạy các lệnh sau trong PowerShell (từng lệnh một):

```powershell
# Kiểm tra xem đã có git repo chưa
git status

# Nếu chưa có, khởi tạo git repo
git init

# Kiểm tra branch hiện tại
git branch

# Nếu branch là master, đổi sang main (hoặc dùng master)
git branch -M main

# Thêm tất cả files
git add .

# Tạo commit đầu tiên
git commit -m "Initial commit: Trợ lý Tư vấn Pháp Luật"

# Kiểm tra remote đã có chưa
git remote -v

# Nếu remote đã tồn tại nhưng sai, xóa và thêm lại
git remote remove origin
git remote add origin https://github.com/allecra/Chatbot_Q-A-Law.git

# Push lên GitHub
git push -u origin main
```

**Nếu branch của bạn là `master` thay vì `main`:**
```powershell
git push -u origin master
```

## Bước 2: Deploy trên Render

1. **Đăng nhập Render:**
   - Truy cập https://render.com
   - Đăng nhập bằng GitHub

2. **Tạo Web Service mới:**
   - Click "New" → "Web Service"
   - Chọn repository: `allecra/Chatbot_Q-A-Law`
   - Click "Connect"

3. **Cấu hình:**
   - **Name:** `tro-ly-luat` (hoặc tên bạn muốn)
   - **Environment:** `Python 3`
   - **Region:** Chọn gần nhất (Singapore hoặc US)
   - **Branch:** `main` (hoặc `master` nếu bạn dùng master)
   - **Root Directory:** (để trống)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Thiết lập Environment Variables:**
   - Scroll xuống phần "Environment Variables"
   - Click "Add Environment Variable"
   - Thêm 2 biến:
     ```
     Key: LANGFLOW_TOKEN
     Value: sk-xfhoXgssl89tL0EjCEQyK8S2MXkv6SfM_tYgqOhVjgg
     ```
     ```
     Key: API_URL
     Value: https://3e16b6762593.ngrok-free.app/api/v1/run/cf9aed3c-a624-4235-8f0a-234970a9afe2
     ```

5. **Deploy:**
   - Click "Create Web Service"
   - Đợi build (2-5 phút)
   - Khi thấy "Live" màu xanh là thành công!

## Bước 3: Truy cập ứng dụng

Sau khi deploy thành công, bạn sẽ có URL công khai:
- Ví dụ: `https://tro-ly-luat.onrender.com`
- Copy URL này và chia sẻ với mọi người!

## ⚠️ Xử lý lỗi thường gặp

### Lỗi "src refspec main does not match any"
**Nguyên nhân:** Chưa có commit nào hoặc branch không đúng

**Giải pháp:**
```powershell
# Kiểm tra branch hiện tại
git branch

# Nếu thấy master, dùng:
git push -u origin master

# Hoặc đổi sang main:
git branch -M main
git push -u origin main
```

### Lỗi "remote origin already exists"
**Giải pháp:**
```powershell
git remote remove origin
git remote add origin https://github.com/allecra/Chatbot_Q-A-Law.git
```

### App bị sleep trên Free plan
- Free plan sẽ sleep sau 15 phút không hoạt động
- Lần đầu truy cập sau khi sleep mất vài giây để wake up
- Để tránh sleep, có thể dùng dịch vụ ping như UptimeRobot

## 📝 Lưu ý quan trọng

1. **Ngrok URL có thể thay đổi:** Nếu ngrok URL thay đổi, cập nhật lại biến `API_URL` trên Render Dashboard
2. **API Key bảo mật:** Đã được lưu trong Environment Variables, không hardcode trong code
3. **Free plan limitations:** Có thể sleep, nhưng đủ dùng cho demo và testing

