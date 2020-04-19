<template>
<div v-if="!islogin" class="loginform">
    <el-card class="box-card">
	<el-form ref="loginForm" :model="form" :rules="rules">
  <el-form-item label="账号" prop="username">
    <el-input type="username" v-model="form.username"></el-input>
  </el-form-item>
  <el-form-item label="密码" prop="password">
    <el-input type="password" v-model="form.password"></el-input>
  </el-form-item>
  <el-button type="primary" v-on:click="submitForm('loginForm')">登录</el-button>
</el-form>
</el-card>
</div>
</template>

<script>
import axios from 'axios'
import {request} from '../network/request'
export default {

  name: 'Login',

  data() {
      return {
        islogin: false,
          form: {
            username: '',
            password: ''
        },
               rules: {
          username: [
            {required: true, message: '账号不可为空', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '密码不可为空', trigger: 'blur'}
          ]
        },
      }
  },
  created() {
              request({
              url:'/api/do_something/',
              method: 'post',
              headers: {'Authorization':localStorage.getItem('logintoken')}
          }).then((res) => {
            if(res.data.msg == '验证通过'){
              this.islogin = true
              this.$router.push('/blog')
            }
          })
  },

  methods: {
       submitForm(formName) {
      this.$refs[formName].validate(valid => {  //vue前台的验证规则
        if (valid) {
          let data = new FormData()
          data.append('username',this.form.username)
          data.append('password',this.form.password)
          request({
              url:'/api/login/',
              method: 'post',
              data: data
          }).then((res) => {
            if(res.data.token){
              console.log(res.data)
              localStorage.setItem('logintoken',res.data.token)
              this.$store.commit('changeLoginStatus')
              console.log(this.$store.state.loginStatus);
              this.loginSuccess()
              // this.$router.push('/blog')
              
              // setTimeout(() => {
              //   window.location.reload();
              // }, 10);
              setTimeout(() => {
                window.location.href="/#/blog";
                window.location.reload();
              }, 500);
              
            }else{
              this.loginFaild()
            }
          })
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

          loginSuccess() {
        this.$notify({
          title: '登录成功',
          message: '欢迎登录，祝您开心',
          type: 'success'
        });
      },

              loginFaild() {
        this.$notify({
          title: '登陆失败',
          message: '请检查账号或密码',
          type: 'error'
        });
      },

  },
  
}
</script>

<style>
.loginform {
    margin: 0 auto;
    margin-top: 2em;
    width: 88%;
    max-width: 480px;
    margin-top: 10%;
  }
</style>
