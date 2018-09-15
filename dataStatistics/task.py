# cf.csv for categorical and numeric data
#example.csv for boolean data
from django.shortcuts import render

import pandas as pd
import matplotlib.pyplot as plt, mpld3
from django.http import HttpResponse




def statistics_of_binary_data(target):
    # the next line has to be hare to be able to use mpld3.fig_to_html
    fig = plt.figure()
    target_list = list()
    target_set = ['0','1']
    #print(target)

    for each in target:
        target_list.append(each)
    #print(target_list)
    numbers_of_occurance = list()
    numbers_of_occurance.append(target_list.count(0)) #get numbers of occurance of 0 and 1 in dataset(true and false)
    numbers_of_occurance.append(target_list.count(1))


    #print(numbers_of_occurance)

    _sum = sum(numbers_of_occurance)
    numbers = [x / _sum * 100 for x in numbers_of_occurance]#convert numbers of occurance to percentage

    plt.figure(1, figsize=(9, 3))

    plt.subplot(131)                                #draw different plots
    plt.bar(target_set, numbers)

    plt.subplot(132)
    plt.scatter(target_set, numbers)

    plt.subplot(133)
    plt.plot(target_set, numbers)
    
    plt.suptitle('Binaery Plotting')
    # cheak if the plot is correct
    plt.show()
    
    # mpld3 makes are plot to html and returns it 
    mpld3.fig_to_html(fig)
    # mpld3.show()
    
    return HttpResponse(mpld3.fig_to_html(fig, template_type="simple"))


def statistics_of_categorical_data(target):
    target_list = list()
    fig = plt.figure()
    for each in target:
        target_list.append(each)

    target_set = list(set(target_list))  # use the set to unify labels

    numbers_of_occurance = list()

    for each in target_set:  # get numbers of unique labels
        numbers_of_occurance.append(target_list.count(each))

    _sum = sum(numbers_of_occurance)
    numbers = [x / _sum * 100 for x in numbers_of_occurance]  # convert numbers of occurance to percentage

    min_index = numbers.index(min(numbers))  # get index of most frequent and least frequent labels
    max_index = numbers.index(max(numbers))

    print("most frequent label is:")
    print(target_set[max_index])  # print most frequent label

    print("least frequent label is: ")
    print(target_set[min_index])  # print least frequeent label
    # print("life:", target_set)
    plt.figure(1, figsize=(9, 3))  # draw different p
    # print("life:", target_set)
    # lots

    plt.subplot(131)
    plt.bar(target_set, numbers)

    plt.subplot(132)
    plt.scatter(target_set, numbers)

    plt.subplot(133)
    plt.plot(target_set, numbers)

    plt.suptitle('Categorical Plotting')
    plt.show()
    # print(mpld3.fig_to_html(fig))
    # print(mpld3.fig_to_html(fig))
      # mpld3 makes are plot to html and returns it 
    mpld3.fig_to_html(fig, template_type="simple")
    return HttpResponse(mpld3.fig_to_html(fig, template_type="simple"))

def statistics_of_numerical_data(target):

    min_of_data = target.min()
    mean_of_data = target.mean()
    max_of_data = target.max()
    range_of_data = max_of_data - min_of_data       #get range of value for plotting
    number_of_bins = 3                              #define numbers of bins
    range_of_bins = range_of_data / number_of_bins  #define range of each bins

    print("Min of target is: ")
    print(min_of_data)                              #print min of target

    print("Max of target is: ")
    print(max_of_data)                              #print max of target

    print("Mean of target is: ")
    print(mean_of_data)                             #print mean of target
     # the next line has to be hare to be able to use mpld3.fig_to_html
    fig = plt.figure()
    out = pd.cut(target, bins=[min_of_data, range_of_bins + min_of_data, range_of_bins*2 + min_of_data, max_of_data], include_lowest=True) #darw plot
    ax = out.value_counts(sort=False).plot.bar(rot=0, color="b", figsize=(6, 4))
      # mpld3 makes are plot to html and returns it 
    mpld3.fig_to_html(fig)
    return HttpResponse(mpld3.fig_to_html(fig,template_type="simple"))


# data_statistics() #call main function






