# CSRBOX
This repository contains the python scripts to generate RISC-V Assembly for Testing the BSV output of the CSRBOX, in the Chromite Core by [InCore Semiconductors](https://incoresemi.com/).

The CSRBOX (https://csrbox.readthedocs.io/en/latest/) is an external python tool which can generate a
bsv CSR module based on the specification provided. According to the RISC-V spec, the CSRs are divided
into 3 major categories based on the privilege modes supported: Machine, Supervisor and User

## File Structure
```
.
├── README.md -- Describes the idea behind each test and how the ASM is generated efficiently using Python 3.
├── uatg_csrbox_infocsr1.py -- Generates ASM to check the csrrw function in registers mvendorid, mempid, marchid, mhartid.
├── uatg_csrbox_infocsr2.py -- Generates ASM to check the csrrs function in registers mvendorid, mempid, marchid, mhartid.
├── uatg_csrbox_infocsr3.py -- Generates ASM to check the csrrc function in registers mvendorid, mempid, marchid, mhartid.
├── uatg_csrbox_minstret.py -- Generates ASM to check the minstret csr by performing sample operations.
├── uatg_csrbox_misam.py -- Generates ASM to checking misam csr by disabling the m field and performing some multiplication operations.
├── uatg_csrbox_misarv.py -- Generates ASM to check misarv csr by using its reset value as reference. 
```

## Code Description

#### uatg_csrbox_infocsr1.py
- here registers `mvendorid`, `mempid`, `marchid`, `mhartid` are considered.
- these are read only registers so we checking whether they violate the rule by changing their values.
- firstly x4 is set to 1s.
- the below steps occurs in a loop for all the given registers.
- then a random number is generated and assigned to x.
- then csr value is copied to x4 and x3 value is copied to csr using `csrrw`.
- later csr and x4 are checked, trap  is raised if they are equal.
- the trap address is stored in x31 register.

#### uatg_csrbox_infocsr2.py
- here registers `mvendorid`, `mempid`, `marchid`, `mhartid` are considered.
- these are read only registers so we checking whether they violate the rule by changing their values.
- firstly x4 is set to 1s.
- the below steps occurs in a loop for all the given registers.
- then a random number is generated and assigned to x.
- then csr value is copied to x4 and the high bits in x3 are also set high in csr using `csrrs`..
- later csr and x3 are checked, trap  is raised if there is a change in value of csr from the initial value.
- the trap address is stored in x31 register. 

#### uatg_csrbox_infocsr3.py
- here registers `mvendorid`, `mempid`, `marchid`, `mhartid` are considered.
- these are read only registers so we checking whether they violate the rule by changing their values.
- firstly x4 is set to 1s.
- the below steps occurs in a loop for all the given registers.
- then a random number is generated and assigned to x.
- then csr value is copied to x4 and the high bits in x3 are cleared in csr using `csrrc`.
- later csr and x3 are checked, trap  is raised if there is a change in value of csr from the initial value.
- the trap address is stored in x31 register. 

#### uatg_csrbox_minstret.py
- first the value of `minstret` is transfered to register x1.
- then we perform n sample operations.
- then later minstret register is checked if it is incremented by n if not trap is raised.
- the address of this trap is copied to x31 register.

#### uatg_csrbox_misam.py
- we generate two random numbers and assign it to x1 and x2 registers.
- later we disable the m field.
- then we perform some multiplication operations.
- the values are checked 
- 
#### uatg_csrbox_misarv.py
- the reset value of `misarv` is extracted from the isa_yaml file and is assigned to x4 register.
- `misarv` value is copied to x5 register.
- later the high bits of x5 are cleared in misa making it zero so we assign it to x0.
- then the register x4 and misa are compared and trap is raised if they are not equal.
- the trap is stored in the x31 register. 

## Contributors
Badrinath Gupta <<nerella.rabasa@gmail.com>>,
B A Manish Kumar <<manishk.2210.2000@gmail.com>>
