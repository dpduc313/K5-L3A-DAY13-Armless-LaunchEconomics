# Báo cáo nhóm · Armless (L3A)

Báo cáo tổng kết Lab 13 — Định giá agent và lập kế hoạch pilot (LogiX-VN, Gate 2a).

---

## 1. Thông tin nhóm

- **Tên nhóm:** Armless
- **Lớp:** L3A
- **Thành viên:**
  1. Đậu Phúc Đức — MSSV: 2A202603580 (Người viết code trước giải lao → Người kiểm số)
  2. Nguyễn Đức Đạt — MSSV: 2A202603544 (Người kiểm số trước giải lao → Người viết code)
  3. Đỗ Cao Cường — MSSV: 2A202603612 (Người gắn nhãn 1)
  4. Nguyễn Văn Minh — MSSV: 2A202603551 (Người gắn nhãn 2, kiêm giữ hồ sơ)
- Chi tiết vai trò và phân công: xem [`TEAM.md`](../../TEAM.md) và [`PHAN_CONG.md`](../../PHAN_CONG.md).

---

## 2. Mục tiêu và cách tiếp cận

- **Bối cảnh:** Công ty giả định LogiX-VN tiếp nhận khoảng 1.500 yêu cầu hoàn phí mỗi ngày (45.000/tháng), vận hành 12 depot và 40 nhân viên CSKH. Trợ lý AI vừa được chạy thử 2 tuần ở 6 depot. Nhóm nhận mẫu ngẫu nhiên 1.200 yêu cầu (1.624 lượt chạy trace) để đánh giá tính khả thi kinh tế và thiết kế thử nghiệm lâm sàng trước Hội đồng Gate 2a.
- **Mục tiêu cốt lõi:**
  1. *Tính toán chi phí thật* cho mỗi việc thành công (Cost-of-Pass), chứng minh sự chênh lệch so với hóa đơn token.
  2. *Phân tích độ nhạy kinh tế*, xác định biến số nhạy cảm nhất để thiết kế kiểm soát rủi ro.
  3. *Phân loại lỗi theo chuẩn Google PAIR*, gán giải pháp khắc phục có thể đo lường và quy trách nhiệm rõ ràng.
  4. *Thiết kế thử nghiệm ngẫu nhiên phân cụm (Cluster RCT)* có nhóm đối chứng song song, đủ cỡ mẫu hiệu dụng và luật dừng an toàn viết trước.
  5. *Đóng gói hồ sơ 1 trang* bảo vệ thành công trước Hội đồng duyệt chéo Gate 2a.
- **Cách tiếp cận:** Tiếp cận theo kỷ luật kỹ thuật và kinh tế thực chứng — "Evidence before assertions". Mọi kết luận đều dựa trên số liệu tính toán từ trace, phân định rõ ràng giữa số đo thực tế và số giả lập (`[simulated]`), không tô hồng kết quả, dám thừa nhận các con số bất lợi và sự đánh đổi thống kê.

---

## 3. Giải pháp

Nhóm đã thực thi tuần tự 5 nhiệm vụ qua 5 checkpoint A–E:

- **Nhiệm vụ A (CP1) — Mô hình chi phí từ trace ([`bang_chi_phi.md`](bang_chi_phi.md)):**
  - Xây dựng hàm `mo_hinh` tính chi phí mỗi việc thành công: tử số gộp toàn bộ chi phí token, tool, thời gian xem lại và làm lại của nhân viên trên *mọi* lần chạy; mẫu số chỉ đếm các đơn `ket_qua == 'thanh_cong'`.
  - Phân rã theo loại đơn: chứng minh đơn `noi_dia` (2.696 đ, 0,22×) và `hang_nang` (8.221 đ, 0,69×) mang lại hiệu quả cao; trong khi đơn `quoc_te` (22.515 đ, 1,88×) bị lỗ nặng và chạy lại tới lần 3 không cải thiện tỉ lệ đúng (30,0% → 11,4% → 2,2%).
  - Cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`: chi phí mỗi việc thành công là 4.599 đ (0,38× ở quy mô 45.000 đơn/tháng) và 5.784 đ (0,48× khi khối lượng giảm một nửa) [simulated].
- **Nhiệm vụ B (CP2) — Bảng độ nhạy kinh tế ([`bang_chi_phi.md`](bang_chi_phi.md)):**
  - Chạy mô phỏng 9 kịch bản biến thiên tham số. Phát hiện yếu tố ảnh hưởng mạnh nhất là *số ca làm lại* (+51,8%) và *tỉ lệ xem lại* (+40,7%), trong khi *giá token* chỉ tác động khiêm tốn (+5,6%).
  - Bài toán TCO (Total Cost of Ownership): Chứng minh giới hạn 2 lần chạy là tối ưu nhất cho toàn công ty (6.901.220 đ [simulated]), không chọn giới hạn 1 lần vì sẽ đẩy thêm 85 đơn thất bại sang cho nhân viên gánh thủ công.
  - Phân tích kịch bản duyệt tay 100%: Chi phí vọt lên 11.743 đ – 12.415 đ (0,98× – 1,03×) [simulated], chứng minh nếu bắt duyệt 100% thì trợ lý không đem lại lợi ích kinh tế.
- **Nhiệm vụ C (CP3) — Phân loại lỗi và cơ chế khắc phục ([`bang_loi.md`](bang_loi.md)):**
  - Hai thành viên gắn nhãn độc lập 20 ca lỗi vào 5 nhóm nguyên nhân gốc theo Google PAIR (*Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Lỗi ngầm*), đạt tỉ lệ đồng thuận 100% (20/20).
  - Lập bảng khắc phục cho 5 ca tiêu biểu, mỗi ca có event theo dõi với ngưỡng kích hoạt cụ thể và một vai trò chịu trách nhiệm duy nhất (PM, Kỹ sư trưởng, Trưởng nhóm CSKH, Kế toán trưởng).
- **Nhiệm vụ D (CP4) — Kế hoạch Pilot chuẩn thống kê ([`pilot_plan.yaml`](pilot_plan.yaml)):**
  - Phân tích tương quan nội cụm ($ICC = 0,02$) với 40 nhân viên (20 nhân viên dùng AI vs. 20 nhân viên đối chứng tự làm).
  - Chứng minh trần cỡ mẫu hiệu dụng tối đa chỉ đạt $c / ICC = 20 / 0,02 = 1.000 < 1.251$ $\implies$ Không thể kiểm định mức chênh 5 điểm với power 80%.
  - Chủ động đề xuất đánh đổi: Nâng mức chênh phát hiện lên 6 điểm ($MDE = 0,06$), xác định mỗi nhân viên cần xử lý tối thiểu $m \ge 299$ đơn hàng ($DE = 6,96$).
  - Thiết lập 4 luật dừng an toàn chuẩn cú pháp `NẾU – TRONG – THÌ – KHÔNG THÌ` và cơ chế rollback trong 30 phút.
- **Nhiệm vụ E (CP5) — Chỉ số, Rủi ro và Hồ sơ Launch v0 ([`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md)):**
  - Đặc tả 3 chỉ số thực tế: chỉ số chính (82,83%), chỉ số dùng (27,12%), chỉ số an toàn (4,25%) trên 1.200 đơn dữ liệu giả lập.
  - Xây dựng danh mục 10 telemetry event có `trace_id` để kết nối toàn diện chuỗi hành vi.
  - Hoàn thiện Hồ sơ Launch v0 gói gọn trong 1 trang với 7 mục và đề xuất **Go có điều kiện**.

---

## 4. Kết quả

- **Chi phí mỗi việc thành công:** 4.472 đ [simulated], gấp **16,3 lần** hóa đơn token + tool chia đều (274,7 đ). Giờ nhân viên (làm lại + xem lại) chiếm **92,5%** tổng chi phí [simulated].
- **Chi phí toàn hệ thống:** 5.865 đ/yêu cầu = 0,49× mức 12.000 đ [simulated] (khi tính cả 222 ca nhân viên làm thay).
- **Phạm vi pilot đề xuất:** Thu hẹp chỉ áp dụng cho `noi_dia` (95,0% thành công, 0,22×) và `hang_nang` (74,1% thành công, 0,69×); loại bỏ hoàn toàn `quoc_te` (1,88×) và `doi_tac` (0,85×) khỏi đợt thử nghiệm.
- **Đề xuất của nhóm tại Gate 2a:** **Go có điều kiện (Conditional Go)** kèm 4 điều kiện ràng buộc:
  1. Giám đốc vận hành ký duyệt bằng văn bản đánh đổi MDE 6 điểm (chấp nhận power ≈ 0,64 nếu mức cải thiện thực chỉ là 5 điểm).
  2. Kỹ sư trưởng hoàn tất kiểm thử diễn tập cờ tắt (rollback ≤ 30 phút) và khóa chống hoàn trùng (`idempotency_key`) trên dịch vụ sổ cái trước ngày khởi động.
  3. Bật đầy đủ hệ thống logging 10 event có `trace_id`, thay thế số phút simulated bằng số đo thực tế sau tuần 1.
  4. Trưởng nhóm CSKH ban hành quy chế giảm dần tỉ lệ xem lại theo bậc khi tỉ lệ sửa/bỏ < 15% trong 2 tuần liên tiếp.
- **Kết quả duyệt chéo tại lớp:** Đạt điểm tối đa **30/30** từ Hội đồng phản biện nhờ lập luận trung thực, dũng cảm nêu con số bất lợi và thiết kế thử nghiệm chặt chẽ.

---

## 5. Khó khăn và cách xử lý

1. **Khó khăn về ảo tưởng chi phí token:** Ban đầu dễ ngộ nhận rằng chi phí AI chỉ vài trăm đồng/đơn.
   - *Cách xử lý:* Viết hàm mô hình tính toán gộp toàn bộ chi phí con người vá lỗi, phân định rạch ròi tỉ trọng: giờ con người chiếm tới 92,5%, khẳng định tầm quan trọng của Human-in-the-loop.
2. **Khó khăn về bế tắc cỡ mẫu phân cụm:** Khi tính cỡ mẫu lý thuyết cho mức chênh 5 điểm cần 1.251 đơn, trong khi trần tối đa của 20 nhân viên bị chặn ở mức 1.000 đơn do $ICC = 0,02$.
   - *Cách xử lý:* Không làm giả số liệu, nhóm dũng cảm chấp nhận bài toán đánh đổi (trade-off) sang mức chênh 6 điểm ($n = 859$) và tính toán chính xác số đơn mỗi nhân viên cần làm ($m \ge 299$), đồng thời công khai minh bạch việc suy giảm power (còn 0,64 nếu tác động thật là 5 điểm).
3. **Khó khăn về việc đặt ngưỡng dừng an toàn:** Tỉ lệ mở lại khiếu nại hiện tại trong dữ liệu đã là 4,25% (và 3,97% ở phạm vi pilot). Nếu đặt ngưỡng dừng tuyệt đối 3% như cảm tính ban đầu thì thử nghiệm sẽ bị sập ngay tuần đầu.
   - *Cách xử lý:* Chuyển sang so sánh tương đối với nhóm đối chứng (cao hơn đối chứng $\ge 2\%$) kết hợp trần tuyệt đối 6%.

---

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của 4 thành viên được ghi nhận đầy đủ trong [`TEAM.md`](../../TEAM.md) và 4 báo cáo cá nhân:
- Đậu Phúc Đức: [`2A202603580_DauPhucDuc.md`](2A202603580_DauPhucDuc.md)
- Nguyễn Đức Đạt: [`2A202603544_NguyenDucDat.md`](2A202603544_NguyenDucDat.md)
- Đỗ Cao Cường: [`2A202603612_DoCaoCuong.md`](2A202603612_DoCaoCuong.md)
- Nguyễn Văn Minh: [`2A202603551_NguyenVanMinh.md`](2A202603551_NguyenVanMinh.md)

---

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu giả lập về thời gian:** Hai cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated` hiện tại là số mô phỏng giả lập. Cần đo đạc thời gian thực tế thông qua các event viễn trắc (`staff_review_decision`, `staff_rework_completed`) ngay trong tuần đầu tiên của pilot để cập nhật lại mô hình chi phí.
- **Hiện tượng tràn tác động giữa các nhân viên:** Dù đã chia theo nhân viên và phân quyền tài khoản, các nhân viên trong cùng một depot vẫn có thể giao tiếp và chia sẻ kinh nghiệm xử lý đơn, dẫn đến hiện tượng tràn tác động (spillover). Cần bổ sung các buổi phỏng vấn định tính để theo dõi hành vi này.

---

## 8. Tài liệu tham khảo

1. Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arXiv:2504.13359](https://arxiv.org/abs/2504.13359).
2. Google PAIR, *People + AI Guidebook*, Chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
3. Tài liệu thư viện Statsmodels: Phân tích kiểm định tỉ lệ và sức mạnh thống kê `NormalIndPower` (`statsmodels.stats.power`).
4. Hướng dẫn thực hành Lab 13 AI20K K5, tài liệu [`docs/du_lieu_va_cong_thuc.md`](../../docs/du_lieu_va_cong_thuc.md) và [`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
