# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** Armless · **Lớp:** L3A · **Trạng thái:** Bản tổng hợp đang cập nhật, **chưa chốt đề xuất**.

> Dữ liệu Lab 13 là giả lập. Mọi chi phí dùng hai cột `_simulated` đều gắn nhãn **simulated**. Số CP1–CP2 lấy từ `origin/cp1-cp2-chi-phi` (chưa merge vào `main` tại lúc tổng hợp), đối chiếu lại bằng phép tính trực tiếp từ CSV; ba chỉ số CP5 bên dưới do Minh tính thử từ CSV và **chưa được nhóm CP5 xác nhận**.

| Mục | Con số chính và bằng chứng | Trạng thái | Người phụ trách (vai trò) |
| --- | --- | --- | --- |
| **1 · Chi phí mỗi việc thành công** | **978/1.200** yêu cầu thành công; **4.472 đ/việc [simulated]**, tổng **4.373.585 đ [simulated]** từ **1.624** lượt chạy (A2). | Giả lập | Người viết code CP1 |
| **2 · Ba yếu tố nhạy nhất** | CP2/B1: **làm lại +51,8%**, **xem lại +40,7%**, **lương nhân viên +25% → chi phí +23,1%** [simulated]. Giá token gấp đôi chỉ **+5,6%**. | Giả lập | Người kiểm số CP2 |
| **3 · So với nhân viên tự làm** | Mốc **12.000 đ/yêu cầu**. Khi tính cả **222 ca nhân viên làm thay**, toàn hệ thống **5.865 đ/yêu cầu [simulated]** trên mẫu 1.200. Phạm vi `noi_dia` + `hang_nang`: **4.599 đ/việc thành công [simulated]** đã cộng **40 triệu đ/tháng** cố định ở giả định **45.000 yêu cầu/tháng** (A4). | Giả lập | Người kiểm số CP1 |
| **4 · Chỉ số chính, dùng, an toàn** | **Tạm tính trực tiếp từ CSV:** đóng trong 24 giờ và không mở lại 7 ngày **994/1.200 = 82,83%**; sửa/bỏ gợi ý **48/177 = 27,12%**; mở lại trong 7 ngày **51/1.200 = 4,25%**. **Chờ Cường/Đạt xác nhận CP5**. | Chưa | Phụ trách chỉ số CP5 |
| **5 · Bảng lỗi và khắc phục** | **20** ca lỗi thuộc **5** loại, yêu cầu hai bộ nhãn độc lập đồng thuận ít nhất **16/20 = 80%** và **5** biện pháp có event/ngưỡng/người phụ trách. Chưa có kết quả xác nhận giữa Minh và Cường. | Chưa | Người gắn nhãn 1 CP3 |
| **6 · Pilot plan** | Giả định đầu bài: baseline **70%**, mục tiêu **75%** (MDE **+5 điểm**), α **0,05**, power **0,80**, ICC **0,02**. Chờ CP4 xác nhận cỡ mẫu, đơn vị phân nhóm, đối chứng, ≥**3** luật dừng và rollback. | Chưa | Người viết code CP4 |
| **7 · Rủi ro kinh tế** | **Ứng viên từ CP2, chờ CP5:** (i) ca làm lại gấp đôi làm chi phí tăng **51,8%**; (ii) xem lại gấp đôi làm chi phí tăng **40,7%** [simulated]. Kịch bản **xem lại 100%** tại `noi_dia` + `hang_nang` lên **11.743 đ/việc [simulated]**, sát mốc 12.000 đ. | Chưa | Phụ trách rủi ro CP5 |

**Phạm vi đề xuất để xem xét:** `noi_dia` (824 yêu cầu, **95,0%** thành công) và `hang_nang` (158 yêu cầu, **74,1%**); chưa đưa `quoc_te` (**27,3%** thành công; **22.515 đ/việc [simulated]**) vào phạm vi pilot. Chốt phạm vi theo thảo luận nhóm khi có CP4.

**Lưu ý về so sánh chi phí:** 5.865 đ/**yêu cầu** đã cộng xử lý thay để so với 12.000 đ/**yêu cầu**; còn 4.599 đ/**việc thành công** là chỉ số khác mẫu số và gắn với quy mô giả định 45.000 yêu cầu/tháng. Không lấy chỉ số của đợt chạy thử làm kết luận agent **đã cải thiện** KPI vì chưa có nhóm đối chứng.

**Đề xuất Gate 2a — chưa quyết định:** Chỉ lựa chọn **Go / Go có điều kiện / No-go** sau khi có kết quả độc lập CP3, CP4 hợp lệ, CP5 được đối chiếu và cả nhóm thống nhất. Nếu Go có điều kiện: ghi rõ từng điều kiện, vai trò chịu trách nhiệm và ngày kiểm tra; nếu No-go: chỉ rõ việc phải sửa trước khi đánh giá lại.
