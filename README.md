Technical White Paper: Tape Street v1.2.7 (Home Edition)
Subject: High-Speed Consumer Grade Encryption & Hardware Locking
Release Date: April 2024 (Revised 2026)
Classification: Secure Home Deployment
1. Executive Summary
Tape Street v1.2.7 "Home" is engineered for the power user who requires a balance of extreme security and operational speed. By utilizing a modified ARX (Add-Rotate-XOR) cipher architecture and a custom 256-bit S-Box, v1.2.7 provides a hardened vault environment optimized for standard consumer hardware.
2. Cryptographic Core
    • Key Derivation: Argon2id (Memory-Hard Function).
        ◦ Parameters: 64MB RAM Cost, 3 Iterations.
        ◦ Purpose: Defeats GPU-accelerated brute-force attacks while maintaining sub-2-second unlock times.
    • The Cipher: 16-Round ARX-Substitution-Permutation Network (SPN).
    • Integrity: HMAC-SHA256 authenticated encryption ensures that any "bit-rot" or manual tampering with the vault results in an immediate lock-out to prevent corrupted data injection.
3. Security Shield (v1.2.8 Retrofit)
The 1.2.7 Home Edition now features the v1.2.8 Gatekeeper Module:
    • Hardware Binding: Mathematical coupling to the Motherboard UUID and CPU ID. The software is non-portable without an authorized .tsl license file.
    • Anti-Debugging: Active memory scanning for attached debuggers (IsDebuggerPresent) to prevent reverse engineering of the entropy pool.
