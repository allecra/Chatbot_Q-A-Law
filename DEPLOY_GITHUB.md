# 🚀 Deploy lên Streamlit Cloud (qua GitHub)

Streamlit Cloud là dịch vụ miễn phí của Streamlit để deploy app trực tiếp từ GitHub repository.

## Bước 1: Push code lên GitHub

Chạy các lệnh sau trong PowerShell:

```powershell
# Kiểm tra git status
git status

# Nếu chưa có git repo, khởi tạo
git init

# Kiểm tra branch
git branch

# Thêm tất cả files
git add .

# Tạo commit
git commit -m "Initial commit: Trợ lý Tư vấn Pháp Luật"

# Kiểm tra remote
git remote -v

# Nếu remote chưa đúng, xóa và thêm lại
git remote remove origin
git remote add origin https://github.com/allecra/Chatbot_Q-A-Law.git

# Push lên GitHub (thử cả main và master)
git branch -M main
git push -u origin main

# Hoặc nếu branch là master:
# git push -u origin master
```

## Bước 2: Deploy lên Streamlit Cloud

1. **Truy cập Streamlit Cloud:**
   - Vào https://share.streamlit.io/
   - Đăng nhập bằng tài khoản GitHub của bạn

2. **Kết nối GitHub:**
   - Click "New app"
   - Chọn "Authorize Streamlit Cloud" nếu chưa kết nối
   - Cho phép Streamlit Cloud truy cập repository của bạn

3. **Cấu hình App:**
   - **Repository:** Chọn `allecra/Chatbot_Q-A-Law`
   - **Branch:** `main` (hoặc `master` nếu bạn dùng master)
   - **Main file path:** `app.py`
   - **App URL:** (tự động tạo, ví dụ: `chatbot-q-a-law`)

4. **Thiết lập Secrets (Environment Variables):**
   - Click "Advanced settings"
   - Vào tab "Secrets"
   - Thêm các secrets sau:
     ```toml
     LANGFLOW_TOKEN = "sk-xfhoXgssl89tL0EjCEQyK8S2MXkv6SfM_tYgqOhVjgg"
     API_URL = "https://3e16b6762593.ngrok-free.app/api/v1/run/cf9aed3c-a624-4235-8f0a-234970a9afe2"
     ```

5. **Deploy:**
   - Click "Deploy!"
   - Đợi vài phút để build và deploy
   - Khi thấy "Your app is live!" là thành công!

## Bước 3: Truy cập ứng dụng

Sau khi deploy thành công, bạn sẽ có URL công khai:
- Format: `https://chatbot-q-a-law.streamlit.app`
- URL này sẽ được hiển thị trên Streamlit Cloud dashboard

## ✅ Ưu điểm của Streamlit Cloud

- ✅ **Miễn phí hoàn toàn**
- ✅ **Tự động deploy** khi push code mới lên GitHub
- ✅ **Không bị sleep** như Render free plan
- ✅ **Tích hợp tốt với GitHub**
- ✅ **Dễ quản lý** qua dashboard

## 🔄 Cập nhật ứng dụng

Mỗi khi bạn push code mới lên GitHub:
```powershell
git add .
git commit -m "Update app"
git push origin main
```

Streamlit Cloud sẽ tự động detect và redeploy app!

## ⚠️ Lưu ý

1. **Secrets:** Đảm bảo đã thêm `LANGFLOW_TOKEN` và `API_URL` trong Secrets
2. **Ngrok URL:** Nếu ngrok URL thay đổi, cập nhật lại trong Secrets
3. **Requirements.txt:** Phải có file `requirements.txt` với đầy đủ dependencies

## 📝 File cần có trong repository

- ✅ `app.py` - File chính
- ✅ `requirements.txt` - Dependencies
- ✅ `.gitignore` - Git ignore file
- ✅ `README.md` - Documentation (tùy chọn)

