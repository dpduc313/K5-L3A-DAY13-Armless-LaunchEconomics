# Báo cáo cá nhân — DoCaoCuong-2A202603612

## 1. Thông tin thành viên

- Họ tên: Đỗ Cao Cường
- MSSV: 2A202603612
- Email: 26ai.cuongdc@vinuni.edu.vn
- GitHub: cuongdc03
- Nhóm: Armless · Lớp: L3A
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người gắn nhãn 1**, kiêm theo dõi điều kiện "Xong khi" của từng checkpoint.

## 2. Phần việc phụ trách

- Đọc đề, chia vai và lập quy trình nhánh/PR cho nhóm (`PHAN_CONG.md`).
- Theo dõi điều kiện "Xong khi" của CP1–CP5 trong `CHECKPOINTS.md` và `RUBRIC.md`, soát từng PR trước khi merge.
- CP3: gắn nhãn độc lập 20 ca (người gắn nhãn 1), tổng hợp `report/team/bang_loi.md`.
- CP4: soạn cách chia và năm câu D2 "tách được tác động" gửi người viết code.
- CP5: soạn `report/team/chi_so.md` (chỉ số, event, kiểm tra chéo, rủi ro kinh tế).

## 3. Đóng góp cụ thể

| Việc | Kết quả |
| --- | --- |
| Phân công | Viết `PHAN_CONG.md`: vai trước và sau giải lao, quy trình tách nhánh từ `main` và mở PR, bảng nhánh theo checkpoint có người duyệt và giờ merge, checklist việc của từng người. Điền tên nhóm, lớp, tên và vai trong `TEAM.md` |
| Soát CP1, CP2 | Chạy `python lab13.py` trên nhánh `cp1-cp2-chi-phi`, đối chiếu A1–A4 và B1–B4 với số tham khảo trong hướng dẫn: tất cả khớp (4.472 đ mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn; B4 lệch 1 đ do làm tròn, trong ngưỡng 2%) |
| CP3 | Tự gắn nhãn 20 ca, không dùng AI. Điền hai bộ nhãn, tỉ lệ đồng thuận 20/20, hai quy tắc phân biệt (Ngầm và Hệ thống; Ngữ cảnh và Hệ thống), bảng khắc phục 5 ca (ca 1, 7, 18, 13, 17), mỗi dòng có cách phát hiện đo được và một vai trò phụ trách. Phát hiện bộ nhãn người 2 do ChatGPT đề xuất nên ghi rõ lưu ý trong `bang_loi.md` thay vì khai là hai bộ nhãn độc lập |
| CP4 | Soạn đề xuất chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm; năm câu D2, dòng đánh đổi, trường `identifiability`; tính thêm khả thi (khoảng 31 yêu cầu/người/ngày, đạt 299 yêu cầu sau khoảng 10 ngày làm việc) và power 0,64 nếu tác động thật là 5 điểm |
| CP5 | `chi_so.md`: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất (tỉ lệ mở gợi ý; tỉ lệ hoàn sai tiền qua kiểm tra mẫu), 10 event có `trace_id`, kiểm tra chéo chỉ số với event, hai dòng rủi ro kinh tế lấy số từ bảng độ nhạy |
| Soát main sau CP4 | Chạy `lab13.py`, `yaml.safe_load`, grep dấu `?` và từ cấm trên main: đều đạt. Phát hiện câu D2 số 4 ghi nhầm ngày quyết định là ngày bắt đầu, báo người viết code sửa |

## 4. Bằng chứng

- PR #1 `docs/phan-cong`: commit `2e689b7`, `5248387` (`PHAN_CONG.md`, `TEAM.md`).
- PR #3 `feat/cp3-error-table`: commit `64702f2` (`report/team/bang_loi.md`).
- PR #4 `feat/cp5-metrics`: commit `4397eab` (`report/team/chi_so.md`, phần E1, event, kiểm tra chéo).
- PR #6 `feat/cp5-e2-risks`: commit `7931055` (`report/team/chi_so.md`, phần E2).
- Con số tự kiểm: D1 (1.251 · 3.103 / 42 người · 1.000 · 300 · m ≥ 299), tỉ lệ mở lại 4,25% và 3,97% trong phạm vi, ba chỉ số E1. Tất cả khớp với output `lab13.py` của nhóm.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

**Claude Code (Claude)**, dùng để:

- Đọc toàn bộ đề, rubric, checkpoint và đề xuất cách chia việc; soạn `PHAN_CONG.md`.
- Chạy lệnh git và GitHub CLI (tạo nhánh, commit, mở PR), kiểm tra nhánh của các thành viên.
- Chạy `lab13.py` và đối chiếu số với hướng dẫn chi tiết khi soát PR.
- Trích 20 ca lỗi từ file docx và tạo phiếu gắn nhãn trống. **Không dùng AI để gắn nhãn:** Claude từ chối gắn nhãn hộ theo `RULES.md`, tôi tự gắn 20 nhãn.
- Điền bảng nhãn, soạn bảng khắc phục 5 ca, năm câu D2, danh sách event, hai chỉ số tự đề xuất và hai dòng rủi ro kinh tế.

Cách tự kiểm tra:

- Mọi con số đều đối chiếu với output `python lab13.py` của nhóm và số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Đọc lại và đồng ý với danh sách event, bảng khắc phục, D2 trước khi merge.
- Chạy `yaml.safe_load`, grep dấu `?` trong `pilot_plan.yaml` và lệnh grep kiểm tra từ cấm trong `report/team` (xem `CHECKPOINTS.md`, CP5) trước khi merge.

## 6. Tự đánh giá

- Làm tốt: giữ được nhịp merge theo checkpoint, soát số trước mỗi lần merge, ghi trung thực việc bộ nhãn người 2 không độc lập.
- Cần cải thiện: phần CP3 chưa đạt đúng yêu cầu hai bộ nhãn độc lập, nên tỉ lệ đồng thuận 100% không đo được độ rõ của định nghĩa; PR #4 bị merge khi bảng E2 còn trống, phải mở thêm PR #6. Lần sau cần chốt checklist trước khi bấm merge.
