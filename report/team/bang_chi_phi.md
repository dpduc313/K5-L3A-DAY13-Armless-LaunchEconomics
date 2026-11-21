# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (chạy `cd src; python lab13.py`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

`python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | | simulated (có phần giả lập) |
| Số việc thành công | 978 | `ket_qua` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công 4.472 đ [simulated] gấp **16,3 lần** hoá đơn token và tool chia số yêu cầu (274,7 đ).
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí [simulated], tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5% [simulated], token và tool chỉ 7,5%.
- So với nhân viên tự làm phải cộng 222 ca không thành công do nhân viên làm thay: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ mỗi yêu cầu = 0,49×** của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace): quoc_te 30,0% → 11,4% → 2,2%; doi_tac 51,5% → 18,2% → 14,8%; noi_dia 91,0% → 75,7% → 38,9%.

- **quoc_te không đáng để trợ lý xử lý:** chỉ thành công 27,3%, tốn 2,32 lần chạy mỗi yêu cầu, chi phí 1,88× nhân viên tự làm [simulated]. Chạy lại không giúp: lần 2 chỉ đúng 11,4%, lần 3 còn 2,2%, vì lỗi lặp lại trên cùng yêu cầu. doi_tac sát ngưỡng (0,85× [simulated]) và có điều khoản riêng.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu, 900 việc thành công; chi phí mỗi việc thành công chưa cộng cố định 3.414 đ [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định không đổi kết luận ở 45.000 yêu cầu/tháng (0,38× [simulated]), nhưng gấp đôi trên mỗi việc khi khối lượng còn một nửa (0,48× [simulated]). Giai đoạn pilot khối lượng nhỏ hơn nên số trong hồ sơ phải ghi rõ đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6 |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8 |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7 |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3 |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8 |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9 |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1 |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2 |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1 |

Tự kiểm: mỗi dòng "giảm một nửa" bằng đúng nửa mức tăng của dòng "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ, +46,3%** [simulated], đúng bằng tổng hai tác động riêng (5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (+51,8%) · 2. **tỉ lệ xem lại** (+40,7%) · 3. **lương nhân viên** (+23,1%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay), trên 1.200 yêu cầu.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 (thấp nhất) |
| 2 lần | 4.093.220 | 234 | **6.901.220 (rẻ nhất)** | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ [simulated]), **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ [simulated]). Tối ưu riêng chi phí mỗi việc thành công đẩy thêm 85 yêu cầu (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang: 982 yêu cầu, 948 yêu cầu có ít nhất một lần chạy ok (xem lại 5 phút mỗi yêu cầu = 9.480.000 đ), 48 ca làm lại, token và tool 224.513 đ, 900 việc thành công.

- Làm lại 9 phút/ca như đề: tổng 10.568.513 đ → **11.743 đ = 0,98×** của 12.000 đ [simulated]. Dữ liệu cho thấy làm lại trung bình 15,3 phút/ca (trung vị 14,5) [simulated]: **12.415 đ = 1,03×** [simulated], tức đắt hơn nhân viên tự làm.
- Pilot phải học được tỉ lệ xem lại giảm an toàn được tới đâu, và mỗi lần xem lại có ngắn được không: hoà vốn khi mỗi lần xem lại ≤ **5,1 phút** (làm lại 9 phút) hoặc ≤ **4,8 phút** (làm lại 15,3 phút) [simulated].
