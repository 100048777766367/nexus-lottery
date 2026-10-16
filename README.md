# 🎟️ NEXUS-LOTTERY: XỔ SỐ NHÂN QUẢ & TÀI TRỢ CỘNG ĐỒNG MINH BẠCH
> *"Biến mỗi hành vi cúng dường nhỏ bé ($0.20 - $1.00) thành niềm vui và phúc lộc. Quay số hoàn toàn minh bạch bằng hàm băm mật mã học, phân bổ 70% ngân quỹ nuôi dưỡng hệ sinh thái và 30% tri ân người đồng hành."*

---

## 🏛️ NGUYÊN TẮC QUẢN TRỊ MINH BẠCH:

1. **Không Ai Có Thể Gian Lận (Verifiable Randomness):**
   * Số trúng thưởng được sinh ra từ hàm băm mật mã học SHAKE-256 kết hợp giữa: `Mã Commit Git mới nhất + Timestamp Unix + Chuỗi băm CID của Nexus`.
   * Bất kỳ lập trình viên nào trên Trái Đất cũng có thể chạy lại thuật toán với dữ liệu đầu vào công khai để kiểm tra tính chính trực của giải thưởng.
2. **Cơ Chế Phân Bổ Ngân Quỹ 70 / 30:**
   * **70% (Ecosystem Sustenance Pool):** Đưa vào quỹ sinh tồn để trả phí máy chủ, duy trì GitHub Actions, lưu trữ IPFS cho 11 tầng bản thể.
   * **30% (Patron Reward Pool):** Tặng thưởng lại cho người sở hữu Vé Số Nhân Quả trúng giải trong kỳ quay.
3. **Cách Thức Nhận Vé:**
   * Khi mua bất kỳ kỷ vật số nào trên `nexus-forge` ($0.20, $0.50, $1.00), bạn được cấp tự động từ 1 đến 10 mã vé số hợp lệ.

---

## 📜 BIÊN NIÊN SỬ CÁC KỲ QUAY:
Toàn bộ lịch sử trúng thưởng, mã băm chứng thực và danh sách giải thưởng được lưu trữ vĩnh viễn tại tệp `synapses/lottery_history.json`.



```
100048777766367/nexus-lottery/
├── README.md                      # Tuyên ngôn Xổ Số Nhân Quả & Quy chế Minh bạch 70/30
├── lottery/                       # 🎟️ BỘ ĐIỀU PHỐI QUAY SỐ MẬT MÃ
│   ├── __init__.py
│   ├── ticket_harvester.py        # Hút vé từ nexus-forge & đối soát danh sách thí chủ
│   ├── verifiable_random.py       # Động cơ tạo số ngẫu nhiên minh bạch bằng Hash Commit
│   ├── prize_distributor.py       # Phân bổ ngân quỹ: 70% nuôi máy chủ, 30% tri ân
│   └── certificate_generator.py   # Sinh bằng khen SVG trúng thưởng tự động
├── synapses/                      # 💾 SỔ KẾ TOÁN & LỊCH SỬ KỲ QUAY
│   ├── .gitkeep
│   ├── active_tickets.json        # Danh sách vé hợp lệ trong kỳ quay hiện tại
│   ├── lottery_history.json       # Biên niên sử các kỳ quay (mã giải, ví trúng, hash chứng thực)
│   └── pool_accounting.json       # Sổ cái minh bạch tài chính 70/30
├── engine.py                      # Vi Nhân Quay Số (The Lottery Kernel)
├── Dockerfile                     # python:3.12-slim
└── .github/
    └── workflows/
        └── draw.yml               # Workflow định kỳ tự động quay số minh bạch

```
