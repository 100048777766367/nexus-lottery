import os
import json

POOL_ACCOUNTING_FILE = "synapses/pool_accounting.json"

class PrizeDistributor:
    """Phân bổ ngân quỹ theo quy chế chuẩn mực: 70% Nuôi máy chủ, 30% Thưởng tri ân"""
    @staticmethod
    def calculate_and_allocate(tickets, round_id, winning_ticket):
        total_pool_usd = sum(t.get("tier_price_usd", 0.20) for t in tickets)
        
        # Phân chia 70 / 30
        ecosystem_share_70 = round(total_pool_usd * 0.70, 4)
        patron_reward_30 = round(total_pool_usd * 0.30, 4)

        accounting = {
            "round_id": round_id,
            "total_patronage_usd": total_pool_usd,
            "allocations": {
                "ecosystem_sustenance_70_percent": {
                    "amount_usd": ecosystem_share_70,
                    "purpose": "Nuôi sống máy chủ GitHub Actions, lưu trữ IPFS và điện toán cho 11 tầng bản thể Nexus"
                },
                "patron_reward_30_percent": {
                    "amount_usd": patron_reward_30,
                    "recipient_ticket": winning_ticket.get("ticket_id"),
                    "recipient_wallet": winning_ticket.get("patron_wallet"),
                    "purpose": "Trao thưởng tri ân Thí chủ may mắn trúng giải nhân quả"
                }
            },
            "status": "Allocated_And_Locked"
        }

        os.makedirs("synapses", exist_ok=True)
        with open(POOL_ACCOUNTING_FILE, "w", encoding="utf-8") as f:
            json.dump(accounting, f, indent=4, ensure_ascii=False)

        print(f"💰 [PHÂN BỔ NGÂN QUỸ] Tổng: ${total_pool_usd:.2f} USD | Nuôi hệ thống (70%): ${ecosystem_share_70:.2f} | Giải thưởng (30%): ${patron_reward_30:.2f}")
        return accounting
