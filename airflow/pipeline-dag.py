
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    dag_id="pipeline",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    A = BashOperator(
        task_id="A",
        bash_command="echo A",
    )
    B = BashOperator(
        task_id="B",
        bash_command="echo B",
    )
    C = BashOperator(
        task_id="C",
        bash_command="echo C",
    )
    D = BashOperator(
        task_id="D",
        bash_command="echo D",
    )
    E = BashOperator(
        task_id="E",
        bash_command="echo E",
    )
    F = BashOperator(
        task_id="F",
        bash_command="echo F",
    )
    G = BashOperator(
        task_id="G",
        bash_command="echo G",
    )

    A >> [D]
    B >> [D]
    C >> [F,E]
    D >> [E,G]
    F >> [G]
