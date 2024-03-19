"use client";

import { useId, useState } from "react";
import { useUIState, useActions, useAIState } from "ai/rsc";
import { AI } from "@/lib/actions/main";
import { Button } from "@/components/ui/button";
import { readStreamableValue } from "ai/rsc";

export default function Page() {
  const [value, setValue] = useState(50);
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useUIState<typeof AI>();
  const [aiState, setAIState] = useAIState();
  const { submitUserMessage, confirmPurchase, getCustomerProfile } =
    useActions<typeof AI>();

  const id = useId();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Add user message to UI state
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: Date.now(),
        display: <div>{inputValue}</div>,
      },
    ]);

    // Submit and get response message
    const responseMessage = await submitUserMessage(inputValue);
    setMessages((currentMessages) => [...currentMessages, responseMessage]);

    setInputValue("");
  };

  // Whenever the slider changes, we need to update the local value state
  // and the history so the LLM also knows what's going on.
  function onSliderChange(event: React.ChangeEvent<HTMLInputElement>) {
    const newValue = Number(event.target.value);
    setValue(newValue);

    // Insert a hidden history info to the list.
    const info = {
      id,
      role: "system" as const,
      content: `[User has changed value to ${newValue}]`,
    };

    // If the last AI state already contains an instance of this slider, update it.
    // If it doesn't exist, append it to history.
    // This is to avoid adding every slider change to the history.
    if (aiState[aiState.length - 1]?.id === id) {
      setAIState([...aiState.slice(0, -1), info]);
    } else {
      setAIState([...aiState, info]);
    }
  }

  const handleGetProfile = async () => {
    const PROFILE_ID = "2";
    const { profile } = await getCustomerProfile(PROFILE_ID);

    let message: {
      id: number;
      display: React.ReactNode;
    };
    for await (const v of readStreamableValue(profile)) {
      if (!v) {
        continue;
      }
      message = {
        id: Date.now(),
        display: (
          <div>
            {v.profile && (
              <>
                <p>{v.profile?.name}</p>
                <p>{v.profile?.customerId}</p>
              </>
            )}
            {v.subscriptions &&
              v.subscriptions.map((subscription) => (
                <p key={subscription.id}>{subscription.name}</p>
              ))}
          </div>
        ),
      };
      console.log(message);
      setMessages((currentMessages) => [...currentMessages, message]);
    }
  };

  const handleConfirmPurchase = async () => {
    const responseMessage = await confirmPurchase("AAPL", value);
    console.log(responseMessage);
    setMessages((currentMessages) => [...currentMessages, responseMessage]);
  };

  return (
    <div>
      {
        // View messages in UI state
        messages.map((message) => (
          <div key={message.id}>{message.display}</div>
        ))
      }

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Send a message..."
          value={inputValue}
          onChange={(event) => {
            setInputValue(event.target.value);
          }}
        />
        <input
          type="range"
          value={value}
          onChange={onSliderChange}
          min="10"
          max="100"
        />
      </form>
      <Button onClick={handleConfirmPurchase}>Confirm purchase</Button>
      <Button onClick={handleGetProfile}>Get customer profile</Button>
    </div>
  );
}
