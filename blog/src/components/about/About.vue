<template>
<div>
<div class="banner"></div>
<el-card class="box-card">
	<div class="text item">
   这是一个以搜索为核心的个人学习资料管理工具。<br><br>
   在XSearch中键入关键字之后，XSearch会将不同的搜索引擎中的结果进行刷选、调优及判断，最终只会返回一个结果。
  <br><br>
  返回的结果可以被Mark，Mark之后的结果会存储在个人私有账户中。在Marks页面可以对其进行方便的管理。
  <br><br>
  *XSearch的算法正在进步...
    </div>
</el-card>

<div class="steps">
<el-steps :active="active" align-center>
  <el-step title="搜索" description="使用XSearch刷选出最佳结果"></el-step>
  <el-step title="收藏" description="觉得有用？那就收藏下来吧"></el-step>
  <!-- <el-step title="备注" description="在Marks中为你的收藏添加备注"></el-step> -->
  <el-step title="管理" description="增删改查，随时管理Marks"></el-step>
</el-steps>
<el-button style="margin-top: 12px;float:right;margin-right:10%" @click="next">下一步</el-button>
</div>

</div>
</template>

<script>
export default {
	name: "About",
	data() {
      return {
        active: 0
      };
    },

    methods: {
      next() {
        if (this.active++ > 2) this.active = 0;
      }
    }
  }
</script>

<style>
.steps {
    position: fixed;
    left: 10%;
    right: 10%;
    bottom: 4em;
}
.banner {
    margin-top: 5em;
}
  .text {
    font-size: 14px;
  }

  .box-card {
    margin: 0 auto;
    margin-top: 2em;
    width: 88%;
    max-width: 480px;
  }
</style>
