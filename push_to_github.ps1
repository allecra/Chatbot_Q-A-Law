# Script PowerShell để push code lên GitHub

Write-Host "=== Kiểm tra git status ===" -ForegroundColor Cyan
git status

Write-Host "`n=== Thêm tất cả files ===" -ForegroundColor Cyan
git add .

Write-Host "`n=== Tạo commit ===" -ForegroundColor Cyan
git commit -m "Tăng timeout cho RAG API lên 120 giây và cải thiện UI"

Write-Host "`n=== Kiểm tra branch ===" -ForegroundColor Cyan
$branch = git branch --show-current
Write-Host "Branch hiện tại: $branch" -ForegroundColor Yellow

Write-Host "`n=== Push lên GitHub ===" -ForegroundColor Cyan
if ($branch -eq "main") {
    git push origin main
} elseif ($branch -eq "master") {
    git push origin master
} else {
    Write-Host "Đang push branch: $branch" -ForegroundColor Yellow
    git push origin $branch
}

Write-Host "`n=== Hoàn thành! ===" -ForegroundColor Green
Write-Host "Code đã được push lên GitHub. Streamlit Cloud sẽ tự động deploy!" -ForegroundColor Green

