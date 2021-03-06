from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any
from random import randint
import random


class uatg_csrbox_infocsr2(IPlugin):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, core_yaml, isa_yaml) -> bool:
    	
        return 
        
    def generate_asm(self) -> Dict[str, str]:
	
        csr = ['mvendorid', 'mempid', 'marchid', 'mhartid'] 
        asm = '\tli x4, 0xffffffff\n'
        for j in range(0, len(csr)):
          for i in range(0,200):
            x = random.randrange(0,2**32)
            asm += f'\tli x3, {hex(x)}\n\tcsrr x2, {csr[j]}\n\tcsrrs x4, {csr[j]}, x3\n\tbne x2, {csr[j]}, trap\n'
	    asm += f'\tcsrrsi x4, {csr[j]}, {hex(x)}\n\tbne x2, {csr[j]}, trap\n'
        asm += 'trap:\n\taddi x31, x3, 0\n'

        compile_macros = []

        return [{
            'asm_code': asm,
            'asm_sig': '',
            'compile_macros': compile_macros
        }]

    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv
