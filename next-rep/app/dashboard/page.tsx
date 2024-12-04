"use client";

import { useClerk } from "@clerk/nextjs";
import Navbar from "../components/Navbar";

const DashboardPage = () => {
  const { signOut } = useClerk();

  const handleSignOut = async () => {
    try {
      await signOut({
     });
      window.location.href = "/auth/sign-in";
    } catch (error) {
      console.error("Sign out error: ", error);
    }
  };

  return (
    <>
      <Navbar />
      <h1>Welcome to your Dashboard</h1>
      <p>Only authenticated users can see this page.</p>
      <button onClick={handleSignOut}>Sign Out</button>
    </>
  );
};

export default DashboardPage;
