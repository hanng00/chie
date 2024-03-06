import { useMindApi } from "@/lib/api";
import { Knowlet } from "@/lib/types/Mind";
import {
  IconArrowWaveRightUp,
  IconBoxAlignRightFilled,
  IconBoxAlignTopLeft,
  IconClipboardCopy,
  IconFileBroken,
  IconSignature,
  IconTableColumn,
} from "@tabler/icons-react";
import { useQuery } from "@tanstack/react-query";
import { useMemo } from "react";

const Skeleton = () => (
  <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-neutral-200 dark:from-neutral-900 dark:to-neutral-800 to-neutral-100">
    {" "}
  </div>
);

const useRandomIcon = () => {
  const defaultClassname = "h-4 w-4 text-neutral-500";
  const allIcons = [
    <IconClipboardCopy className={defaultClassname} />,
    <IconFileBroken className={defaultClassname} />,
    <IconSignature className={defaultClassname} />,
    <IconTableColumn className={defaultClassname} />,
    <IconArrowWaveRightUp className={defaultClassname} />,
    <IconBoxAlignTopLeft className={defaultClassname} />,
    <IconBoxAlignRightFilled className={defaultClassname} />,
  ];

  const randomId = Math.floor(Math.random() * allIcons.length);

  return allIcons[randomId];
};

const useBentoItems = ({ knowlets }: { knowlets: Knowlet[] | undefined }) => {
  const defaultHeader = <Skeleton />;

  const bentoItems = useMemo(() => {
    if (!knowlets) {
      return undefined;
    }
    return knowlets.map((item) => {
      return {
        ...item,
        header: defaultHeader,
        icon: useRandomIcon(),
      };
    });
  }, [knowlets]);

  return { bentoItems };
};

export default useBentoItems;
