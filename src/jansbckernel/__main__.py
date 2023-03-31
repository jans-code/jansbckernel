#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""bc kernel main"""

from ipykernel.kernelapp import IPKernelApp
from .kernel import jansbckernel
IPKernelApp.launch_instance(kernel_class=jansbckernel)
