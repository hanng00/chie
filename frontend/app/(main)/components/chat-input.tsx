import { Button } from "@/components/ui/button";

interface ChatInputProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  disabled?: boolean;
}

const ChatInput = ({ value, onChange, disabled }: ChatInputProps) => {
  return (
    <div className="p-2 w-full max-w-2xl">
      <input
        type="text"
        className="w-full h-full border bg-secondary border-secondary-foreground/20 rounded-xl text-sm p-3"
        placeholder="Type a message..."
        value={value}
        onChange={onChange}
        disabled={disabled}
      />
    </div>
  );
};

export default ChatInput;
