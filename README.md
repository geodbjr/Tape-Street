Tape Street (v1.2.7-M)
Overview
Jokers High.exe is a hardware-bound cryptographic audit tool designed to demonstrate the "Scorched Earth" security philosophy. This utility is used to verify the integrity of the encrypted container: 20201017_213110.jpg.tsl.
Unlike traditional software that aims for efficiency, this protocol is intentionally expensive. It does not merely check a password; it initiates a physical handshake with your system's memory bus.

Technical Specifications
This build utilizes a strictly tuned implementation of the Argon2id algorithm. It is designed to be a "Memory-Hard" bottleneck.
    • The 50% RAM Wall: Upon initiation, the engine identifies your total physical RAM and claims 50% of your system capacity to execute the handshake.
    • Work Factor (Time Cost 12): The memory bus remains saturated for a sustained duration (~2-4 seconds), creating a physical "plateau" in system telemetry.
    • Parallelism (8): The engine saturates multi-core throughput to ensure the hardware, not just the software being tested.

The Challenge: Hardware Integrity Audit
The provided file 20201017_213110.jpg.tsl is a secured image vault. This application (Jokers High.exe) acts as the gatekeeper.
Note: The application is designed to perform the integrity handshake and report on hardware endurance. It will not "open" the file in a standard viewer; it is an Audit Tool meant to test if your machine can survive the cryptographic grind.
Ranking System:
As you perform handshakes, your Score will increase and your Rank will evolve based on your hardware's endurance:
    • NOVICE: 1-9 Attempts
    • GLADIATOR: 10-24 Attempts
    • TITAN: 25+ Attempts
The Reward: Every 5 successful handshakes grant you Sparkle Stars. These are visual indicators that your RAM has successfully traversed the "Scorched Earth" wall.

How to Run
    1. Place Jokers High.exe and 20201017_213110.jpg.tsl in the same folder.
    2. Launch the .exe.
    3. Enter a security key to initiate the handshake.
    4. Monitor your Task Manager: Watch your RAM usage spike as the 5.6GB (or 50% capacity) "Everest" plateau appears.
    5. Earn your Stars: Post a screenshot of your TITAN rank and your system load as proof of your rig's power.
