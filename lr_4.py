import pandas as pd
import random
def kubik(n: int) -> list:
    """

    :param n: Количество подбрасываний
    :return:  Список слкучайных подюрасываний кубика
    """
    data = []
    while len(data) <n:
        data.append(random.randint(1,6))
    return data

def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

def sorted_rate(counted_rate: dict):
    """
    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def create_dataframe(sorted_date: dict):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df

def probability_solving(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

# Выполним код для получения бросков кубика для 6 бросков каждым методом

df = kubik(6) #список
print(df)

df = count_rate(kubik(6)) #словарь
print(df)

df = sorted_rate(count_rate(kubik(6))) #отсортированный словарь
print(df)

df = create_dataframe(sorted_rate(count_rate(kubik(6)))) #датафрейм
print(df)

df = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(6)))))
print(df)

#Выполним аналогичный код для 100 бросков каждым методом

df = kubik(100) #список
print(df)

df = count_rate(kubik(100)) #словарь
print(df)

df = sorted_rate(count_rate(kubik(100))) #отсортированный словарь
print(df)

df = create_dataframe(sorted_rate(count_rate(kubik(100)))) #датафрейм
print(df)

df = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(100)))))
print(df)

#Выполним аналогичный код для 1000 бросков каждым методом

df = kubik(1000) #список
print(df)

df = count_rate(kubik(1000)) #словарь
print(df)

df = sorted_rate(count_rate(kubik(1000))) #отсортированный словарь
print(df)

df = create_dataframe(sorted_rate(count_rate(kubik(1000)))) #датафрейм
print(df)

df = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(1000)))))
print(df)

#Выполним аналогичный код для 10000 бросков каждым методом

df = kubik(10000) #список
print(df)

df = count_rate(kubik(10000)) #словарь
print(df)

df = sorted_rate(count_rate(kubik(10000))) #отсортированный словарь
print(df)

df = create_dataframe(sorted_rate(count_rate(kubik(10000)))) #датафрейм
print(df)

df = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(10000)))))
print(df)

#Выполним аналогичный код для 1000000 бросков каждым методом

df = kubik(1000000) #список
print(df)

df = count_rate(kubik(1000000)) #словарь
print(df)

df = sorted_rate(count_rate(kubik(1000000))) #отсортированный словарь
print(df)

df = create_dataframe(sorted_rate(count_rate(kubik(1000000)))) #датафрейм
print(df)

df = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(1000000)))))
print(df)


import matplotlib.pyplot as plt
proba = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(6)))))
print(proba)

plt.figure(figsize=(10, 5))
ax = proba['Вероятность'].plot(kind='barh', color='blue', alpha=0.5)
plt.xlabel('Вероятность')
plt.ylabel('Значение кубика')
plt.title('Распределение вероятностей при бросании кубика')
plt.grid(axis='x', linestyle='--')
plt.show()

#Построим гистограмму для 100 бросков
proba = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(100)))))
print(proba)

plt.figure(figsize=(10, 5))
ax = proba['Вероятность'].plot(kind='barh', color='blue', alpha=0.5)
plt.xlabel('Вероятность')
plt.ylabel('Значение кубика')
plt.title('Распределение вероятностей при бросании кубика')
plt.grid(axis='x', linestyle='--')
plt.show()

#Построим гистограмму для 1000 бросков
proba = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(1000)))))
print(proba)

plt.figure(figsize=(10, 5))
ax = proba['Вероятность'].plot(kind='barh', color='blue', alpha=0.5)
plt.xlabel('Вероятность')
plt.ylabel('Значение кубика')
plt.title('Распределение вероятностей при бросании кубика')
plt.grid(axis='x', linestyle='--')
plt.show()

#Построим гистограмму для 10000 бросков
proba = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(10000)))))
print(proba)

plt.figure(figsize=(10, 5))
ax = proba['Вероятность'].plot(kind='barh', color='blue', alpha=0.5)
plt.xlabel('Вероятность')
plt.ylabel('Значение кубика')
plt.title('Распределение вероятностей при бросании кубика')
plt.grid(axis='x', linestyle='--')
plt.show()

#Построим гистограмму для 1000000 бросков
proba = probability_solving(create_dataframe(sorted_rate(count_rate(kubik(1000000)))))
print(proba)

plt.figure(figsize=(10, 5))
ax = proba['Вероятность'].plot(kind='barh', color='blue', alpha=0.5)
plt.xlabel('Вероятность')
plt.ylabel('Значение кубика')
plt.title('Распределение вероятностей при бросании кубика')
plt.grid(axis='x', linestyle='--')
plt.show()