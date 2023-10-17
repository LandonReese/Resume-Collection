Welcome to the MIPS Simulator project! This README provides essential information on how to build and use the simulator, as well as details about its architecture and the statistics it reports.

Running the Simulator
To run the simulator, follow these simple steps:

1. Build the Simulator: Use the following command to build the simulator:

'make simulator'


2. Execute the Simulator: Once the simulator is built, execute it with a MIPS assembly file as an argument. Replace [mips file] with the name of your MIPS assembly file:

'simulator [mips file]'


Simulator Architecture
The MIPS simulator is designed with a pipelined architecture, featuring the following pipeline stages:

IF1 (Instruction Fetch 1)
IF2 (Instruction Fetch 2)
ID (Instruction Decode)
EXE1 (Execution 1)
EXE2 (Execution 2)
MEM1 (Memory 1)
MEM2 (Memory 2)
WB (Write-Back)
Key architectural features include:

Branch Handling: Branch instructions are resolved in the ID stage, with no branch delay. This means that branches do not introduce additional clock cycles.

Load Delay: There is no load delay slot. Instructions that read a register written by an immediately-preceding load receive the loaded value without delay.

No Structural Hazards: The architecture eliminates structural hazards, ensuring efficient execution.

Data Forwarding: The simulator provides full data forwarding, minimizing the need for bubbles. Bubbles are only inserted for data hazards that cannot be resolved by data forwarding. Static scoreboarding is used to detect hazards and insert the appropriate number of bubbles.

Memory Hierarchy
The simulator also models pipeline stalls caused by memory latency in a Level 1 (L1) data cache. Key characteristics of the data cache include:

- Cache Size: The simulated data cache stores 1 KiB (1024 bytes) of data in block sizes of 8 words (32 bytes).
- Associativity: It is 4-way set associative, utilizing a round-robin replacement policy.
- Write Policy: The cache uses a write-back write-allocate policy.
- Write Buffer: Notably, the cache does not employ a write buffer, meaning that a store operation must complete before the processor can proceed.
- Instruction Fetch: Instruction fetches are assumed to hit in a perfect instruction cache (I-cache) with immediate access. Therefore, there are no stalls for instruction fetches.

Reporting Statistics
At the end of the program execution, the simulator provides the following statistics:

- Clock Cycles: The exact number of clock cycles required to execute the program on this CPU.
- CPI (Cycle per Instruction): The cycle count divided by the instruction count, giving insights into the efficiency of the CPU.
- Bubble Cycles: The number of cycles injected due to data dependencies.
- Flush Cycles: The number of cycles required in the shadows of jumps and taken branches.
- Stall Cycles: The number of cycles stalled due to cache and memory latency.
- Accesses: The total number of memory accesses, distinguishing between loads and stores.
- Misses: The total number of cache misses, including those caused by loads and stores.
- Writebacks: The number of writebacks to the cache.
- Hit Ratio: The ratio of cache hits to the total memory accesses, providing insights into cache efficiency.