# Team

## Thông tin nhóm

- Tên nhóm: Armless
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Armless-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/dpduc313/K5-L3A-DAY13-Armless-LaunchEconomics · `main` · (điền khi chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đậu Phúc Đức | 2A202603580 | teflon125.work@gmail.com      | https://github.com/dpduc313 | Người viết code (trước giải lao) → người kiểm số |
|   2 | Nguyễn Đức Đạt | 2A202603544 |       |        | Người kiểm số (trước giải lao) → người viết code; người gắn nhãn 2 ở CP3 (thay Minh) |
|   3 | Đỗ Cao Cường | 2A202603612 | 26ai.cuongdc@vinuni.edu.vn | https://github.com/cuongdc03 | Người gắn nhãn 1 |
|   4 | Nguyễn Văn Minh | 2A202603551 | minhvjjp@gmail.com | https://github.com/killy-mv/ | Giữ hồ sơ (bộ nhãn CP3 của Minh bị bỏ vì có AI đề xuất, xem `bang_loi.md`) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Phân công chi tiết, nhánh và PR: [PHAN_CONG.md](PHAN_CONG.md).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## DauPhucDuc-2A202603580

### Phần việc phụ trách

- Tạo repo nhóm và môi trường chạy `src/.venv`.
- Trước giải lao (người viết code): CP1 và CP2 trong `src/lab13.py`, điền `report/team/bang_chi_phi.md`.
- Sau giải lao (người kiểm số): soạn luật dừng cho `pilot_plan.yaml`, hai dòng rủi ro kinh tế cho `chi_so.md`; chạy các lệnh kiểm tra trước khi merge.

### Đóng góp cụ thể

- A1–A4: ba hàm A1 in ĐẠT (1,20 · 1,25 · 1,25); `mo_hinh` cho chi phí 4.472 đ mỗi ca thành công [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; tách theo loại (quoc_te 1,88×); chi phí cố định 4.599 đ/ca [simulated].
- B1–B4: 9 kịch bản độ nhạy, xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]; giới hạn 2 lần chạy rẻ nhất cho công ty; xem lại 100% tốn 0,98–1,03× [simulated].
- Bốn luật dừng (an toàn, chi phí, mức sử dụng, thời gian xem lại) kèm định nghĩa và cách tính tay số đợt chạy thử.
- Hai dòng rủi ro kinh tế E2 (làm lại gấp đôi, xem lại gấp đôi), số lấy từ bảng B1, B4.
- Rà hồ sơ launch, tên vai thống nhất giữa các file; lưu phiếu gắn nhãn độc lập của Đạt cho CP3.

### Bằng chứng

- PR #2 (commit `6e7da01`): CP1, CP2 trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- PR #10: bốn luật dừng trong `report/team/pilot_plan.yaml`.
- PR #6 (Cường commit): hai dòng rủi ro E2 do Đức soạn, trong `report/team/chi_so.md`.
- PR #12, #13: cập nhật `bang_loi.md`, mục 5 hồ sơ, phiếu `report/team/nhan_cp3_Dat.md`.
- PR #7: báo cáo cá nhân `report/team/2A202603580_DauPhucDuc.md`.
