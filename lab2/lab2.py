import pandas as pd

#1
df = pd.read_csv("math_students.csv")

#2
print("Первые 10 строк:")
print(df.head(10))
print("\nПоследние 10 строк:")
print(df.tail(10))

#3
print("\nРазмер датасета:")
print(df.size)

#4
print("\nНазвания колонок:")
print(df.columns)

#5
missing_values = df.isnull().sum()
if missing_values.sum() > 0:
    print("\nВ данных есть пропуски.")
else:
    print("\nПропуски в данных отсутствуют.")

#6
print("\nСтатистика по значениям признаков:")
print(df.describe())

#7
print("\nОписание значений признаков")
df.info()

#8
print("\nУникальные значения признака 'guardian':")
print(df['guardian'].unique())
print("\nЧастота каждого значения признака 'guardian':")
print(df['guardian'].value_counts())

#9
filtered_students = df[(df['guardian'] == "mother") & (df['Mjob'] == "teacher") | (df['Mjob']=="at_home")]
print("\nСтуденты, у которых опекуном является мать и она работает учителем или на дому:")
print(filtered_students)

#10
df['alc'] = df['Dalc'] + df['Walc']

#11
print("\nНовый размер датасета:", df.shape)
print("\nНовые колонки:")
print(df.columns)

#12
print("\nСамая частая причина выбора школы:", df['reason'].value_counts().idxmax())

#13
no_edu = df[(df['Fedu'] == 0) & (df['Medu'] == 0)]
print("\nКоличество студентов, у родителей которых нет никакого образования:", len(no_edu))
print("\nИнформация о студентах:")
print(no_edu)

#14
ms_students = df[df['school']=="MS"]
min_age = ms_students['age'].min()
print("\nМинимальный возраст учащегося в школе Mousinho da Silveira:", min_age)
print("\nИнформация об учащихся с минимальным возрастом:")
print(ms_students[ms_students['age']==min_age])

#15
odd_absences = df[df['absences'] % 2 != 0]
print("\nКоличество студентов с нечетным числом пропусков:", len(odd_absences))
print("\nИнформация о студентах:")
print(odd_absences)

#16
avg_G3 = df.groupby('romantic')['G3'].mean()
difference = abs(avg_G3['yes'] - avg_G3['no']) 
print("\nРазность между средними итоговыми оценками студентов в романтических и не романтических отношениях:", round(difference, 2))

#17
df['study_time_ratio'] = df['studytime'] / (df['studytime'] + df['freetime'])

#18
print("\nНаиболее распространенное количество несданных предметов:", df['failures'].value_counts().idxmax())

#19
work_par_students = df[(df['Mjob']!="at_home") & (df['Fjob']!="at_home")]
print("\nКоличество студентов, чьи мать и отец работают:", len(work_par_students))
print("\nИнформация о студентах:")
print(work_par_students)

#20
parent_service = df[(df['Mjob'] == "services")&(df['Fjob'] == "services")]
max_age = parent_service['age'].max()
print("\nМаксимальный возраст студентов, у которых оба родителя работают в сфере услуг:", max_age)
print("\nИнформация о студентах:")
print(parent_service[parent_service['age']==max_age])

#21
above_avg = df[(df['G1'] > df['G1'].mean())]
print("\nКоличество студентов, имеющих оценку за первый семестр выше среднего балла:", len(above_avg))
print("\nИнформация о студентах:")
print(above_avg)

#22
high_edu = df[df['Medu']==4]
low_edu = df[df['Medu']!=4]
print("\nРазница средних итоговых оценок двумя группами студентов:",abs(high_edu['G3'].mean() - low_edu['G3'].mean()))
