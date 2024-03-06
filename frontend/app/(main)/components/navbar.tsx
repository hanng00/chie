import { ModeToggle } from "@/components/mode-toggle";

const Navbar = () => {
  return (
    <div className="w-full h-fit flex flex-row items-center justify-between py-4">
      <div>
        <h1 className="text-2xl font-bold text-foreground ">Chien</h1>
      </div>
      <div>
        <ModeToggle />
      </div>
    </div>
  );
};

export default Navbar;
