# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** Armless · **Lớp:** L3A · **Phiên bản:** Dự thảo, chờ biểu quyết theo lịch nhóm 16:50.

> Các chi phí có dùng cột `_simulated` được ghi **[simulated]**; các tỷ lệ E1 là số tính thử trên dữ liệu giả lập, không chứng minh tác động nhân quả. Gate 2a chỉ xét kế hoạch pilot.

| Mục | Con số / bằng chứng chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí/việc thành công | **978/1.200** thành công; **4.472 đ/việc [simulated]** trên tổng **4.373.585 đ [simulated]** (CP1/A2). | Giả lập | Giám đốc vận hành |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% khiến chi phí **+23,1%** [simulated] (CP2/B1). | Giả lập | Giám đốc vận hành |
| 3 · So với nhân viên | Mốc **12.000 đ/yêu cầu**; trợ lý cộng 222 ca nhân viên làm thay: **5.865 đ/yêu cầu [simulated]**. Phạm vi nội địa + hàng nặng, đã cộng cố định 40 triệu/tháng ở quy mô 45.000 yêu cầu/tháng: **4.599 đ/việc [simulated]** (A4). | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính/dùng/an toàn | Đóng ≤24 giờ, không mở lại 7 ngày: **82,83% (994/1.200)**; sửa/bỏ gợi ý: **27,12% (48/177)**; mở lại: **4,25% (51/1.200)**. E1 có **10 event với `trace_id`** trên nhánh `feat/cp5-metrics` (chưa merge). | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Lỗi và khắc phục | CP3: **20/20 nhãn trùng (100%)** và **5/5 loại lỗi** có biện pháp đo được (`bang_loi.md`, main `8da7efd`). **Lưu ý:** nhãn Minh được AI hỗ trợ, chưa đạt điều kiện gắn nhãn độc lập. | Xong, có bằng chứng | Product owner trợ lý hoàn phí |
| 6 · Pilot plan | Baseline **70%**, MDE **+5 điểm**, α=0,05, power mục tiêu **0,80**, ICC=0,02. Nếu chỉ có **859 mẫu hiệu dụng/nhóm**, power đối với +5 điểm khoảng **0,64**; đây là cảnh báo thiết kế, **chưa phải kết quả CP4**. | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi **+51,8%**; xem lại gấp đôi **+40,7%** [simulated]. Xem lại 100% khiến chi phí **11.743 đ/việc = 0,98×** mốc thủ công [simulated]. Chờ E2 hoàn thiện biện pháp và owner. | Chưa | Giám đốc vận hành |

**Phạm vi pilot đề xuất:** chỉ `noi_dia` (**95,0%** thành công) + `hang_nang` (**74,1%**); chưa đưa `quoc_te` (**27,3%**, **22.515 đ/việc [simulated]**) vào pilot.

**Đề xuất dự thảo: Go có điều kiện.** (1) **Giám đốc vận hành** duyệt lại cỡ mẫu, power và đối chứng trong CP4; (2) **Trưởng nhóm kỹ thuật** xác nhận ba luật dừng có ngưỡng/thời hạn và phương án rollback; (3) **Trưởng nhóm CSKH** xác nhận ngưỡng an toàn và giám sát chi phí xem lại, tránh vượt mốc 12.000 đ/việc. **Mốc rà soát theo phân công: 16:50–17:00, 21/11/2026.** Nếu CP4/E2 hoặc điều kiện an toàn chưa đạt thì **không chốt Go**; trình phương án No-go/đánh giá lại. Quyết định cuối cùng cần nhóm xác nhận.
