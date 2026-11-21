# Báo cáo cá nhân — NguyenDucDat-2A202603544

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Đạt
- MSSV: 2A202603544
- Email: nguyenducdat298@gmail.com
- GitHub: https://github.com/nguyenducdat298
- Vai trong nhóm: Người kiểm số (trước giải lao: 14:00–15:20) → Người viết code (sau giải lao: 15:35–18:00)

## 2. Phần việc phụ trách

- **Trước giải lao (Người kiểm số):** 
  - Cài đặt và cấu hình môi trường chạy code.
  - Kiểm số độc lập bằng tính tay các khoản chi phí token, tool, giờ nhân viên (xem lại, làm lại) để đối chiếu với code CP1 của Đức; xác nhận độ lệch 0%.
  - Rà soát bảng A1, A2, A3, A4 trong `report/team/bang_chi_phi.md`, đảm bảo mọi con số tính từ cột `_simulated` đều có nhãn `[simulated]`.
  - Phân tích và kiểm tra tính cộng tuyến tính ở B1, B2: xác nhận kịch bản "giảm một nửa" làm chi phí giảm đúng bằng một nửa mức tăng của "gấp đôi".
- **Sau giải lao (Người viết code):**
  - Phụ trách chính phần code thống kê cỡ mẫu D1 và tỉ lệ mở lại D3 trong `src/lab13.py` cho Checkpoint CP4.
  - Triển khai tính toán 3 cách chia cụm (theo yêu cầu, theo nhân viên, theo depot); tính trần cỡ mẫu hiệu dụng tối đa $c / ICC = 20 / 0,02 = 1.000$ và giải bài toán đánh đổi MDE 6 điểm ($m \ge 299$ đơn/người).
  - Code tính toán thử nghiệm 3 chỉ số E1 (chính: 82,83%, dùng: 27,12%, an toàn: 4,25%) từ dữ liệu trace để cung cấp cho Cường và Minh điền hồ sơ.
  - Viết `group_report.md`, hoàn thiện `phieu_cham.md` duyệt chéo và hoàn thiện báo cáo cá nhân này.

## 3. Đóng góp cụ thể

- **CP1 & CP2 (Kiểm số & Thẩm định kinh tế):**
  - Thẩm định công thức A1: $E[\text{lần chạy}] = (1 - (1 - p)^k) / p$; với $p=0,8, k=2 \implies 1,20$; $k=None \implies 1,25$. Hệ số chi phí với $k=3 \implies 1,25$. Khớp 100% với 3 phép thử chuẩn.
  - Kiểm tra độc lập tổng chi phí A2: $245.585\text{ đ (token)} + 84.000\text{ đ (tool)} + 1.780.000\text{ đ (xem lại)} + 2.264.000\text{ đ (làm lại)} = 4.373.585\text{ đ [simulated]}$. Chia cho 978 việc thành công ra đúng 4.472 đ/việc [simulated], gấp 16,3 lần hóa đơn token+tool chia số yêu cầu (274,7 đ).
  - Xác nhận khoản chi phí lớn nhất là làm lại (51,8% [simulated]) và xem lại (40,7% [simulated]); giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
  - Kiểm tra bảng độ nhạy B1 & B2: Giá token gấp đôi + xem lại gấp đôi ra đúng 6.543 đ (+46,3% [simulated]), bằng tổng hai tác động riêng lẻ $(+5,6\% + 40,7\%)$ do mô hình cộng tuyến tính.
  - Phân tích B3 (Toàn hệ thống): Giới hạn 2 lần chạy là rẻ nhất cho toàn công ty (6.901.220 đ [simulated]), tối ưu hơn giới hạn 1 lần (7.449.781 đ) vì tránh đẩy 85 việc sang cho nhân viên tự làm thủ công.
  - Phân tích B4 (Xem lại 100%): Chi phí vọt lên 11.743 đ (0,98×) đến 12.415 đ (1,03×) [simulated], chứng minh nếu duyệt tay toàn bộ thì trợ lý AI không tiết kiệm được gì.
- **CP4 (Viết code thống kê & Kế hoạch pilot):**
  - Viết hàm tính cỡ mẫu `co_mau(p1, p2, alpha, power)` bằng `statistics.NormalDist()`, tính ra chuẩn xác 1.251 đơn/nhóm cho mức chênh 5 điểm.
  - Chứng minh bằng toán học: Với 20 nhân viên mỗi nhóm và $ICC = 0,02$, trần cỡ mẫu tối đa là $\frac{c}{ICC} = \frac{20}{0,02} = 1.000 < 1.251 \implies$ Bất khả thi để đo mức chênh 5 điểm.
  - Giải phương trình tìm cỡ mẫu cho mức chênh 6 điểm (cần 859 đơn/nhóm):
    $$\frac{20m}{1 + (m - 1) \times 0,02} \ge 859 \iff 2,82m \ge 841,82 \implies m \ge 298,52 \implies m \ge 299 \text{ đơn/người}.$$
  - Tính tỉ lệ `mo_lai_trong_7_ngay` thực tế: $4,25\%$ (toàn bộ 1.200 yêu cầu) và $3,97\%$ (trong phạm vi `noi_dia` + `hang_nang`), làm căn cứ thiết lập luật dừng an toàn so với đối chứng thay vì đặt ngưỡng tuyệt đối 3%.
- **CP5 & Tổng kết:**
  - Viết code tính toán 3 chỉ số E1: đóng trong 24h và không mở lại trong 7 ngày đạt 82,83% (994/1.200); tỉ lệ bỏ qua gợi ý đạt 27,12% (48/177); lỗi mở lại là 4,25% (51/1.200).
  - Hoàn thiện `group_report.md` tóm tắt toàn diện bài toán, giải pháp và kết quả Gate 2a.
  - Hoàn thiện phiếu chấm hội đồng `phieu_cham.md`.

## 4. Bằng chứng

- File code `src/lab13.py` chạy thông suốt toàn bộ các khối A, B, D, E.
- File hồ sơ: `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`.
- Kiểm tra tự động:
  - `python src/lab13.py` in ĐẠT 3 phép thử và toàn bộ các bảng A2, A3, A4, B1, B2, B3, B4, D1, D3, E1.
  - `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"` chạy không lỗi, không còn dấu `?`.
  - Không xuất hiện từ cấm trong toàn bộ thư mục `report/team/` (chỉ dùng từ pilot, không dùng từ chạy chính thức ngoài đời).

## 5. Công cụ AI đã dùng

- **Mô hình sử dụng:** Gemini 3.8 Flash và Claude Code để hỗ trợ kiểm tra chéo công thức toán học, rà soát lỗi chính tả và định dạng markdown.
- **Cách tự kiểm chứng:** 
  - Tự tay tính toán trên giấy và viết script kiểm chứng độc lập các công thức cỡ mẫu, $DE$, $n_{\text{hiệu dụng}}$, đối chiếu từng con số với tài liệu hướng dẫn `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
  - Kiểm tra chéo toàn bộ dữ liệu CSV bằng pandas để xác nhận tính chính xác tuyệt đối của các chỉ số.
- **Quy tắc liêm chính:** Không dùng AI để gắn nhãn tự động 20 ca lỗi CP3 hay chấm điểm thay con người.

## 6. Tự đánh giá

- **Điểm làm tốt:** Nắm chắc bản chất toán học của mô hình kinh tế và thống kê phân cụm (ICC, Design Effect). Chuyển giao vai trò viết code sau giải lao nhịp nhàng, đảm bảo tính liên tục và độ chính xác cao của toàn bộ số liệu nhóm.
- **Điểm cần cải thiện:** Cần tăng tốc độ đọc và phân tích tài liệu đặc tả nghiệp vụ ban đầu để dành nhiều thời gian hơn cho việc thảo luận phản biện các kịch bản ngoại lệ.
