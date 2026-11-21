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
|   2 | Nguyễn Đức Đạt | 2A202603544 | nguyenducdat298@gmail.com | https://github.com/nguyenducdat298 | Người kiểm số (trước giải lao) → người viết code |
|   3 | Đỗ Cao Cường | 2A202603612 | 26ai.cuongdc@vinuni.edu.vn | https://github.com/cuongdc03 | Người gắn nhãn 1 |
|   4 | Nguyễn Văn Minh | 2A202603551 | minhvjjp@gmail.com | https://github.com/killy-mv/ | Người gắn nhãn 2, kiêm giữ hồ sơ |

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
