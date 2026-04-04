Tape Street v1.2.8 | Deployment Manifest
Hardware-Aware ARX Encapsulation Suite
Tape Street v1.2.8 is a specialized encryption bridge designed for high-stakes data isolation. Unlike conventional tools, v1.2.8 treats the host's physical state (Power, CPU, and Memory) as an active component of the cryptographic boundary.

The "Super Sauce" (Core Logic)
    • Adaptive Power Scaling: The engine queries psutil to determine the machine's power state.
        ◦ High-Performance Mode (AC): Unlocks maximum CPU parallelism for rapid Argon2id key derivation.
        ◦ Efficiency Mode (Battery): Constrains threading to 2 cores to prevent thermal detection and maintain stealth.
    • Protocol Sigma (Anti-Debug): Direct ctypes hooks into kernel32.dll. If an external debugger (like x64dbg or Ghidra) is detected, the bridge executes an immediate Memory Purge and shuts down.
    • The Argon2 Anchor: Utilizes a fixed 128MB RAM allocation during the "Burning" process, creating a heavy computational footprint that renders standard brute-force attacks economically unfeasible.
    • Dynamic S-Box: Features a Fisher-Yates shuffled S-Box generated uniquely per session via a SHA-512 entropy pool. No two encryption sessions share the same substitution path.


Component	Specification
Engine	256-bit ARX (Addition-Rotation-XOR)
KDF	Argon2id (128MB / 4 Iterations)
Diffusion	8-column MDS Matrix (GF256)
Integrity	HMAC-SHA256 (32-byte Tail)
Lockout	60-Second Hardware Cooldown


Operational Instructions
1. The Security Scan
Upon launch, the bridge performs a stealth scan. If the system was recently tampered with or an incorrect key was entered, a .ts_secure_lock will trigger a 60-second hardware lockout.
2. Vault Ignition (🔒 SECURE DATA)
    1. Input your Master Security Key.
    2. Select the target file via the "Secure Data" vector.
    3. The status will shift to "🔥 BURNING..." as the ARX engine encapsulates the data into a .tsl fragment.
3. Recovery (🔓 RECOVER DATA)
    1. Input the exact Master Security Key.
    2. Select the .tsl fragment.
    3. Warning: v1.2.8 operates on a "One-Strike" policy. If the HMAC signature fails to match, the system locks the hardware and terminates immediately.

⚠️ Tactical Warnings
    • Zero-Recovery: There are no "Forgot Password" or "Backdoor" protocols. Data lost to entropy cannot be recovered.
    • Integrity Trap: Any modification to the encrypted .tsl file (even 1 bit of change) will trigger a Critical Failure during recovery.
    • Standalone Execution: For maximum stability, always run the binary as a standalone process. Running within an IDE may trigger Protocol Sigma and purge the memory.

📜 Authorization
Proprietary Build. Access restricted. Any attempt to reverse-engineer the MDS matrix or ARX rotation constants is a breach of the Rules of Main.
"Respect the entropy, or be consumed by it." — The Architect
