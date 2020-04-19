const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
    configureWebpack: {

	plugins:[
	  new CompressionPlugin({
	    filename:"[path].gz[query]",
	    algorithm:"gzip",
	    test:new RegExp("\\.(js|css)$"),
	    threshold:10240,
	    minRatio:0.8,
            deleteOriginalAssets:false
	  
	  
	   }
	  )
	],

        resolve:{
            alias: {
                'assets': '@/assets',
                'common': '@/common',
                'components': '@/components',
                'network': '@/network',
                'views': '@/views',
            }
        }
    },

    publicPath: './',
    productionSourceMap: false,
}
