# plugins/steps/messages.py
from airflow.providers.telegram.hooks.telegram import TelegramHook

def send_telegram_success_message(context): # на вход принимаем словарь с контекстными переменными
    hook = TelegramHook(token='8636608313:AAFBXGS5xmjplSZlYevYUpr0AaA8bjPWKdc', chat_id='4389963477')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '{4389963477}',
        'text': message
    })

def send_telegram_failure_message(context):
    # ваш код здесь #
    hook = TelegramHook(token='8636608313:AAFBXGS5xmjplSZlYevYUpr0AaA8bjPWKdc', chat_id='4389963477')
    dag = context['dag']
    run_id = context['run_id']
    task_instance_key = context['task_instance_key_str']
    
    message = f'Исполнение DAG {dag} с id {run_id} упало на {task_instance_key}' # определение текста сообщения
    hook.send_message({
        'chat_id': '{4389963477}',
        'text': message
    })