<template>
<div>
  <div class="banner"></div>
  
  <div v-for="i in res" :key='i.title'>
 
  <el-card class="blog-box-card">
  <div slot="header" class="clearfix">
    <span>{{i.title}}</span>
    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
  </div>


<!-- <el-collapse v-model="activeNames" @change="handleChange(i.id)">
   <el-collapse-item :name="i.id">
     <div slot="title">{{i.content.substring(0,18)}}</div> -->
  
  <div class="text item">
    {{i.content}}
  </div>
<!-- </el-collapse-item>
</el-collapse> -->

    <div style="font-size:0.8em;margin-top:1em;">
    <i class="el-icon-date"> {{i.time}}</i><el-button style="float: right; padding: 3px 0" type="text" @click="handleChange(i.id)"><i class="el-icon-date" style="float:right;color:#66b1ff;"> Read All</i></el-button>
  </div>
</el-card>

</div>
<div class="pages">
<div class="block">
    <el-pagination
      background
      @current-change="handleCurrentChange"
      layout="prev, pager, next"
      :page-count=pagecount	
      :page-size=8>
    </el-pagination>
  </div>
  </div>
  <div class="hidden-sm-and-down"><footer-cpn></footer-cpn></div>

   <div id="space" class="hidden-sm-and-up" style="margin-bottom: 65px;"></div>

 <el-backtop :bottom="100"></el-backtop>
</div>


</template>

<script>
import {request} from '../../network/request'
import axios from 'axios'
import FooterCpn from 'components/footer/FooterCpn'
export default {
  name: 'Blog',
  components: {
    FooterCpn
  },
  created() {
    this.handleCurrentChange(1)
  },
  data() {
    return {
      decShow: true,
      nodecShow: false,
      showtitle:'',
      nums: 10,
      pagecount: 0,
      res: '',
      // activeNames: ['1'],
      blogId:''
    }
  },
  methods: {
    more(i) {
      console.log(i);
    },
    // handleChange(val) {
    //   if(this.activeNames.indexOf(val)){
    //   }else{
    //     this.activeNames.push(val)
    //   }
      
    //   console.log(this.activeNames);
    // },
    handleCurrentChange(val) {
      request({
        url: '/api/blog/',
        params:{
              page: val
            },
      }).then(res => {
        this.res = res.data
        this.pagecount = this.res.pop()
        scrollTo(0,0);
        console.log(res.data)
      })
        console.log(val);
      }
  }
}
</script>

<style scoped>
.el-collapse-item {
    padding-bottom: 0px;
    font-size: 14px;
    border-bottom: 0px !important;
}


.el-card {
    padding-top: 0.1em !important;
}
.el-collapse {
    border-top: 0px solid #EBEEF5;
    border-bottom: 0px solid #EBEEF5;
}
.pages{
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1em;
}
.banner{
  height: 3em;
}
  .text {
    font-size: 14px;
    letter-spacing: 0.1em;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

 
  .blog-box-card {
    margin: 0 auto;
    margin-top: 2em;
    width: 88%;
    max-width: 800px;
  }
</style>
