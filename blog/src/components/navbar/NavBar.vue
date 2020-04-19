<template>
	<div class="nav-bar">
		<el-container>
			<el-header>
				<div class="header">
					<el-row type="flex" class="row-bg" justify="space-between">



							<el-col class="hidden-sm-and-up">
							<div>

								<slot name="left">
									<h1>XiaoXi</h1>
								</slot>

							</div>
						</el-col>



						<el-col :span="5" class="hidden-xs-only">
							<div class="left">

								<slot name="left">
									<h1>XiaoXi</h1>
								</slot>

							</div>
						</el-col>
						<el-col :span="7" class="hidden-sm-and-down">
							<div class="center">
								<slot name="center">


<el-menu :default-active="this.$route.path" router mode="horizontal">
    <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
    </el-menu-item>
</el-menu>


									<!-- <el-menu
										:default-active="activeIndex"
										class="el-menu-demo"
										mode="horizontal"
										@select="handleSelect"
									>
										<el-menu-item index="1" path="/search">
											<router-link to="/search">Search</router-link>
										</el-menu-item>
										<el-menu-item index="2">
											<template slot="title">
												<router-link to="/blog">Blog</router-link>
											</template>
										</el-menu-item>
										<el-menu-item index="3">Notebooks</el-menu-item>
										<el-menu-item index="4">Marks</el-menu-item>
										<el-menu-item index="5">Links</el-menu-item>
									</el-menu> -->
								</slot>
							</div>
						</el-col>


						<el-col class="hidden-sm-and-up">
							<div style="margin-top:17px;float:right">
								<slot name="right">

									<router-link to="/login" v-if="!loginStatus"><el-button round >Sign In{{loginStatus}}</el-button></router-link>
									<el-button round v-else @click="outLog">Log Out</el-button>
								</slot>
							</div>
						</el-col>


						<el-col :span="5" class="hidden-xs-only">
							<div class="right">
								<slot name="right">

									<router-link to="/login" v-if="!loginStatus"><el-button round >Sign In{{loginStatus}}</el-button></router-link>
									<el-button round v-else @click="outLog">Log Out</el-button>
								</slot>
							</div>
						</el-col>
					</el-row>
				</div>
			</el-header>
		</el-container>

	</div>
</template>

<script>

export default {
	components: {
   
  },
  name: "NavBar",
	data() {
		return {
			loginStatus: localStorage.getItem('logintoken'), //获取token挺好的
      navList:[
            {name:'/search',navItem:'Search'},
            {name:'/blog',navItem:'Blog'},
            {name:'/notes',navItem:'Notes'},
            {name:'/marks',navItem:'Marks'},
            {name:'/links',navItem:'Links'},
        ],
      		blog: '/blog',
			activeIndex: "1",
			activeIndex2: "1",
		};
	},
	methods: {
		handleSelect(key, keyPath) {
      if (key == 1){
        this.$router.push('/search')
      }
      console.log(key, keyPath);
      
	},
	
	outLog() {
      localStorage.removeItem('logintoken')
      window.location.reload()
	},
	
	}
};
</script>

<style scoped>


h1 {
	color: #303133;
}
.left {
  float: right;
  margin-top: -7px;
}

.right {
	float: left;
	margin-top: 10px;
}
.center {
	float: right;
}
.header {
	margin-top: 20px;
}
</style>
