<template>
	<div><div class="Welcome-wrapper">
		<h1 class="Welcome-title">筛选最优结果</h1>
		<p class="Welcome-text"> </p>
		<div class="Welcome-formWrapper">
			<form
				class="Welcome-form"
				data-track-event="signup_website"
				data-active-campaign-list="90"
				data-active-campaign-skip-free="true"
			>
				<input
					class="Welcome-formInput"
					placeholder="Input Something"
					v-model="keyword"
					required
				/>
                
				<button class="Welcome-formSubmit" v-on:click.stop.prevent="searchClick">Search Now</button>
			</form>
		</div>



	</div>
<keep-alive>
<result ref="resultRef"></result>
</keep-alive>
    
 
    <footer-cpn></footer-cpn>
    </div>

</template>

<script>    
import FooterCpn from 'components/footer/FooterCpn'
import Result from 'components/search/Result'
export default {
    name: "Search",
    components:{
        Result,
        FooterCpn
	},
	data() {
		return {
			keyword: '',
			loginStatus: this.$store.getters.getStatus
		}
	},
    methods: {
        searchClick() {
			console.log(this.loginStatus);
			
			if(this.loginStatus){
				if(this.keyword.length>0){
				this.$refs.resultRef.keyword = this.keyword
				this.$refs.resultRef.searchClick()		
			}else{
				this.keywordErr()
			}

			}else{
				this.noLogin()
			}
		},
		
		noLogin() {
        this.$notify.info({
          title: '消息',
          message: '登陆后才可以进行相关操作'
        });
	  },
	  
	  	keywordErr() {
        this.$notify.info({
		  title: '警告',
		  type: 'error',
          message: '输入不能为空',
          
        });
	  },
	  
    },
    // data() {
    //     return {
    //         isShow: false,
    //         isLoading: true
    //     }
    // },
    // methods: {
    //     searchClick() {
    //         this.isShow = true
    //         this.isLoading = true
    //         setTimeout(() => {
    //         this.isLoading = false
    //         }, 1000);
            
    //     }
    // },
    }
</script>






<style>



.Welcome-wrapper {
    text-align: center;
    margin-top: 6em;
}
.Welcome-title {
	margin-top: 0;
	margin-bottom: 10px;
	color: #091d41;
	font-size: 36px;
	font-weight: 500;
    line-height: 1.2083333333;
    letter-spacing: 0.2em;
}
.Welcome-text,
.Welcome-title {
	font-family: Calibre, sans-serif;
}
.Welcome-text {
	max-width: 725px;
	margin-right: auto;
	margin-left: auto;
	color: #50556c;
	font-size: 18px;
	line-height: 1.4444444444;
}
.Welcome-formWrapper {
	margin-top: 25px;
	margin-bottom: 25px;
}
.Welcome-form {
	display: -webkit-inline-box;
	display: -ms-inline-flexbox;
	display: inline-flex;
	width: 88%;
	max-width: 500px;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-shadow: 0 0 30px rgba(0, 0, 0, 0.1);
	box-shadow: 0 0 30px rgba(0, 0, 0, 0.1);
	border-radius: 100px;
}
.Welcome-formInput {
	-webkit-box-flex: 1;
	-ms-flex: 1 1 0%;
	flex: 1 1 0%;
	height: 46px;
	max-width: 325px;
	padding-left: 30px;
	background-color: #fff;
	color: #091d41 !important;
	font-family: Calibre, sans-serif;
	font-size: 18px;
	border: none !important;
	outline: none;
	border-top-left-radius: 100px;
	border-bottom-left-radius: 100px;
}
.Welcome-formInput:focus {
	border: none !important;
}
.Welcome-formInput::-webkit-input-placeholder {
	color: rgba(9, 29, 65, 0.5) !important;
}
.Welcome-formInput::-moz-placeholder {
	color: rgba(9, 29, 65, 0.5) !important;
}
.Welcome-formInput:-ms-input-placeholder {
	color: rgba(9, 29, 65, 0.5) !important;
}
.Welcome-formInput::-ms-input-placeholder {
	color: rgba(9, 29, 65, 0.5) !important;
}
.Welcome-formInput::placeholder {
	color: rgba(9, 29, 65, 0.5) !important;
}
.Welcome-formSubmit {
	display: inline-block;
	-ms-flex-preferred-size: 170px;
	flex-basis: 170px;
	max-width: 170px;
	height: 46px;
	background-color: #409EFF;
	color: #fff;
	font-family: Calibre, sans-serif;
	font-size: 18px;
	font-weight: 500;
	line-height: 44px;
	border: none;
	border-radius: 200px;
}
.Welcome-list {
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-ms-flex-wrap: wrap;
	flex-wrap: wrap;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
}
.Welcome-listItem {
	margin-bottom: 5px;
	padding-right: 10px;
	padding-left: 10px;
	font-size: 0;
}
.Welcome-listItem:before {
	content: url("data:image/svg+xml;charset=utf-8,%3Csvg width='12' height='9' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M4.5 9L0 4.846 2.25 2.77 4.5 4.846 9.75 0 12 2.077 4.5 9z' fill='%23C5CACF'/%3E%3C/svg%3E");
}
.Welcome-listItemText {
	display: inline-block;
	margin-left: 5px;
	color: #8c94a5;
	font-family: Calibre, sans-serif;
	font-size: 14px;
}

button {
        outline:none;
        cursor:pointer;
}
</style>
