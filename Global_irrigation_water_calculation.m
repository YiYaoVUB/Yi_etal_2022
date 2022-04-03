str_surf = 'E:\Data_Evaluation\Surface_data\surfdata_0.9x1.25_hist_78pfts_CMIP6_simyr2000_c201126 - ¸±±¾.nc'
AREA=ncread(str_surf,'AREA')
LONGXY=ncread(str_surf,'LONGXY')
LATIXY=ncread(str_surf,'LATIXY')

num_year = 30

str_PCT_CFT = 'E:\Data_Evaluation\Surface_data\PCT_CFT.nc'
data_PCT_CFT   = ncread(str_PCT_CFT,'Runoff') 
[row,col] = find(data_PCT_CFT)

str_middle = ["CTL","IRR_drai","IRR_meth","IRR_pool","IRR_satu"]        %IRR1 = "IRR_new_nopool" 

len_expe = size(str_middle)
len_expe = len_expe(2)

str_raw = 'E:\Research1\QIRRIG\'
str_end = '\QIRRIG_yearmean_mm_year.nc'

QIRRIG_YEAR_sum = zeros(len_expe, 30)

for exp = 1 : len_expe
    str_qirrig = strcat(str_raw, str_middle(exp), str_end)
    QIRRIG_FROM_GW_CONFINED=ncread(str_qirrig,'QIRRIG_FROM_GW_CONFINED')
    QIRRIG_FROM_GW_UNCONFINED=ncread(str_qirrig,'QIRRIG_FROM_GW_UNCONFINED')
    QIRRIG_FROM_SURFACE=ncread(str_qirrig,'QIRRIG_FROM_SURFACE')
    
    QIRRIG = QIRRIG_FROM_SURFACE + QIRRIG_FROM_GW_UNCONFINED + QIRRIG_FROM_GW_CONFINED
    QIRRIG_YEAR = zeros(288, 192, num_year)
    for i = 1 : num_year
        QIRRIG_TEMP = QIRRIG(:, :, i)
        QIRRIG_YEAR(:, :, i) = QIRRIG_TEMP.*AREA
    end
    QIRRIG_YEAR = QIRRIG_YEAR * 1000 / 1000000000
    QIRRIG_YEAR_sum(exp, :) = nansum(QIRRIG_YEAR, [1 2])
    
end

    

