# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** Armless · **Lớp:** L3A · **Phiên bản:** Hồ sơ tổng hợp CP1–CP5 từ `main`; đề xuất đã chốt ngày 21/11/2026.

> Các chi phí có dùng cột `_simulated` được ghi **[simulated]**; các tỷ lệ E1 là số tính thử trên dữ liệu giả lập, không chứng minh tác động nhân quả. Gate 2a chỉ xét kế hoạch pilot.

| Mục | Con số / bằng chứng chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí/việc thành công | **978/1.200** thành công; **4.472 đ/việc [simulated]** trên tổng **4.373.585 đ [simulated]** (CP1/A2). | Giả lập | Giám đốc vận hành |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% khiến chi phí **+23,1%** [simulated] (CP2/B1). | Giả lập | Giám đốc vận hành |
| 3 · So với nhân viên | Mốc **12.000 đ/yêu cầu**; trợ lý cộng 222 ca nhân viên làm thay: **5.865 đ/yêu cầu [simulated]**. Phạm vi nội địa + hàng nặng, đã cộng cố định 40 triệu/tháng ở quy mô 45.000 yêu cầu/tháng: **4.599 đ/việc [simulated]** (A4). | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính/dùng/an toàn | **E1 đã merge main (PR #4):** đóng ≤24 giờ, không mở lại 7 ngày **82,83% (994/1.200)**; sửa/bỏ gợi ý **27,12% (48/177)**; mở lại **4,25% (51/1.200)**. Có **10 event với `trace_id`** trong `chi_so.md`. Đây là chỉ số chạy thử trên dữ liệu giả lập, **chưa chứng minh cải thiện so với đối chứng**. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Lỗi và khắc phục | CP3: **20/20 nhãn trùng (100%)** và **5/5 loại lỗi** có biện pháp đo được (`bang_loi.md`, main `8da7efd`). **Lưu ý:** nhãn Minh được AI hỗ trợ, chưa đạt điều kiện gắn nhãn độc lập. | Xong, có bằng chứng | Product owner trợ lý hoàn phí |
| 6 · Pilot plan | **CP4 đã merge main (PR #5):** ngẫu nhiên theo **40 nhân viên (20/nhóm)**, phân tầng theo depot; đối chứng chạy đồng thời. **MDE +6 điểm**, α=0,05, power mục tiêu **0,80**, ICC **0,02**; cần **859 mẫu hiệu dụng/nhóm**, tương đương **299 yêu cầu/nhân viên**. Nếu chỉ cải thiện +5 điểm, power ≈ **0,64**. YAML hợp lệ, không còn `?`, có **4 luật dừng** (an toàn, chi phí, mức độ sử dụng, thời gian xem lại) và rollback **30 phút**, ngày quyết định **05/01/2027**. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | **E2 đã merge main (PR #6):** làm lại gấp đôi → **6.787 đ/việc (+51,8%) [simulated]**; cảnh báo khi tỷ lệ làm lại > **7%/tuần**, thu hẹp về nội địa và rà 20 trace. Xem lại 100% → **11.743 đ/việc (0,98×)**; nếu làm lại 15,3 phút → **12.415 đ/việc (1,03×)** [simulated]; theo dõi tỷ lệ xem lại > **50%** cuối bước rollout 25%, chỉ giảm khi sửa/bỏ < **15%** trong 2 tuần. | Giả lập | Giám đốc vận hành |

**Phạm vi pilot đề xuất:** chỉ `noi_dia` (**95,0%** thành công) + `hang_nang` (**74,1%**); chưa đưa `quoc_te` (**27,3%**, **22.515 đ/việc [simulated]**) vào pilot.

**Đề xuất: Go có điều kiện.** Chỉ pilot `noi_dia` và `hang_nang`; không đưa `quoc_te`/`doi_tac` vào pilot. Con số bất lợi đã chấp nhận: power chỉ ≈ **0,64** nếu tác động thật là +5 điểm; xem lại 100% đẩy chi phí lên **11.743–12.415 đ/việc (0,98–1,03×) [simulated]**.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Phê duyệt bằng văn bản đánh đổi MDE +6 điểm (power ≈ 0,64 nếu tác động +5 điểm) | Giám đốc vận hành | Trước ngày bắt đầu pilot |
| Diễn tập cờ tắt: rollback trong 30 phút; khoá chống hoàn trùng (`idempotency_key`) chạy được | Trưởng nhóm kỹ thuật | Trước ngày bắt đầu pilot |
| Tỉ lệ yêu cầu được xem lại giảm dưới 50% khi tỉ lệ sửa + bỏ < 15% hai tuần liên tiếp | Trưởng nhóm CSKH | Cuối bậc rollout 25% |
| Ra quyết định mở rộng theo chỉ số chính và 4 luật dừng trong `pilot_plan.yaml` | Giám đốc vận hành | 05/01/2027 |
