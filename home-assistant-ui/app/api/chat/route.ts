// @errors: 2558 2345
import { RemoteRunnable } from "@langchain/core/runnables/remote";
import type { RunnableConfig } from "@langchain/core/runnables";
import { LangChainAdapter,  type AssistantMessage } from "ai";

export const maxDuration = 300;

export async function POST(req: Request) {
  const { messages } = (await req.json()) as { messages: AssistantMessage[] };
  const content = messages.map(message => message.content)
  const text = content.map(item => item.map(i=>i.text)).join(" ")

  // TODO replace with your own langserve URL
  const remoteChain = new RemoteRunnable<
    { text: String },
    string,
    RunnableConfig
  >({
    url: "http://127.0.0.1:8100/ask",
  });

  console.log(JSON.stringify(text))

  const stream = await remoteChain.stream({
    text,
  });

  return LangChainAdapter.toDataStreamResponse(stream);
}
