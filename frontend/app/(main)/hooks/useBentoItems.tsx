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
import { useMemo } from "react";

const Skeleton = () => (
  <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-neutral-200 dark:from-neutral-900 dark:to-neutral-800 to-neutral-100">
    {" "}
  </div>
);

const useBentoItems = ({ knowlets }: { knowlets: Knowlet[] | undefined }) => {
  const defaultHeader = <Skeleton />;

  const getRandomIcon = () => {
    const defaultClassname = "h-4 w-4 text-neutral-500";
    const allIcons = [
      <IconClipboardCopy key="icon1" className={defaultClassname} />,
      <IconFileBroken key="icon2" className={defaultClassname} />,
      <IconSignature key="icon3" className={defaultClassname} />,
      <IconTableColumn key="icon4" className={defaultClassname} />,
      <IconArrowWaveRightUp key="icon5" className={defaultClassname} />,
      <IconBoxAlignTopLeft key="icon6" className={defaultClassname} />,
      <IconBoxAlignRightFilled key="icon7" className={defaultClassname} />,
    ];

    const randomId = Math.floor(Math.random() * allIcons.length);

    return allIcons[randomId];
  };

  const bentoItems = useMemo(() => {
    if (!knowlets) {
      return undefined;
    }
    return knowlets.map((item, idx) => {
      return {
        ...item,
        header: defaultHeader,
        icon: getRandomIcon(),
      };
    });
  }, [knowlets]);

  return { bentoItems };
};

export default useBentoItems;
