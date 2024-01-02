#!/bin/sh
# Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

ip link add name br0 type bridge
ip link set br0 up
ip link set dev eth0 master br0
ip link set dev vmtap0 master br0
ip addr add 192.168.1.1/24 dev br0
ifconfig vmtap0 0.0.0.0
ifconfig eth0 0.0.0.0
