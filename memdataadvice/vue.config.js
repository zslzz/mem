const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
   // disableHostCheck: true,
    host: '0.0.0.0',
  }
})
