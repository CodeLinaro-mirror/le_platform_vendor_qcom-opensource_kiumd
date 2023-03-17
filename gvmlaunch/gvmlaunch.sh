#!/bin/bash
# Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

modprobe qcom_q6v5_pas
modprobe gunyah
modprobe gh_ctrl
insmod /lib/modules/5.14.0-999.124ES.test.el9.aarch64/kernel/drivers/tty/hvc/hvc_gunyah.ko.xz
modprobe vhost_net

RUST_BACKTRACE=full qcrosvm --vm=autoghgvm --disk=/dev/sda11,label=17,rw=true --disk=/dev/sda13,label=16,rw=true --disk=/dev/sda12,label=15,rw=true --disk=/dev/sda14,label=11,rw=true --disk=/dev/sda10,label=10,rw=true --net label=13 --ip_addr=192.168.1.13 --netmask=255.255.255.0 --mac=5A:6F:F0:05:7C:24 &
