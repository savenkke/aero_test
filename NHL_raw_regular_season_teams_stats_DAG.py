from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'kosavenkov',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
    'execution_timeout': timedelta(minutes=10),
}

dag = DAG(
    'NHL_raw_regular_season_teams_stats',
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    concurrency=1, 
    schedule_interval='25 3,15 * * *',
    description='Забор стат. команд НХЛ из апишки Лиги',
    tags=['Sport', 'NHL']
)

def taska_kolbaska_executable(**op_kwargs):
    from NHL_raw_regular_season_teams_stats_executable import NHL_raw_regular_season_teams_stats_func
    return NHL_raw_regular_season_teams_stats_func(op_kwargs['pg_conn_info'])


taska_kolbaska = PythonOperator(
    task_id='taska_kolbaska',
    dag=dag,
    python_callable=taska_kolbaska_executable,
    op_kwargs={'pg_conn_info': "{{ macros.connections.get_conn('pg_connection') }}"}, # подразумевается наличие макроса, идущего через Basehook к словарю подключений
)

taska_kolbaska
