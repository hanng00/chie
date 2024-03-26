import { Spinner } from "@/components/spinner";
import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

const messageSchema = z.object({
  message: z.string().min(1),
});
export type FormData = z.infer<typeof messageSchema>;

interface ChatInputProps {
  disabled?: boolean;
  onSubmit: (data: FormData) => void;
}

const ChatInput = ({ disabled, onSubmit }: ChatInputProps) => {
  const {
    register,
    handleSubmit,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<FormData>({
    resolver: zodResolver(messageSchema),
    defaultValues: {
      message: "",
    },
  });

  useEffect(() => {
    if (isSubmitSuccessful && !disabled) {
      reset();
    }
  }, [isSubmitSuccessful, disabled]);

  return (
    <div className="p-2 w-full max-w-2xl ">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-row items-center justify-center space-x-2"
      >
        <input
          id="message"
          {...register("message")}
          type="text"
          className="w-full h-full border bg-secondary border-secondary-foreground/20 rounded-xl text-sm p-3"
          placeholder="Type a message..."
          disabled={disabled}
        />
        <Button
          className="w-24"
          type="submit"
          variant="default"
          disabled={disabled}
        >
          {!disabled ? "Send" : <Spinner color="secondary" />}
        </Button>
      </form>
    </div>
  );
};

export default ChatInput;
