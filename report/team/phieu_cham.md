# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- **Nhóm chấm (hội đồng):** Armless (Nhóm 01 - L3A)
- **Nhóm được chấm:** Nhóm 02 (L3A)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| **Đề xuất khớp bằng chứng** | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất "Go có điều kiện" khớp hoàn toàn với số liệu. Nhóm dũng cảm chỉ rõ con số bất lợi: power chỉ đạt 0,64 nếu tác động thật là +5 điểm; chi phí duyệt tay 100% lên tới 11.743 đ – 12.415 đ (0,98× – 1,03× [simulated]). Đã có 4 điều kiện ràng buộc cụ thể kèm người phụ trách và hạn kiểm tra trước khi bấm máy. |
| **Số giả lập và phạm vi** | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Ghi nhãn `[simulated]` đầy đủ và nhất quán ở tất cả các con số tính từ hai cột thời gian xem lại/làm lại. Thu hẹp phạm vi rõ ràng: chỉ nhận `noi_dia` (95,0% thành công, 0,22×) và `hang_nang` (74,1%, 0,69×); loại bỏ hoàn toàn `quoc_te` (27,3% thành công, 1,88× của 12.000 đ [simulated]) và `doi_tac` (0,85× [simulated]). |
| **Pilot ra được quyết định** | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Thiết kế thử nghiệm RCT có nhóm đối chứng song song (20 nhân viên thử nghiệm vs. 20 nhân viên đối chứng). Đủ cỡ mẫu hiệu dụng cho MDE 6 điểm ($n = 859$, yêu cầu $m \ge 299$ đơn/người). Có 4 luật dừng đầy đủ cú pháp NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng đo lường được và chỉ định đích danh vai trò có quyền dừng (Giám đốc vận hành). |
| **Tổng** | | | | **30 / 30** | Hồ sơ mẫu mực, số liệu minh bạch, lập luận chặt chẽ và tuân thủ tuyệt đối kỷ luật thống kê. |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ phản ánh trung thực toàn diện bài toán kinh tế và rủi ro kỹ thuật. Nhóm không tô hồng chi phí AI (chỉ rõ chi phí mỗi việc thành công gấp 16,3 lần hóa đơn token), thu hẹp phạm vi hợp lý, thiết kế thử nghiệm lâm sàng chuẩn xác và có cơ chế phòng vệ dừng khẩn cấp rõ ràng.

**Một câu hỏi cho đội trình:**  
*"Với tỉ lệ mở lại khiếu nại hiện tại trong phạm vi pilot là 3,97% (và 4,25% trên toàn bộ mẫu), nếu nhóm đặt ngưỡng dừng an toàn là 'tỉ lệ mở lại vượt 3%' thì thử nghiệm sẽ bị sập ngay tuần đầu. Nhóm đã xử lý mâu thuẫn này trong luật dừng như thế nào?"*

**Câu trả lời của đội trình (ghi lại tại buổi):**  
*"Đội ngũ đã lường trước điều này nên không dùng ngưỡng tuyệt đối cứng 3%. Thay vào đó, luật dừng an toàn được thiết kế theo phương pháp so sánh tương đối với nhóm đối chứng song song: chỉ kích hoạt dừng khi 'tỉ lệ mở lại của nhóm trợ lý cao hơn nhóm đối chứng từ 2 điểm phần trăm trở lên' VÀ kết hợp trần tuyệt đối khống chế ở mức 6% trong 3 ngày liên tiếp. Thiết kế này giúp pilot không bị dừng oan uổng bởi tỉ lệ lỗi nền vốn có của hệ thống."*
