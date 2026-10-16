import os
import sys
import json
import urllib.request

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lottery.ticket_harvester import TicketHarvester
from lottery.verifiable_random import VerifiableRandomEngine
from lottery.prize_distributor import PrizeDistributor
from lottery.certificate_generator import CertificateGenerator

HISTORY_FILE = "synapses/lottery_history.json"

class NexusLotteryKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-lottery")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.harvester = TicketHarvester(self.owner)

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f: return json.load(f)
            except Exception: pass
        return []

    def fetch_entropy_pulse(self):
        """Hút nhịp đập mật mã từ nexus-14 để làm hạt giống ngẫu nhiên khách quan"""
        url = f"https://raw.githubusercontent/{self.owner}/nexus-14/main/synapse_forward.json"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NexusLottery"})
            with urllib.request.urlopen(req, timeout=3.5) as resp:
                data = json.loads(resp.read().decode())
                return data.get("quantum_cid", "GENESIS_NEXUS_ENTROPY")
        except Exception:
            return "DEFAULT_COSMIC_ENTROPY_SEED"

    def run(self):
        print("=" * 80)
        print("🎟️ [NEXUS-LOTTERY] KHỞI ĐỘNG ĐỘNG CƠ QUAY SỐ NHÂN QUẢ & MINH BẠCH 70/30")
        print("⚖️ Quy Chế: 70% Nuôi máy chủ Nexus • 30% Tri ân Thí chủ cúng dường")
        print("=" * 80)

        history = self.load_history()
        current_round = len(history)

        # 1. Thu thập vé số từ nexus-forge
        tickets = self.harvester.harvest()

        # 2. Lấy hạt giống ngẫu nhiên khách quan
        entropy = self.fetch_entropy_pulse()

        # 3. Quay số ngẫu nhiên mật mã học
        winning_ticket, proof_hash, proof_meta = VerifiableRandomEngine.draw_winner(
            tickets, current_round, entropy
        )

        # 4. Phân bổ ngân quỹ 70/30
        accounting = PrizeDistributor.calculate_and_allocate(tickets, current_round, winning_ticket)
        reward_usd = accounting["allocations"]["patron_reward_30_percent"]["amount_usd"]
        funded_usd = accounting["allocations"]["ecosystem_sustenance_70_percent"]["amount_usd"]

        # 5. Sinh bằng khen SVG trúng giải
        CertificateGenerator.generate_svg(current_round, winning_ticket, reward_usd, proof_hash)

        # 6. Ghi nhận vào biên niên sử
        history_record = {
            "round_id": current_round,
            "timestamp": proof_meta.get("timestamp"),
            "winning_ticket": winning_ticket.get("ticket_id"),
            "patron_wallet": winning_ticket.get("patron_wallet"),
            "proof_hash": f"0x{proof_hash}",
            "reward_usd": reward_usd,
            "ecosystem_funded_usd": funded_usd,
            "verification_data": proof_meta
        }
        history.append(history_record)
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

        print("=" * 80)
        print(f"🎉 [KẾT QUẢ KỲ QUAY #{current_round}] Vé trúng giải: {winning_ticket.get('ticket_id')}")
        print(f"💎 Đã khóa ${funded_usd:.2f} USD vào quỹ nuôi máy chủ hệ sinh thái!")
        print("=" * 80)

if __name__ == "__main__":
    lottery = NexusLotteryKernel()
    lottery.run()
