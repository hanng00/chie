"use client";

import { Button } from "@/components/ui/button";
import Navbar from "./components/navbar";
import { BentoGrid, BentoGridItem } from "@/components/bento-grid";
import ChatInput from "./components/chat-input";
import useBentoItems from "./hooks/useBentoItems";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useMindApi } from "@/lib/api";
import { useState } from "react";
import { Spinner } from "@/components/spinner";

const MainPage = () => {
  const mindApi = useMindApi();
  const queryClient = useQueryClient();

  const { data: knowlets } = useQuery({
    queryKey: ["knowlets"],
    queryFn: mindApi.listKnowlets,
  });

  const { mutate, isPending } = useMutation({
    mutationFn: mindApi.askMind,
    onSuccess: (data) => {
      queryClient.setQueryData(["knowlets"], data);
    },
  });
  const { bentoItems } = useBentoItems({ knowlets });

  /* CHAT INPUT THINGY */
  const [input, setInput] = useState("");

  const handleSend = () => {
    mutate(input);
    setInput("");
  };

  return (
    <div className="container p-2 flex flex-col h-full items-center">
      <Navbar />

      <div className="flex-1 flex overflow-y-auto scroll-smooth w-full px-2">
        <BentoGrid className="mx-auto">
          {!bentoItems ? (
            <div>Loading ...</div>
          ) : (
            bentoItems.map((item, i) => (
              <BentoGridItem
                key={i}
                title={item.title}
                description={item.content}
                header={item.header}
                icon={item.icon}
                className={i === 2 || i === 4 ? "md:col-span-2" : ""}
                variant={i % 4 === 0 ? "primary" : "secondary"}
              />
            ))
          )}
        </BentoGrid>
      </div>
      <div className="w-full flex flex-row items-center justify-center space-x-2">
        <ChatInput
          value={input}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setInput(e.target.value)
          }
          disabled={isPending}
        />
        <Button className="w-24" variant="default" disabled={isPending} onClick={handleSend}>
          {!isPending ? "Send": <Spinner />}
        </Button>
      </div>
    </div>
  );
};

export default MainPage;
