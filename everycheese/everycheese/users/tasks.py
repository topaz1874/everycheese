from everycheese.taskapp.celery import app

@app.task()
def another_debug_task():
    print "debugging!!!"

