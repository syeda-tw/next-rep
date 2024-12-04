import { Navbar } from '@shadcn/ui';
import { useRouter } from 'next/router';

const CustomNavbar = () => {
  const router = useRouter();

  return (
    <Navbar className="bg-gray-800 text-white">
      <Navbar.Brand onClick={() => router.push('/')}>MyApp</Navbar.Brand>
      <Navbar.Content>
        <Navbar.Link href="/dashboard">Dashboard</Navbar.Link>
        <Navbar.Link href="/profile">Profile</Navbar.Link>
        <Navbar.Link href="/auth/sign-out">
        </Navbar.Link>
      </Navbar.Content>
    </Navbar>
  );
};

export default CustomNavbar;
