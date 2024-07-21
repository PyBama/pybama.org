import Image from "next/image"
import clsx from "clsx"

import backgroundImage from "@/images/background.png"

export function BackgroundImage({ className, position = "left" }: { className?: string; position?: "left" | "right" }) {
  return (
    <div className={clsx("absolute inset-0 overflow-hidden bg-blue-50", className)}>
      <Image
        className={clsx(
          "absolute top-0",
          position === "left" &&
            "left-0 translate-x-[-55%] translate-y-[-10%] -scale-x-100 sm:left-1/2 sm:translate-x-[-98%] sm:translate-y-[-6%] lg:translate-x-[-106%] xl:translate-x-[-122%]",
          position === "right" &&
            "left-full -translate-x-1/2 sm:left-1/2 sm:translate-x-[-20%] sm:translate-y-[-15%] md:translate-x-0 lg:translate-x-[5%] lg:translate-y-[4%] xl:translate-x-[27%] xl:translate-y-[-8%]",
        )}
        src={backgroundImage}
        alt=""
        width={1200}
        height={1495}
        priority
        unoptimized
      />
      <div className="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-white" />
      <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-white" />
      <div className="absolute inset-y-0 left-0 w-40 bg-gradient-to-r from-white" />
      <div className="absolute inset-y-0 right-0 w-40 bg-gradient-to-l from-white" />
    </div>
  )
}
