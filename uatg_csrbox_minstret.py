from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, mext_instructions
from uatg.utils import rvtest_data
from typing import Dict, Any
from random import randint
import random


class uatg_csrbox_minstret(IPlugin):

    def __init__(self) -> None:
        super().__init__()

    def execute(self, core_yaml, isa_yaml) -> bool:
    	self.hart0 = isa_yaml['hart0']
    	self.misa = hart0['misa']
    	self.rv = misa['reset-val']
        return 
        
    def generate_asm(self) -> Dict[str, str]:
	
        for i in range(0,200):
          x = random.randrange(0,800)
          asm += '\taddi x1, minstret, 0\n'
          for j in range(x):
            asm += '\taddi x2, x2, 1\n'
          asm += '\taddi x1, x1, n\n'
          asm += '\tbne x1, minstret, trap\n'
        asm += 'trap:\n\taddi x31, x1,0\n'

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
