<template>
  <div id="app">
    <!-- 头部导航 -->
        <header class="header">
          <el-row>
              <el-col :span="24">
                <el-menu default-active="2" class="el-menu-demo" mode="horizontal" >
                  <el-menu-item index="1">构建队列</el-menu-item>
                  <el-menu-item index="2">我的工作台</el-menu-item>
                  <el-menu-item index="3">测试平台</el-menu-item>
                  <el-menu-item index="4">后台管理</el-menu-item>
                </el-menu>
              </el-col>
          </el-row>
        </header>
        <main>
           <router-view></router-view> 
        </main>
  </div></template>

<script>
export default {
      name: 'app',
      data: function (){
        return {
          active:true
        }
      }
    }
</script>

<style>
body{margin: 0;}
#app {
      min-width: 1200px;
      margin: 0 auto;
      font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
    }
/* 头部导航 */
header{z-index: 1000;min-width: 1200px;transition: all 0.5s ease;  background-color: #fff;  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);  }
header.header-fixed{position: fixed;top: 0;left: 0;right: 0;}
header .el-menu-demo{padding-left: 300px!important;}

/* 主内容区 */
  main{    display: -webkit-box;  display: -ms-flexbox;  display: flex;  min-height: 100%;  border: solid 2px #E9ECF1;  background-color: #FCFCFC;  }
</style>
