# CSRBOX
This repository contains the python scripts to generate RISC-V Assembly for Testing the BSV output of the CSRBOX, in the Chromite Core by [InCore Semiconductors](https://incoresemi.com/).

The CSRBOX (https://csrbox.readthedocs.io/en/latest/) is an external python tool which can generate a
bsv CSR module based on the specification provided. According to the RISC-V spec, the CSRs are divided
into 3 major categories based on the privilege modes supported: Machine, Supervisor and User

## File Structure
```
.
├── README.md -- Describes the idea behind each test and how the ASM is generated efficiently using Python 3.
├── uatg_CSRBOX_test01.py -- Generates ASM to 
├── uatg_CSRBOX_test02.py -- Generates ASM to 
├── uatg_CSRBOX_test03.py -- Generates ASM to 
├── uatg_CSRBOX_test04.py -- Generates ASM to 
├── uatg_CSRBOX_test05.py -- Generates ASM to 
```

## Test Description
- 


## Code Description

#### CSRBOX_test01.py
- Perform a `fence` operation to clear out the data cache subsystem and the fill buffer. 
- Load some data into a temporary register and perform `numerous store operations` to fill up the cache.
- Each loop in ASM has an unconditional `jump` back to that label, a branch takes us out of the loop.
- Each iteration, we visit the next `set`.
- The total number of iterations is parameterized based on YAML input.
#### CSRBOX_test02.py
- Perform a `fence` operation to clear out the data cache subsystem and the fill buffer. 
- In each iteration, we visit the next way in the same set. Once all the ways in a set are touched, we visit the next set.
- The total number of iterations is parameterized based on YAML input.
#### CSRBOX_test03.py
- Perform a `fence` operation to clear out the data cache subsystem and the fill buffer. 
- Perform `numerous load operations` to fill up the cache
- In each iteration, we visit the next way in the same set. Once all the ways in a set are touched, we visit the next set.
- The total number of iterations is parameterized based on YAML input.
#### CSRBOX_test04.py
- Perform a `fence` operation to clear out the data cache subsystem and the fill buffer. 
- Load some data into a temporary register and perform `numerous load operations` to fill up the cache.
- Each loop in ASM has an unconditional `jump` back to that label, a branch takes us out of the loop.
- Each iteration, we visit the next `set`.
- The total number of iterations is parameterized based on YAML input.
#### CSRBOX_test05.py
- Perform a `fence` operation to clear out the data cache subsystem and the fill buffer.
- Load some data into a temporary register and perform `numerous store operations` to fill up the cache.
- Each loop in ASM has an unconditional `jump` back to that label, a branch takes us out of the loop.
- Each iteration, we visit the next `set`.
- The total number of iterations is parameterized based on YAML input.
- Once the cache is full, we perform numerous `consecutive store operations`.
- The number of iterations is parameterized based on the YAML input such that the fill_buffer is completely full.
- Post filling the caches, we perform a series of `nop` instructions to ensure that the fill buffer is empty.


## Contributors
Badrinath Gupta << >>,
B A Manish Kumar <<manishk.2210.2000@gmail.com>>
