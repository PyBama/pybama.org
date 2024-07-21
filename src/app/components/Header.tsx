"use client"

import { useState } from "react"
import { Button } from "@/components/Button"
import { Container } from "@/components/Container"
import Image from "next/image"
import Logo from "@/images/logos/badge.png"
import { DiamondIcon } from "@/components/DiamondIcon"

export function Header() {
  const [isAboutOpen, setIsAboutOpen] = useState(false)

  return (
    <header className="relative z-50 flex-none lg:pt-11">
      <Container className="flex flex-wrap items-center justify-center sm:justify-between lg:flex-nowrap">
        <div className="mt-10 lg:mt-0 lg:grow lg:basis-0">
          <Image src={Logo} alt="PyBama" className="h-24 w-auto" />
        </div>
        <div className="order-first -mx-4 flex flex-auto basis-full overflow-x-auto whitespace-nowrap border-b border-primary/10 py-4 font-mono text-sm text-primary sm:-mx-6 lg:order-none lg:mx-0 lg:basis-auto lg:border-0 lg:py-0">
          <div className="mx-auto flex items-center gap-4 px-4">
            <p>
              Next Event:
              <time dateTime="2024-08-17"> 2024-08-17</time>
            </p>
            <DiamondIcon className="h-1.5 w-1.5 overflow-visible fill-current stroke-current" />
            <p>Virtual</p>
          </div>
        </div>
        <div className="hidden sm:mt-10 sm:flex lg:mt-0 lg:grow lg:basis-0 lg:justify-end space-x-4">
          <Button href="/api/swagger">Events</Button>
          <Button href="/api/swagger">Contact</Button>
          <div className="relative">
            <Button onClick={() => setIsAboutOpen(!isAboutOpen)} className="flex items-center">
              About
              <svg
                className="w-4 h-4 ml-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </Button>
            {isAboutOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-10">
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                  Code of Conduct
                </a>
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                  Privacy
                </a>
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                  Team
                </a>
              </div>
            )}
          </div>
          <Button href="/api/swagger">Sponsor</Button>
        </div>
      </Container>
    </header>
  )
}
