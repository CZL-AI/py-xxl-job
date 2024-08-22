import asyncio

from pyxxl import ExecutorConfig, PyxxlRunner
from pyxxl.ctx import g

config = ExecutorConfig(
    xxl_admin_baseurl="http://localhost:18080/xxl-job-admin/api/",
    executor_app_name="py-xxl-job-executor-sample",
    executor_host="127.0.0.1",
    access_token="default_token"
)

app = PyxxlRunner(config)

@app.register(name="demoJobHandler")
async def test_task():
    await asyncio.sleep(5)
    g.logger.info("==============任务执行成功！！！=============================")
    return "成功..."

# 如果你代码里面没有实现全异步，请使用同步函数，不然会阻塞其他任务
@app.register(name="xxxxx")
def test_task3():
    return "成功3"


app.run_executor()