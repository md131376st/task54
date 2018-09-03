# cf.csv for categorical and numeric data
#example.csv for boolean data


import pandas as pd
import matplotlib.pyplot as plt

# def data_statistics():
#
#
#
#     data = pd.read_csv('cf.csv')                #read csv file
#     print(data.info)                                 #print information of data
#     target = data['LAW_CAT_CD']                         #define target
#     type_of_target = target.dtypes                   #detect type of target
#     #print(type_of_target)
#     print("Number of attributes: ")
#     print(data.count())                              #number of attributes
#
#     print("Number of variables by data type:")
#     print(data.dtypes.value_counts())                #number of variables by data type
#
#     isBool = True                                    #flag for detecting boolean data
#
#
#     if(type_of_target == 'object'):
#         statistics_of_categorical_data(target)       #statistics of categorical data
#     else:
#         for each in target:
#             if (each != 0 and each != 1):
#                 isBool = False
#                 break
#         if isBool == True:
#             statistics_of_binary_data(target)        #statistics of binary data
#         else:
#             statistics_of_numerical_data(target)     #statistics of numerical data
#


def statistics_of_binary_data(target):

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
    plt.show()
    plt.savefig("media/")

def statistics_of_categorical_data(target):

    target_list = list()

    for each in target:
        target_list.append(each)
   # print(target_list)

    target_set = list(set(target_list))            #use the set to unify labels

    numbers_of_occurance = list()
    for each in target_set:                        #get numbers of unique labels
        numbers_of_occurance.append(target_list.count(each))

    _sum = sum(numbers_of_occurance)
    numbers = [x / _sum * 100  for x in numbers_of_occurance]#convert numbers of occurance to percentage

    min_index = numbers.index(min(numbers))        #get index of most frequent and least frequent labels
    max_index = numbers.index(max(numbers))

    #print(target_set)
    #print(numbers_of_occurance)
    print("most frequent label is:")
    print(target_set[max_index])                  #print most frequent label

    print("least frequent label is: ")
    print(target_set[min_index])                  #print least frequeent label


    plt.figure(1, figsize=(9, 3))                 #draw different plots

    plt.subplot(131)
    plt.bar(target_set,numbers)


    plt.subplot(132)
    plt.scatter(target_set, numbers)

    plt.subplot(133)
    plt.plot(target_set, numbers)

    plt.suptitle('Categorical Plotting')
    plt.show()
    plt.savefig("media/")

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

    out = pd.cut(target, bins=[min_of_data, range_of_bins + min_of_data, range_of_bins*2 + min_of_data, max_of_data], include_lowest=True) #darw plot
    ax = out.value_counts(sort=False).plot.bar(rot=0, color="b", figsize=(6, 4))
    plt.show()
    plt.savefig("media/")


# data_statistics() #call main function






