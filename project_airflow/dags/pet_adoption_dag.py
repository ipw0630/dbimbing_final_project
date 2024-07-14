from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.hooks.mysql_hook import MySqlHook
from airflow.utils.dates import days_ago
import pandas as pd
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

file_path = '/opt/airflow/data/pet_adoption_data.csv'

def verify_path(**kwargs):
    print("Current working directory:", os.getcwd())
    print("Files in the directory:", os.listdir('/opt/airflow/data/'))

def read_csv_file(**kwargs):
    df = pd.read_csv(file_path)
    kwargs['ti'].xcom_push(key='raw_data', value=df.to_dict())

def transform_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data', task_ids='extract_csv')
    df = pd.DataFrame.from_dict(raw_data)
    df['AgeCategory'] = df['AgeMonths'].apply(lambda x: 'kitten/puppy' if x < 12 else 'young' if x < 36 else 'adult' if x < 84 else 'senior')
    kwargs['ti'].xcom_push(key='transformed_data', value=df.to_dict())

def load_to_mysql(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform_data')
    df = pd.DataFrame.from_dict(transformed_data)

    # Print DataFrame info for debugging
    print("Transformed DataFrame:")
    print(df.info())
    print(df.head())

    #connect to mysql
    mysql_hook = MySqlHook(mysql_conn_id='mysql')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    #insert table into pe_adoption_db
    try:
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO pet_adopt (PetID, PetType, Breed, AgeMonths, Color, Size, WeightKg, 
                Vaccinated, HealthCondition, TimeInShelterDays, AdoptionFee, PreviousOwner, AdoptionLikelihood, AgeCategory)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, tuple(row))

        connection.commit()
        print("Data loaded successfully.")

    except Exception as e:
        print("Error loading data to MySQL:", e)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

with DAG(
    'pet_adoption_dag',
    default_args=default_args,
    description='A DAG to extract, transform, and load data from a CSV file to MySQL',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    verify_path_task = PythonOperator(
        task_id='verify_path',
        python_callable=verify_path,
        provide_context=True,
    )

    extract_task = PythonOperator(
        task_id='extract_csv',
        python_callable=read_csv_file,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load_to_mysql',
        python_callable=load_to_mysql,
        provide_context=True,
    )

    verify_path_task >> extract_task >> transform_task >> load_task
