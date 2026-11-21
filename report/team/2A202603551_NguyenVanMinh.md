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
| Hồ sơ launch v0 | Chuẩn bị bản nháp **7 mục** trong `report/team/ho_so_launch_v0.md`: số liệu nền theo đề, trạng thái từng mục, vai trò phụ trách, phạm vi pilot dự kiến và điều kiện bổ sung bằng chứng. Không tự điền kết quả chưa được tính. | **Đã chuẩn bị bản nháp**; chưa chốt Gate 2a |
| CP3 — Phân loại lỗi | Đọc **20 ca lỗi** trong đề và chuẩn bị bản nháp phân loại có lý do từng ca với sự hỗ trợ của ChatGPT tại `report/team/nhan_cp3_Minh_draft.md` (file làm việc cục bộ, không nộp). | **Chưa hoàn tất** gắn nhãn độc lập tự xác nhận, đối chiếu với Cường hoặc duyệt bảng lỗi |
| CP4 — Kiểm tra YAML | Chuẩn bị và chạy công cụ đọc/kiểm tra `pilot_plan.yaml` bằng PyYAML, rà các trường bắt buộc, placeholder, câu D1/D2 và luật dừng. File đang kiểm tra là **mẫu chưa hoàn thiện**: cú pháp YAML hợp lệ nhưng còn **15 dòng có dấu `?`** trong nội dung. | **Đã chuẩn bị bộ kiểm tra**; sẽ kiểm tra lại file hoàn chỉnh từ Đạt |
| Thông tin nhóm `TEAM.md` | Đã xem thông tin nhóm và phân công trong repo để phục vụ hồ sơ. | **Chưa điền đầy đủ** MSSV, email, GitHub của cả nhóm |
| Duyệt chéo Gate 2a | Đã đọc yêu cầu phiếu chấm **3 tiêu chí, 30 điểm**. | **Chưa chấm**; cần hồ sơ và phiên duyệt chéo thực tế |
| Báo cáo cá nhân | Viết báo cáo này theo sáu mục của mẫu và tách rõ việc đã làm, việc còn chờ. | **Bản nháp**; cập nhật lại khi kết thúc lab |

## 4. Bằng chứng

- **Hồ sơ launch v0:** `report/team/ho_so_launch_v0.md`, nhánh `docs/ho-so-launch`, commit **`60a9098`** (`docs: prepare launch v0 dossier draft for Gate 2a`). Đây là **bản nháp**, không phải hồ sơ đã được hội đồng phê duyệt.
- **CP3:** file làm việc cục bộ `report/team/nhan_cp3_Minh_draft.md` chứa đề xuất AI cho 20 ca và cột chờ tự xác nhận; không được coi là bộ nhãn độc lập hoàn tất hay điểm đồng thuận thực tế.
- **CP4:** công cụ cục bộ `local_checks/check_cp4_yaml_minh.py` chạy với `src/.venv` và PyYAML 6.0.4; kết quả kiểm tra ban đầu: `yaml.safe_load` đọc được file, nhưng **chưa đạt checklist** do còn placeholder và thiếu câu trả lời D1/D2. Công cụ chỉ phục vụ tự kiểm tra, không phải deliverable nhóm.
- **Tài liệu đối chiếu:** `PHAN_CONG.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `RULES.md`, `SUBMISSION.md`.

**Bằng chứng cần bổ sung sau khi hoàn tất:** nhãn CP3 do tôi tự xác nhận, tỷ lệ đồng thuận tính từ hai bộ nhãn độc lập, kết quả kiểm tra lại YAML hoàn chỉnh, nhận xét duyệt PR, phiếu Gate 2a và trạng thái hồ sơ cuối cùng.

## 5. Công cụ AI đã dùng và cách tự kiểm tra

- **ChatGPT:** hỗ trợ đọc yêu cầu Lab 13 và phân công, tổ chức khung hồ sơ bảy mục, đề xuất cách phân loại 20 ca lỗi, tạo công cụ kiểm tra YAML và hỗ trợ soạn báo cáo cá nhân này.
- **Bash 2.0 và Git:** đọc file trực tiếp trong repo, kiểm tra nhánh, thay đổi và bằng chứng. Không dùng mô hình AI để tạo số liệu giả làm kết quả tính toán hoặc kết quả duyệt chéo.
- **PyYAML:** chạy `yaml.safe_load` để kiểm tra cú pháp; kiểm tra bằng mã Python các dấu `?` và cấu trúc cơ bản. Tôi phân biệt rõ **YAML hợp lệ về cú pháp** với **kế hoạch pilot đạt yêu cầu nội dung**.

**Cần tự xác minh trước khi nộp:** đọc lại 20 tình huống và tự chốt bộ nhãn độc lập; đối chiếu số liệu CP1–CP5 với code và file nhóm; chạy lại kiểm tra CP4 trên bản Đạt hoàn thành; rà các trạng thái/bằng chứng trong hồ sơ launch v0. Các đề xuất từ AI không được dùng thay kết quả quan sát, quyết định hoặc đóng góp thực tế.

## 6. Tự đánh giá

Tôi đã chuẩn bị được cấu trúc hồ sơ launch v0 theo yêu cầu **7 mục**, xác định rõ dữ liệu còn thiếu và xây dựng quy trình kiểm tra YAML nhằm giảm lỗi định dạng trước lúc duyệt Gate 2a. Tôi cũng đã tìm hiểu năm loại lỗi để chuẩn bị cho nhiệm vụ CP3.

Hạn chế hiện tại là tôi chưa tự xác nhận toàn bộ 20 nhãn, chưa đối chiếu nhãn với Cường, chưa kiểm tra phiên bản pilot hoàn chỉnh của Đạt và chưa có kết quả duyệt chéo. Trước khi nộp, tôi cần hoàn tất các bước đó, cập nhật bằng chứng và đề xuất cuối cùng theo số liệu đã kiểm chứng thay vì suy đoán.
