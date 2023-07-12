/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Copyright (c) 2016-2017, The Linux Foundation. All rights reserved.
 * Copyright (c) 2018, Craig Tatlor.
 */

#ifndef _DT_BINDINGS_CLK_MSM_GCC_660_H
#define _DT_BINDINGS_CLK_MSM_GCC_660_H

#define BLSP1_QUP1_I2C_APPS_CLK_SRC		0
#define BLSP1_QUP1_SPI_APPS_CLK_SRC		1
#define BLSP1_QUP2_I2C_APPS_CLK_SRC		2
#define BLSP1_QUP2_SPI_APPS_CLK_SRC		3
#define BLSP1_QUP3_I2C_APPS_CLK_SRC		4
#define BLSP1_QUP3_SPI_APPS_CLK_SRC		5
#define BLSP1_QUP4_I2C_APPS_CLK_SRC		6
#define BLSP1_QUP4_SPI_APPS_CLK_SRC		7
#define BLSP1_UART1_APPS_CLK_SRC		8
#define BLSP1_UART2_APPS_CLK_SRC		9
#define BLSP2_QUP1_I2C_APPS_CLK_SRC		10
#define BLSP2_QUP1_SPI_APPS_CLK_SRC		11
#define BLSP2_QUP2_I2C_APPS_CLK_SRC		12
#define BLSP2_QUP2_SPI_APPS_CLK_SRC		13
#define BLSP2_QUP3_I2C_APPS_CLK_SRC		14
#define BLSP2_QUP3_SPI_APPS_CLK_SRC		15
#define BLSP2_QUP4_I2C_APPS_CLK_SRC		16
#define BLSP2_QUP4_SPI_APPS_CLK_SRC		17
#define BLSP2_UART1_APPS_CLK_SRC		18
#define BLSP2_UART2_APPS_CLK_SRC		19
#define GCC_AGGRE2_UFS_AXI_CLK			20
#define GCC_AGGRE2_USB3_AXI_CLK			21
#define GCC_BIMC_GFX_CLK			22
#define GCC_BIMC_HMSS_AXI_CLK			23
#define GCC_BIMC_MSS_Q6_AXI_CLK			24
#define GCC_BLSP1_AHB_CLK			25
#define GCC_BLSP1_QUP1_I2C_APPS_CLK		26
#define GCC_BLSP1_QUP1_SPI_APPS_CLK		27
#define GCC_BLSP1_QUP2_I2C_APPS_CLK		28
#define GCC_BLSP1_QUP2_SPI_APPS_CLK		29
#define GCC_BLSP1_QUP3_I2C_APPS_CLK		30
#define GCC_BLSP1_QUP3_SPI_APPS_CLK		31
#define GCC_BLSP1_QUP4_I2C_APPS_CLK		32
#define GCC_BLSP1_QUP4_SPI_APPS_CLK		33
#define GCC_BLSP1_UART1_APPS_CLK		34
#define GCC_BLSP1_UART2_APPS_CLK		35
#define GCC_BLSP2_AHB_CLK			36
#define GCC_BLSP2_QUP1_I2C_APPS_CLK		37
#define GCC_BLSP2_QUP1_SPI_APPS_CLK		38
#define GCC_BLSP2_QUP2_I2C_APPS_CLK		39
#define GCC_BLSP2_QUP2_SPI_APPS_CLK		40
#define GCC_BLSP2_QUP3_I2C_APPS_CLK		41
#define GCC_BLSP2_QUP3_SPI_APPS_CLK		42
#define GCC_BLSP2_QUP4_I2C_APPS_CLK		43
#define GCC_BLSP2_QUP4_SPI_APPS_CLK		44
#define GCC_BLSP2_UART1_APPS_CLK		45
#define GCC_BLSP2_UART2_APPS_CLK		46
#define GCC_BOOT_ROM_AHB_CLK			47
#define GCC_CFG_NOC_USB2_AXI_CLK		48
#define GCC_CFG_NOC_USB3_AXI_CLK		49
#define GCC_DCC_AHB_CLK				50
#define GCC_GP1_CLK				51
#define GCC_GP2_CLK				52
#define GCC_GP3_CLK				53
#define GCC_GPU_BIMC_GFX_CLK			54
#define GCC_GPU_CFG_AHB_CLK			55
#define GCC_GPU_GPLL0_CLK			56
#define GCC_GPU_GPLL0_DIV_CLK			57
#define GCC_HMSS_DVM_BUS_CLK			58
#define GCC_HMSS_RBCPR_CLK			59
#define GCC_MMSS_GPLL0_CLK			60
#define GCC_MMSS_GPLL0_DIV_CLK			61
#define GCC_MMSS_NOC_CFG_AHB_CLK		62
#define GCC_MMSS_SYS_NOC_AXI_CLK		63
#define GCC_MSS_CFG_AHB_CLK			64
#define GCC_MSS_GPLL0_DIV_CLK			65
#define GCC_MSS_MNOC_BIMC_AXI_CLK		66
#define GCC_MSS_Q6_BIMC_AXI_CLK			67
#define GCC_MSS_SNOC_AXI_CLK			68
#define GCC_PDM2_CLK				69
#define GCC_PDM_AHB_CLK				70
#define GCC_PRNG_AHB_CLK			71
#define GCC_QSPI_AHB_CLK			72
#define GCC_QSPI_SER_CLK			73
#define GCC_SDCC1_AHB_CLK			74
#define GCC_SDCC1_APPS_CLK			75
#define GCC_SDCC1_ICE_CORE_CLK			76
#define GCC_SDCC2_AHB_CLK			77
#define GCC_SDCC2_APPS_CLK			78
#define GCC_UFS_AHB_CLK				79
#define GCC_UFS_AXI_CLK				80
#define GCC_UFS_CLKREF_CLK			81
#define GCC_UFS_ICE_CORE_CLK			82
#define GCC_UFS_PHY_AUX_CLK			83
#define GCC_UFS_RX_SYMBOL_0_CLK			84
#define GCC_UFS_RX_SYMBOL_1_CLK			85
#define GCC_UFS_TX_SYMBOL_0_CLK			86
#define GCC_UFS_UNIPRO_CORE_CLK			87
#define GCC_USB20_MASTER_CLK			88
#define GCC_USB20_MOCK_UTMI_CLK			89
#define GCC_USB20_SLEEP_CLK			90
#define GCC_USB30_MASTER_CLK			91
#define GCC_USB30_MOCK_UTMI_CLK			92
#define GCC_USB30_SLEEP_CLK			93
#define GCC_USB3_CLKREF_CLK			94
#define GCC_USB3_PHY_AUX_CLK			95
#define GCC_USB3_PHY_PIPE_CLK			96
#define GCC_USB_PHY_CFG_AHB2PHY_CLK		97
#define GP1_CLK_SRC				98
#define GP2_CLK_SRC				99
#define GP3_CLK_SRC				100
#define GPLL0					101
#define GPLL0_EARLY				102
#define GPLL1					103
#define GPLL1_EARLY				104
#define GPLL4					105
#define GPLL4_EARLY				106
#define HMSS_GPLL0_CLK_SRC			107
#define HMSS_GPLL4_CLK_SRC			108
#define HMSS_RBCPR_CLK_SRC			109
#define PDM2_CLK_SRC				110
#define QSPI_SER_CLK_SRC			111
#define SDCC1_APPS_CLK_SRC			112
#define SDCC1_ICE_CORE_CLK_SRC			113
#define SDCC2_APPS_CLK_SRC			114
#define UFS_AXI_CLK_SRC				115
#define UFS_ICE_CORE_CLK_SRC			116
#define UFS_PHY_AUX_CLK_SRC			117
#define UFS_UNIPRO_CORE_CLK_SRC			118
#define USB20_MASTER_CLK_SRC			119
#define USB20_MOCK_UTMI_CLK_SRC			120
#define USB30_MASTER_CLK_SRC			121
#define USB30_MOCK_UTMI_CLK_SRC			122
#define USB3_PHY_AUX_CLK_SRC			123
#define GPLL0_OUT_MSSCC				124
#define GCC_UFS_AXI_HW_CTL_CLK			125
#define GCC_UFS_ICE_CORE_HW_CTL_CLK		126
#define GCC_UFS_PHY_AUX_HW_CTL_CLK		127
#define GCC_UFS_UNIPRO_CORE_HW_CTL_CLK		128
#define GCC_RX0_USB2_CLKREF_CLK			129
#define GCC_RX1_USB2_CLKREF_CLK			130

#define PCIE_0_GDSC	0
#define UFS_GDSC	1
#define USB_30_GDSC	2

#define GCC_QUSB2PHY_PRIM_BCR		0
#define GCC_QUSB2PHY_SEC_BCR		1
#define GCC_UFS_BCR			2
#define GCC_USB3_DP_PHY_BCR		3
#define GCC_USB3_PHY_BCR		4
#define GCC_USB3PHY_PHY_BCR		5
#define GCC_USB_20_BCR                  6
#define GCC_USB_30_BCR			7
#define GCC_USB_PHY_CFG_AHB2PHY_BCR	8
#define GCC_MSS_RESTART			9

#endif
