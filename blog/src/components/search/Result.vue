<template>

     <div v-show="isShow"><el-card class="box-card" v-loading="isLoading">
  <div slot="header" class="clearfix">
    <span>{{title | show25Str}}</span>
    <i v-if="markIconShow" v-bind:class="{'el-icon-star-off':nomark, 'el-icon-star-on':marked}" style="float:right;color:#409EFF" @click="markResult"></i>
  </div>
  <div class="text item">
    {{description}}
  </div>
    <div class="url">
   <el-link type="primary" :href="realurl" target="_blank">{{url}}</el-link>
  </div>
</el-card>
{{result.result}}
</div>

</template>

<script>
import {request} from '../../network/request'
export default {
  name: 'Result',
      data() {
        return {
            markIconShow:false,
            nomark:true,
            marked:false,
            isShow: true,
            isLoading: false,
            title: '搜索历史',
            description: '',
            url: '',
            result: '',
            keyword: '',
            realurl:''
        }
    },
    methods: {
        markResult() {

          request({
            url: '/api/mark/',
            method: 'post',
            headers: {'Authorization':localStorage.getItem('logintoken')},
            data:{
              title: this.title,
              description: this.description,
              url: this.realurl,
              is_mark: this.nomark
            },
            
          }).then(res => {
             console.log('结果'+res);
            //  this.title = res.data.title
            //  this.description = res.data.description
            //  this.url = res.data.url.substring(0,35) + '...'
            //  this.realurl = res.data.url
            //  this.result = res.data
            //  this.isShow = true
            //  this.isLoading = false
          }).catch(err => {
            console.log(123);
            // this.title = '请求失败'
            // this.description = '筛选最优结果失败你可以直接Google该关键词。'
            // this.url = ''
            // this.isShow = true
            // this.isLoading = false
          }) 
          
          if(this.nomark == true){
            this.nomark = false
            this.marked = true
          }else{
            this.nomark = true
            this.marked = false
          }

      },
        searchClick() {
          this.isLoading = true
          const keyword = this.keyword
          console.log(keyword);
          

          
          // request({
          //   url: 'http://127.0.0.1:8000/api/mark/',
          //   method: 'post',
          //   headers: {'Authorization':localStorage.getItem('logintoken')},
          //   data:{
          //     title: this.title,
          //     description: this.description,
          //     url: this.url,
          //     is_mark: this.nomark
          //   },
            
          // }).then(res => {
          //    console.log('结果'+res);
          //   //  this.title = res.data.title
          //   //  this.description = res.data.description
          //   //  this.url = res.data.url.substring(0,35) + '...'
          //   //  this.realurl = res.data.url
          //   //  this.result = res.data
          //   //  this.isShow = true
          //   //  this.isLoading = false
          // }).catch(err => {
          //   console.log(123);
          //   // this.title = '请求失败'
          //   // this.description = '筛选最优结果失败你可以直接Google该关键词。'
          //   // this.url = ''
          //   // this.isShow = true
          //   // this.isLoading = false
          // }) 


          request({
            url: '/api/search/',
            method: 'post',
            headers: {'Authorization':localStorage.getItem('logintoken')},
            data:{
              search: keyword
            },
            // params:{
            //   search: keyword
            // },
            
          }).then(res => {
             console.log('结果'+res.data.title);
             if(res.data.title == undefined){
               rejert()
             }


             this.nomark = true
             this.marked = false
             if(res.data.is_marked) {
               this.nomark = false
               this.marked = true
             }
             this.markIconShow = true

             this.title = res.data.title
             this.description = res.data.description
             this.url = res.data.url.substring(0,35) + '...'
             this.realurl = res.data.url
             this.result = res.data
             this.isShow = true
             this.isLoading = false
          }).catch(err => {
            console.log(123);
            this.title = '请求失败'
            this.description = '筛选最优结果失败你可以直接Google该关键词。'
            this.url = ''
            this.isShow = true
            this.isLoading = false
          }) 

          
        }
    },
    filters: {
      show25Str(str) {
        return str.substring(0,25)
      },
    }
}
</script>

<style scope>
  .text {
    font-size: 14px;
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

  .box-card {
    width: 480px;
    margin: 0 auto;
    margin-top: 4em;
    width: 88%;
    max-width: 490px;
  }


</style>
