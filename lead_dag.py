import airflow
from airflow.example_dags.subdags.subdag import subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from subdag_1 import sub_dag_1
from subdag_2 import sub_dag_2

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}
main_dag = DAG(
    dag_id= 'lead_dag',
    default_args=args,
    schedule_interval="@once",
)
start = DummyOperator(
    task_id='start',
    dag=main_dag,
)

section_1 = SubDagOperator(
    task_id= 'child_dag1',
    subdag = sub_dag_1(main_dag.dag_id,'child_dag1',main_dag.schedule_interval),
    dag=main_dag,
)
section_2 = SubDagOperator(
    task_id= 'child_dag2',
    subdag = sub_dag_2(main_dag.dag_id,'child_dag2',main_dag.schedule_interval),
    dag=main_dag,
)

end = DummyOperator(
    task_id='end',
    dag=main_dag,
)
#dependencies
start >> section_1 >> section_2 >> end