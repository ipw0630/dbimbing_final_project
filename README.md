<<<<<<< HEAD
# Dibimbing Final Project

# Data Source 
 link kaggle : https://www.kaggle.com/datasets/rabieelkharoua/predict-pet-adoption-status-dataset?resource=download&select=pet_adoption_data.csv

# Project Background's 
- For Today’s digital age, monitoring and analyzing data are crucial for understanding trends and making informed decisions. This project focuses on monitoring pet adoption data using Grafana, a powerful tool for visualizing and analyzing metrics. By leveraging Grafana's capabilities, we can track various metrics related to pet adoption, such as adoption rates, time spent in shelters, adoption fees, and more.

# Objectives
Real-time Monitoring: Utilize Grafana to monitor real-time updates on pet adoption metrics.
Visualization: Create interactive dashboards to visualize adoption trends, including geographical distribution, age preferences, and adoption likelihood.
Data Analysis: Perform in-depth analysis to identify patterns and correlations within the adoption data.
Performance Tracking: Monitor shelter efficiency metrics like average time pets spend in shelters before adoption.

# Transformation & Consideration
- ![alt text](image-1.png)
- Transformation 
<!-- ` def transform_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data', task_ids='extract_csv')
    df = pd.DataFrame.from_dict(raw_data)
    df['AgeCategory'] = df['AgeMonths'].apply(lambda x: 'kitten/puppy' if x < 12 else 'young' if x < 36 else 'adult' if x < 84 else 'senior')
    kwargs['ti'].xcom_push(key='transformed_data', value=df.to_dict())` -->
- On mysql 
![alt text](<WhatsApp Image 2024-07-14 at 23.42.44_9afabd27.jpg>) | ![alt text](<WhatsApp Image 2024-07-14 at 23.43.19_cda849c5.jpg>)

# To run this repo must have docker, dbeaver
1. clone this repo
2. after clone cd project_airflow for the running project er airflow
    2.1 Run docker compose up -d, to up container `airflow`
3. Open terminal then run docker-mysql 
    3.1 cd docker-mysql, lalu jalankan docker compose up -d
4. Open another terminal to run docker-graphana, to monitor the live time of the DAGS that has been created

Here's the progress that has been made 

![alt text](<WhatsApp Image 2024-07-10 at 22.17.13_d98397ac.jpg>)

![alt text](<WhatsApp Image 2024-07-10 at 22.17.39_ad9bd047.jpg>)

![alt text](image.png)
![alt text](<WhatsApp Image 2024-07-10 at 22.35.13_10b9589a.jpg>)

# Conclusion & Recommendation
- Conclusion: By implementing Grafana for monitoring pet adoption data, this project aims to provide shelters, animal welfare organizations, and policymakers with actionable insights to improve adoption processes, optimize resource allocation, and ultimately enhance the welfare of animals in need.
Future Directions: 
- Future enhancements could include predictive analytics for adoption trends, integrating additional data sources for enriched analysis, and expanding dashboard functionalities to include public engagement metrics.

# please contact me to enhancement this repo 

thanks
=======
# Dibimbing Final Project

untuk menjalankan repo ini wajib memiliki docker, dbeaver
1. clone this repo
2. after clone cd project_airflow untuk masuk kedalam folder airflow
    2.1 jalankan perintah docker compose up -d, untuk menjalankan airflow di dalam docker
3. buka terminal lainnya untuk menjalankan docker-mysql 
    3.1 cd docker-mysql, lalu jalankan docker compose up -d
4. buka terminal lainnya untuk menjalankan docker-grafana, untuk memonitoring secara live time dari DAGS yang sudah dibuat

berikut progress yang sudah dijalankan 
Airflow
![WhatsApp Image 2024-07-10 at 22 17 13_7b68857f](https://github.com/ipw0630/dbimbing_final_project/assets/166195995/8bab0019-816f-4fe8-ac9d-3f5d9e5048fd)

on dbeaver
![WhatsApp Image 2024-07-10 at 22 17 39_cb3a1c64](https://github.com/ipw0630/dbimbing_final_project/assets/166195995/1ba8d942-df0d-44ce-9217-ee48595055b8)

![WhatsApp Image 2024-07-10 at 23 43 11_4e4d755b](https://github.com/ipw0630/dbimbing_final_project/assets/166195995/6ebcc7af-f904-4f5e-bc55-e9303597d4c7)
![WhatsApp Image 2024-07-10 at 22 35 13_0809aa82](https://github.com/ipw0630/dbimbing_final_project/assets/166195995/88c3e72d-c9f8-4456-86b2-c0122408e437)

# please contact me to enhancement this repo 

thanks
>>>>>>> 52343caed02a8972a250706e7e2a5982e0a01782
