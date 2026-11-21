# Phân công nhóm Armless · Lab 13

## Vai

| Người | Vai trước giải lao (14:00–15:20) | Vai sau giải lao (15:35–18:00) |
| --- | --- | --- |
| **Đức** | Người viết code | Người kiểm số |
| **Đạt** | Người kiểm số | Người viết code |
| **Cường** | Người gắn nhãn 1, theo dõi điều kiện "Xong khi" | Người gắn nhãn 1 |
| **Minh** | Người gắn nhãn 2, kiêm giữ hồ sơ | Người gắn nhãn 2, kiêm giữ hồ sơ |

Đổi người viết code sau giải lao là yêu cầu của đề (`TEAM.md`), để ít nhất hai người tự tay tính được chi phí.

## Việc của từng người

### Đức

- [ ] **14:00** Cài môi trường, chạy thử `python lab13.py`.
- [ ] **CP1** Nhánh `feat/cp1-cost-model`: viết ba hàm A1 trong `src/lab13.py` cho tới khi in ĐẠT (1,20 · 1,25 · 1,25); viết `mo_hinh` (A2); gọi lại theo từng `loai` (A3); cộng chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang` (A4). Mở PR, Đạt duyệt.
- [ ] **CP2** Nhánh `feat/cp2-sensitivity`: code 9 kịch bản B1, cặp B2, giới hạn 1/2/3 lần chạy (B3), xem lại 100% (B4). Commit thêm câu trả lời B3, B4 do Cường viết. Mở PR, Đạt duyệt.
- [ ] **Sau giải lao** (chuyển sang kiểm số): duyệt PR CP4 của Đạt; soạn ít nhất ba luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ, đưa Đạt.
- [ ] **CP5** Soạn ít nhất hai dòng rủi ro kinh tế (lấy số từ bảng độ nhạy), đưa Cường. Duyệt PR hồ sơ của Minh.
- [ ] **Cuối buổi** Báo cáo cá nhân (nhánh `docs/report-duc`).

### Đạt

- [ ] **14:00** Cài môi trường.
- [ ] **CP1** Tính tay chi phí token và tool để đối chiếu với code của Đức; điền bảng A1, A2, A3, A4 vào `report/team/bang_chi_phi.md` (commit vào nhánh của Đức), ghi nhãn `simulated` cho dòng xem lại và làm lại. Duyệt PR CP1.
- [ ] **CP2** Điền bảng B1–B4; kiểm tra "giảm một nửa" làm chi phí giảm đúng bằng nửa mức tăng của "gấp đôi". Duyệt PR CP2.
- [ ] **CP3** (lúc Cường và Minh gắn nhãn) Cùng Đức hoàn thiện nốt CP2, rồi đọc trước phần D1 trong hướng dẫn.
- [ ] **CP4** (chuyển sang viết code) Nhánh `feat/cp4-pilot-plan`, tách **sau khi** CP2 đã merge: code năm câu D1 (cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm); tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại; điền hết dấu `?` trong `pilot_plan.yaml`, ghép D2 của Cường và luật dừng của Đức. Mở PR, Đức duyệt.
- [ ] **CP5** Code tính thử ba chỉ số E1 (chính, dùng, an toàn), đưa số cho Cường. Duyệt PR CP5.
- [ ] **17:45** Nhánh `docs/group-report`: viết `group_report.md`. Báo cáo cá nhân (nhánh `docs/report-dat`).

### Cường

- [ ] **14:00** Đọc `CHECKPOINTS.md`, `RUBRIC.md`; giữ danh sách điều kiện "Xong khi" của từng checkpoint, nhắc nhóm trước mỗi lần merge.
- [ ] **CP1** Soát bảng A2: đủ 9 dòng, hai dòng giả lập có nhãn `simulated`, A3 đủ 4 dòng.
- [ ] **CP2** Viết câu trả lời B3, B4 (mỗi câu tối đa ba dòng, có số), đưa Đức commit.
- [ ] **CP3** Nhánh `feat/cp3-error-table`: gắn nhãn độc lập 20 ca trong 8 phút; điền cả hai bộ nhãn, tỉ lệ đồng thuận, quy tắc cho ca lệch, bảng khắc phục 5 ca vào `bang_loi.md`. Mở PR, Minh duyệt.
- [ ] **CP4** Soạn năm câu D2 "tách được tác động" và đề xuất cách chia, đưa Đạt.
- [ ] **CP5** Nhánh `feat/cp5-metrics`: điền `chi_so.md`, gồm số ba chỉ số (Đạt đưa), ít nhất sáu event có `trace_id`, một chỉ số dùng và một chỉ số an toàn tự đề xuất, phần kiểm tra chéo chỉ số với event, rủi ro kinh tế (Đức đưa). Mở PR, Đạt duyệt.
- [ ] **17:45** Chạy các lệnh kiểm tra cuối (mục dưới). Báo cáo cá nhân (nhánh `docs/report-cuong`).

### Minh

- [ ] **14:00** Nhánh `docs/team-setup`: thu MSSV, email, GitHub của cả nhóm, điền `TEAM.md`. Mở PR, Đức duyệt.
- [ ] **14:10** Nhánh `docs/ho-so-launch`: mở draft PR ngay. Sau mỗi checkpoint chép con số chính vào `ho_so_launch_v0.md`: mục 1, 3 sau CP1 · mục 2 sau CP2 · mục 5 sau CP3 · mục 6 sau CP4 · mục 4, 7 sau CP5. Mỗi mục có trạng thái và người phụ trách là một vai trò.
- [ ] **CP3** Gắn nhãn độc lập 20 ca trong 8 phút, đưa bản nháp cho Cường; cùng so nhãn. Duyệt PR CP3.
- [ ] **CP4** Chạy `yaml.safe_load` và lệnh grep dấu `?` trên `pilot_plan.yaml` trước khi Đạt merge.
- [ ] **16:55** Chốt hồ sơ đủ bảy mục, viết đề xuất (Go / Go có điều kiện / No-go) cùng cả nhóm, merge trước 17:00 và gửi cho nhóm hội đồng.
- [ ] **17:00** Nhánh `docs/phieu-cham`: ghi phiếu nhóm mình chấm nhóm n + 1. Mở PR, Cường duyệt. Duyệt PR `group-report`.
- [ ] **Cuối buổi** Báo cáo cá nhân (nhánh `docs/report-minh`).

## Quy trình Git

1. Luôn tách nhánh từ `main` mới nhất:
   ```bash
   git checkout main && git pull
   git checkout -b <ten-nhanh>
   ```
2. Làm xong một checkpoint thì push và mở PR vào `main`:
   ```bash
   git push -u origin <ten-nhanh>
   gh pr create --base main --fill
   ```
3. Mỗi PR cần **một người duyệt** (cột "Người duyệt" bên dưới), duyệt xong thì merge. Không force-push, không push thẳng lên `main`.
4. Trước khi bắt đầu nhánh tiếp theo, `git checkout main && git pull` để có code của người trước.
5. `src/lab13.py` chỉ có **một người sửa tại một thời điểm**: Đức trước giải lao, Đạt sau giải lao. Đạt chỉ tách nhánh CP4 **sau khi** PR CP2 của Đức đã merge.
6. Không commit `.venv/`, `.env`; không sửa hai file CSV.

## Nhánh và PR

| # | Nhánh | Người làm | Người duyệt | File | Nội dung | Merge trước |
| --: | --- | --- | --- | --- | --- | --- |
| 0 | `docs/team-setup` | Minh | Đức | `TEAM.md` | Điền MSSV, email, GitHub của cả nhóm | 14:10 |
| 1 | `feat/cp1-cost-model` | Đức | Đạt | `src/lab13.py`, `report/team/bang_chi_phi.md` (A1–A4) | Ba hàm A1 (in ĐẠT 1,20 · 1,25 · 1,25), `mo_hinh` A2, tách theo `loai` A3, chi phí cố định A4. Đạt tính tay token và tool để đối chiếu rồi điền bảng; hai dòng xem lại và làm lại ghi nhãn `simulated` | 14:53 |
| 2 | `feat/cp2-sensitivity` | Đức | Đạt | `src/lab13.py`, `report/team/bang_chi_phi.md` (B1–B4) | 9 kịch bản B1, cặp B2 và xếp hạng, B3, B4. Cường viết câu trả lời B3 và B4 (đưa Đức để commit vào cùng nhánh) | 15:35 |
| 3 | `feat/cp3-error-table` | Cường | Minh | `report/team/bang_loi.md` | Xem quy trình gắn nhãn bên dưới | 16:08 |
| 4 | `feat/cp4-pilot-plan` | Đạt | Đức | `src/lab13.py` (D1), `report/team/pilot_plan.yaml` | Năm câu D1, tỉ lệ `mo_lai_trong_7_ngay` hiện tại, năm câu D2 (Cường soạn), ít nhất ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ (Đức soạn). Không còn dấu `?`, chạy được `yaml.safe_load` | 16:36 |
| 5 | `feat/cp5-metrics` | Cường | Đạt | `report/team/chi_so.md` | Ba chỉ số tính thử (Đạt tính bằng code rồi đưa số), ít nhất sáu event có `trace_id`, một chỉ số dùng và một chỉ số an toàn tự đề xuất, ít nhất hai dòng rủi ro kinh tế (Đức soạn, lấy số từ bảng độ nhạy) | 16:55 |
| 6 | `docs/ho-so-launch` | Minh | Đức | `report/team/ho_so_launch_v0.md` | Mở **draft PR từ 14:10**, điền dần sau mỗi checkpoint; chốt đủ bảy mục và đề xuất, rồi merge | **17:00** |
| 7 | `docs/phieu-cham` | Minh | Cường | `report/team/phieu_cham.md` | Phiếu nhóm mình chấm nhóm n + 1 (cả nhóm cùng chấm, Minh ghi) | 17:45 |
| 8 | `docs/group-report` | Đạt | Minh | `report/team/group_report.md` | Báo cáo nhóm ngắn, dẫn lại con số chính và đề xuất | 18:00 |
| 9 | `docs/report-<ten>` | Từng người | Một người bất kỳ | `report/team/<MSSV>_<HoTen>.md`, phần của mình trong `TEAM.md` | Báo cáo cá nhân, ghi công cụ AI đã dùng và cách tự kiểm tra | 23:59 |

### Gắn nhãn CP3 (Cường và Minh)

1. Hai người ngồi tách nhau, gắn nhãn cả 20 ca trong 8 phút **trên giấy hoặc file nháp riêng**, không trao đổi, chưa commit.
2. Gắn xong, Cường điền cả hai cột nhãn vào `bang_loi.md` y nguyên bản gốc. Không sửa nhãn sau khi đã so.
3. So nhãn và tính tỉ lệ đồng thuận (cần ít nhất 16/20). Với mỗi ca lệch: thống nhất nhãn và ghi một câu quy tắc phân biệt.
4. Điền bảng khắc phục cho 5 ca, mỗi loại lỗi một ca. Mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
5. Trong lúc đó, Đức và Đạt hoàn thiện nốt CP2.

## Kiểm tra trước khi merge PR cuối

Chạy trong thư mục `src/`:

```bash
python lab13.py                                                      # ba phép thử in ĐẠT
python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"
grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'          # không in gì
grep -rni production ../report/team                                  # không in gì
```

Cuối cùng, **mỗi người tự nộp link repo trên LMS** trước 23h59 GMT+7.
