import { ChatOllama } from "@langchain/community/chat_models/ollama";
import { ConversationChain } from "langchain/chains";
import { ConversationSummaryMemory } from "langchain/memory";

const llm = new ChatOllama({
  baseUrl: "http://localhost:11434",
  model: "llama3",
});

const memory = new ConversationSummaryMemory({
  llm: llm,
});

const chain = new ConversationChain({
  llm: llm,
  memory: memory,
});

async function run() {
  console.log(await chain.call({ input: "Hi, my name is Aarman" }));
  console.log(await chain.call({ input: "I like AI and coding" }));
  console.log(await chain.call({ input: "What do you remember about me?" }));
}

run();