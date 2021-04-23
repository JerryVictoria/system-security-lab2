#!/usr/bin/env python3

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    pass

if len(sys.argv) != 2:
    print(sys.argv[0], "too few args")

s = AuthRpcServer()
s.run_fork(sys.argv[1])


