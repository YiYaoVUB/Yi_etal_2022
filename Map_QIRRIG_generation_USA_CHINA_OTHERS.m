str_surf = 'E:\Data_Evaluation\Surface_data\surfdata_0.9x1.25_hist_78pfts_CMIP6_simyr2000_c201126 - 副本.nc'
AREA=ncread(str_surf,'AREA')
LONGXY=ncread(str_surf,'LONGXY')
LATIXY=ncread(str_surf,'LATIXY')

num_year = 30

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
Qirr_obs_china = csvread('E:\Data_Evaluation\QIRRIG\chinadata1.csv')

str_map_usa = 'E:\Data_Evaluation\QIRRIG\States_shapefile-shp\States_shapefile.shp'
Map_usa = shaperead(str_map_usa)
Qirr_obs_usa = csvread('E:\Data_Evaluation\QIRRIG\usadata.csv')

str_middle = ["CTL","CTL_limit","IRR_meth","IRR_meth_limit","IRR_drai","IRR_new_nopool_limit","IRR_new_pool","IRR_new_pool_limit","IRR_new_satu","IRR_new_satu_limit"]
str_middle = ["CTL","IRR_meth","IRR_drai","IRR_pool","IRR_satu"]
len_expe = size(str_middle)
len_expe = len_expe(2)

%str_raw = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\'

str_raw = 'E:\Research1\QIRRIG\'
str_end = '\QIRRIG_yearmean_mm_year.nc'

countries = load('E:\Data_Evaluation\Scripts\data_needed.txt')
len_countries = size(countries)
len_countries = len_countries(1)

QIRRIG_AQUASTAT = zeros(len_countries, len_expe)

province = [13, 1, 14, 29, 20, 21, 25, 3, 17, 9, 18, 19, 8, 15, 7, 5, 31, 30, 16, 4, 28, 24, 2, 26, 12, 23, 22, 11, 10, 32, 27]
len_province = size(province)
len_province = len_province(2)

QIRRIG_CHINA = zeros(len_expe, len_province)

len_state = 51

QIRRIG_USA = zeros(len_state, len_expe)


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
    end
    QIRRIG_AQUASTAT(:,exp) = QIRRIG_COUNTRY(:, 17)
    
    
    
    
    QIRRIG_PROVINCE = zeros(num_year,len_province)
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
    end
    QIRRIG_CHINA(exp, :) = QIRRIG_PROVINCE(15, :)
    
    QIRRIG_STATE = zeros(len_state, num_year)
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
    end
    QIRRIG_USA(:, exp) = QIRRIG_STATE(:, 15)
end

% Calculation finished

str_map = 'E:\Data_Evaluation\World_Countries\World_Countries.shp'
Map_raw=shaperead(str_map)

Qirr_obs = csvread('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\aquastat_total.csv',1,1)
Qirr_obs(Qirr_obs==0) = NaN
Qirr_ctl = QIRRIG_AQUASTAT(:,1)
%Qirr_ctl(Qirr_ctl==0) = NaN
Qirr_irr = QIRRIG_AQUASTAT(:,2)
%Qirr_irr(Qirr_irr==0) = NaN
Qirr_irr_nopool = QIRRIG_AQUASTAT(:,3)
%Qirr_irr_nopool(Qirr_irr_nopool==0) = NaN
Qirr_irr_pool = QIRRIG_AQUASTAT(:,4)
%Qirr_irr_pool(Qirr_irr_pool==0) = NaN
Qirr_irr_satu = QIRRIG_AQUASTAT(:,5)
%Qirr_irr_satu(Qirr_irr_satu==0) = NaN

%Qirr_ctl_limit = QIRRIG_AQUASTAT(:,2)
%Qirr_ctl_limit(Qirr_ctl_limit==0) = NaN
%Qirr_irr_limit = QIRRIG_AQUASTAT(:,4)
%Qirr_irr_limit(Qirr_irr_limit==0) = NaN
%Qirr_irr_nopool_limit = QIRRIG_AQUASTAT(:,6)
%Qirr_irr_nopool_limit(Qirr_irr_nopool_limit==0) = NaN
%Qirr_irr_pool_limit = QIRRIG_AQUASTAT(:,8)
%Qirr_irr_pool_limit(Qirr_irr_pool_limit==0) = NaN
%Qirr_irr_satu_limit = QIRRIG_AQUASTAT(:,10)
%Qirr_irr_satu_limit(Qirr_irr_satu_limit==0) = NaN

len = size(Qirr_obs)
len = len(1)-2

for i = 1 : 35
   
    Map(i).Geometry = 'Polygon';
    Map(i).BoundingBox = Map_raw(Qirr_obs(i,8)).BoundingBox;
    Map(i).X = Map_raw(Qirr_obs(i,8)).X;
    Map(i).Y = Map_raw(Qirr_obs(i,8)).Y;
    Map(i).Name = Map_raw(Qirr_obs(i,8)).COUNTRY;
    
    Map(i).Obs = Qirr_obs(i,3)
    Map(i).Ctl = Qirr_ctl(i)
    Map(i).Irr = Qirr_irr(i)
    Map(i).Irr_drai = Qirr_irr_nopool(i)
    Map(i).Irr_pool = Qirr_irr_pool(i)
    Map(i).Irr_satu = Qirr_irr_satu(i)
    
    %Map(i).Ctl_limit = Qirr_ctl_limit(i)
    %Map(i).Irr_limit = Qirr_irr_limit(i)
    %Map(i).Irr_drai_limit = Qirr_irr_nopool_limit(i)
    %Map(i).Irr_pool_limit = Qirr_irr_pool_limit(i)
    %Map(i).Irr_satu_limit = Qirr_irr_satu_limit(i)
    
    Map(i).Bias_ctl = Qirr_ctl(i) - Qirr_obs(i,3)
    Map(i).Bias_irr = Qirr_irr(i) - Qirr_obs(i,3)
    Map(i).Bias_drai = Qirr_irr_nopool(i) - Qirr_obs(i,3)
    Map(i).Bias_pool = Qirr_irr_pool(i) - Qirr_obs(i,3)
    Map(i).Bias_satu = Qirr_irr_satu(i) - Qirr_obs(i,3)
    
    %Map(i).Bias_ctl_limit = Qirr_ctl_limit(i) - Qirr_obs(i,7)
    %Map(i).Bias_irr_limit = Qirr_irr_limit(i) - Qirr_obs(i,7)
    %Map(i).Bias_drai_limit = Qirr_irr_nopool_limit(i) - Qirr_obs(i,7)
    %Map(i).Bias_pool_limit = Qirr_irr_pool_limit(i) - Qirr_obs(i,7)
    %Map(i).Bias_satu_limit = Qirr_irr_satu_limit(i) - Qirr_obs(i,7)
    
    Map(i).AbBias_1 = abs(Qirr_irr(i)-Qirr_obs(i,3)) - abs(Qirr_ctl(i)-Qirr_obs(i,3))
    Map(i).AbBias_2 = abs(Qirr_irr_nopool(i)-Qirr_obs(i,3)) - abs(Qirr_ctl(i)-Qirr_obs(i,3))
    Map(i).AbBias_3 = abs(Qirr_irr_pool(i)-Qirr_obs(i,3)) - abs(Qirr_ctl(i)-Qirr_obs(i,3))
    Map(i).AbBias_4 = abs(Qirr_irr_satu(i)-Qirr_obs(i,3)) - abs(Qirr_ctl(i)-Qirr_obs(i,3))
    
    %Map(i).AbBias_5 = abs(Qirr_irr_limit(i)-Qirr_obs(i,7)) - abs(Qirr_ctl_limit(i)-Qirr_obs(i,7))
    %Map(i).AbBias_6 = abs(Qirr_irr_nopool_limit(i)-Qirr_obs(i,7)) - abs(Qirr_ctl_limit(i)-Qirr_obs(i,7))
    %Map(i).AbBias_7 = abs(Qirr_irr_pool_limit(i)-Qirr_obs(i,7)) - abs(Qirr_ctl_limit(i)-Qirr_obs(i,7))
    %Map(i).AbBias_8 = abs(Qirr_irr_satu_limit(i)-Qirr_obs(i,7)) - abs(Qirr_ctl_limit(i)-Qirr_obs(i,7))
    
    
    
end
for i = 36 : 190
   
    Map(i).Geometry = 'Polygon';
    Map(i).BoundingBox = Map_raw(Qirr_obs(i+1,8)).BoundingBox;
    Map(i).X = Map_raw(Qirr_obs(i+1,8)).X;
    Map(i).Y = Map_raw(Qirr_obs(i+1,8)).Y;
    Map(i).Name = Map_raw(Qirr_obs(i+1,8)).COUNTRY;
    
    Map(i).Obs = Qirr_obs(i+1,3)
    Map(i).Ctl = Qirr_ctl(i+1)
    Map(i).Irr = Qirr_irr(i+1)
    Map(i).Irr_drai = Qirr_irr_nopool(i+1)
    Map(i).Irr_pool = Qirr_irr_pool(i+1)
    Map(i).Irr_satu = Qirr_irr_satu(i+1)
    
    %Map(i).Ctl_limit = Qirr_ctl_limit(i+1)
    %Map(i).Irr_limit = Qirr_irr_limit(i+1)
    %Map(i).Irr_drai_limit = Qirr_irr_nopool_limit(i+1)
    %Map(i).Irr_pool_limit = Qirr_irr_pool_limit(i+1)
    %Map(i).Irr_satu_limit = Qirr_irr_satu_limit(i+1)
    
    Map(i).Bias_ctl = Qirr_ctl(i+1) - Qirr_obs(i+1,3)
    Map(i).Bias_irr = Qirr_irr(i+1) - Qirr_obs(i+1,3)
    Map(i).Bias_drai = Qirr_irr_nopool(i+1) - Qirr_obs(i+1,3)
    Map(i).Bias_pool = Qirr_irr_pool(i+1) - Qirr_obs(i+1,3)
    Map(i).Bias_satu = Qirr_irr_satu(i+1) - Qirr_obs(i+1,3)
    
    %Map(i).Bias_ctl_limit = Qirr_ctl_limit(i+1) - Qirr_obs(i+1,7)
    %Map(i).Bias_irr_limit = Qirr_irr_limit(i+1) - Qirr_obs(i+1,7)
    %Map(i).Bias_drai_limit = Qirr_irr_nopool_limit(i+1) - Qirr_obs(i+1,7)
    %Map(i).Bias_pool_limit = Qirr_irr_pool_limit(i+1) - Qirr_obs(i+1,7)
    %Map(i).Bias_satu_limit = Qirr_irr_satu_limit(i+1) - Qirr_obs(i+1,7)
    
    Map(i).AbBias_1 = abs(Qirr_irr(i+1)-Qirr_obs(i+1,3)) - abs(Qirr_ctl(i+1)-Qirr_obs(i+1,3))
    Map(i).AbBias_2 = abs(Qirr_irr_nopool(i+1)-Qirr_obs(i+1,3)) - abs(Qirr_ctl(i+1)-Qirr_obs(i+1,3))
    Map(i).AbBias_3 = abs(Qirr_irr_pool(i+1)-Qirr_obs(i+1,3)) - abs(Qirr_ctl(i+1)-Qirr_obs(i+1,3))
    Map(i).AbBias_4 = abs(Qirr_irr_satu(i+1)-Qirr_obs(i+1,3)) - abs(Qirr_ctl(i+1)-Qirr_obs(i+1,3))
    
    %Map(i).AbBias_5 = abs(Qirr_irr_limit(i+1)-Qirr_obs(i+1,7)) - abs(Qirr_ctl_limit(i+1)-Qirr_obs(i+1,7))
    %Map(i).AbBias_6 = abs(Qirr_irr_nopool_limit(i+1)-Qirr_obs(i+1,7)) - abs(Qirr_ctl_limit(i+1)-Qirr_obs(i+1,7))
    %Map(i).AbBias_7 = abs(Qirr_irr_pool_limit(i+1)-Qirr_obs(i+1,7)) - abs(Qirr_ctl_limit(i+1)-Qirr_obs(i+1,7))
    %Map(i).AbBias_8 = abs(Qirr_irr_satu_limit(i+1)-Qirr_obs(i+1,7)) - abs(Qirr_ctl_limit(i+1)-Qirr_obs(i+1,7))
    
end

for i = 191 : len
   
    Map(i).Geometry = 'Polygon';
    Map(i).BoundingBox = Map_raw(Qirr_obs(i+2,8)).BoundingBox;
    Map(i).X = Map_raw(Qirr_obs(i+2,8)).X;
    Map(i).Y = Map_raw(Qirr_obs(i+2,8)).Y;
    Map(i).Name = Map_raw(Qirr_obs(i+2,8)).COUNTRY;
    
    Map(i).Obs = Qirr_obs(i+2,3)
    Map(i).Ctl = Qirr_ctl(i+2)
    Map(i).Irr = Qirr_irr(i+2)
    Map(i).Irr_drai = Qirr_irr_nopool(i+2)
    Map(i).Irr_pool = Qirr_irr_pool(i+2)
    Map(i).Irr_satu = Qirr_irr_satu(i+2)
    
    %Map(i).Ctl_limit = Qirr_ctl_limit(i+2)
    %Map(i).Irr_limit = Qirr_irr_limit(i+2)
    %Map(i).Irr_drai_limit = Qirr_irr_nopool_limit(i+2)
    %Map(i).Irr_pool_limit = Qirr_irr_pool_limit(i+2)
    %Map(i).Irr_satu_limit = Qirr_irr_satu_limit(i+2)
    
    Map(i).Bias_ctl = Qirr_ctl(i+2) - Qirr_obs(i+2,3)
    Map(i).Bias_irr = Qirr_irr(i+2) - Qirr_obs(i+2,3)
    Map(i).Bias_drai = Qirr_irr_nopool(i+2) - Qirr_obs(i+2,3)
    Map(i).Bias_pool = Qirr_irr_pool(i+2) - Qirr_obs(i+2,3)
    Map(i).Bias_satu = Qirr_irr_satu(i+2) - Qirr_obs(i+2,3)
    
    %Map(i).Bias_ctl_limit = Qirr_ctl_limit(i+2) - Qirr_obs(i+2,7)
    %Map(i).Bias_irr_limit = Qirr_irr_limit(i+2) - Qirr_obs(i+2,7)
    %Map(i).Bias_drai_limit = Qirr_irr_nopool_limit(i+2) - Qirr_obs(i+2,7)
    %Map(i).Bias_pool_limit = Qirr_irr_pool_limit(i+2) - Qirr_obs(i+2,7)
    %Map(i).Bias_satu_limit = Qirr_irr_satu_limit(i+2) - Qirr_obs(i+2,7)
    
    Map(i).AbBias_1 = abs(Qirr_irr(i+2)-Qirr_obs(i+2,3)) - abs(Qirr_ctl(i+2)-Qirr_obs(i+2,3))
    Map(i).AbBias_2 = abs(Qirr_irr_nopool(i+2)-Qirr_obs(i+2,3)) - abs(Qirr_ctl(i+2)-Qirr_obs(i+2,3))
    Map(i).AbBias_3 = abs(Qirr_irr_pool(i+2)-Qirr_obs(i+2,3)) - abs(Qirr_ctl(i+2)-Qirr_obs(i+2,3))
    Map(i).AbBias_4 = abs(Qirr_irr_satu(i+2)-Qirr_obs(i+2,3)) - abs(Qirr_ctl(i+2)-Qirr_obs(i+2,3))
    
    %Map(i).AbBias_5 = abs(Qirr_irr_limit(i+2)-Qirr_obs(i+2,7)) - abs(Qirr_ctl_limit(i+2)-Qirr_obs(i+2,7))
    %Map(i).AbBias_6 = abs(Qirr_irr_nopool_limit(i+2)-Qirr_obs(i+2,7)) - abs(Qirr_ctl_limit(i+2)-Qirr_obs(i+2,7))
    %Map(i).AbBias_7 = abs(Qirr_irr_pool_limit(i+2)-Qirr_obs(i+2,7)) - abs(Qirr_ctl_limit(i+2)-Qirr_obs(i+2,7))
    %Map(i).AbBias_8 = abs(Qirr_irr_satu_limit(i+2)-Qirr_obs(i+2,7)) - abs(Qirr_ctl_limit(i+2)-Qirr_obs(i+2,7))
    
end

str_map = 'E:\Data_Evaluation\QIRRIG\区划\省.shp'
Map_raw = shaperead(str_map)
index = [13, 1, 14, 29, 20, 21, 25, 3, 17, 9, 18, 19, 8, 15, 7, 5, 31, 30, 16, 4, 28, 24, 2, 26, 12, 23, 22, 11, 10, 32, 27, 33, 34, 35]
name = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh']
Qirr_chn = csvread('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\China.csv')
Qirr_chn(Qirr_chn==0) = NaN

Qirr_ctl = zeros(1,34)
Qirr_irr = zeros(1,34)
Qirr_irr_nopool = zeros(1,34)
Qirr_irr_pool = zeros(1,34)
Qirr_irr_satu = zeros(1,34)

%Qirr_ctl_limit = zeros(1,34)
%Qirr_irr_limit = zeros(1,34)
%Qirr_irr_nopool_limit = zeros(1,34)
%Qirr_irr_pool_limit = zeros(1,34)
%Qirr_irr_satu_limit = zeros(1,34)

Qirr_ctl(1,1:31) = QIRRIG_CHINA(1,:)
%Qirr_ctl(Qirr_ctl==0) = NaN
Qirr_irr(1,1:31) = QIRRIG_CHINA(2,:)
%Qirr_irr(Qirr_irr==0) = NaN
Qirr_irr_nopool(1,1:31) = QIRRIG_CHINA(3,:)
%Qirr_irr_nopool(Qirr_irr_nopool==0) = NaN
Qirr_irr_pool(1,1:31) = QIRRIG_CHINA(4,:)
%Qirr_irr_pool(Qirr_irr_pool==0) = NaN
Qirr_irr_satu(1,1:31) = QIRRIG_CHINA(5,:)
%Qirr_irr_satu(Qirr_irr_satu==0) = NaN

%Qirr_ctl_limit(1,1:31) = QIRRIG_CHINA(2,:)
%Qirr_ctl_limit(Qirr_ctl_limit==0) = NaN
%Qirr_irr_limit(1,1:31) = QIRRIG_CHINA(4,:)
%Qirr_irr_limit(Qirr_irr_limit==0) = NaN
%Qirr_irr_nopool_limit(1,1:31) = QIRRIG_CHINA(6,:)
%Qirr_irr_nopool_limit(Qirr_irr_nopool_limit==0) = NaN
%Qirr_irr_pool_limit(1,1:31) = QIRRIG_CHINA(8,:)
%Qirr_irr_pool_limit(Qirr_irr_pool_limit==0) = NaN
%Qirr_irr_satu_limit(1,1:31) = QIRRIG_CHINA(10,:)
%Qirr_irr_satu_limit(Qirr_irr_satu_limit==0) = NaN


len_ch = size(index)
len_ch = len_ch(2)
for i = len+1 : len+len_ch
    Map(i).Geometry = 'Polygon';
	Map(i).BoundingBox = Map_raw(i-len).BoundingBox;
    Map(i).X = Map_raw(index(i-len)).X;
	Map(i).Y = Map_raw(index(i-len)).Y;
    Map(i).Name = name(i-len);
    
    Map(i).Obs = Qirr_chn(1,i-len)
    Map(i).Ctl = Qirr_ctl(i-len)
    Map(i).Irr = Qirr_irr(i-len)
    Map(i).Irr_drai = Qirr_irr_nopool(i-len)
    Map(i).Irr_pool = Qirr_irr_pool(i-len)
    Map(i).Irr_satu = Qirr_irr_satu(i-len)
    
    %Map(i).Ctl_limit = Qirr_ctl_limit(i-len)
    %Map(i).Irr_limit = Qirr_irr_limit(i-len)
    %Map(i).Irr_drai_limit = Qirr_irr_nopool_limit(i-len)
    %Map(i).Irr_pool_limit = Qirr_irr_pool_limit(i-len)
    %Map(i).Irr_satu_limit = Qirr_irr_satu_limit(i-len)
    
    Map(i).Bias_ctl = Qirr_ctl(i-len) - Qirr_chn(1,i-len)
    Map(i).Bias_irr = Qirr_irr(i-len) - Qirr_chn(1,i-len)
    Map(i).Bias_drai = Qirr_irr_nopool(i-len) - Qirr_chn(1,i-len)
    Map(i).Bias_pool = Qirr_irr_pool(i-len) - Qirr_chn(1,i-len)
    Map(i).Bias_satu = Qirr_irr_satu(i-len) - Qirr_chn(1,i-len)
    
    %Map(i).Bias_ctl_limit = Qirr_ctl_limit(i-len) - Qirr_chn(1,i-len)
    %Map(i).Bias_irr_limit = Qirr_irr_limit(i-len) - Qirr_chn(1,i-len)
    %Map(i).Bias_drai_limit = Qirr_irr_nopool_limit(i-len) - Qirr_chn(1,i-len)
    %Map(i).Bias_pool_limit = Qirr_irr_pool_limit(i-len) - Qirr_chn(1,i-len)
    %Map(i).Bias_satu_limit = Qirr_irr_satu_limit(i-len) - Qirr_chn(1,i-len)
    
    Map(i).AbBias_1 = abs(Qirr_irr(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl(i-len)-Qirr_chn(1,i-len))
    Map(i).AbBias_2 = abs(Qirr_irr_nopool(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl(i-len)-Qirr_chn(1,i-len))
    Map(i).AbBias_3 = abs(Qirr_irr_pool(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl(i-len)-Qirr_chn(1,i-len))
    Map(i).AbBias_4 = abs(Qirr_irr_satu(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl(i-len)-Qirr_chn(1,i-len))
    
    %Map(i).AbBias_5 = abs(Qirr_irr_limit(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl_limit(i-len)-Qirr_chn(1,i-len))
    %Map(i).AbBias_6 = abs(Qirr_irr_nopool_limit(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl_limit(i-len)-Qirr_chn(1,i-len))
    %Map(i).AbBias_7 = abs(Qirr_irr_pool_limit(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl_limit(i-len)-Qirr_chn(1,i-len))
    %Map(i).AbBias_8 = abs(Qirr_irr_satu_limit(i-len)-Qirr_chn(1,i-len)) - abs(Qirr_ctl_limit(i-len)-Qirr_chn(1,i-len))
end

str_map = 'E:\Data_Evaluation\QIRRIG\States_shapefile-shp\States_shapefile.shp'
Map_raw=shaperead(str_map)

Qirr_usa = csvread('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\USA.csv')
Qirr_usa(Qirr_usa==0) = NaN
Qirr_ctl = QIRRIG_USA(:,1)
%Qirr_ctl(Qirr_ctl==0) = NaN
Qirr_irr = QIRRIG_USA(:,2)
%Qirr_irr(Qirr_irr==0) = NaN
Qirr_irr_nopool = QIRRIG_USA(:,3)
%Qirr_irr_nopool(Qirr_irr_nopool==0) = NaN
Qirr_irr_pool = QIRRIG_USA(:,4)
%Qirr_irr_pool(Qirr_irr_pool==0) = NaN
Qirr_irr_satu = QIRRIG_USA(:,5)
%Qirr_irr_satu(Qirr_irr_satu==0) = NaN

%Qirr_ctl_limit = QIRRIG_USA(:,2)
%Qirr_ctl_limit(Qirr_ctl_limit==0) = NaN
%Qirr_irr_limit = QIRRIG_USA(:,4)
%Qirr_irr_limit(Qirr_irr_limit==0) = NaN
%Qirr_irr_nopool_limit = QIRRIG_USA(:,6)
%Qirr_irr_nopool_limit(Qirr_irr_nopool_limit==0) = NaN
%Qirr_irr_pool_limit = QIRRIG_USA(:,8)
%Qirr_irr_pool_limit(Qirr_irr_pool_limit==0) = NaN
%Qirr_irr_satu_limit = QIRRIG_USA(:,10)
%Qirr_irr_satu_limit(Qirr_irr_satu_limit==0) = NaN

len_us = 51
for i = len+len_ch+1 : len+len_ch+len_us
    Map(i).Geometry = 'Polygon';
    Map(i).BoundingBox = Map_raw(i-len-len_ch).BoundingBox;
    Map(i).X = Map_raw(i-len-len_ch).X;
	Map(i).Y = Map_raw(i-len-len_ch).Y;
    Map(i).Name = Map_raw(i-len-len_ch).State_Name;
    
    Map(i).Obs = Qirr_usa(i-len-len_ch,1)
    Map(i).Ctl = Qirr_ctl(i-len-len_ch)
    Map(i).Irr = Qirr_irr(i-len-len_ch)
    Map(i).Irr_drai = Qirr_irr_nopool(i-len-len_ch)
    Map(i).Irr_pool = Qirr_irr_pool(i-len-len_ch)
    Map(i).Irr_satu = Qirr_irr_satu(i-len-len_ch)
    
    %Map(i).Ctl_limit = Qirr_ctl_limit(i-len-len_ch)
    %Map(i).Irr_limit = Qirr_irr_limit(i-len-len_ch)
    %Map(i).Irr_drai_limit = Qirr_irr_nopool_limit(i-len-len_ch)
    %Map(i).Irr_pool_limit = Qirr_irr_pool_limit(i-len-len_ch)
    %Map(i).Irr_satu_limit = Qirr_irr_satu_limit(i-len-len_ch)
    
    Map(i).Bias_ctl = Qirr_ctl(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    Map(i).Bias_irr = Qirr_irr(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    Map(i).Bias_drai = Qirr_irr_nopool(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    Map(i).Bias_pool = Qirr_irr_pool(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    Map(i).Bias_satu = Qirr_irr_satu(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    
    %Map(i).Bias_ctl_limit = Qirr_ctl_limit(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    %Map(i).Bias_irr_limit = Qirr_irr_limit(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    %Map(i).Bias_drai_limit = Qirr_irr_nopool_limit(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    %Map(i).Bias_pool_limit = Qirr_irr_pool_limit(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    %Map(i).Bias_satu_limit = Qirr_irr_satu_limit(i-len-len_ch) - Qirr_usa(i-len-len_ch,1)
    
    Map(i).AbBias_1 = abs(Qirr_irr(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    Map(i).AbBias_2 = abs(Qirr_irr_nopool(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    Map(i).AbBias_3 = abs(Qirr_irr_pool(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    Map(i).AbBias_4 = abs(Qirr_irr_satu(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    
    %Map(i).AbBias_5 = abs(Qirr_irr_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    %Map(i).AbBias_6 = abs(Qirr_irr_nopool_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    %Map(i).AbBias_7 = abs(Qirr_irr_pool_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
    %Map(i).AbBias_8 = abs(Qirr_irr_satu_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1)) - abs(Qirr_ctl_limit(i-len-len_ch)-Qirr_usa(i-len-len_ch,1))
end

str_map = 'E:\Data_Evaluation\World_Countries\World_Countries.shp'
Map_raw=shaperead(str_map)
data_lacked = csvread('E:\Data_Evaluation\QIRRIG\data_lacked.csv')
for i = len+len_ch+len_us+1 : 286
    Map(i).Geometry = 'Polygon';
	Map(i).BoundingBox = Map_raw(data_lacked(i-(len+len_ch+len_us))).BoundingBox;
    Map(i).X = Map_raw(data_lacked(i-(len+len_ch+len_us))).X;
	Map(i).Y = Map_raw(data_lacked(i-(len+len_ch+len_us))).Y;
    Map(i).Name = Map_raw(data_lacked(i-(len+len_ch+len_us))).COUNTRY;
    Map(i).Obs = NaN
    Map(i).Irr = NaN
    Map(i).Ctl = NaN
    Map(i).Irr_drai = NaN
    Map(i).Irr_pool = NaN
    Map(i).Irr_satu = NaN
    
    %Map(i).Ctl_limit = NaN
    %Map(i).Irr_limit = NaN
    %Map(i).Irr_drai_limit = NaN
    %Map(i).Irr_pool_limit = NaN
    %Map(i).Irr_satu_limit = NaN
    
    Map(i).Bias_ctl = NaN
    Map(i).Bias_irr = NaN
    Map(i).Bias_drai = NaN
    Map(i).Bias_pool = NaN
    Map(i).Bias_satu = NaN
    
    %Map(i).Bias_ctl_limit = NaN
    %Map(i).Bias_irr_limit = NaN
    %Map(i).Bias_drai_limit = NaN
    %Map(i).Bias_pool_limit = NaN
    %Map(i).Bias_satu_limit = NaN
    
    Map(i).AbBias_1 = NaN
    Map(i).AbBias_2 = NaN
    Map(i).AbBias_3 = NaN
    Map(i).AbBias_4 = NaN
    
    %Map(i).AbBias_5 = NaN
    %Map(i).AbBias_6 = NaN
    %Map(i).AbBias_7 = NaN
    %Map(i).AbBias_8 =NaN

end
for i = 287 : 287+52
    Map(i).Geometry = 'Polygon';
	Map(i).BoundingBox = Map_raw(data_lacked(i-286)).BoundingBox;
    Map(i).X = Map_raw(data_lacked(i-286)).X;
	Map(i).Y = Map_raw(data_lacked(i-286)).Y;
    Map(i).Name = Map_raw(data_lacked(i-286)).COUNTRY;
    Map(i).Obs = NaN
    Map(i).Irr = NaN
    Map(i).Ctl = NaN
    Map(i).Irr_drai = NaN
    Map(i).Irr_pool = NaN
    Map(i).Irr_satu = NaN
    
    %Map(i).Ctl_limit = NaN
    %Map(i).Irr_limit = NaN
    %Map(i).Irr_drai_limit = NaN
    %Map(i).Irr_pool_limit = NaN
    %Map(i).Irr_satu_limit = NaN
    
    Map(i).Bias_ctl = NaN
    Map(i).Bias_irr = NaN
    Map(i).Bias_drai = NaN
    Map(i).Bias_pool = NaN
    Map(i).Bias_satu = NaN
    
    %Map(i).Bias_ctl_limit = NaN
    %Map(i).Bias_irr_limit = NaN
    %Map(i).Bias_drai_limit = NaN
    %Map(i).Bias_pool_limit = NaN
    %Map(i).Bias_satu_limit = NaN
    
    Map(i).AbBias_1 = NaN
    Map(i).AbBias_2 = NaN
    Map(i).AbBias_3 = NaN
    Map(i).AbBias_4 = NaN
    
    %Map(i).AbBias_5 = NaN
    %Map(i).AbBias_6 = NaN
    %Map(i).AbBias_7 = NaN
    %Map(i).AbBias_8 =NaN
end

shapewrite(Map,'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Example_final_final_final.shp');
