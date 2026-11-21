# Báo cáo cá nhân — NguyenVanMinh-2A202603551

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Văn Minh
- **MSSV:** 2A202603551
- **Email:** minhvjjp@gmail.com
- **GitHub:** https://github.com/killy-mv/
- **Nhóm:** Armless · **Lớp:** L3A
- **Vai trò:** Người gắn nhãn 2, kiêm giữ hồ sơ launch v0.

## 2. Phần việc phụ trách

Theo `PHAN_CONG.md`, tôi phụ trách chuẩn bị thông tin nhóm, duy trì hồ sơ launch v0, gắn nhãn độc lập 20 ca lỗi CP3, kiểm tra cấu trúc và tính đầy đủ của `pilot_plan.yaml` CP4, ghi phiếu chấm hội đồng Gate 2a và chuẩn bị báo cáo cá nhân. Tôi cũng có trách nhiệm phối hợp chốt đề xuất Go / Go có điều kiện / No-go dựa trên bằng chứng CP1–CP5 và duyệt báo cáo nhóm khi có PR.

## 3. Đóng góp cụ thể và trạng thái

| Công việc | Công việc đã thực hiện | Trạng thái |
| --- | --- | --- |
| Hồ sơ launch v0 | Chuẩn bị đủ **7 mục**; cập nhật CP1–CP2 từ nhánh `origin/cp1-cp2-chi-phi`, tự kiểm tra lại số liệu chi phí từ CSV. Tính thử ba chỉ số CP5 từ CSV, giữ nhãn chờ nhóm xác nhận. | **Đã cập nhật CP1–CP2**; chưa chốt Gate 2a |
| CP3 — Phân loại lỗi | Đọc **20 ca lỗi** trong đề và chuẩn bị bản nháp phân loại có lý do từng ca với sự hỗ trợ của ChatGPT tại `report/team/nhan_cp3_Minh_draft.md` (file làm việc cục bộ, không nộp). | **Chưa hoàn tất** gắn nhãn độc lập tự xác nhận, đối chiếu với Cường hoặc duyệt bảng lỗi |
| CP4 — Kiểm tra YAML | Chuẩn bị và chạy công cụ đọc/kiểm tra `pilot_plan.yaml` bằng PyYAML, rà các trường bắt buộc, placeholder, câu D1/D2 và luật dừng. File đang kiểm tra là **mẫu chưa hoàn thiện**: cú pháp YAML hợp lệ nhưng còn **15 dòng có dấu `?`** trong nội dung. | **Đã chuẩn bị bộ kiểm tra**; sẽ kiểm tra lại file hoàn chỉnh từ Đạt |
| Thông tin nhóm `TEAM.md` | Điền họ tên, MSSV, email và GitHub của Minh; giữ nguyên các hàng của thành viên khác. | **Đã điền phần cá nhân**, còn thiếu thông tin của ba thành viên khác |
| Duyệt chéo Gate 2a | Đã đọc yêu cầu phiếu chấm **3 tiêu chí, 30 điểm**. | **Chưa chấm**; cần hồ sơ và phiên duyệt chéo thực tế |
| Báo cáo cá nhân | Viết báo cáo này theo sáu mục của mẫu và tách rõ việc đã làm, việc còn chờ. | **Bản nháp**; cập nhật lại khi kết thúc lab |

## 4. Bằng chứng

- **Hồ sơ launch v0:** bản nháp ban đầu trên nhánh `docs/ho-so-launch`, commit **`60a9098`** (`docs: prepare launch v0 dossier draft for Gate 2a`). Bản cập nhật tại working tree hiện có kết quả từ nhánh `origin/cp1-cp2-chi-phi` (commit `6e7da01`), **chưa commit hoặc được hội đồng phê duyệt**.
- **CP3:** file làm việc cục bộ `report/team/nhan_cp3_Minh_draft.md` chứa đề xuất AI cho 20 ca và cột chờ tự xác nhận; không được coi là bộ nhãn độc lập hoàn tất hay điểm đồng thuận thực tế.
- **CP4:** công cụ cục bộ `local_checks/check_cp4_yaml_minh.py` chạy với `src/.venv` và PyYAML 6.0.4; kết quả kiểm tra ban đầu: `yaml.safe_load` đọc được file, nhưng **chưa đạt checklist** do còn placeholder và thiếu câu trả lời D1/D2. Công cụ chỉ phục vụ tự kiểm tra, không phải deliverable nhóm.
- **Kiểm chứng số liệu:** tính độc lập từ `src/logix_runs.csv` và `src/logix_requests.csv` bằng Python: **978/1.200** ca thành công; tổng chi phí **4.373.585 đ [simulated]** và **4.472 đ/việc [simulated]**; ba chỉ số thử nghiệm **82,83%**, **27,12%**, **4,25%** (chờ CP5 đối chiếu).
- **Thông tin nhóm:** đã điền riêng dòng Nguyễn Văn Minh vào `TEAM.md`.
- **Tài liệu đối chiếu:** `PHAN_CONG.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `RULES.md`, `SUBMISSION.md`.

**Bằng chứng cần bổ sung sau khi hoàn tất:** nhãn CP3 do tôi tự xác nhận, tỷ lệ đồng thuận tính từ hai bộ nhãn độc lập, kết quả kiểm tra lại YAML hoàn chỉnh, nhận xét duyệt PR, phiếu Gate 2a và trạng thái hồ sơ cuối cùng.

## 5. Công cụ AI đã dùng và cách tự kiểm tra

- **ChatGPT:** hỗ trợ đọc yêu cầu Lab 13 và phân công, tổ chức khung hồ sơ bảy mục, đề xuất cách phân loại 20 ca lỗi, tạo công cụ kiểm tra YAML và hỗ trợ soạn báo cáo cá nhân này.
- **Bash 2.0 và Git:** đọc file trực tiếp trong repo, kiểm tra nhánh, thay đổi và bằng chứng. Không dùng mô hình AI để tạo số liệu giả làm kết quả tính toán hoặc kết quả duyệt chéo.
- **PyYAML:** chạy `yaml.safe_load` để kiểm tra cú pháp; kiểm tra bằng mã Python các dấu `?` và cấu trúc cơ bản. Tôi phân biệt rõ **YAML hợp lệ về cú pháp** với **kế hoạch pilot đạt yêu cầu nội dung**.

**Cách kiểm chứng đã thực hiện:** dùng Python đọc trực tiếp hai file CSV, kiểm tra số lượng bản ghi, phân nhóm theo loại và tính lại chi phí; so với `bang_chi_phi.md` trên nhánh CP1–CP2. Từ `logix_requests.csv`, tính tỷ lệ 994/1.200, 48/177 và 51/1.200 để chuẩn bị đối chiếu CP5. **Cần tự xác minh trước khi nộp:** tự chốt nhãn CP3, chạy lại kiểm tra YAML sau khi Đạt hoàn thành, đối chiếu các chỉ số với báo cáo CP5, ghi nhận bằng chứng duyệt chéo. Đề xuất AI không thay kết quả tự đánh giá hoặc quyết định của nhóm.

## 6. Tự đánh giá

Tôi đã chuẩn bị hồ sơ launch v0 đủ **7 mục**, cập nhật các số chi phí và độ nhạy từ kết quả nhóm đồng thời kiểm tra độc lập chi phí trên mẫu **1.200 yêu cầu**. Tôi tính thử ba chỉ số CP5 (chưa xác nhận với nhóm), bổ sung thông tin cá nhân trong `TEAM.md`, và xây dựng quy trình kiểm tra YAML. Tôi cũng tìm hiểu năm loại lỗi để chuẩn bị cho nhiệm vụ CP3.

Hạn chế hiện tại là tôi chưa tự xác nhận toàn bộ 20 nhãn, chưa đối chiếu nhãn với Cường, chưa kiểm tra phiên bản pilot hoàn chỉnh của Đạt và chưa có kết quả duyệt chéo. Trước khi nộp, tôi cần hoàn tất các bước đó, cập nhật bằng chứng và đề xuất cuối cùng theo số liệu đã kiểm chứng thay vì suy đoán.
