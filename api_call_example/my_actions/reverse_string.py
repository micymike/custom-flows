from asyncflows import Action, BaseModel, Field

import aiohttp


class Inputs(BaseModel):
    input_string: str


class Outputs(BaseModel):
    reversed_string: str


class MyReverseString(Action[Inputs, Outputs]):
    name = 'my_reverse_string'

    async def run(self, inputs: Inputs) -> Outputs:
        return Outputs(
            reversed_string=inputs.input_string[::-1]
        )

### from test.py

import os
from asyncflows import AsyncFlows


async def main():
    dirname = os.path.dirname(__file__)
    flow = AsyncFlows.from_file(
        os.path.join(dirname, "string_reversal.yaml")
    )

    # Run the flow and return the default output (result of the extract_title action)
    result = await flow.set_vars(
        my_input="hahahah hihihih",
    ).run()
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
