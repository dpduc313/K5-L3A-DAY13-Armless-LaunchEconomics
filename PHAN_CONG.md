# Phân công nhóm Armless · Lab 13

## Vai

| Người | Vai trước giải lao (14:00–15:20) | Vai sau giải lao (15:35–18:00) |
| --- | --- | --- |
| **Đức** | Người viết code | Người kiểm số |
| **Đạt** | Người kiểm số | Người viết code |
| **Cường** | Người gắn nhãn 1, theo dõi điều kiện "Xong khi" | Người gắn nhãn 1 |
| **Minh** | Người gắn nhãn 2, kiêm giữ hồ sơ | Người gắn nhãn 2, kiêm giữ hồ sơ |

Đổi người viết code sau giải lao là yêu cầu của đề (`TEAM.md`), để ít nhất hai người tự tay tính được chi phí.

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
