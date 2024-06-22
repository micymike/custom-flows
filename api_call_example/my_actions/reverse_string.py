from asyncflows import Action, BaseModel, Field

import aiohttp

class Inputs(BaseModel):
    input_string: str
    word_index: int = 0

class Outputs(BaseModel):
    reversed_string: str

class MyReverseString(Action[Inputs, Outputs]):
    name = 'my_reverse_string'

    async def run(self, inputs: Inputs) -> Outputs:
        words = inputs.input_string.split()
        if 0 <= inputs.word_index < len(words):
            words[inputs.word_index] = words[inputs.word_index][::-1]
        reversed_string = ' '.join(words)
        return Outputs(reversed_string=reversed_string)

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
        word_index=1  # Reverse the second word
    ).run()
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
