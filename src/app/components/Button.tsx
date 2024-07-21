import Link from "next/link"
import clsx from "clsx"

type ButtonProps =
  | React.ComponentPropsWithoutRef<typeof Link>
  | (React.ComponentPropsWithoutRef<"button"> & { href?: undefined })

export function Button({ className, ...props }: ButtonProps) {
  className = clsx(
    "inline-flex justify-center rounded-2xl bg-primary p-4 text-base font-semibold text-white hover:bg-secondary focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 active:text-white/70",
    className,
  )

  return typeof props.href === "undefined" ? (
    <button className={className} {...props} />
  ) : (
    <Link className={className} {...props} />
  )
}
