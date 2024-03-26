import { cn } from "@/lib/utils";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "./ui/button";
import { useState } from "react";
import MarkdownDisplay from "./markdown-display";

export const BentoGrid = ({
  className,
  children,
}: {
  className?: string;
  children?: React.ReactNode;
}) => {
  return (
    <div
      className={cn(
        "grid md:auto-rows-[18rem] grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 w-full",
        className
      )}
    >
      {children}
    </div>
  );
};

interface BentoGridItemProps {
  className?: string;
  title?: string | React.ReactNode;
  description?: string;
  header?: React.ReactNode;
  icon?: React.ReactNode;
  variant?: "primary" | "secondary";
}

export const BentoGridItem = ({
  className,
  title,
  description,
  header,
  icon,
  variant,
}: BentoGridItemProps) => {
  const [isOpen, setIsOpen] = useState(false);

  const onOpenChange = () => {
    setIsOpen((prevState) => !prevState);
  };
  return (
    <>
      <BentoGridCard
        title={title}
        description={description}
        header={header}
        icon={icon}
        variant={variant}
        className={className}
        onClick={onOpenChange}
      />
      <BentoGridDialog
        isOpen={isOpen}
        onOpenChange={onOpenChange}
        title={title}
        description={description}
        header={header}
      />
    </>
  );
};

/* SPEPARATE COMPONENTS */
interface DialogProps extends BentoGridItemProps {
  isOpen: boolean;
  onOpenChange: () => void;
}
export const BentoGridDialog = ({
  isOpen,
  onOpenChange,
  header,
  title,
  description,
}: DialogProps) => {
  return (
    <Dialog
      open={isOpen}
      onOpenChange={onOpenChange}
      modal
      defaultOpen={isOpen}
    >
      <DialogContent className="max-w-md md:max-w-xl">
        <DialogHeader>
          <div className="py-2">{header}</div>
          <DialogTitle>{title}</DialogTitle>
        </DialogHeader>

        <MarkdownDisplay markdownText={description || ""} />

        <DialogFooter className="sm:justify-start">
          <DialogClose asChild>
            <Button type="button" variant="secondary">
              Close
            </Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};

interface BentoGridCardProps extends BentoGridItemProps {
  onClick?: () => void;
}
export const BentoGridCard = ({
  className,
  title,
  description,
  header,
  icon,
  variant,
  onClick,
}: BentoGridCardProps) => {
  const trimMarkdownCharacters = (str: string | undefined) => {
    if (!str) return "";

    return str.replace(/[*#_]/g, "");
  };

  return (
    <div
      className={cn(
        "row-span-1 rounded-xl group/bento hover:shadow-xl transition duration-200 shadow-input shadow-none p-4 bg-background border-foreground/20 border justify-between flex flex-col space-y-4 hover:cursor-pointer",
        variant === "primary" && "bg-secondary",
        variant === "secondary" && "",
        className
      )}
      onClick={onClick}
    >
      {header}
      <div className="group-hover/bento:translate-x-2 transition duration-200">
        {icon}
        <div className="font-sans font-bold text-neutral-600 dark:text-neutral-200 mb-2 mt-2">
          {title}
        </div>
        <div className="font-sans font-normal text-neutral-600 text-xs dark:text-neutral-300 truncate">
          {trimMarkdownCharacters(description)}
        </div>
      </div>
    </div>
  );
};
