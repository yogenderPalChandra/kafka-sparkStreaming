import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as clrs

path ="./csvFile_2021_01_27.csv"
listColors = ["b","g","r","c","m","y","k","b","g","r","c","m","y","k","b","g","r","c","m","y"]
#Try with other file and use to remove the columns to see if
# its again 34 columns - No Dosent work, gives just 4 columns
df = pd.read_csv(path, sep = ';', encoding = 'unicode_escape', skiprows = 5, error_bad_lines=False)

#df2 = pd.read_csv(path2, sep = ';', encoding = 'unicode_escape', skiprows = 5)


df = df.stack().str.replace(',','.').unstack()

#df2 = df2.stack().str.replace(',','.').unstack()


#df = df.dropna(axis='columns')

df_tem = df.iloc[:, 2:]

df = df_tem.applymap(float)

df2 = pd.read_csv(path2, sep = ';', encoding = 'unicode_escape', skiprows = 5)

df2 = df2.stack().str.replace(',','.').unstack()

df2 = df2.iloc[:, 2:-10]

df2 = df2.dropna(axis = 0)

df2 = df2.applymap(float)




df3 = pd.read_csv(path3, sep = ';', encoding = 'unicode_escape', skiprows = 5)

df3 = df3.stack().str.replace(',','.').unstack()

df3 = df3.iloc[:, 2:-25]

df3 = df3.dropna(axis = 0)

df3 = df3.applymap(float)

string = [x for x in  df3.iloc[:,1].str.contains('43:33')]

df3 = df3.replace(r'^([A-Za-z]|[0-9]|_)+$', np.NaN, regex=True)

def killString(df):
    for col in df.columns:
        x = pd.to_numeric(df[col], errors='coerce')
    return x
string_re_moved = killString(df3)


def l_dfs()
def killString(df):
    x= [pd.to_numeric(df[col], errors='coerce') for col in df.columns]
    return x
string_re_moved = killString(df3)
    

def df_tankStrat(df):
    columnsName = [f'M{i}: øC' for i in range(80, 100)]
    return df.loc[:, columnsName ]
df_tankStratTem, df2_tankStratTem = df_tankStrat(df), df_tankStrat(df2)

def create_color_step_obj(cmap_name, n):
    """
    Return scalarMap object with n colors in gradient from color map
    given in cmap_name.
    """
    cmap = plt.get_cmap(cmap_name)
    values = range(n)
    cNorm  = clrs.Normalize(vmin=values[0], vmax=values[-1])
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
    return(scalarMap)

def temProfile(df, df_full, cmap_name = "jet", alpha =0.7):
    x = df.index
    y = df
    scm = create_color_step_obj(cmap_name, 20)
    plt.figure()
    for i in range(0, 20):
        plt.plot(x, df.iloc[:, i], label = 'Layer ' + str(20-i), color= scm.to_rgba(20-i, alpha))
    #plt.plot(x, df.iloc[:, 3], label = 'Condensor out', linestyle = '-.', marker='.', ms=3, markevery= 3)
    plt.plot(x, df_full.iloc[:, 3], label = 'Condensor out', linestyle = ':', color = 'g')
    plt.plot(x, df_full.iloc[:, 4], label = 'Condensor In', linestyle = '-.', color = 'r')
    plt.plot(x, df_full.iloc[:, 5], label = 'tank out to load', linestyle = '--', color = 'b')
    plt.plot(x, df_full.iloc[:, 6], label = 'tank in from load', linestyle = '--', color ='m')
    plt.plot(x, df_full.iloc[:, 7], label = 'mixing tem (thermostat load tem )', linestyle = '--', color = 'c')
    plt.plot(x, df_full.iloc[:, 11], label = 'load tank tem (mid)', linestyle = '--', color = 'y')
    plt.legend(loc=1, bbox_to_anchor=(1.23,1), fontsize='small')
    plt.title("Temperature profile - Thermosta = 35C, pump=25%, max/o=45, max/in =40, Load=20C")
    plt.show()

temProfile(df2_tankStratTem, df2, alpha=0.7)



def headAddition(df):
   x= df.iloc[:, 8]*(1/3600)*(1/1000)*1000*4.18*(df.iloc[:, 3] - df.iloc[:, 4])
   return x, x.sum(axis=0)*(5/3600)
heatAddition_kjPers, heatAddition_kWh = headAddition(df2)


def loadkjPerS(df):
    x = df.iloc[:, 10]*(1/3600)*(1/1000)*1000*4.18*(df.iloc[:, 5] - df.iloc[:, 6])
    return x, x.sum(axis=0)*(5/3600)

load_kJPerS, load_kWh = loadkjPerS(df2)

def temProfile(df, df_full, heat_addition_kjPerS, cmap_name = "jet", alpha =0.7):
    x = df.index
    y = df
    scm = create_color_step_obj(cmap_name, 20)
    #fig=plt.figure()
    fig, ax1 = plt.subplots()
    for i in range(0, 20):
        
        #ax1.set_ylabel('Tem', color=red)
        ax1.set_xlabel('Index')
        ax1.set_ylabel('Tem, heat addition kj/s', color='r')
        ax1.plot(x, df.iloc[:, i], label = 'Layer ' + str(20-i), color= scm.to_rgba(20-i, alpha))
    ax1.plot(x, df_full.iloc[:, 3], label = 'Condensor out', linestyle = ':', color = 'g')
    ax1.plot(x, df_full.iloc[:, 4], label = 'Condensor In', linestyle = '-.', color = 'r')
    ax1.plot(x, df_full.iloc[:, 5], label = 'tank out to load', linestyle = '--', color = 'b')
    ax1.plot(x, df_full.iloc[:, 6], label = 'tank in from load', linestyle = '--', color ='m')
    ax1.plot(x, df_full.iloc[:, 7], label = 'mixing tem (thermostat load tem )', linestyle = '--', color = 'c')
    ax1.plot(x, df_full.iloc[:, 11], label = 'load tank tem (mid)', linestyle = '--', color = 'y')
    ax1.plot(x, heat_addition_kjPerS, label = 'heat addition -kj/s', linestyle = '--', color = 'k')
    ax1.plot(x, load_kJPerS, label = 'load - kj/s', linestyle = ':', color = 'k')
    
    plt.legend(loc=1, bbox_to_anchor=(1.23,0.8), fontsize='small')

    ax2 = ax1.twinx()
    
    ax2.set_ylabel('flow rate', color='b')
    ax2.plot(x, df_full.iloc[:, 8], label = 'cond. flow rate l/h', linestyle='dashed',  marker='^', markersize=4, markevery = 9, color = 'b')
    ax2.plot(x, df_full.iloc[:, 10], label = 'dischare flow rate l/h', linestyle='dashed',  marker='H', markersize=4, markevery=9, color = 'b')
    plt.legend(loc=1, bbox_to_anchor=(1.1,1), fontsize='small')
    plt.title("Temperature profile - Thermosta = 35C, pump=25%, max/o=45, max/in =40, Load=20C")
    plt.show()

temProfile(df2_tankStratTem,  df2, heatAddition_kjPers, cmap_name = "jet", alpha=0.7)



'''
def temProfile(listOfDfs_scaledTime,
               listOfDfs_tem,
               colors,
               markers,
               labels,
               xlabel = "Dimensionless time",
              ylabel = "Dimensionless Temperature"):
    plt.figure()
    ttl = plt.title("Temperature profile")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    for dfs_time, dfs_tem in zip(listOfDfs_scaledTime, listOfDfs_tem):
        xdata = dfs_time
        ydata = dfs_tem
        for i in range(0, 20):
            plt.plot(xdata, ydata.iloc[:,i], color= colors[i], marker = markers[i],label = labels[i], ms = 3, markevery = 20)
        plt.legend()
        plt.show()
TemProfile = temProfile(timeScaled,
                        temScaled,
                        listColors,
                        listMarkers,
                        reversedTemlegends,
                        xlabel = "Dimensionless time",
                        ylabel = "Dimensionless Temperature")
