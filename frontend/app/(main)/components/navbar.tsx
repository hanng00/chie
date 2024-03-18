import { ModeToggle } from "@/components/mode-toggle";
import UserProfile from "@/components/user-profile";

const Navbar = () => {
  return (
    <div className="w-full h-fit flex flex-row items-center justify-between py-4">
      <div>
        <h1 className="text-2xl font-bold text-foreground ">Chien</h1>
      </div>
      <div className="flex flex-row space-x-2 items-center">
        <ModeToggle />
        <UserProfile />
      </div>
    </div>
  );
};

export default Navbar;
