import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Load_data import Data_from_nc

def set_plot_param():
    """Set my own customized plotting parameters"""

    mpl.rc('axes', edgecolor='dimgrey')
    mpl.rc('axes', labelcolor='dimgrey')
    mpl.rc('xtick', color='dimgrey')
    mpl.rc('ytick', color='dimgrey')
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

def plot_without_obs(ax1, x, x1, x2, v_IRR_NOI, v_IRR_CTL, v_QIRR_IRR, v_QIRR_CTL, label_IRR_NOI, label_IRR_CTL, label_QIRR_IRR,
                     label_QIRR_CTL, legloc_DIFF, legloc_QIRR, ylabel_DIFF, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    set_plot_param()
    plt.plot(x, v_IRR_NOI, 'green', marker='v', label=label_IRR_NOI,
             linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR_CTL, 'blue', marker='>', label=label_IRR_CTL,
             linewidth=0.8, markersize=5, alpha=0.5)
    plt.legend(loc=legloc_DIFF, frameon=False, fontsize=10)
    plt.ylabel(ylabel_DIFF, fontsize=10)
    plt.xticks(xtick_value,
               xtick_month,
               )
    plt.tick_params(labelsize=10)
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.3, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.3, label=label_QIRR_CTL)
    plt.legend(loc=legloc_QIRR, frameon=False, fontsize=10)
    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')


def plot_with_obs(ax1, x, x1, x2, v_OBS, v_NOI, v_CTL, v_IRR, v_QIRR_IRR, v_QIRR_CTL, label_OBS, label_NOI, label_CTL, label_IRR,
                  label_QIRR_IRR, label_QIRR_CTL,legloc_VAR, legloc_QIRR, ylabel_VAR, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    plt.plot(x, v_OBS, 'black', marker='o', label=label_OBS, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_NOI, 'red', marker='v', label=label_NOI, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_CTL, 'blue', marker='>', label=label_CTL, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR, 'green', marker='^', label=label_IRR, linewidth=0.8, markersize=5, alpha=0.5)
    plt.ylabel(ylabel_VAR, fontsize=10)
    # plt.xlabel('month')
    plt.xticks(xtick_value,
               xtick_month,
               )
    plt.legend(loc=legloc_VAR, frameon=False, fontsize=10)
    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.2, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.2, label=label_QIRR_CTL)
    plt.legend(loc=legloc_QIRR, frameon=False, fontsize=10)
    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')

def plot_with_obs_without(ax1, x, x1, x2, v_NOI, v_CTL, v_IRR, v_QIRR_IRR, v_QIRR_CTL, label_NOI, label_CTL, label_IRR,
                  label_QIRR_IRR, label_QIRR_CTL,legloc_VAR, legloc_QIRR, ylabel_VAR, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    plt.plot(x, v_NOI, 'red', marker='v', label=label_NOI, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_CTL, 'blue', marker='>', label=label_CTL, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR, 'green', marker='^', label=label_IRR, linewidth=0.8, markersize=5, alpha=0.5)
    plt.ylabel(ylabel_VAR, fontsize=10)
    # plt.xlabel('month')
    plt.xticks(xtick_value,
               xtick_month,
               )
    plt.legend(loc=legloc_VAR, frameon=False, fontsize=10)
    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.2, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.2, label=label_QIRR_CTL)
    plt.legend(loc=legloc_QIRR, frameon=False, fontsize=10)
    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')

def plot_without_obs_nolegend(ax1, x, x1, x2, v_IRR_NOI, v_IRR_CTL, v_QIRR_IRR, v_QIRR_CTL, label_IRR_NOI, label_IRR_CTL, label_QIRR_IRR,
                     label_QIRR_CTL, legloc_DIFF, legloc_QIRR, ylabel_DIFF, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    set_plot_param()
    plt.plot(x, v_IRR_NOI, 'green', marker='v', label=label_IRR_NOI,
             linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR_CTL, 'blue', marker='>', label=label_IRR_CTL,
             linewidth=0.8, markersize=5, alpha=0.5)

    plt.ylabel(ylabel_DIFF, fontsize=10)
    plt.xticks(xtick_value,
               xtick_month,
               )
    plt.tick_params(labelsize=10)
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.3, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.3, label=label_QIRR_CTL)

    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')


def plot_with_obs_nolegend(ax1, x, x1, x2, v_OBS, v_NOI, v_CTL, v_IRR, v_QIRR_IRR, v_QIRR_CTL, label_OBS, label_NOI, label_CTL, label_IRR,
                  label_QIRR_IRR, label_QIRR_CTL,legloc_VAR, legloc_QIRR, ylabel_VAR, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    plt.plot(x, v_OBS, 'black', marker='o', label=label_OBS, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_NOI, 'red', marker='v', label=label_NOI, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_CTL, 'blue', marker='>', label=label_CTL, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR, 'green', marker='^', label=label_IRR, linewidth=0.8, markersize=5, alpha=0.5)
    plt.ylabel(ylabel_VAR, fontsize=10)
    # plt.xlabel('month')
    plt.xticks(xtick_value,
               xtick_month,
               )

    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.2, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.2, label=label_QIRR_CTL)

    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')

def plot_with_obs_without_nolegend(ax1, x, x1, x2, v_NOI, v_CTL, v_IRR, v_QIRR_IRR, v_QIRR_CTL, label_NOI, label_CTL, label_IRR,
                  label_QIRR_IRR, label_QIRR_CTL,legloc_VAR, legloc_QIRR, ylabel_VAR, ylabel_QIRR, xtick_value, xtick_month, title, num, site):
    plt.plot(x, v_NOI, 'red', marker='v', label=label_NOI, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_CTL, 'blue', marker='>', label=label_CTL, linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, v_IRR, 'green', marker='^', label=label_IRR, linewidth=0.8, markersize=5, alpha=0.5)
    plt.ylabel(ylabel_VAR, fontsize=10)
    # plt.xlabel('month')
    plt.xticks(xtick_value,
               xtick_month,
               )

    plt.tick_params(labelsize=10)
    plt.title(title, loc='right')
    plt.title(site, loc='left')
    ax2 = ax1.twinx()
    plt.bar(x1, v_QIRR_IRR, width=0.3, color='green', alpha=0.2, label=label_QIRR_IRR)
    plt.bar(x2, v_QIRR_CTL, width=0.3, color='blue', alpha=0.2, label=label_QIRR_CTL)

    plt.ylabel(ylabel_QIRR, fontsize=10)
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')

str_infile_cas = 'D:\Forcing_tower\Castellaro\\test.csv'
pd_reader_cas = pd.read_csv(str_infile_cas, header=None)
data_forc_cas = np.array(pd_reader_cas)
le_cas = data_forc_cas[:, 0]
hs_cas = data_forc_cas[:, 1]
sm_cas = data_forc_cas[:, 2]/100
lw_cas = data_forc_cas[:, 3]
sw_cas = data_forc_cas[:, 4]

le_month_cas = np.zeros(12)
hs_month_cas = np.zeros(12)
sm_month_cas = np.zeros(12)
lw_month_cas = np.zeros(12)
sw_month_cas = np.zeros(12)

num_le_cas = np.zeros(12)
num_hs_cas = np.zeros(12)
num_sm_cas = np.zeros(12)
num_lw_cas = np.zeros(12)
num_sw_cas = np.zeros(12)

data_CTL_cas = Data_from_nc('E:\Single_point\\Castellaro_drip_SpGs_QIRRIG')
QIRRIG_CTL_cas = data_CTL_cas.load_variable('QIRRIG_FROM_SURFACE')
data_IRR_cas = Data_from_nc('E:\Single_point\\Castellaro_flood_SpGs_QIRRIG')
QIRRIG_IRR_cas = data_IRR_cas.load_variable('QIRRIG_FROM_SURFACE')

QIRRIG_CTL_month_cas = np.zeros(12)
QIRRIG_IRR_month_cas = np.zeros(12)


data_NOI_cas = Data_from_nc('E:\Single_point\\Castellaro_noirr_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_NOI_cas = data_NOI_cas.load_variable('EFLX_LH_TOT')
data_CTL_cas = Data_from_nc('E:\Single_point\\Castellaro_drip_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_CTL_cas = data_CTL_cas.load_variable('EFLX_LH_TOT')
data_IRR_cas = Data_from_nc('E:\Single_point\\Castellaro_flood_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_IRR_cas = data_IRR_cas.load_variable('EFLX_LH_TOT')

EFLX_LH_TOT_NOI_month_cas = np.zeros(12)
EFLX_LH_TOT_CTL_month_cas = np.zeros(12)
EFLX_LH_TOT_IRR_month_cas = np.zeros(12)

data_NOI_cas = Data_from_nc('E:\Single_point\\Castellaro_noirr_SpGs_QSOIL_monmean')
FSH_NOI_cas = data_NOI_cas.load_variable('QSOIL')
data_CTL_cas = Data_from_nc('E:\Single_point\\Castellaro_drip_SpGs_QSOIL_monmean')
FSH_CTL_cas = data_CTL_cas.load_variable('QSOIL')
data_IRR_cas = Data_from_nc('E:\Single_point\\Castellaro_flood_SpGs_QSOIL_monmean')
FSH_IRR_cas = data_IRR_cas.load_variable('QSOIL')

FSH_NOI_month_cas = np.zeros(12)
FSH_CTL_month_cas = np.zeros(12)
FSH_IRR_month_cas = np.zeros(12)

data_NOI_cas = Data_from_nc('E:\Single_point\\Castellaro_noirr_SpGs_QVEGE_monmean')
LWup_NOI_cas = data_NOI_cas.load_variable('QVEGE')
data_CTL_cas = Data_from_nc('E:\Single_point\\Castellaro_drip_SpGs_QVEGE_monmean')
LWup_CTL_cas = data_CTL_cas.load_variable('QVEGE')
data_IRR_cas = Data_from_nc('E:\Single_point\\Castellaro_flood_SpGs_QVEGE_monmean')
LWup_IRR_cas = data_IRR_cas.load_variable('QVEGE')

LWup_NOI_month_cas = np.zeros(12)
LWup_CTL_month_cas = np.zeros(12)
LWup_IRR_month_cas = np.zeros(12)

data_NOI_cas = Data_from_nc('E:\Single_point\\Castellaro_noirr_SpGs_QVEGT_monmean')
SWup_NOI_cas = data_NOI_cas.load_variable('QVEGT')
data_CTL_cas = Data_from_nc('E:\Single_point\\Castellaro_drip_SpGs_QVEGT_monmean')
SWup_CTL_cas = data_CTL_cas.load_variable('QVEGT')
data_IRR_cas = Data_from_nc('E:\Single_point\\Castellaro_flood_SpGs_QVEGT_monmean')
SWup_IRR_cas = data_IRR_cas.load_variable('QVEGT')

SWup_NOI_month_cas = np.zeros(12)
SWup_CTL_month_cas = np.zeros(12)
SWup_IRR_month_cas = np.zeros(12)


for year in range(2):
    for month in range(12):
        #if le_cas[12*year + month] > -90:
        le_month_cas[month] = le_month_cas[month] + le_cas[12*year + month]
        EFLX_LH_TOT_NOI_month_cas[month] = EFLX_LH_TOT_NOI_month_cas[month] + EFLX_LH_TOT_NOI_cas[12 * year + month]
        EFLX_LH_TOT_CTL_month_cas[month] = EFLX_LH_TOT_CTL_month_cas[month] + EFLX_LH_TOT_CTL_cas[12 * year + month]
        EFLX_LH_TOT_IRR_month_cas[month] = EFLX_LH_TOT_IRR_month_cas[month] + EFLX_LH_TOT_IRR_cas[12 * year + month]

        QIRRIG_CTL_month_cas[month] = QIRRIG_CTL_month_cas[month] + QIRRIG_CTL_cas[12 * year + month]
        QIRRIG_IRR_month_cas[month] = QIRRIG_IRR_month_cas[month] + QIRRIG_IRR_cas[12 * year + month]
        num_le_cas[month] = num_le_cas[month] + 1

        hs_month_cas[month] = hs_month_cas[month] + hs_cas[12*year + month]
        FSH_NOI_month_cas[month] = FSH_NOI_month_cas[month] + FSH_NOI_cas[12 * year + month]
        FSH_CTL_month_cas[month] = FSH_CTL_month_cas[month] + FSH_CTL_cas[12 * year + month]
        FSH_IRR_month_cas[month] = FSH_IRR_month_cas[month] + FSH_IRR_cas[12 * year + month]
        num_hs_cas[month] = num_hs_cas[month] + 1

        lw_month_cas[month] = lw_month_cas[month] + lw_cas[12*year + month]
        LWup_NOI_month_cas[month] = LWup_NOI_month_cas[month] + LWup_NOI_cas[12 * year + month]
        LWup_CTL_month_cas[month] = LWup_CTL_month_cas[month] + LWup_CTL_cas[12 * year + month]
        LWup_IRR_month_cas[month] = LWup_IRR_month_cas[month] + LWup_IRR_cas[12 * year + month]
        num_lw_cas[month] = num_lw_cas[month] + 1

        sw_month_cas[month] = sw_month_cas[month] + sw_cas[12*year + month]
        SWup_NOI_month_cas[month] = SWup_NOI_month_cas[month] + SWup_NOI_cas[12 * year + month]
        SWup_CTL_month_cas[month] = SWup_CTL_month_cas[month] + SWup_CTL_cas[12 * year + month]
        SWup_IRR_month_cas[month] = SWup_IRR_month_cas[month] + SWup_IRR_cas[12 * year + month]
        num_sw_cas[month] = num_sw_cas[month] + 1

le_month_cas = le_month_cas / num_le_cas
EFLX_LH_TOT_NOI_month_cas = EFLX_LH_TOT_NOI_month_cas / num_le_cas
EFLX_LH_TOT_CTL_month_cas = EFLX_LH_TOT_CTL_month_cas / num_le_cas
EFLX_LH_TOT_IRR_month_cas = EFLX_LH_TOT_IRR_month_cas / num_le_cas

QIRRIG_CTL_month_cas = QIRRIG_CTL_month_cas / num_le_cas
QIRRIG_IRR_month_cas = QIRRIG_IRR_month_cas / num_le_cas

FSH_NOI_month_cas = FSH_NOI_month_cas / num_le_cas * 28.94 * 86400
FSH_CTL_month_cas = FSH_CTL_month_cas / num_le_cas * 28.94 * 86400
FSH_IRR_month_cas = FSH_IRR_month_cas / num_le_cas  * 28.94 * 86400

LWup_NOI_month_cas = LWup_NOI_month_cas / num_le_cas * 28.94 * 86400
LWup_CTL_month_cas = LWup_CTL_month_cas / num_le_cas * 28.94 * 86400
LWup_IRR_month_cas = LWup_IRR_month_cas / num_le_cas * 28.94 * 86400

SWup_NOI_month_cas = SWup_NOI_month_cas / num_le_cas * 28.94 * 86400
SWup_CTL_month_cas = SWup_CTL_month_cas / num_le_cas * 28.94 * 86400
SWup_IRR_month_cas = SWup_IRR_month_cas / num_le_cas * 28.94 * 86400



x = range(1, 13)
x1 = np.array(x) - 0.15
x2 = np.array(x) + 0.15

f = plt.figure(figsize = (16, 10), dpi=100)
f.subplots_adjust(hspace=0.4, wspace=0.4, left = 0.07, right = 0.95, top = 0.95, bottom = 0.05)
set_plot_param()

ax1 = plt.subplot(3, 4, 5)
plot_with_obs_nolegend(ax1, x, x1, x2, le_month_cas, EFLX_LH_TOT_NOI_month_cas, EFLX_LH_TOT_CTL_month_cas, EFLX_LH_TOT_IRR_month_cas,
                  QIRRIG_IRR_month_cas * 86400, QIRRIG_CTL_month_cas * 86400, 'OBS', 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'ET ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Evapotranspiration', 'e', 'CAS')

ax1 = plt.subplot(3, 4, 6)
plot_with_obs_without_nolegend(ax1, x, x1, x2, FSH_NOI_month_cas, FSH_CTL_month_cas, FSH_IRR_month_cas,
                  QIRRIG_IRR_month_cas * 86400, QIRRIG_CTL_month_cas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'GE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Ground evaporation', 'f', 'CAS')

ax1 = plt.subplot(3, 4, 7)
plot_with_obs_without_nolegend(ax1, x, x1, x2, LWup_NOI_month_cas, LWup_CTL_month_cas, LWup_IRR_month_cas,
                  QIRRIG_IRR_month_cas * 86400, QIRRIG_CTL_month_cas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'CE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Canopy evaporation', 'g', 'CAS')

ax1 = plt.subplot(3, 4, 8)
plot_with_obs_without_nolegend(ax1, x, x1, x2, SWup_NOI_month_cas, SWup_CTL_month_cas, SWup_IRR_month_cas,
                  QIRRIG_IRR_month_cas * 86400, QIRRIG_CTL_month_cas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'TR ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Transpiration', 'h', 'CAS')

str_infile_neb = 'D:\Forcing_tower\\NE1\\test.csv'
pd_reader_neb = pd.read_csv(str_infile_neb, header=None)
data_forc_neb = np.array(pd_reader_neb)
le_neb = data_forc_neb[:, 0]
hs_neb = data_forc_neb[:, 1]
sm_neb = data_forc_neb[:, 2]/100
lw_neb = data_forc_neb[:, 3]
sw_neb = data_forc_neb[:, 4]

le_month_neb = np.zeros(12)
hs_month_neb = np.zeros(12)
sm_month_neb = np.zeros(12)
lw_month_neb = np.zeros(12)
sw_month_neb = np.zeros(12)

num_le_neb = np.zeros(12)
num_hs_neb = np.zeros(12)
num_sm_neb = np.zeros(12)
num_lw_neb = np.zeros(12)
num_sw_neb = np.zeros(12)

data_CTL_neb = Data_from_nc('E:\Single_point\\Ne1_drip_SpGs_QIRRIG')
QIRRIG_CTL_neb = data_CTL_neb.load_variable('QIRRIG_FROM_SURFACE')
data_IRR_neb = Data_from_nc('E:\Single_point\\Ne1_sprinkler_SpGs_QIRRIG')
QIRRIG_IRR_neb = data_IRR_neb.load_variable('QIRRIG_FROM_SURFACE')

QIRRIG_CTL_month_neb = np.zeros(12)
QIRRIG_IRR_month_neb = np.zeros(12)







data_NOI_neb = Data_from_nc('E:\Single_point\\Ne1_noirr_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_NOI_neb = data_NOI_neb.load_variable('EFLX_LH_TOT')
data_CTL_neb = Data_from_nc('E:\Single_point\\Ne1_drip_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_CTL_neb = data_CTL_neb.load_variable('EFLX_LH_TOT')
data_IRR_neb = Data_from_nc('E:\Single_point\\Ne1_sprinkler_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_IRR_neb = data_IRR_neb.load_variable('EFLX_LH_TOT')

EFLX_LH_TOT_NOI_month_neb = np.zeros(12)
EFLX_LH_TOT_CTL_month_neb = np.zeros(12)
EFLX_LH_TOT_IRR_month_neb = np.zeros(12)

data_NOI_neb = Data_from_nc('E:\Single_point\\Ne1_noirr_SpGs_QSOIL_monmean')
FSH_NOI_neb = data_NOI_neb.load_variable('QSOIL')
data_CTL_neb = Data_from_nc('E:\Single_point\\Ne1_drip_SpGs_QSOIL_monmean')
FSH_CTL_neb = data_CTL_neb.load_variable('QSOIL')
data_IRR_neb = Data_from_nc('E:\Single_point\\Ne1_sprinkler_SpGs_QSOIL_monmean')
FSH_IRR_neb = data_IRR_neb.load_variable('QSOIL')

FSH_NOI_month_neb = np.zeros(12)
FSH_CTL_month_neb = np.zeros(12)
FSH_IRR_month_neb = np.zeros(12)

data_NOI_neb = Data_from_nc('E:\Single_point\\Ne1_noirr_SpGs_QVEGE_monmean')
LWup_NOI_neb = data_NOI_neb.load_variable('QVEGE')
data_CTL_neb = Data_from_nc('E:\Single_point\\Ne1_drip_SpGs_QVEGE_monmean')
LWup_CTL_neb = data_CTL_neb.load_variable('QVEGE')
data_IRR_neb = Data_from_nc('E:\Single_point\\Ne1_sprinkler_SpGs_QVEGE_monmean')
LWup_IRR_neb = data_IRR_neb.load_variable('QVEGE')

LWup_NOI_month_neb = np.zeros(12)
LWup_CTL_month_neb = np.zeros(12)
LWup_IRR_month_neb = np.zeros(12)

data_NOI_neb = Data_from_nc('E:\Single_point\\Ne1_noirr_SpGs_QVEGT_monmean')
SWup_NOI_neb = data_NOI_neb.load_variable('QVEGT')
data_CTL_neb = Data_from_nc('E:\Single_point\\Ne1_drip_SpGs_QVEGT_monmean')
SWup_CTL_neb = data_CTL_neb.load_variable('QVEGT')
data_IRR_neb = Data_from_nc('E:\Single_point\\Ne1_sprinkler_SpGs_QVEGT_monmean')
SWup_IRR_neb = data_IRR_neb.load_variable('QVEGT')

SWup_NOI_month_neb = np.zeros(12)
SWup_CTL_month_neb = np.zeros(12)
SWup_IRR_month_neb = np.zeros(12)


for year in range(13):
    for month in range(12):
        #if le_neb[12*year + month] > -90:
        le_month_neb[month] = le_month_neb[month] + le_neb[12*year + month]
        EFLX_LH_TOT_NOI_month_neb[month] = EFLX_LH_TOT_NOI_month_neb[month] + EFLX_LH_TOT_NOI_neb[12 * year + month]
        EFLX_LH_TOT_CTL_month_neb[month] = EFLX_LH_TOT_CTL_month_neb[month] + EFLX_LH_TOT_CTL_neb[12 * year + month]
        EFLX_LH_TOT_IRR_month_neb[month] = EFLX_LH_TOT_IRR_month_neb[month] + EFLX_LH_TOT_IRR_neb[12 * year + month]

        QIRRIG_CTL_month_neb[month] = QIRRIG_CTL_month_neb[month] + QIRRIG_CTL_neb[12 * year + month]
        QIRRIG_IRR_month_neb[month] = QIRRIG_IRR_month_neb[month] + QIRRIG_IRR_neb[12 * year + month]

        num_le_neb[month] = num_le_neb[month] + 1

        hs_month_neb[month] = hs_month_neb[month] + hs_neb[12*year + month]
        FSH_NOI_month_neb[month] = FSH_NOI_month_neb[month] + FSH_NOI_neb[12 * year + month]
        FSH_CTL_month_neb[month] = FSH_CTL_month_neb[month] + FSH_CTL_neb[12 * year + month]
        FSH_IRR_month_neb[month] = FSH_IRR_month_neb[month] + FSH_IRR_neb[12 * year + month]

        num_hs_neb[month] = num_hs_neb[month] + 1

        lw_month_neb[month] = lw_month_neb[month] + lw_neb[12*year + month]
        LWup_NOI_month_neb[month] = LWup_NOI_month_neb[month] + LWup_NOI_neb[12 * year + month]
        LWup_CTL_month_neb[month] = LWup_CTL_month_neb[month] + LWup_CTL_neb[12 * year + month]
        LWup_IRR_month_neb[month] = LWup_IRR_month_neb[month] + LWup_IRR_neb[12 * year + month]

        num_lw_neb[month] = num_lw_neb[month] + 1

        sw_month_neb[month] = sw_month_neb[month] + sw_neb[12*year + month]
        SWup_NOI_month_neb[month] = SWup_NOI_month_neb[month] + SWup_NOI_neb[12 * year + month]
        SWup_CTL_month_neb[month] = SWup_CTL_month_neb[month] + SWup_CTL_neb[12 * year + month]
        SWup_IRR_month_neb[month] = SWup_IRR_month_neb[month] + SWup_IRR_neb[12 * year + month]

        num_sw_neb[month] = num_sw_neb[month] + 1

le_month_neb = le_month_neb / num_le_neb
EFLX_LH_TOT_NOI_month_neb = EFLX_LH_TOT_NOI_month_neb / num_le_neb
EFLX_LH_TOT_CTL_month_neb = EFLX_LH_TOT_CTL_month_neb / num_le_neb
EFLX_LH_TOT_IRR_month_neb = EFLX_LH_TOT_IRR_month_neb / num_le_neb


QIRRIG_CTL_month_neb = QIRRIG_CTL_month_neb / num_le_neb
QIRRIG_IRR_month_neb = QIRRIG_IRR_month_neb / num_le_neb



FSH_NOI_month_neb = FSH_NOI_month_neb / num_le_neb * 28.94 * 86400
FSH_CTL_month_neb = FSH_CTL_month_neb / num_le_neb * 28.94 * 86400
FSH_IRR_month_neb = FSH_IRR_month_neb / num_le_neb  * 28.94 * 86400



LWup_NOI_month_neb = LWup_NOI_month_neb / num_le_neb * 28.94 * 86400
LWup_CTL_month_neb = LWup_CTL_month_neb / num_le_neb * 28.94 * 86400
LWup_IRR_month_neb = LWup_IRR_month_neb / num_le_neb * 28.94 * 86400



SWup_NOI_month_neb = SWup_NOI_month_neb / num_le_neb * 28.94 * 86400
SWup_CTL_month_neb = SWup_CTL_month_neb / num_le_neb * 28.94 * 86400
SWup_IRR_month_neb = SWup_IRR_month_neb / num_le_neb * 28.94 * 86400



x = range(1, 13)
x1 = np.array(x) - 0.15
x2 = np.array(x) + 0.15



ax1 = plt.subplot(3, 4, 1)
plot_with_obs(ax1, x, x1, x2, le_month_neb, EFLX_LH_TOT_NOI_month_neb, EFLX_LH_TOT_CTL_month_neb, EFLX_LH_TOT_IRR_month_neb,
                  QIRRIG_IRR_month_neb * 86400, QIRRIG_CTL_month_neb * 86400, 'OBS', 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'ET ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Evapotranspiration', 'a', 'NEB')

ax1 = plt.subplot(3, 4, 2)
plot_with_obs_without_nolegend(ax1, x, x1, x2, FSH_NOI_month_neb, FSH_CTL_month_neb, FSH_IRR_month_neb,
                  QIRRIG_IRR_month_neb * 86400, QIRRIG_CTL_month_neb * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'GE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Ground evaporation', 'b', 'NEB')

ax1 = plt.subplot(3, 4, 3)
plot_with_obs_without_nolegend(ax1, x, x1, x2, LWup_NOI_month_neb, LWup_CTL_month_neb, LWup_IRR_month_neb,
                  QIRRIG_IRR_month_neb * 86400, QIRRIG_CTL_month_neb * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'CE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Canopy evaporation', 'c', 'NEB')

ax1 = plt.subplot(3, 4, 4)
plot_with_obs_without_nolegend(ax1, x, x1, x2, SWup_NOI_month_neb, SWup_CTL_month_neb, SWup_IRR_month_neb,
                  QIRRIG_IRR_month_neb * 86400, QIRRIG_CTL_month_neb * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'TR ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Transpiration', 'd', 'NEB')

str_infile_mas = 'D:\Forcing_tower\Japan\\test.csv'
pd_reader_mas = pd.read_csv(str_infile_mas, header=None)
data_forc_mas = np.array(pd_reader_mas)
le_mas = data_forc_mas[:, 0]
hs_mas = data_forc_mas[:, 1]
sm_mas = data_forc_mas[:, 2]/100
lw_mas = data_forc_mas[:, 3]
sw_mas = data_forc_mas[:, 4]

le_month_mas = np.zeros(12)
hs_month_mas = np.zeros(12)
sm_month_mas = np.zeros(12)
lw_month_mas = np.zeros(12)
sw_month_mas = np.zeros(12)

num_le_mas = np.zeros(12)
num_hs_mas = np.zeros(12)
num_sm_mas = np.zeros(12)
num_lw_mas = np.zeros(12)
num_sw_mas = np.zeros(12)

data_CTL_mas = Data_from_nc('E:\Single_point\\Japan_drip_SpGs_QIRRIG')
QIRRIG_CTL_mas = data_CTL_mas.load_variable('QIRRIG_FROM_SURFACE')
data_IRR_mas = Data_from_nc('E:\Single_point\\Japan_flood_SpGs_QIRRIG')
QIRRIG_IRR_mas = data_IRR_mas.load_variable('QIRRIG_FROM_SURFACE')

QIRRIG_CTL_month_mas = np.zeros(12)
QIRRIG_IRR_month_mas = np.zeros(12)



data_NOI_mas = Data_from_nc('E:\Single_point\\Japan_noirr_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_NOI_mas = data_NOI_mas.load_variable('EFLX_LH_TOT')
data_CTL_mas = Data_from_nc('E:\Single_point\\Japan_drip_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_CTL_mas = data_CTL_mas.load_variable('EFLX_LH_TOT')
data_IRR_mas = Data_from_nc('E:\Single_point\\Japan_flood_SpGs_EFLX_LH_TOT_monmean')
EFLX_LH_TOT_IRR_mas = data_IRR_mas.load_variable('EFLX_LH_TOT')

EFLX_LH_TOT_NOI_month_mas = np.zeros(12)
EFLX_LH_TOT_CTL_month_mas = np.zeros(12)
EFLX_LH_TOT_IRR_month_mas = np.zeros(12)

data_NOI_mas = Data_from_nc('E:\Single_point\\Japan_noirr_SpGs_QSOIL_monmean')
FSH_NOI_mas = data_NOI_mas.load_variable('QSOIL')
data_CTL_mas = Data_from_nc('E:\Single_point\\Japan_drip_SpGs_QSOIL_monmean')
FSH_CTL_mas = data_CTL_mas.load_variable('QSOIL')
data_IRR_mas = Data_from_nc('E:\Single_point\\Japan_flood_SpGs_QSOIL_monmean')
FSH_IRR_mas = data_IRR_mas.load_variable('QSOIL')

FSH_NOI_month_mas = np.zeros(12)
FSH_CTL_month_mas = np.zeros(12)
FSH_IRR_month_mas = np.zeros(12)

data_NOI_mas = Data_from_nc('E:\Single_point\\Japan_noirr_SpGs_QVEGE_monmean')
LWup_NOI_mas = data_NOI_mas.load_variable('QVEGE')
data_CTL_mas = Data_from_nc('E:\Single_point\\Japan_drip_SpGs_QVEGE_monmean')
LWup_CTL_mas = data_CTL_mas.load_variable('QVEGE')
data_IRR_mas = Data_from_nc('E:\Single_point\\Japan_flood_SpGs_QVEGE_monmean')
LWup_IRR_mas = data_IRR_mas.load_variable('QVEGE')

LWup_NOI_month_mas = np.zeros(12)
LWup_CTL_month_mas = np.zeros(12)
LWup_IRR_month_mas = np.zeros(12)

data_NOI_mas = Data_from_nc('E:\Single_point\\Japan_noirr_SpGs_QVEGT_monmean')
SWup_NOI_mas = data_NOI_mas.load_variable('QVEGT')
data_CTL_mas = Data_from_nc('E:\Single_point\\Japan_drip_SpGs_QVEGT_monmean')
SWup_CTL_mas = data_CTL_mas.load_variable('QVEGT')
data_IRR_mas = Data_from_nc('E:\Single_point\\Japan_flood_SpGs_QVEGT_monmean')
SWup_IRR_mas = data_IRR_mas.load_variable('QVEGT')

SWup_NOI_month_mas = np.zeros(12)
SWup_CTL_month_mas = np.zeros(12)
SWup_IRR_month_mas = np.zeros(12)


for year in range(1):
    for month in range(12):
        if le_mas[12*year + month] > -90:
            le_month_mas[month] = le_month_mas[month] + le_mas[12*year + month]
            EFLX_LH_TOT_NOI_month_mas[month] = EFLX_LH_TOT_NOI_month_mas[month] + EFLX_LH_TOT_NOI_mas[12 * year + month]
            EFLX_LH_TOT_CTL_month_mas[month] = EFLX_LH_TOT_CTL_month_mas[month] + EFLX_LH_TOT_CTL_mas[12 * year + month]
            EFLX_LH_TOT_IRR_month_mas[month] = EFLX_LH_TOT_IRR_month_mas[month] + EFLX_LH_TOT_IRR_mas[12 * year + month]

            QIRRIG_CTL_month_mas[month] = QIRRIG_CTL_month_mas[month] + QIRRIG_CTL_mas[12 * year + month]
            QIRRIG_IRR_month_mas[month] = QIRRIG_IRR_month_mas[month] + QIRRIG_IRR_mas[12 * year + month]

            num_le_mas[month] = num_le_mas[month] + 1

            hs_month_mas[month] = hs_month_mas[month] + hs_mas[12*year + month]
            FSH_NOI_month_mas[month] = FSH_NOI_month_mas[month] + FSH_NOI_mas[12 * year + month]
            FSH_CTL_month_mas[month] = FSH_CTL_month_mas[month] + FSH_CTL_mas[12 * year + month]
            FSH_IRR_month_mas[month] = FSH_IRR_month_mas[month] + FSH_IRR_mas[12 * year + month]

            num_hs_mas[month] = num_hs_mas[month] + 1

            lw_month_mas[month] = lw_month_mas[month] + lw_mas[12*year + month]
            LWup_NOI_month_mas[month] = LWup_NOI_month_mas[month] + LWup_NOI_mas[12 * year + month]
            LWup_CTL_month_mas[month] = LWup_CTL_month_mas[month] + LWup_CTL_mas[12 * year + month]
            LWup_IRR_month_mas[month] = LWup_IRR_month_mas[month] + LWup_IRR_mas[12 * year + month]

            num_lw_mas[month] = num_lw_mas[month] + 1

            sw_month_mas[month] = sw_month_mas[month] + sw_mas[12*year + month]
            SWup_NOI_month_mas[month] = SWup_NOI_month_mas[month] + SWup_NOI_mas[12 * year + month]
            SWup_CTL_month_mas[month] = SWup_CTL_month_mas[month] + SWup_CTL_mas[12 * year + month]
            SWup_IRR_month_mas[month] = SWup_IRR_month_mas[month] + SWup_IRR_mas[12 * year + month]

            num_sw_mas[month] = num_sw_mas[month] + 1

le_month_mas = le_month_mas / num_le_mas
EFLX_LH_TOT_NOI_month_mas = EFLX_LH_TOT_NOI_month_mas / num_le_mas
EFLX_LH_TOT_CTL_month_mas = EFLX_LH_TOT_CTL_month_mas / num_le_mas
EFLX_LH_TOT_IRR_month_mas = EFLX_LH_TOT_IRR_month_mas / num_le_mas


QIRRIG_CTL_month_mas = QIRRIG_CTL_month_mas / num_le_mas
QIRRIG_IRR_month_mas = QIRRIG_IRR_month_mas / num_le_mas


FSH_NOI_month_mas = FSH_NOI_month_mas / num_le_mas * 28.94 * 86400
FSH_CTL_month_mas = FSH_CTL_month_mas / num_le_mas * 28.94 * 86400
FSH_IRR_month_mas = FSH_IRR_month_mas / num_le_mas  * 28.94 * 86400



LWup_NOI_month_mas = LWup_NOI_month_mas / num_le_mas * 28.94 * 86400
LWup_CTL_month_mas = LWup_CTL_month_mas / num_le_mas * 28.94 * 86400
LWup_IRR_month_mas = LWup_IRR_month_mas / num_le_mas * 28.94 * 86400



SWup_NOI_month_mas = SWup_NOI_month_mas / num_le_mas * 28.94 * 86400
SWup_CTL_month_mas = SWup_CTL_month_mas / num_le_mas * 28.94 * 86400
SWup_IRR_month_mas = SWup_IRR_month_mas / num_le_mas * 28.94 * 86400



x = range(1, 13)
x1 = np.array(x) - 0.15
x2 = np.array(x) + 0.15


ax1 = plt.subplot(3, 4, 9)
plot_with_obs_nolegend(ax1, x, x1, x2, le_month_mas, EFLX_LH_TOT_NOI_month_mas, EFLX_LH_TOT_CTL_month_mas, EFLX_LH_TOT_IRR_month_mas,
                  QIRRIG_IRR_month_mas * 86400, QIRRIG_CTL_month_mas * 86400, 'OBS', 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'ET ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Evapotranspiration', 'i', 'MAS')

ax1 = plt.subplot(3, 4, 10)
plot_with_obs_without_nolegend(ax1, x, x1, x2, FSH_NOI_month_mas, FSH_CTL_month_mas, FSH_IRR_month_mas,
                  QIRRIG_IRR_month_mas * 86400, QIRRIG_CTL_month_mas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'GE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Ground evaporation', 'j', 'MAS')


ax1 = plt.subplot(3, 4, 11)
plot_with_obs_without_nolegend(ax1, x, x1, x2, LWup_NOI_month_mas, LWup_CTL_month_mas, LWup_IRR_month_mas,
                  QIRRIG_IRR_month_mas * 86400, QIRRIG_CTL_month_mas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'CE ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Canopy evaporation', 'k', 'MAS')

ax1 = plt.subplot(3, 4, 12)
plot_with_obs_without_nolegend(ax1, x, x1, x2, SWup_NOI_month_mas, SWup_CTL_month_mas, SWup_IRR_month_mas,
                  QIRRIG_IRR_month_mas * 86400, QIRRIG_CTL_month_mas * 86400, 'NOI', 'CTL', 'IRR',
                  'Qirr_irr', 'Qirr_ctl', 'upper left', 'upper right', 'TR ($W/m^2$)', 'Qirr (mm/day)', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
                    'Transpiration', 'l', 'MAS')


plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Single_point1.png')
#plt.show()