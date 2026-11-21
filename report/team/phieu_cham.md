# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Armless (L3A)
- Nhóm được chấm: QCDH (L3A), repo `olivercuongnguyen-ca/K5-L3A-DAY13-QCDH-LaunchEconomics`, commit `4a2d595`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện chỉ cho `noi_dia` + `hang_nang`, khớp A3 (0,22× và 0,69× [simulated]). Nêu hai con số bất lợi kèm cách xử lý: xem lại 100% lên 0,98–1,03× [simulated] (điều kiện 4: giảm xem lại theo bậc khi sửa + bỏ < 15%); power 0,64 nếu tác động thật là 5 điểm (điều kiện 2: Giám đốc vận hành ký chấp nhận). Bốn điều kiện đều có vai trò và ngày kiểm tra (04/12/2026, 14/12/2026). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn `[simulated]` ở A2, A3, A4, B1–B3, E2 và hồ sơ. Phạm vi loại `quoc_te` (27,3% thành công, 1,88× [simulated]) và `doi_tac` (0,85× [simulated]). Sót nhỏ: "92,5%" ở mục 1 hồ sơ chưa gắn nhãn, dù cột trạng thái ghi "Giả lập". |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng chạy đồng thời, bốc thăm 20 + 20 nhân viên phân tầng theo depot; MDE 6 điểm cần m ≥ 299 yêu cầu mỗi nhân viên (hệ số thiết kế 6,96). Bậc 50% chỉ 1 tuần (khoảng 215 yêu cầu mỗi người, dưới 299); QCDH trả lời sẽ kéo dài bậc 50% cho đủ số. 3 luật dừng đủ bốn vế, có ngưỡng (+2 điểm hoặc 6%, 8.000 đ, 40%) và vai trò có quyền dừng. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp số của chính nhóm và nêu thẳng hai con số bất lợi (0,98–1,03× khi xem lại 100% [simulated]; power 0,64 ở mức 5 điểm). Pilot cần kéo dài bậc 50% để đạt m ≥ 299 yêu cầu mỗi nhân viên trước ngày quyết định 2027-01-05. Lỗi hình thức: hồ sơ còn dòng hướng dẫn "Go · Go có điều kiện · No-go (giữ một)" của mẫu; `bang_loi.md` chưa ghi tên hai người gắn nhãn.

**Một câu hỏi cho đội trình:** Luật dừng an toàn ghi "1 ca hoàn trùng TRONG 3 ngày liên tiếp". Nếu ngày đầu có 1 ca hoàn trùng thì tắt ngay hay chờ đủ 3 ngày?

**Câu trả lời của đội trình (ghi lại tại buổi):** Ý của nhóm là tắt ngay khi có 1 ca hoàn trùng đầu tiên, không đợi đủ 3 ngày. Hoàn trùng là mất tiền thật và không thể thu hồi, nên với chỉ số an toàn này ngưỡng là 0 ca, không có thời gian quan sát. Chữ "TRONG 3 ngày liên tiếp" trong câu luật là phần viết chưa chặt. Nó chỉ nên áp cho vế mở lại 7 ngày (đo theo cửa sổ), không áp cho vế hoàn trùng. Khi có ca đầu tiên, Giám đốc vận hành bật cờ tắt trong 30 phút, Kỹ sư trưởng agent đọc trace ca đó và đối soát idempotency_key. Chỉ bật lại khi có văn bản đồng ý của Giám đốc vận hành.
