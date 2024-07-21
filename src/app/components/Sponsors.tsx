import Image from "next/image"

import { Container } from "@/components/Container"
import logoLitestar from "@/images/logos/litestar.svg"

const sponsors = [
  { name: "Litestar", logo: logoLitestar },
  { name: "Litestar", logo: logoLitestar },
  { name: "Litestar", logo: logoLitestar },
]

export function Sponsors() {
  return (
    <section id="sponsors" aria-label="Sponsors" className="py-10 sm:py-12">
      <Container>
        <h2 className="mx-auto max-w-2xl text-center font-display text-4xl font-medium tracking-tighter text-tertiary sm:text-5xl">
          Sponsors from local and afar.
        </h2>
        <div className="mx-auto mt-20 grid max-w-max grid-cols-1 place-content-center gap-x-32 gap-y-12 sm:grid-cols-3 md:gap-x-16 lg:gap-x-32">
          {sponsors.map(sponsor => (
            <div key={sponsor.name} className="flex items-center justify-center">
              <Image src={sponsor.logo} alt={sponsor.name} unoptimized />
            </div>
          ))}
        </div>
      </Container>
    </section>
  )
}
