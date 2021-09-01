import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from planar_snake_prototype_RL.benchmark import plots

# matplotlib.style.use('ggplot')

def main():
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # dir = '/home/chris/openai_logdir/power_velocity/'
    dir = '/home/bing/openai_logdir/power_velocity/'

    my_plots = plots.Plots(None, dir)


    #args = parser.parse_args()
    #plots = Plots(None)
    #plots.plot_snake_gait(None)

    eq_fname='xxx_grid_search_results_600'
    eq_data = pd.read_csv(dir+eq_fname+'.csv')
    eq_data['controller'] = 15

    plt.figure(figsize=(8,4)) 
    my_plots.plot_velocity_power_diagram(eq_data, eq_fname)
    my_plots.plot_energy_distance_diagram(eq_data, eq_fname)

    ## Histogram Plot by Zhenshan bing ##
    my_plots.plot_hist_joint_power_diagram(eq_data, eq_fname)


    #eq_data.plot(x='velocity', y='power', kind='scatter', title='Grid search result: Equation-controller on velocity and power',
    #             xlim=[0, None], ylim=[0.0, 10000.0], figsize=(9, 6))
    #plt.savefig(dir + eq_fname + '_velocity_power_diagram.pdf')



    #fname = 'grid_search_results_2018-05-31_22:14:47__power_new7'
    # fname = 'grid_search_results_2018-06-02_22:36:23_new12'

    #name = 'grid_search_results_2018-05-29_17:11:29_new5'
    fname = 'x_grid_search_results_2018-07-02_15:43:47'
    ppo_data = pd.read_csv(dir+fname+'.csv')
    ppo_data['controller'] = 16

    #ppo_data.plot(x='velocity', y='power', kind='scatter',
    #             title='Grid search result: PPO-controller on velocity and power', xlim=[0, None],
    #             ylim=[0.0, None], figsize=(9, 6))
    #plt.savefig(dir + fname + '_velocity_power_diagram.pdf')

    my_plots.plot_velocity_power_diagram(ppo_data, fname)

    my_plots.plot_energy_distance_diagram(ppo_data, fname)







    # compare!
    #df = pd.concat([eq_data, ppo_data])
    fname_c = fname +'_' + eq_fname + '_compare'

    ppo_data['total_power_mWh'] = ppo_data['total_power_sec'] / 3600 * 1000
    eq_data['total_power_mWh'] = eq_data['total_power_sec'] / 3600 * 1000



    #ax = df.plot(x='velocity', y='power', c='controller', kind='scatter', colors=['r', 'g', 'b'], xlim=[0.0, 0.3], ylim=[0.0, 10000.0])
    #plt.figure(figsize=(8,5))
    ax = eq_data.plot(kind='scatter', x='velocity', y='total_power_mWh',  label = 'Equation controller', figsize=(9,5))
    

    bayes_opt_data_power = []
    bayes_opt_data_velocity = []

    for i in range(0, 12):
        df = pd.read_csv('./bayes_opt_data/bayes_opt_data_'+str(i)+'.csv', header=None, skiprows=1)
        a = df.values
        a = np.amax(a, axis=0)
        bayes_opt_data_power.append(a[0])
        bayes_opt_data_velocity.append(a[1])

    # plt.figure(figsize=(8,5))
    plt.scatter(bayes_opt_data_velocity, bayes_opt_data_power, marker='D', color='darkorange', label='Bayesian controller', s=20)



    # ppo_data.plot(kind='scatter', x='velocity', y='total_power_mWh',  color='red',
    #               label='PPO controller', ax = ax, xlim=[-0.02, 0.28], ylim=[-2, 50], figsize=(9, 5))#, figsize=(9,6))
    ax.set_xlabel("Velocity [m/s]")
    ax.set_ylabel("Total Power [mW]")


    # plt.legend('Equation controller', 'PPO controller', 'Bayes Controller')
    # plt.legend(loc='upper left')

    # plt.figure(figsize=(8,5)) 
    plt.legend(loc=2, prop={'size': 14})
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(16)
    plt.savefig(dir + fname_c + '_velocity_power_diagram_compare.pdf', bbox_inches='tight')
    plt.savefig(dir + fname_c + '_velocity_power_diagram_compare.png', dpi=1200, bbox_inches='tight')
    # print os.


if __name__ == '__main__':
    main()

