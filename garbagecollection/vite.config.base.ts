import { fileURLToPath, URL } from 'url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 8080,
    host:'0.0.0.0',
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',  		//要请求的域名 
        ws: false,							// 是否启用websockets
        changeOrigin: true					//开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
      }
    }
  },
  css: {
    // css预处理器
    preprocessorOptions: {
      less: {
        charset: false,
        javascriptEnabled: true,
        additionalData: '@import "./src/styles/commonless/index.less";',
      },
    },
  }
})
