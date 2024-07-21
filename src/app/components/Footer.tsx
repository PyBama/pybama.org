import { Container } from "@/components/Container"
import Image from "next/image"
import Logo from "@/images/logos/badge.png"

export function Footer() {
  return (
    <footer className="flex-none py-16">
      <Container className="flex flex-col items-center justify-between md:flex-row">
        <Image src={Logo} alt="PyBama" className="h-12 w-auto" />
        <p className="mt-6 text-base text-slate-500 md:mt-0">
          Copyright &copy; {new Date().getFullYear()} PyBama Organization. All rights reserved.
        </p>
      </Container>
    </footer>
  )
}
