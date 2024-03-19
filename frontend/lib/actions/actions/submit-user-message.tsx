import { getMutableAIState, render } from "ai/rsc";
import { OpenAI } from "openai";
import { createGetFlightInfoTool } from "../tools";

export async function submitUserMessage(userInput: string, openai: OpenAI) {
  "use server"
  console.log("submitUserMessage", userInput);

  const aiState = getMutableAIState();
  console.log("aiState", aiState.get());

  const handleTextResponse = ({
    content,
    done,
  }: {
    content: string;
    done: boolean;
  }) => {
    // When it's the final content, mark the state as done and ready for the client to access.
    if (done) {
      aiState.done([
        ...aiState.get(),
        {
          role: "assistant",
          content,
        },
      ]);
    }

    return <p>{content}</p>;
  };

  // Update the AI state with the new user message.
  aiState.update([
    ...aiState.get(),
    {
      role: "user",
      content: userInput,
    },
  ]);

  // The `render()` creates a generated, streamable UI.
  const ui = render({
    model: "gpt-4-0125-preview",
    provider: openai,
    messages: [
      { role: "system", content: "You are a flight assistant" },
      { role: "user", content: userInput },
    ],
    // `text` is called when an AI returns a text response (as opposed to a tool call).
    // Its content is streamed from the LLM, so this function will be called
    // multiple times with `content` being incremental.
    text: handleTextResponse,
    tools: {
      get_flight_info: createGetFlightInfoTool(aiState),
    },
  });

  return {
    id: Date.now(),
    display: ui,
  };
}
