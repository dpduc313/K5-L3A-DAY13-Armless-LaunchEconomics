# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Cường · Người gắn nhãn 2: Đạt

> **Lịch sử bộ nhãn người 2:** lần gắn đầu, người 2 là Minh, nhưng 20 nhãn do ChatGPT đề xuất rồi Minh chấp thuận (`report/team/nhan_cp3_Minh.md` trên nhánh `docs/report-minh`), nên không đạt yêu cầu gắn độc lập. Cả nhóm thống nhất bỏ bộ đó và để Đạt gắn lại: Đạt tự gắn cả 20 ca trong khoảng 8 phút (xong trước 16:40), trên phiếu chỉ có mô tả ca và định nghĩa năm loại, không dùng AI, không trao đổi, chưa xem bộ nhãn nào trước đó. Việc thay người gắn là quyết định của nhóm, chưa hỏi ý kiến giảng viên.

| Ca | Nhãn người 1 (Cường) | Nhãn người 2 (Đạt) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (Cường và Đạt)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (20/20). Hai quy tắc nhóm dùng cho các cặp dễ lẫn:
- **Ngầm và Hệ thống:** cái sai đã lộ ra (khách mở lại, nhân viên bắt được, có cảnh báo) thì là Hệ thống; chỉ khi không ai nhận ra cho tới lúc kiểm tra mới là Ngầm (ca 15 là Hệ thống vì nhân viên bắt được; ca 5, 12, 17 là Ngầm).
- **Ngữ cảnh và Hệ thống:** trợ lý làm đúng thiết kế và chính sách mà khách vẫn thấy sai thì là Ngữ cảnh (ca 3, 10, 16, 18); làm sai so với thiết kế hoặc chính sách thì là Hệ thống (ca 2, 7, 8, 15, 20).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_bank_rejected` (ngân hàng trả lỗi sai số tài khoản), theo dõi tỉ lệ hằng ngày; cảnh báo khi vượt 1% số lệnh hoàn | Kiểm tra độ dài và checksum số tài khoản ngay khi khách nhập; hiện lại tên chủ tài khoản để khách xác nhận trước khi tạo lệnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Event `ledger_write_failed` có cùng `trace_id` với `refund_confirmed_sent`; ngưỡng: 0 ca, kiểm tra theo thời gian thực | Chỉ gửi "đã hoàn tiền thành công" khi sổ cái trả xác nhận ghi; lỗi 503 sau 3 lần thì báo khách "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `mo_lai_trong_7_ngay` của các ca hoàn một phần (lý do mở lại "hoàn thiếu"), theo dõi hằng tuần; cảnh báo khi vượt 5% | Tin nhắn hoàn tiền luôn kèm cách tính: phí gốc, tỉ lệ hoàn, điều khoản áp dụng | Trưởng nhóm CSKH |
| 13 | Giới hạn hệ thống | Event `out_of_scope_detected` so với số yêu cầu có từ khoá ngoài phạm vi (bảo hiểm, đối tác) trong mẫu kiểm tra 50 hội thoại mỗi tuần; ngưỡng bỏ sót dưới 5% | Thêm bộ phân loại phạm vi: nói rõ "trợ lý không xử lý hoàn phí bảo hiểm" và chuyển đúng đầu mối kèm tóm tắt | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra đối soát hằng ngày: so số tiền hoàn với bảng giá hiện hành trên mẫu 100 đơn; cảnh báo khi lệch quá 0,5% số đơn; event `price_table_version` ghi kèm mỗi `trace_id` | Xoá bộ nhớ đệm bảng giá khi có bản mới, ghi phiên bản bảng giá vào mỗi lần tính; rà lại 212 đơn lệch và hoàn bù | Kỹ sư trưởng agent |
