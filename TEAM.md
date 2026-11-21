# Team

## Thông tin nhóm

- Tên nhóm: Armless
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Armless-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/dpduc313/K5-L3A-DAY13-Armless-LaunchEconomics · `main` · (điền khi chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đậu Phúc Đức | 2A202603580 | teflon125.work@gmail.com | https://github.com/dpduc313 | Người viết code (trước giải lao) → người kiểm số |
|   2 | Nguyễn Đức Đạt | 2A202603544 | nguyenducdat298@gmail.com | https://github.com/nguyenducdat298 | Người kiểm số (trước giải lao) → người viết code; người gắn nhãn 2 ở CP3 (gắn lại) |
|   3 | Đỗ Cao Cường | 2A202603612 | 26ai.cuongdc@vinuni.edu.vn | https://github.com/cuongdc03 | Người gắn nhãn 1 |
|   4 | Nguyễn Văn Minh | 2A202603551 | minhvjjp@gmail.com | https://github.com/killy-mv/ | Giữ hồ sơ (ban đầu kiêm người gắn nhãn 2) |

Người gắn nhãn 2 ở CP3 đổi từ Minh sang Đạt: bộ nhãn đầu của Minh có AI đề xuất nên không đạt yêu cầu gắn độc lập; cả nhóm thống nhất để Đạt gắn lại. Chi tiết trong [report/team/bang_loi.md](report/team/bang_loi.md).

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Phân công chi tiết, nhánh và PR: [PHAN_CONG.md](PHAN_CONG.md).

## Báo cáo cá nhân của từng thành viên

Mỗi thành viên có một báo cáo riêng trong thư mục `report/team/`:

1. **Đậu Phúc Đức:** [`report/team/2A202603580_DauPhucDuc.md`](report/team/2A202603580_DauPhucDuc.md)
2. **Nguyễn Đức Đạt:** [`report/team/2A202603544_NguyenDucDat.md`](report/team/2A202603544_NguyenDucDat.md)
3. **Đỗ Cao Cường:** [`report/team/2A202603612_DoCaoCuong.md`](report/team/2A202603612_DoCaoCuong.md)
4. **Nguyễn Văn Minh:** [`report/team/2A202603551_NguyenVanMinh.md`](report/team/2A202603551_NguyenVanMinh.md)

---

## Đậu Phúc Đức — 2A202603580

### Phần việc phụ trách

- Tạo repo nhóm và môi trường chạy `src/.venv`.
- Trước giải lao (người viết code): CP1 và CP2 trong `src/lab13.py`, điền `report/team/bang_chi_phi.md`.
- Sau giải lao (người kiểm số): soạn luật dừng cho `pilot_plan.yaml`, hai dòng rủi ro kinh tế cho `chi_so.md`; chạy các lệnh kiểm tra trước khi merge.

### Đóng góp cụ thể

- A1–A4: ba hàm A1 in ĐẠT (1,20 · 1,25 · 1,25); `mo_hinh` cho chi phí 4.472 đ mỗi ca thành công [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; tách theo loại (quoc_te 1,88×); chi phí cố định 4.599 đ/ca [simulated].
- B1–B4: 9 kịch bản độ nhạy, xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]; giới hạn 2 lần chạy rẻ nhất cho công ty; xem lại 100% tốn 0,98–1,03× [simulated].
- Bốn luật dừng (an toàn, chi phí, mức sử dụng, thời gian xem lại) kèm định nghĩa và cách tính tay số đợt chạy thử.
- Hai dòng rủi ro kinh tế E2 (làm lại gấp đôi, xem lại gấp đôi), số lấy từ bảng B1, B4.
- Rà hồ sơ launch, tên vai thống nhất giữa các file; lưu phiếu gắn nhãn độc lập của Đạt cho CP3.

### Bằng chứng

- PR #2 (commit `6e7da01`): CP1, CP2 trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- PR #10: bốn luật dừng trong `report/team/pilot_plan.yaml`.
- PR #6 (Cường commit): hai dòng rủi ro E2 do Đức soạn, trong `report/team/chi_so.md`.
- PR #12, #13: cập nhật `bang_loi.md`, mục 5 hồ sơ, phiếu `report/team/nhan_cp3_Dat.md`.
- PR #7: báo cáo cá nhân `report/team/2A202603580_DauPhucDuc.md`.

---

## Nguyễn Đức Đạt — 2A202603544

### Phần việc phụ trách
- Người kiểm số (trước giải lao: CP1, CP2) → Người viết code (sau giải lao: CP4, CP5).
- Kiểm số độc lập A1–A4, B1–B4; kiểm tra tính cộng tuyến tính và chi phí cả hệ thống TCO.
- Viết code D1 (cỡ mẫu 3 cách chia), D3 (tỉ lệ mở lại khiếu nại hiện tại), E1 (ba chỉ số kết quả, sử dụng, an toàn).
- Hoàn thiện `group_report.md`, `phieu_cham.md` và báo cáo cá nhân `2A202603544_NguyenDucDat.md`.

### Đóng góp cụ thể
- Xác nhận độc lập chi phí 4.472 đ/việc [simulated] (gấp 16,3 lần hóa đơn token), tỉ trọng giờ nhân viên chiếm 92,5% [simulated].
- Chứng minh giới hạn 2 lần chạy là tối ưu nhất cho cả hệ thống (6.901.220 đ [simulated]).
- Chứng minh bằng toán học trần mẫu $c / ICC = 1.000 < 1.251$ khiến việc đo mức chênh 5 điểm là bất khả thi; giải bài toán đánh đổi đo mức chênh 6 điểm với $m \ge 299$ đơn/người ($DE = 6,96$).
- Đo lường và cung cấp số liệu 3 chỉ số E1: chính 82,83%, dùng 27,12%, an toàn 4,25% trên 1.200 đơn.

### Bằng chứng
- Code chạy hoàn tất trong `src/lab13.py`.
- Các file tài liệu: `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`, `report/team/2A202603544_NguyenDucDat.md`.

---

## Đỗ Cao Cường — 2A202603612

### Phần việc phụ trách

- Người gắn nhãn 1, kiêm theo dõi điều kiện "Xong khi" của CP1–CP5 và soát từng PR trước khi merge.
- Chia vai và lập quy trình nhánh, PR cho nhóm (`PHAN_CONG.md`).
- CP3: gắn nhãn độc lập 20 ca, tổng hợp `report/team/bang_loi.md`.
- CP4: soạn cách chia và năm câu D2 "tách được tác động" gửi người viết code.
- CP5: soạn `report/team/chi_so.md`.

### Đóng góp cụ thể

- Soát CP1, CP2: chạy `lab13.py`, đối chiếu A1–A4 và B1–B4 với số tham khảo, tất cả khớp (4.472 đ mỗi việc thành công [simulated]; B4 lệch 1 đ do làm tròn).
- CP3: tự gắn 20 nhãn không dùng AI; hai quy tắc phân biệt loại lỗi; bảng khắc phục 5 ca (ca 1, 7, 18, 13, 17), mỗi dòng có cách phát hiện đo được và một vai trò phụ trách; ghi rõ bộ nhãn người 2 ban đầu có AI đề xuất.
- CP4: đề xuất chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm; năm câu D2, dòng đánh đổi, trường `identifiability`; tính khả thi khoảng 31 yêu cầu/người/ngày, đạt 299 yêu cầu sau khoảng 10 ngày làm việc.
- CP5: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo chỉ số với event, hai dòng rủi ro kinh tế.
- Soát `main` sau CP4: phát hiện câu D2 số 4 ghi nhầm ngày quyết định là ngày bắt đầu, báo người viết code sửa.

### Bằng chứng

- PR #1 `docs/phan-cong`: commit `2e689b7`, `5248387` (`PHAN_CONG.md`, `TEAM.md`).
- PR #3 `feat/cp3-error-table`: commit `64702f2` (`report/team/bang_loi.md`).
- PR #4 `feat/cp5-metrics`: commit `4397eab` (`report/team/chi_so.md`, phần E1, event, kiểm tra chéo).
- PR #6 `feat/cp5-e2-risks`: commit `7931055` (`report/team/chi_so.md`, phần E2).
- Báo cáo cá nhân: `report/team/2A202603612_DoCaoCuong.md`.

---

## Nguyễn Văn Minh — 2A202603551

### Phần việc phụ trách

- Giữ hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`) từ đầu buổi.
- Ban đầu kiêm người gắn nhãn 2 ở CP3; bộ nhãn này bị nhóm thay bằng bộ Đạt gắn lại (xem `report/team/bang_loi.md`).
- Kiểm tra cấu trúc `pilot_plan.yaml` ở CP4.

### Đóng góp cụ thể

- Hồ sơ launch v0: dựng khung đủ 7 mục, cập nhật lần lượt theo CP1–CP2, CP3, CP4–CP5 và góp ý Gate 2a; tự tính lại từ CSV 978/1.200 ca thành công, tổng chi phí 4.373.585 đ và 4.472 đ/việc [simulated].
- Tính thử ba chỉ số CP5 từ CSV (994/1.200 = 82,83%, 48/177 = 27,12%, 51/1.200 = 4,25%) để đối chiếu với `chi_so.md`.
- CP3: 20 nhãn do ChatGPT đề xuất rồi Minh chấp thuận, lưu tại `report/team/nhan_cp3_Minh.md` để đối chiếu; không dùng để tính đồng thuận vì không đạt yêu cầu gắn độc lập.
- CP4: viết công cụ kiểm tra `pilot_plan.yaml` bằng PyYAML (đọc file, rà trường bắt buộc, dấu `?`, câu D1/D2, luật dừng); lần chạy đầu trên bản nháp phát hiện còn 15 dòng có dấu `?`.

### Bằng chứng

- Hồ sơ launch v0: commit `19c2bb8` (số CP1–CP2), `3203283` (kết quả CP3), `a001964` (sửa theo góp ý Gate 2a), `673ba0e` (bằng chứng CP4, CP5), đều đã nằm trong `main`.
- Phiếu nhãn CP3 ban đầu: `report/team/nhan_cp3_Minh.md`.
- Báo cáo cá nhân: `report/team/2A202603551_NguyenVanMinh.md`.
