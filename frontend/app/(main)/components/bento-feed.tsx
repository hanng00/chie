import { BentoGrid, BentoGridItem } from "@/components/bento-grid";

export type BentoItem = {
  title: string;
  content: string;
  header: React.ReactNode;
  icon: React.ReactNode;
};

interface BentoFeedProps {
  bentoItems: BentoItem[];
}
const BentoFeed = ({ bentoItems }: BentoFeedProps) => {
  return (
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
  );
};

export default BentoFeed;
