import { Loader2 } from "lucide-react";

import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const spinnerVariance = cva("text-muted-foreground animate-spin", {
  variants: {
    size: {
      default: "h-4 w-4",
      sm: "h-2 w-2",
      lg: "h-6 w-6",
      icon: "h-10 w-10",
    },
    color: {
      default: "text-muted-foreground",
      primary: "text-primary",
      secondary: "text-secondary",
      white: "text-white",
    }
  },
  defaultVariants: {
    size: "default",
  },
});

interface SpinnerProps extends VariantProps<typeof spinnerVariance> {}

export const Spinner = ({ size, color }: SpinnerProps) => {
  return <Loader2 className={cn(spinnerVariance({ size , color}))} />;
};
