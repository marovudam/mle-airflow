from airflow import DAG
from steps.messages import send_telegram_failure_message, send_telegram_success_message
from steps.churn import extract, transform, load, create_table
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='alt_churn',
    schedule='@once',
    start_date=datetime(2022, 1, 1), 
    on_success_callback=send_telegram_success_message,
    on_failure_callback=send_telegram_failure_message
) as dag:
    step_0 = PythonOperator(task_id='create_table', python_callable=create_table)
    step_1 = PythonOperator(task_id='extract', python_callable=extract)
    step_2 = PythonOperator(task_id='transform', python_callable=transform)
    step_3 = PythonOperator(task_id='load', python_callable=load)
    step_0 >> step_1 >> step_2 >> step_3