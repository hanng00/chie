"use client";

import Navbar from "./components/navbar";
import ChatInput from "./components/chat-input";
import useBentoItems from "./hooks/useBentoItems";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useMindApi } from "@/lib/api";
import BentoFeed from "./components/bento-feed";
import { FormData as MessageFormData } from "./components/chat-input";

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
      queryClient.setQueryData(
        ["knowlets"],
        knowlets ? [...knowlets, data] : [data]
      );
    },
  });
  const { bentoItems } = useBentoItems({ knowlets });

  const handleSend = (data: MessageFormData) => {
    mutate(data.message);
  };

  return (
    <div className="container p-2 flex flex-col h-full items-center">
      <Navbar />

      <div className="flex-1 flex overflow-y-auto scroll-smooth w-full px-2">
        <BentoFeed bentoItems={bentoItems} />
      </div>
      <div className="w-full flex justify-center">
        <ChatInput onSubmit={handleSend} disabled={isPending} />
      </div>
    </div>
  );
};

export default MainPage;
