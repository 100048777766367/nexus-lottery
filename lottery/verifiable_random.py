import hashlib
import json
import time

class VerifiableRandomEngine:
    """Tạo số ngẫu nhiên minh bạch bằng hàm băm mật mã học SHAKE-256"""
    @staticmethod
    def draw_winner(tickets, round_id, entropy_source):
        if not tickets:
            return None, "NO_TICKETS", {}

        timestamp = int(time.time())
        # Hợp nhất entropy bất biến: Mã commit Git/CID + Vòng quay + Dấu thời gian
        seed_payload = f"ROUND_{round_id}_{timestamp}_{entropy_source}_{len(tickets)}".encode()
        
        # Tạo hàm băm chứng thực 64 ký tự hex
        proof_hash = hashlib.shake_256(seed_payload).hexdigest(32)
        
        # Chuyển đổi mã băm thành số nguyên lớn để chọn vị trí trúng thưởng
        hash_int = int(proof_hash, 16)
        winning_index = hash_int % len(tickets)
        winner_ticket = tickets[winning_index]

        proof_data = {
            "round_id": round_id,
            "timestamp": timestamp,
            "entropy_source": entropy_source,
            "proof_hash": f"0x{proof_hash}",
            "winning_index": winning_index,
            "total_pool_tickets": len(tickets),
            "mathematical_formula": f"int(proof_hash, 16) % {len(tickets)} == {winning_index}"
        }

        print(f"🎲 [QUAY SỐ MINH BẠCH] Hash: 0x{proof_hash[:16]}... ──► Chọn vé số vị trí #{winning_index}")
        return winner_ticket, proof_hash, proof_data
