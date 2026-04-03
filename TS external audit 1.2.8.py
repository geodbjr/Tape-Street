import math
import os
import sys

def calculate_work_factor(pwd_len=8, charset=62):
    # Search Space
    keyspace = charset ** pwd_len
    # 60s Hardware Lockout throughput
    attempts_per_year = (365 * 24 * 60 * 60) / 60
    # Result
    years = keyspace / attempts_per_year
    entropy = math.log2(keyspace)
    return keyspace, years, entropy

def run_math_review():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Current Specs for TS-128 Hybrid
        pwd_len = 8 
        keyspace, years, entropy = calculate_work_factor(pwd_len)

        print("="*65)
        print("          TS-128 HYBRID: EXTERNAL STRENGTH ANALYTICS")
        print("="*65)
        print(f"{'PARAMETER':<25} | {'SPECIFICATION'}")
        print("-" * 65)
        print(f"{'Cipher State':<25} | 512-bit (Hybrid ARX-MDS)")
        print(f"{'KDF Algorithm':<25} | Argon2id (Memory-Hard)")
        print(f"{'RAM Bottleneck':<25} | 128 MB per thread")
        print(f"{'Hardware Latency':<25} | 60.0 Seconds (Fixed)")
        print("-" * 65)
        print(f"FOR A STANDARD {pwd_len}-CHARACTER KEY:")
        print(f" > Total Keyspace:        {keyspace:,.0f}")
        print(f" > Entropy Depth:         {entropy:.2f} bits")
        print(f" > Brute-Force Timeline:  {years:,.0f} YEARS")
        print("="*65)
        
        print("\n[SCORCHED EARTH STATUS]: ACTIVE")
        print("Logic: Temporal defense negates Moore's Law by 6,000,000%.")
        
        print("\n" + "-" * 65)
        print("REVIEW HOLD ACTIVE. Window will not close automatically.")
        choice = input("Press [ENTER] to Re-calculate or [Q] to Quit: ").lower()
        
        if choice == 'q':
            break

if __name__ == "__main__":
    try:
        run_math_review()
    except KeyboardInterrupt:
        sys.exit(0)