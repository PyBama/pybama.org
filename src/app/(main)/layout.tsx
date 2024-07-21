import { Layout } from "@/components/Layout"
import React from "react"

export default function MainLayout({ children }: { children: React.ReactNode }) {
  return <Layout>{children}</Layout>
}
