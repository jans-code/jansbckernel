#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""bc kernel class module"""

import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

class jansbckernel(Kernel):
    """bc kernel uses ipykernel to run bc"""
    implementation = 'IPython'
    implementation_version = '8.12.0'
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
            if "read" in code:
                solution = "read is not allowed in bc kernel."
            else:
                workingdir = "/tmp/bckernel/"
                os.mkdir(workingdir)
                with open(workingdir + "calculation.txt", "w", encoding="UTF-8") as file:
                    file.write(code + "\nquit")
                solution = pexpect.run('bc -ql ' + workingdir + 'calculation.txt').decode('ascii')
                solution = solution.replace("\\", "")
                shutil.rmtree(workingdir)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)


        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
