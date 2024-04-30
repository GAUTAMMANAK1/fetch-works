from uagents import Agent, Context # type: ignore
 
alice = Agent(name="alice", seed="alice recovery phrase")
 
@alice.on_interval(period=1.0)
async def on_interval(ctx: Context):
    current_count = ctx.storage.get("count") or 0
 
    ctx.logger.info(f"My count is: {current_count}")
 
    ctx.storage.set("count", current_count + 1)
 
if __name__ == "__main__":
    alice.run()