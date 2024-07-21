import { BackgroundImage } from "@/components/BackgroundImage"
import { Button } from "@/components/Button"
import { Container } from "@/components/Container"

export function Hero() {
  return (
    <div className="relative sm:pb-24 sm:pt-36">
      <BackgroundImage className="-bottom-14 -top-36" />
      <Container className="relative">
        <div className="mx-auto max-w-2xl lg:max-w-4xl lg:px-12">
          <h1 className="font-display text-5xl font-bold tracking-tighter text-primary sm:text-7xl">
            <span className="sr-only">PyBama - </span>Python in the South.
          </h1>
          <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-tertiary">
            <p>
              PyBama is the regional Python group for the South - uniquely accessible for visitors throughout the
              southeastern United States. We host monthly meetups across the state or online, an annual conference with
              a rotating location, and a variety of other events throughout the year.
            </p>
            <p>
              If you&apos;re interested in Python, web development, data science, or any other Python-related topic,
              you&apos;re in the right place. Join us at our next event to learn, network, and grow your Python skills,
              no matter your experience level!
            </p>
          </div>
          <Button href="#" className="mt-10 w-full sm:hidden">
            View Events Schedule
          </Button>
          <dl className="mt-10 grid grid-cols-2 gap-x-10 gap-y-6 sm:mt-16 sm:gap-x-16 sm:gap-y-10 sm:text-center lg:auto-cols-auto lg:grid-flow-col lg:grid-cols-none lg:justify-start lg:text-left">
            {[
              ["Topics", "Data Science, Tooling, Web Development"],
              ["Date", "2024-08-17"],
              ["Location", "Virtual"],
            ].map(([name, value]) => (
              <div key={name}>
                <dt className="font-mono text-sm text-primary">{name}</dt>
                <dd className="mt-0.5 text-2xl font-semibold tracking-tight text-tertiary">{value}</dd>
              </div>
            ))}
          </dl>
        </div>
      </Container>
    </div>
  )
}
