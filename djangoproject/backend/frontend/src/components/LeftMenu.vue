<template>
  <el-container>
    <el-aside width="200px">
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        background-color="rgb(58, 153, 94)"
        active-text-color="rgb(58, 153, 94)"
        text-color="#eee"
        router
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>Integration</span>
          </template>
          <el-menu-item-group>
            <template slot="title"></template>
            <el-menu-item index="/test/analysis">数据清洗</el-menu-item>
            <el-menu-item index="/test/present">图像展示</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group>
            <el-menu-item index="/test/home">home</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="2">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-container>
      <el-main>
        <el-col :span="24" class="content-wrapper">
          <transition name="fade" mode="out-in">
            <router-view></router-view>
          </transition>
        </el-col>
      </el-main>
    </el-container>
  </el-container>
</template>
<style>
.el-aside {
  background-color: rgb(70, 180, 112);
  color: rgb(58, 153, 94);
  text-align: center;
  line-height: 400px;
}

.el-main {
  background-color: hsl(145, 61%, 90%);
  color: hsl(0, 0%, 20%);
  text-align: center;
  line-height: 360px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
