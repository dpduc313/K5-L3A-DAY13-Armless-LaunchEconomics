# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: tỉ lệ nhân viên nhóm can thiệp mở gợi ý của trợ lý | Số yêu cầu nhóm can thiệp có event `agent_suggestion_shown`, chia số yêu cầu nhóm can thiệp (`refund_request_created` có `arm = treatment`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17 trong `bang_loi.md`) | Số đơn trong mẫu có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra (`audit_sample_checked`) | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83%. Không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách | request_id, depot, staff_id, loai, so_tien_vnd, arm (treatment/control), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), price_table_version, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (het_3_lan, ngoai_pham_vi, thieu_du_lieu), tom_tat, trace_id | Khi chuyển cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok/loi_503), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | created_at, closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày sau closed_at, chia số `refund_request_created`. Đo được.
- **Dùng, tỉ lệ bỏ qua gợi ý:** `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`. Đo được.
- **An toàn, lỗi lọt đến khách:** `ticket_reopened` trong 7 ngày, chia số `refund_request_created`. Đo được.
- **Dùng, tự đề xuất:** `agent_suggestion_shown` nối với `refund_request_created` có arm = treatment qua trace_id. Đo được.
- **An toàn, tự đề xuất:** `audit_sample_checked`. Đo được.
- Chi phí mỗi việc thành công trong pilot tính từ `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho hai cột `_simulated`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ⏳ chờ anh Đức | | | | |
| ⏳ chờ anh Đức | | | | |
