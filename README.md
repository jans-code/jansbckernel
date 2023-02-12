# jansbckernel

![alt](jansbckernel/logo-svg.svg)

A very simple and dirty jupyter kernel for [GNU bc](https://www.gnu.org/software/bc/).

This was implemented with the IPython Kernel subclass and pexpect.
You can just do oneshot calculations with this kernel.
So far assigning variables or changing bc's settings is not supported.

## Installation

- install bc from you distro's package manager
- `pip install` jupyterlab and pexpect
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user jansbckernel`

## Uninstall

- `jupyter kernelspec uninstall jansbckernel`
- `pip uninstall jansbckernel`