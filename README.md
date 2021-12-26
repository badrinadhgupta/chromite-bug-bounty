# CSRBOX
This repository contains the python scripts to generate RISC-V Assembly for Testing the BSV output of the CSRBOX, in the Chromite Core by [InCore Semiconductors](https://incoresemi.com/).

The CSRBOX (https://csrbox.readthedocs.io/en/latest/) is an external python tool which can generate a
bsv CSR module based on the specification provided. According to the RISC-V spec, the CSRs are divided
into 3 major categories based on the privilege modes supported: Machine, Supervisor and User

## File Structure
```
.
├── README.md -- Describes the idea behind each test and how the ASM is generated efficiently using Python 3.
├── uatg_csrbox_infocsr1.py -- Generates ASM to 
├── uatg_csrbox_infocsr1.py -- Generates ASM to 
├── uatg_csrbox_infocsr1.py -- Generates ASM to 
├── uatg_csrbox_minstret.py -- Generates ASM to 
├── uatg_csrbox_misam.py -- Generates ASM to 
├── uatg_csrbox_misarv.py -- Generates ASM to 
```

## Code Description

#### CSRBOX_test01.py
- 
#### CSRBOX_test02.py
- 
#### CSRBOX_test03.py
-
#### uatg_csrbox_minstret.py
- first the value of 'minstret' is transfered to register x1.
- then later we perform n sample operations.
- then later minstret register is checked if it is incremented by n if not trap is raised.
- the address of this trap is copied to x31 register.

#### uatg_csrbox_misarv.py
- 


## Contributors
Badrinath Gupta <<nerella.rabasa@gmail.com>>,
B A Manish Kumar <<manishk.2210.2000@gmail.com>>
