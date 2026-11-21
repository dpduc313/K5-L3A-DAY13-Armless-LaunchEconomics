# Báo cáo cá nhân — DauPhucDuc-2A202603580

## 1. Thông tin thành viên

- Họ tên: Đậu Phúc Đức
- MSSV: 2A202603580
- Email: [Đức điền]
- GitHub: dpduc313
- Vai trong nhóm: người viết code (trước giải lao), người kiểm số (sau giải lao)

## 2. Phần việc phụ trách

- Tạo repo nhóm `K5-L3A-DAY13-Armless-LaunchEconomics` và môi trường chạy `src/.venv`.
- CP1 và CP2: viết `src/lab13.py` cho nhiệm vụ A (A1–A4) và B (B1–B4), điền `report/team/bang_chi_phi.md`.
- Sau giải lao: soạn luật dừng cho `pilot_plan.yaml` (đưa Đạt) và hai dòng rủi ro kinh tế cho `chi_so.md` (đưa Cường); kiểm số trước khi merge.

## 3. Đóng góp cụ thể

- **A1:** ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** hàm `mo_hinh` cộng token và tool trên **mọi** lần chạy (kể cả lần lỗi), chia cho số việc thành công: 4.472 đ mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ). Khoản lớn nhất là làm lại, 51,8% [simulated].
- **A3, A4:** tách theo `loai` (quoc_te 1,88× của 12.000 đ, chạy lại không giúp: 30% → 11,4% → 2,2%); chi phí cố định 40 triệu/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× khi khối lượng còn một nửa [simulated].
- **B1–B4:** 9 kịch bản độ nhạy, xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]; B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]); B4: xem lại 100% tốn 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated].
- **Luật dừng:** soạn luật an toàn, chi phí, mức sử dụng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ, đặt ngưỡng an toàn so với nhóm đối chứng vì tỉ lệ mở lại hiện tại đã 3,97% trong phạm vi.
- **Rủi ro kinh tế:** hai dòng làm lại gấp đôi và xem lại gấp đôi, số lấy từ bảng B1.

## 4. Bằng chứng

- Commit `6e7da01` "CP1, CP2: mô hình chi phí và bảng độ nhạy", merge qua PR #2.
- File: `src/lab13.py` (phần A, B), `report/team/bang_chi_phi.md`.
- Kiểm số lúc 15:44 trên `main` (sau khi merge CP1–CP4): `python lab13.py` chạy hết và in ĐẠT; `pilot_plan.yaml` đọc được bằng `yaml.safe_load`; ngoài dòng chú thích không còn dấu `?`; không có từ cấm trong `report/team/`.
- [Đức điền: link PR đã duyệt, nếu có]

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus 5.5):** phân tích đề; viết nháp `lab13.py` phần A, B theo công thức trong `docs/du_lieu_va_cong_thuc.md`; chép số từ output vào `bang_chi_phi.md`; soạn nháp luật dừng, dòng rủi ro kinh tế và báo cáo này.
- **Cách tự kiểm tra:** chạy `python lab13.py`, đối chiếu từng số với số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (cho phép lệch ≤ 2%; thực tế khớp hoàn toàn); kiểm tra "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" ở B1; tính tay một số: 1.780.000 + 2.264.000 + 245.585 + 84.000 = 4.373.585, chia 978 = 4.472 đ.
- **Không dùng AI để:** gắn nhãn 20 ca lỗi của nhiệm vụ C, hay chấm phiếu duyệt chéo (`RULES.md`).

## 6. Tự đánh giá

[Đức tự viết: điều làm tốt, điều sẽ làm khác, điều học được về chi phí mỗi việc thành công và thiết kế pilot.]
