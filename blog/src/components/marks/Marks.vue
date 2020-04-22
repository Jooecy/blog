<template>
<div>
    <div class="banner"></div>
    <div v-if="!marksList" style="text-align:center">暂无Mark</div>
     <div v-for="(i, index) in marksList" :key="i.url"><el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>{{i.title | show25Str}}{{index}}</span>
    <i class="el-icon-delete" style="float:right;color:#409EFF;cursor:pointer" @click="open(index)"></i>
  </div>
  <div class="text item">
    {{i.description}}
  </div>
    <div class="url">
   <el-link type="primary" :href="i.url" target="_blank">{{i.url.substring(0,35) + '...'}}</el-link>
  </div>
</el-card>

</div>
<div class="banner"></div>
</div>
</template>

<script>
import {request} from '../../network/request'
export default {
  name: 'Marks',
  data() {
      return {
          marksList:[],
      }
  },
  created() {

      request({
        url: '/api/do_something/',
        method: 'post',
        headers: {'Authorization':localStorage.getItem('logintoken')}
      }).then(request({
        url: '/api/mark/all',
        method: 'post',
        headers: {'Authorization':localStorage.getItem('logintoken')},
      }).then(res => {
             console.log(res);
             this.marksList = res.data
          }).catch(err => {
            console.log(123);
     
          }) ).catch(err => {
            this.$router.push('/login')
          })

      // request({
      //   url: '/api/mark/all',
      //   method: 'post',
      //   headers: {'Authorization':localStorage.getItem('logintoken')},
      // }).then(res => {
      //        console.log(res);
      //        this.marksList = res.data
      //     }).catch(err => {
      //       console.log(123);
     
      //     }) 

  },
  methods: {
      delMark(index) {
        
        // console.log(this.marksList[index]['url']);
        request({
        url: '/api/mark/list_del_mark',
        method: 'post',
        headers: {'Authorization':localStorage.getItem('logintoken')},
        data:{
            url: this.marksList[index]['url']
        },
      }).then(res => {
             console.log(res);
             this.marksList = res.data
          }).catch(err => {
            console.log(123);
     
          }) 
        this.marksList.splice(index,1)
      },

          open(index) {
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.delMark(index)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
      }

  },

    filters: {
        show25Str(str) {
        return str.substring(0,25)
        },
    },

}
</script>

<style scoped>
.box-card {
   width: 480px;
    margin: 0 auto;
    margin-top: 2em;
    width: 88%;
    max-width: 490px;
}
.banner {
    margin-top: 5em;
}
</style>
