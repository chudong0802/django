<template>
  <div id="app">
    <div class="nav">
      <ul>
        <router-link :to="{ name: 'Container' }">index</router-link> |
        <router-link :to="{ name: 'test' }">test</router-link> |
        <!-- <router-link :to="{ name: 'home' }">home</router-link> | -->
        <!-- <router-link :to="{ name: '数据分析' }">data</router-link> |
        <router-link :to="{ name: '图像展示' }">data2</router-link> | -->

      </ul>
    </div>
    <div class="main">
      <router-view/>
    </div>
  </div>
</template>
<script>
</script>
<style>
</style>