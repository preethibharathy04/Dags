import airflow
from airflow.example_dags.subdags.subdag import subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

def sub_dag_2(parent_dag_name, child_dag_name, schedule_interval):
    dag = DAG(
        dag_id= 'lead_dag.child_dag2', 
        schedule_interval= schedule_interval,
        default_args= args,)

    start = DummyOperator(  
        task_id='start',
        dag=dag,
    )
    some_other_task = DummyOperator(
        task_id='some-other-task',
        dag=dag,
    )
    end = DummyOperator(
        task_id='end',
        dag=dag, 
    )
    #dependencies
    start >> some_other_task >> end
    return dag