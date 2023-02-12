#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansbckernel
IPKernelApp.launch_instance(kernel_class=jansbckernel)