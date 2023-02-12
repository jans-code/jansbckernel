#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect

class jansbckernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'bc'
    language_version = '1.07.1'
    language_info = {
        'name': 'GNU bc',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "bc is ready to crunch some numbers..."

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if "quit" in code:
                solution = "(standard_in) 99: quit not allowed in bc kernel"
            else:
                bc_kernel = pexpect.spawn('bc -q -l')
                bc_kernel.sendline(code)
                bc_kernel.expect('\r\n')
                solution = bc_kernel.buffer.decode('ascii')
                if "\r" in solution:
                    solution = solution.split("\r")
                    solution = solution[-2]
                solution = solution.strip()
                if "." in solution:
                    if solution[0] == ".":
                        solution = "0" + solution
                    while solution[-1] == "0":
                        solution = solution[:-1]
                bc_kernel.close()
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }