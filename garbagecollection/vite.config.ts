import baseConfig from "./vite.config.base";
import devConfig from "./vite.config.dev"
import prodConfig from "./vite.config.prod"
import { defineConfig, loadEnv } from 'vite'

const viteConfig = {
  "build": () => ({ ...baseConfig, ...devConfig }),
  "serve": () => ({ ...baseConfig, ...prodConfig })
}

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  loadEnv(mode, process.cwd());
  return viteConfig[command]();
})

