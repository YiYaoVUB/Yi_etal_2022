import scipy.io as scio
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def set_plot_param():
    """Set my own customized plotting parameters"""

    mpl.rc('axes', edgecolor='dimgrey')
    mpl.rc('axes', labelcolor='dimgrey')
    mpl.rc('xtick', color='dimgrey')
    mpl.rc('xtick', labelsize=10)
    mpl.rc('ytick', color='dimgrey')
    mpl.rc('ytick', labelsize=10)
    mpl.rc('axes', titlesize=10)
    mpl.rc('axes', labelsize=10)
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

str_data_ctl = 'E:\Research1\CTL_final.mat'
dic_data_ctl = scio.loadmat(str_data_ctl)
data_ctl = dic_data_ctl['sum_ctl']

str_data_irr = 'E:\Research1\IRR_final.mat'
dic_data_irr = scio.loadmat(str_data_irr)
data_irr = dic_data_irr['sum_irr']

str_data_noi = 'E:\Research1\\NOI_final.mat'
dic_data_noi = scio.loadmat(str_data_noi)
data_noi = dic_data_noi['sum_noi']


# GLO
WNA_CTL_EFLX_LH_TOT = data_ctl[0, :, 0]
WNA_CTL_FSH = data_ctl[0, :, 1]
WNA_CTL_LWup = data_ctl[0, :, 2]
WNA_CTL_SWup = data_ctl[0, :, 3]
WNA_CTL_Qle = data_ctl[0, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[0, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[0, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[0, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[0, :, 0]
WNA_IRR_FSH = data_irr[0, :, 1]
WNA_IRR_LWup = data_irr[0, :, 2]
WNA_IRR_SWup = data_irr[0, :, 3]
WNA_IRR_Qle = data_irr[0, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[0, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[0, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[0, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[0, :, 0]
WNA_NOI_FSH = data_noi[0, :, 1]
WNA_NOI_LWup = data_noi[0, :, 2]
WNA_NOI_SWup = data_noi[0, :, 3]
WNA_NOI_Qle = data_noi[0, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[0, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[0, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[0, :, 7]

def plot_var(ax1, x, var_IRR, var_CTL, var_NOI,legloc, ylabel,title, num,region):
    set_plot_param()
    plt.plot(x, var_IRR, 'green', marker='v', label='IRR', linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, var_CTL, 'blue', marker='>', label='CTL', linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, var_NOI, 'red', marker='^', label='NOI', linewidth=0.8, markersize=5, alpha=0.5)
    plt.legend(loc=legloc, frameon=False, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
               fontsize=8)
    plt.title(title, fontsize=10,loc='right')
    plt.title(region, fontsize=10, loc='left')
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')

def plot_var_nolegend(ax1, x, var_IRR, var_CTL, var_NOI,legloc, ylabel,title, num,region):
    set_plot_param()
    plt.plot(x, var_IRR, 'green', marker='v', label='IRR', linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, var_CTL, 'blue', marker='>', label='CTL', linewidth=0.8, markersize=5, alpha=0.5)
    plt.plot(x, var_NOI, 'red', marker='^', label='NOI', linewidth=0.8, markersize=5, alpha=0.5)

    plt.ylabel(ylabel, fontsize=10)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               [r'J', r'F', r'M', r'A', r'M', 'J', r'J', r'A', r'S', r'O', r'N', r'D'],
               fontsize=8)
    plt.title(title, fontsize=10,loc='right')
    plt.title(region, fontsize=10, loc='left')
    plt.tick_params(labelsize=10)
    ax1.text(-0.15, 1.05, num, color='dimgrey', fontsize=12, transform=ax1.transAxes, weight='bold')


x = range(1, 13)
f = plt.figure(figsize = (16, 10), dpi=100)
set_plot_param()
f.subplots_adjust(hspace=0.4, wspace=0.4, left = 0.07, right = 0.95, top = 0.95, bottom = 0.05)
ax1 = plt.subplot(3, 4, 1)
plot_var(ax1, x, WNA_IRR_EFLX_LH_TOT, WNA_CTL_EFLX_LH_TOT, WNA_NOI_EFLX_LH_TOT, 'upper left', r'LHF ($W/m^2$)', 'Latent heat flux', 'a', 'GLO')

ax1 = plt.subplot(3, 4, 2)
plot_var_nolegend(ax1, x, WNA_IRR_FSH, WNA_CTL_FSH, WNA_NOI_FSH, 'upper left', r'SHF ($W/m^2$)', 'Sensible heat flux', 'b', 'GLO')

ax1 = plt.subplot(3, 4, 3)
plot_var_nolegend(ax1, x, WNA_IRR_LWup, WNA_CTL_LWup, WNA_NOI_LWup, 'upper left', r'LWup ($W/m^2$)', 'Upwelling longwave radiation', 'c', 'GLO')

ax1 = plt.subplot(3, 4, 4)
plot_var_nolegend(ax1, x, WNA_IRR_SWup, WNA_CTL_SWup, WNA_NOI_SWup, 'upper left', r'SWup ($W/m^2$)', 'Upwelling shortwave radiation', 'd', 'GLO')

# WNA
WNA_CTL_EFLX_LH_TOT = data_ctl[4, :, 0]
WNA_CTL_FSH = data_ctl[4, :, 1]
WNA_CTL_LWup = data_ctl[4, :, 2]
WNA_CTL_SWup = data_ctl[4, :, 3]
WNA_CTL_Qle = data_ctl[4, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[4, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[4, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[4, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[4, :, 0]
WNA_IRR_FSH = data_irr[4, :, 1]
WNA_IRR_LWup = data_irr[4, :, 2]
WNA_IRR_SWup = data_irr[4, :, 3]
WNA_IRR_Qle = data_irr[4, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[4, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[4, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[4, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[4, :, 0]
WNA_NOI_FSH = data_noi[4, :, 1]
WNA_NOI_LWup = data_noi[4, :, 2]
WNA_NOI_SWup = data_noi[4, :, 3]
WNA_NOI_Qle = data_noi[4, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[4, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[4, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[4, :, 7]

x = range(1, 13)
ax1 = plt.subplot(3, 4, 5)
plot_var_nolegend(ax1, x, WNA_IRR_EFLX_LH_TOT, WNA_CTL_EFLX_LH_TOT, WNA_NOI_EFLX_LH_TOT, 'upper left', r'LHF ($W/m^2$)', 'Latent heat flux', 'e', 'WNA')

ax1 = plt.subplot(3, 4, 6)
plot_var_nolegend(ax1, x, WNA_IRR_FSH, WNA_CTL_FSH, WNA_NOI_FSH, 'upper left', r'SHF ($W/m^2$)', 'Sensible heat flux', 'f', 'WNA')

ax1 = plt.subplot(3, 4, 7)
plot_var_nolegend(ax1, x, WNA_IRR_LWup, WNA_CTL_LWup, WNA_NOI_LWup, 'upper left', r'LWup ($W/m^2$)', 'Upwelling longwave radiation', 'g', 'WNA')

ax1 = plt.subplot(3, 4, 8)
plot_var_nolegend(ax1, x, WNA_IRR_SWup, WNA_CTL_SWup, WNA_NOI_SWup, 'upper left', r'SWup ($W/m^2$)', 'Upwelling shortwave radiation', 'h', 'WNA')

# SAS
WNA_CTL_EFLX_LH_TOT = data_ctl[38, :, 0]
WNA_CTL_FSH = data_ctl[38, :, 1]
WNA_CTL_LWup = data_ctl[38, :, 2]
WNA_CTL_SWup = data_ctl[38, :, 3]
WNA_CTL_Qle = data_ctl[38, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[38, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[38, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[38, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[38, :, 0]
WNA_IRR_FSH = data_irr[38, :, 1]
WNA_IRR_LWup = data_irr[38, :, 2]
WNA_IRR_SWup = data_irr[38, :, 3]
WNA_IRR_Qle = data_irr[38, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[38, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[38, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[38, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[38, :, 0]
WNA_NOI_FSH = data_noi[38, :, 1]
WNA_NOI_LWup = data_noi[38, :, 2]
WNA_NOI_SWup = data_noi[38, :, 3]
WNA_NOI_Qle = data_noi[38, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[38, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[38, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[38, :, 7]

x = range(1, 13)
ax1 = plt.subplot(3, 4, 9)
plot_var_nolegend(ax1, x, WNA_IRR_EFLX_LH_TOT, WNA_CTL_EFLX_LH_TOT, WNA_NOI_EFLX_LH_TOT, 'upper left', r'LHF ($W/m^2$)', 'Latent heat flux', 'i', 'SAS')

ax1 = plt.subplot(3, 4, 10)
plot_var_nolegend(ax1, x, WNA_IRR_FSH, WNA_CTL_FSH, WNA_NOI_FSH, 'upper left', r'SHF ($W/m^2$)', 'Sensible heat flux', 'j', 'SAS')

ax1 = plt.subplot(3, 4, 11)
plot_var_nolegend(ax1, x, WNA_IRR_LWup, WNA_CTL_LWup, WNA_NOI_LWup, 'upper left', r'LWup ($W/m^2$)', 'Upwelling longwave radiation', 'k', 'SAS')

ax1 = plt.subplot(3, 4, 12)
plot_var_nolegend(ax1, x, WNA_IRR_SWup, WNA_CTL_SWup, WNA_NOI_SWup, 'upper left', r'SWup ($W/m^2$)', 'Upwelling shortwave radiation', 'l', 'SAS')


plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Timeseries_energy1.png')


str_data_ctl = 'E:\Research1\CTL_final.mat'
dic_data_ctl = scio.loadmat(str_data_ctl)
data_ctl = dic_data_ctl['sum_ctl']

str_data_irr = 'E:\Research1\IRR_final.mat'
dic_data_irr = scio.loadmat(str_data_irr)
data_irr = dic_data_irr['sum_irr']

str_data_noi = 'E:\Research1\\NOI_final.mat'
dic_data_noi = scio.loadmat(str_data_noi)
data_noi = dic_data_noi['sum_noi']


# GLO
WNA_CTL_EFLX_LH_TOT = data_ctl[0, :, 0]
WNA_CTL_FSH = data_ctl[0, :, 1]
WNA_CTL_LWup = data_ctl[0, :, 2]
WNA_CTL_SWup = data_ctl[0, :, 3]
WNA_CTL_Qle = data_ctl[0, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[0, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[0, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[0, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[0, :, 0]
WNA_IRR_FSH = data_irr[0, :, 1]
WNA_IRR_LWup = data_irr[0, :, 2]
WNA_IRR_SWup = data_irr[0, :, 3]
WNA_IRR_Qle = data_irr[0, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[0, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[0, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[0, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[0, :, 0]
WNA_NOI_FSH = data_noi[0, :, 1]
WNA_NOI_LWup = data_noi[0, :, 2]
WNA_NOI_SWup = data_noi[0, :, 3]
WNA_NOI_Qle = data_noi[0, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[0, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[0, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[0, :, 7]

x = range(1, 13)
f = plt.figure(figsize = (16, 10), dpi=100)
set_plot_param()
f.subplots_adjust(hspace=0.4, wspace=0.4, left = 0.07, right = 0.95, top = 0.95, bottom = 0.05)

ax1 = plt.subplot(3, 4, 1)
plot_var(ax1, x, WNA_IRR_Qle, WNA_CTL_Qle, WNA_NOI_Qle, 'upper left', r'E ($mm/day$)', 'Evaporation', 'a', 'GLO')

ax1 = plt.subplot(3, 4, 2)
plot_var_nolegend(ax1, x, WNA_IRR_QVEGT, WNA_CTL_QVEGT, WNA_NOI_QVEGT, 'upper left', r'TR ($mm/day$)', 'Transpiration', 'b', 'GLO')

ax1 = plt.subplot(3, 4, 3)
plot_var_nolegend(ax1, x, WNA_IRR_QRUNOFF, WNA_CTL_QRUNOFF, WNA_NOI_QRUNOFF, 'upper left', r'R ($mm/day$)', 'Runoff', 'c', 'GLO')

ax1 = plt.subplot(3, 4, 4)
plot_var_nolegend(ax1, x, WNA_IRR_TOTSOILLIQ, WNA_CTL_TOTSOILLIQ, WNA_NOI_TOTSOILLIQ, 'upper left', r'TSW ($kg/m^2$)', 'Total soil water', 'd', 'GLO')

# WNA
WNA_CTL_EFLX_LH_TOT = data_ctl[4, :, 0]
WNA_CTL_FSH = data_ctl[4, :, 1]
WNA_CTL_LWup = data_ctl[4, :, 2]
WNA_CTL_SWup = data_ctl[4, :, 3]
WNA_CTL_Qle = data_ctl[4, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[4, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[4, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[4, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[4, :, 0]
WNA_IRR_FSH = data_irr[4, :, 1]
WNA_IRR_LWup = data_irr[4, :, 2]
WNA_IRR_SWup = data_irr[4, :, 3]
WNA_IRR_Qle = data_irr[4, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[4, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[4, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[4, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[4, :, 0]
WNA_NOI_FSH = data_noi[4, :, 1]
WNA_NOI_LWup = data_noi[4, :, 2]
WNA_NOI_SWup = data_noi[4, :, 3]
WNA_NOI_Qle = data_noi[4, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[4, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[4, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[4, :, 7]

x = range(1, 13)
ax1 = plt.subplot(3, 4, 5)
plot_var_nolegend(ax1, x, WNA_IRR_Qle, WNA_CTL_Qle, WNA_NOI_Qle, 'upper left', r'E ($mm/day$)', 'Evaporation', 'e', 'WNA')

ax1 = plt.subplot(3, 4, 6)
plot_var_nolegend(ax1, x, WNA_IRR_QVEGT, WNA_CTL_QVEGT, WNA_NOI_QVEGT, 'upper left', r'TR ($mm/day$)', 'Transpiration', 'f', 'WNA')

ax1 = plt.subplot(3, 4, 7)
plot_var_nolegend(ax1, x, WNA_IRR_QRUNOFF, WNA_CTL_QRUNOFF, WNA_NOI_QRUNOFF, 'upper left', r'R ($mm/day$)', 'Runoff', 'g', 'WNA')

ax1 = plt.subplot(3, 4, 8)
plot_var_nolegend(ax1, x, WNA_IRR_TOTSOILLIQ, WNA_CTL_TOTSOILLIQ, WNA_NOI_TOTSOILLIQ, 'upper left', r'TSW ($kg/m^2$)', 'Total soil water', 'h', 'WNA')


# SAS
WNA_CTL_EFLX_LH_TOT = data_ctl[38, :, 0]
WNA_CTL_FSH = data_ctl[38, :, 1]
WNA_CTL_LWup = data_ctl[38, :, 2]
WNA_CTL_SWup = data_ctl[38, :, 3]
WNA_CTL_Qle = data_ctl[38, :, 4]  / 28.94
WNA_CTL_QVEGT = data_ctl[38, :, 5]  * 86400
WNA_CTL_QRUNOFF = data_ctl[38, :, 6]  * 86400
WNA_CTL_TOTSOILLIQ = data_ctl[38, :, 7]

WNA_IRR_EFLX_LH_TOT = data_irr[38, :, 0]
WNA_IRR_FSH = data_irr[38, :, 1]
WNA_IRR_LWup = data_irr[38, :, 2]
WNA_IRR_SWup = data_irr[38, :, 3]
WNA_IRR_Qle = data_irr[38, :, 4]  / 28.94
WNA_IRR_QVEGT = data_irr[38, :, 5]  * 86400
WNA_IRR_QRUNOFF = data_irr[38, :, 6]  * 86400
WNA_IRR_TOTSOILLIQ = data_irr[38, :, 7]

WNA_NOI_EFLX_LH_TOT = data_noi[38, :, 0]
WNA_NOI_FSH = data_noi[38, :, 1]
WNA_NOI_LWup = data_noi[38, :, 2]
WNA_NOI_SWup = data_noi[38, :, 3]
WNA_NOI_Qle = data_noi[38, :, 4]  / 28.94
WNA_NOI_QVEGT = data_noi[38, :, 5]  * 86400
WNA_NOI_QRUNOFF = data_noi[38, :, 6]  * 86400
WNA_NOI_TOTSOILLIQ = data_noi[38, :, 7]

x = range(1, 13)
ax1 = plt.subplot(3, 4, 9)
plot_var_nolegend(ax1, x, WNA_IRR_Qle, WNA_CTL_Qle, WNA_NOI_Qle, 'upper left', r'E ($mm/day$)', 'Evaporation', 'i', 'SAS')

ax1 = plt.subplot(3, 4, 10)
plot_var_nolegend(ax1, x, WNA_IRR_QVEGT, WNA_CTL_QVEGT, WNA_NOI_QVEGT, 'upper left', r'TR ($mm/day$)', 'Transpiration', 'j', 'SAS')

ax1 = plt.subplot(3, 4, 11)
plot_var_nolegend(ax1, x, WNA_IRR_QRUNOFF, WNA_CTL_QRUNOFF, WNA_NOI_QRUNOFF, 'upper left', r'R ($mm/day$)', 'Runoff', 'k', 'SAS')

ax1 = plt.subplot(3, 4, 12)
plot_var_nolegend(ax1, x, WNA_IRR_TOTSOILLIQ, WNA_CTL_TOTSOILLIQ, WNA_NOI_TOTSOILLIQ, 'upper left', r'TSW ($kg/m^2$)', 'Total soil water', 'l', 'SAS')

plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Timeseries_water1.png')
#plt.show()


