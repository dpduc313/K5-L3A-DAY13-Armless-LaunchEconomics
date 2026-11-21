"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm Armless (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py. Công thức theo docs/du_lieu_va_cong_thuc.md.
Mọi số tính từ cột *_simulated được in kèm nhãn [simulated].
"""
import math
import sys

import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')   # in được tiếng Việt cả khi chuyển output sang file

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000   # đồng mỗi tháng
YC_MOI_THANG = 45_000          # yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi dùng ở A4 và B4
SIM = '[simulated]'


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy của các yêu cầu trong reqs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong' (mẫu số).
    - max_lan_chay: bỏ các lần chạy có attempt > giới hạn; yêu cầu có so_lan_chay > giới hạn
      coi là chuyen_nhan_vien, phút xem lại và làm lại bằng 0.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def tieu_de(chu):
    print(f'\n===== {chu} =====')


def a2_in_bang(runs, reqs):
    tieu_de('A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps là simulated)')
    kq = mo_hinh(runs, reqs)
    for ten, gia_tri in kq.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f'Số lần gọi tool: {runs["tool_calls"].sum():,}; '
          f'phút xem lại {reqs["phut_xem_lai_simulated"].sum():,}, '
          f'phút làm lại {reqs["phut_lam_lai_simulated"].sum():,} {SIM}')
    print(f'cps gấp {kq["cps"] / kq["hoa_don_moi_yc"]:.1f} lần hoá đơn token + tool chia số yêu cầu')
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  Tỉ trọng {khoan:8s} {kq[khoan] / kq["tong"]:6.1%}')
    print(f'  Giờ nhân viên (xem lại + làm lại): {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"]:.1%} {SIM}')
    # So với nhân viên tự làm: cộng phần nhân viên làm thay các ca không thành công.
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}x {SIM}')


# ---------- Nhiệm vụ A3, A4 ----------
def a3_theo_loai(runs, reqs):
    tieu_de('A3 · Tách theo loại yêu cầu')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"chay/yc":>8s} {"cps [sim]":>10s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r):9.1%} {so_chay / len(r):8.2f} '
              f'{kq["cps"]:10,.0f} {kq["cps"] / BASELINE:6.2f}x')
    # Tỉ lệ lần chạy status == ok theo loại và theo lần thử: chạy lại có giúp không?
    gop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    gop['ok'] = (gop['status'] == 'ok').astype(float)
    bang = gop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    print('\nTỉ lệ lần chạy ok theo lần thử, % (đo từ trace):')
    print((bang * 100).round(1).to_string())


def a4_co_dinh(runs, reqs):
    tieu_de('A4 · Chi phí cố định 40 triệu/tháng, phạm vi noi_dia + hang_nang')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    print(f'Phạm vi: {len(r)} yêu cầu, {kq["thanh_cong"]} việc thành công, '
          f'cps chưa cộng cố định {kq["cps"]:,.0f} đ {SIM}')
    for ten, he_so in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_MOI_THANG * he_so * kq['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong = kq['cps'] + co_dinh
        print(f'{ten:22s} việc TC/tháng {tc_thang:8,.0f} · cố định/việc {co_dinh:6,.0f} đ · '
              f'cps + cố định {tong:6,.0f} đ = {tong / BASELINE:.2f}x {SIM}')


# ---------- Nhiệm vụ B · Độ nhạy ----------
def b_do_nhay(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    tieu_de('B1 · Đổi từng yếu tố')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":28s} {goc:8,.0f} đ {SIM}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:8,.0f} đ {(cps / goc - 1) * 100:+6.1f}% {SIM}')

    tieu_de('B2 · Đổi một cặp')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    rieng = (mo_hinh(runs, reqs, gia_vao=52, gia_ra=260)['cps'] - goc) + \
            (mo_hinh(runs, reqs, he_so_xem_lai=2)['cps'] - goc)
    print(f'Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) {SIM}; '
          f'tổng hai tác động riêng: {rieng / goc * 100:+.1f}%')

    tieu_de('B3 · Giới hạn chạy lại và chi phí cả hệ thống (1.200 yêu cầu)')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE
        print(f'Tối đa {k} lần: tổng trợ lý {kq["tong"]:10,.0f} đ · không TC {khong_tc:3d} · '
              f'cả hệ thống {he_thong:10,.0f} đ · cps {kq["cps"]:6,.0f} đ {SIM}')


def b4_xem_lai_tat_ca(runs, reqs, phut_xem=5, phut_lam_lai=9):
    tieu_de('B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    ru = runs[runs['request_id'].isin(r['request_id'])]
    co_ok = ru.loc[ru['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((r['ket_qua'] == 'lam_lai').sum())
    token_tool = (ru['tokens_in'] / 1000 * GIA_VAO + ru['tokens_out'] / 1000 * GIA_RA
                  + ru['tool_calls'] * GIA_TOOL).sum()
    thanh_cong = int((r['ket_qua'] == 'thanh_cong').sum())
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'{len(r)} yêu cầu · có ≥1 lần chạy ok: {co_ok} · ca làm lại: {so_lam_lai} · '
          f'token + tool: {token_tool:,.0f} đ · việc thành công: {thanh_cong}')
    print(f'Phút làm lại trong dữ liệu (mọi ca lam_lai): trung bình {tb_lam_lai.mean():.1f}, '
          f'trung vị {tb_lam_lai.median():.1f} {SIM}')
    for nhan, phut in [(f'làm lại {phut_lam_lai} phút (đề cho)', phut_lam_lai),
                       (f'làm lại {tb_lam_lai.mean():.1f} phút (dữ liệu)', tb_lam_lai.mean())]:
        tien_xem = co_ok * phut_xem * LUONG_PHUT
        tien_lam = so_lam_lai * phut * LUONG_PHUT
        tong = tien_xem + tien_lam + token_tool
        cps = tong / thanh_cong
        hoa_von = (BASELINE * thanh_cong - token_tool - tien_lam) / (co_ok * LUONG_PHUT)
        print(f'{nhan:30s} xem lại {tien_xem:,.0f} + làm lại {tien_lam:,.0f} + token/tool → '
              f'tổng {tong:,.0f} đ · cps {cps:,.0f} đ = {cps / BASELINE:.2f}x · '
              f'hoà vốn khi mỗi lần xem lại ≤ {hoa_von:.1f} phút {SIM}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    a2_in_bang(runs, reqs)
    a3_theo_loai(runs, reqs)
    a4_co_dinh(runs, reqs)
    b_do_nhay(runs, reqs)
    b4_xem_lai_tat_ca(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
