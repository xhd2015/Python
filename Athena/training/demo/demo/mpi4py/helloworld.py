#!/usr/bin/env python
"""
Parallel Hello World

To run this with multiple processes use the mpiexec command.
For example, this

$ mpiexec -n 4 python helloworld.py

will run the command with 4 processes.
"""

from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n" 
    % (rank, size, name))
