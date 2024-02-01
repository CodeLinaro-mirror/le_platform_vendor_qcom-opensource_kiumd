#!/bin/sh
# Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

ip link set dev vmtap0 master br0
ifconfig vmtap0 0.0.0.0
