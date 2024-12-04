'use client'

import { useClerk } from '@clerk/nextjs';

const DashboardPage = () => {
  const { signOut } = useClerk(); // Use the useClerk hook to access signOut

  // Sign out handler
  const handleSignOut = async () => {
    try {
      // Sign out from all sessions (use sessionId for specific sessions)
      await signOut({ 
        // Optionally, pass a sessionId if you want to target a specific session.
        // sessionId: 'your-session-id-here', 
      });
      
      // Redirect to sign-in page after successful sign-out
      window.location.href = '/auth/sign-in'; 
    } catch (error) {
      console.error("Sign out error: ", error);
    }
  };

  return (
    <div>
      <h1>Welcome to your Dashboard</h1>
      <p>Only authenticated users can see this page.</p>
      {/* Button to trigger sign-out */}
      <button onClick={handleSignOut}>Sign Out</button>
    </div>
  );
};

export default DashboardPage;
