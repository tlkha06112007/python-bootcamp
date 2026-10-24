
import copy
import math

import pytest

from log_stats import analyse


# ---------- vi du cua thay ----------

def test_w3_2_vi_du_cua_thay():
    pairs = [
        ("fee", 100), ("fee", 200), ("fee", 300),
        ("rag", 400), ("rag", 500),
    ]
    result = analyse(pairs)

    assert result["counts"] == {"fee": 3, "rag": 2}
    assert result["p95"]["fee"] == 300  # nearest-rank, KHONG phai 290
    assert result["slowest"] == "rag"


def test_w3_2_khong_dung_noi_suy_tuyen_tinh():
    # noi suy tuyen tinh cho 290, nearest-rank phai cho 300
    result = analyse([("fee", 100), ("fee", 200), ("fee", 300)])
    assert result["p95"]["fee"] != pytest.approx(290)
    assert result["p95"]["fee"] == 300


# ---------- edge case ----------

def test_w3_2_route_chi_co_1_request():
    result = analyse([("solo", 42)])

    assert result["counts"] == {"solo": 1}
    assert result["p95"] == {"solo": 42}
    assert result["slowest"] == "solo"


def test_w3_2_danh_sach_rong():
    result = analyse([])

    assert result["counts"] == {}
    assert result["p95"] == {}
    assert result["slowest"] is None


def test_w3_2_hai_route_hoa_p95():
    pairs = [("a", 100), ("a", 200), ("b", 200), ("b", 100)]
    result = analyse(pairs)

    assert result["p95"]["a"] == result["p95"]["b"] == 200
    # de bai chua noi hoa thi chon ai; chi can la 1 trong 2 route hoa
    assert result["slowest"] in {"a", "b"}


def test_w3_2_20_phan_tu_nearest_rank():
    # n = 20 -> ceil(0.95 * 20) - 1 = 18 -> phan tu thu 19 sau khi sort
    latencies = list(range(1, 21))
    result = analyse([("r", x) for x in latencies])

    assert result["counts"] == {"r": 20}
    assert result["p95"]["r"] == 19
    assert result["p95"]["r"] == sorted(latencies)[math.ceil(0.95 * 20) - 1]


def test_w3_2_khong_phu_thuoc_thu_tu_dau_vao():
    pairs = [("r", x) for x in (50, 10, 40, 20, 30)]
    result = analyse(pairs)

    # n = 5 -> ceil(4.75) - 1 = 4 -> phan tu lon nhat
    assert result["p95"]["r"] == 50


def test_w3_2_du_lieu_vao_khong_bi_sua():
    pairs = [("b", 300), ("a", 100), ("b", 100), ("a", 200), ("b", 200)]
    truoc = copy.deepcopy(pairs)

    analyse(pairs)

    assert pairs == truoc  # khong sort/xoa/them tren danh sach goc


def test_w3_2_goi_hai_lan_cho_cung_ket_qua():
    pairs = [("a", 1), ("a", 2), ("b", 3)]
    assert analyse(pairs) == analyse(pairs)