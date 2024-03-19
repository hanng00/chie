import { OpenAI } from "openai";
import { createAI } from "ai/rsc";

import { submitUserMessage } from "./actions/submit-user-message";
import { confirmPurchase } from "./actions/confirm-purchase";
import { getCustomerProfile } from "./actions/get-customer-profile";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Define the initial state of the AI. It can be any JSON object.
const initialAIState: {
  role: "user" | "assistant" | "system" | "function";
  content: string;
  id?: string;
  name?: string;
}[] = [];

// The initial UI state that the client will keep track of, which contains the message IDs and their UI nodes.
const initialUIState: {
  id: number;
  display: React.ReactNode;
}[] = [];

// AI is a provider you wrap your application with so you can access AI and UI state in your components.
export const AI = createAI({
  actions: {
    submitUserMessage: async (userInput: string) => {
      "use server";
      return await submitUserMessage(userInput, openai);
    },

    confirmPurchase,
    getCustomerProfile,
  },
  // Each state can be any shape of object, but for chat applications
  // it makes sense to have an array of messages. Or you may prefer something like { id: number, messages: Message[] }
  initialUIState,
  initialAIState,
});
