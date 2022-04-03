str_surf = 'E:\Data_Evaluation\Surface_data\surfdata_0.9x1.25_hist_78pfts_CMIP6_simyr2000_c201126 - 副本.nc'
AREA=ncread(str_surf,'AREA')
LONGXY=ncread(str_surf,'LONGXY')
LATIXY=ncread(str_surf,'LATIXY')

num_year = 10

str_PCT_CFT = 'E:\Data_Evaluation\Surface_data\PCT_CFT.nc'
data_PCT_CFT   = ncread(str_PCT_CFT,'Runoff') 
[row,col] = find(data_PCT_CFT)

x = LONGXY(row, col)
x = x(:, 1)
x_unchanged = x 
x(x>180) = x(x>180)-360 %because there are 7 countries which crosses the 0 deg lon, thus we use different x
y = LATIXY(row, col)
y = y(1, :)

str_map_world = 'E:\Data_Evaluation\World_Countries\World_Countries.shp'
Map_world = shaperead(str_map_world)
Qirr_obs_world = csvread('E:\Data_Evaluation\QIRRIG\aquadata.csv')

str_map_china = 'E:\Data_Evaluation\QIRRIG\区划\省.shp'
Map_china = shaperead(str_map_china)
Qirr_obs_china = csvread('E:\Data_Evaluation\QIRRIG\chinadata.csv')

str_map_usa = 'E:\Data_Evaluation\QIRRIG\States_shapefile-shp\States_shapefile.shp'
Map_usa = shaperead(str_map_usa)
Qirr_obs_usa = csvread('E:\Data_Evaluation\QIRRIG\usadata.csv')
%str_middle = ["CTL","CTL_limit","IRR","IRR_limit","IRR_new_nopool","IRR_new_nopool_limit","IRR_new_pool","IRR_new_pool_limit"]
%str_middle = ["IRR_new_satu_limit"]%,"IRR_new_satu_nolimit"]
str_middle = ["CTL","CTL_limit","IRR","IRR_limit","IRR_new_nopool","IRR_new_nopool_limit","IRR_new_pool","IRR_new_pool_limit","IRR_new_satu","IRR_new_satu_limit"]        %IRR1 = "IRR_new_nopool" 
%str_middle = ["CTL","IRR","CTL_GRD_LIM","CTL_NOGRD_LIM","IRR_GRD_LIM","IRR_NOGRD_LIM","frequency3day","frequency3day_no_threshold","frequency5day","frequency5day_no_threshold","frequency7day","frequency7day_no_threshold","frequency10day","frequency10day_no_threshold","frequency14day","frequency14day_no_threshold","lenth1h","lenth2h","lenth12h","lenth24h","start0h","start12h","start18h"]
str_middle = ["CTL", "IRR_drai", "IRR_meth"]
len_expe = size(str_middle)
len_expe = len_expe(2)

str_raw = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\'
str_raw = 'E:\Research1\QIRRIG_'
str_end = '_QIRRIG_yearmean_mm_year.nc'
str_end = '_2006-2015_yearmean_mm_year.nc'

countries = load('E:\Data_Evaluation\Scripts\data_needed.txt')
len_countries = size(countries)
len_countries = len_countries(1)
QIRRIG_COUNTRY = zeros(len_countries,num_year)

province = [13, 1, 14, 29, 20, 21, 25, 3, 17, 9, 18, 19, 8, 15, 7, 5, 31, 30, 16, 4, 28, 24, 2, 26, 12, 23, 22, 11, 10, 32, 27]
len_province = size(province)
len_province = len_province(2)

len_state = 51

bias_aqua = zeros(len_expe, 1)
rmse_aqua = zeros(len_expe, 1)

bias_china = zeros(len_expe, 1)
rmse_china = zeros(len_expe, 1)

bias_usa = zeros(len_expe, 1)
rmse_usa = zeros(len_expe, 1)

for exp = 1 : len_expe
    str_qirrig = strcat(str_raw, str_middle(exp), str_end)
    QIRRIG_FROM_GW_CONFINED=ncread(str_qirrig,'QIRRIG_FROM_GW_CONFINED')
    QIRRIG_FROM_GW_UNCONFINED=ncread(str_qirrig,'QIRRIG_FROM_GW_UNCONFINED')
    QIRRIG_FROM_SURFACE=ncread(str_qirrig,'QIRRIG_FROM_SURFACE')
    
    QIRRIG_COUNTRY = zeros(len_countries,num_year)
    
    QIRRIG = QIRRIG_FROM_SURFACE + QIRRIG_FROM_GW_UNCONFINED + QIRRIG_FROM_GW_CONFINED
    QIRRIG_YEAR = zeros(288, 192, num_year)
    for i = 1 : num_year
        QIRRIG_TEMP = QIRRIG(:, :, i)
        QIRRIG_YEAR(:, :, i) = QIRRIG_TEMP.*AREA
    end
    QIRRIG_YEAR = QIRRIG_YEAR * 1000 / 1000000000
    
    sum_bias = 0
    sum_rmse = 0
    number = 0
    for index = 1 : len_countries
        if countries(index)==228 || countries(index)==78 || countries(index)==203 || countries(index)==4 || countries(index)==145 || countries(index)==231 || countries(index)==219 || countries(index)==83
            x_bord = Map_world(countries(index)).X
            %x_bord(x_bord<0) = x_bord(x_bord<0)+360
            y_bord = Map_world(countries(index)).Y  

            [in,on] = inpolygon(x,y,x_bord,y_bord) 
            row1 = row(in)
            col1 = col(in)

            line = size(row1)
            line = line(1)

            for i = 1 : line
                for j = 1 : num_year
                    if ~isnan(QIRRIG_YEAR(row1(i), col1(i), j))
                        QIRRIG_COUNTRY(index, j) = QIRRIG_COUNTRY(index, j) + QIRRIG_YEAR(row1(i), col1(i), j)
                    end
                end
            end
        else
            x_bord = Map_world(countries(index)).X
            x_bord(x_bord<0) = x_bord(x_bord<0)+360
            y_bord = Map_world(countries(index)).Y  

            [in,on] = inpolygon(x_unchanged,y,x_bord,y_bord) 
            row1 = row(in)
            col1 = col(in)

            line = size(row1)
            line = line(1)

            for i = 1 : line
                for j = 1 : num_year
                    if ~isnan(QIRRIG_YEAR(row1(i), col1(i), j))
                        QIRRIG_COUNTRY(index, j) = QIRRIG_COUNTRY(index, j) + QIRRIG_YEAR(row1(i), col1(i), j)
                    end
                end
            end
        end
        if (Qirr_obs_world(index, 4))% && QIRRIG_COUNTRY(index, 2))
            sum_bias = sum_bias + (QIRRIG_COUNTRY(index, 2) - Qirr_obs_world(index, 4))
            sum_rmse = sum_rmse + (QIRRIG_COUNTRY(index, 2) - Qirr_obs_world(index, 4))^2
            number = number + 1
        end
        if (Qirr_obs_world(index, 5))% && QIRRIG_COUNTRY(index, 7))
            sum_bias = sum_bias + (QIRRIG_COUNTRY(index, 7) - Qirr_obs_world(index, 5))
            sum_rmse = sum_rmse + (QIRRIG_COUNTRY(index, 7) - Qirr_obs_world(index, 5))^2
            number = number + 1
        end
    end
    bias_aqua(exp) = sum_bias / number
    rmse_aqua(exp) = (sum_rmse/ number)^(1/2)
    
    
    
    QIRRIG_PROVINCE = zeros(num_year,len_province)
    sum_bias = 0
    sum_rmse = 0
    number = 0
    for index = 1 : len_province
        x_bord = Map_china(province(index)).X
        x_bord(x_bord<0) = x_bord(x_bord<0)+360
        y_bord = Map_china(province(index)).Y  

        [in,on] = inpolygon(x_unchanged,y,x_bord,y_bord) 
        row1 = row(in)
        col1 = col(in)

        line = size(row1)
        line = line(1)
        for i = 1 : line
            for j = 1 : num_year
                if ~isnan(QIRRIG_YEAR(row1(i), col1(i), j))
                    QIRRIG_PROVINCE(j, index) = QIRRIG_PROVINCE(j, index) + QIRRIG_YEAR(row1(i), col1(i), j)
                end
            end
        end
        for year = 1 : 8
            sum_bias = sum_bias + (QIRRIG_PROVINCE(year, index) - Qirr_obs_china(year, index))
            sum_rmse = sum_rmse + (QIRRIG_PROVINCE(year, index) - Qirr_obs_china(year, index))^2
            number = number + 1
        end
    end
    bias_china(exp) = sum_bias / number
    rmse_china(exp) = (sum_rmse / number)^(1/2)
    
    QIRRIG_STATE = zeros(len_state, num_year)
    sum_bias = 0
    sum_rmse = 0
    number = 0
    for index = 1 : len_state
        x_bord = Map_usa(index).X
        %x_bord(x_bord<0) = x_bord(x_bord<0)+360
        y_bord = Map_usa(index).Y  

        [in,on] = inpolygon(x,y,x_bord,y_bord) 
        row1 = row(in)
        col1 = col(in)

        line = size(row1)
        line = line(1)
        for i = 1 : line
            for j = 1 : num_year
                if ~isnan(QIRRIG_YEAR(row1(i), col1(i), j))
                    QIRRIG_STATE(index, j) = QIRRIG_STATE(index, j) + QIRRIG_YEAR(row1(i), col1(i), j)
                end
            end
        end
        if (Qirr_obs_usa(index, 6))% && QIRRIG_STATE(index, 5))
            sum_bias = sum_bias + (QIRRIG_STATE(index, 5) - Qirr_obs_usa(index, 6))
            sum_rmse = sum_rmse + (QIRRIG_STATE(index, 5) - Qirr_obs_usa(index, 6))^2
            number = number + 1
        end
        if (Qirr_obs_usa(index, 7))% && QIRRIG_STATE(index, 10))
            sum_bias = sum_bias + (QIRRIG_STATE(index, 10) - Qirr_obs_usa(index, 7))
            sum_rmse = sum_rmse + (QIRRIG_STATE(index, 10) - Qirr_obs_usa(index, 7))^2
            number = number + 1
        end
    end
    bias_usa(exp) = sum_bias / number
    rmse_usa(exp) = (sum_rmse/ number)^(1/2)
end

    

