import Vue from 'vue'
import Router from 'vue-router'
import Container from '@/components/Container'
import Home from '@/components/home'
import test from '@/components/LeftMenu'
import analysis from '@/components/left/analysis'
import present from '@/components/left/present'

Vue.use(Router)

export default new Router({
    mode: 'history',
    scrollBehavior: () => ({
    y: 0
    }),
    routes:[
        {
            path:'/',
            name:'Container',
            component: Container,
            
        },
        {
            path: '/test',
            name: 'test',
            component: test,
            iconCls: 'el-icon-location',
            children:[
            {
                path: '/test/analysis',
                component: analysis,
                name: '数据分析',
                hidden: true
    
            },
            {
                path: '/test/present',
                component: present,
                name: '图像展示',
            },
            {
                path:'/test/home',
                name: 'home',
                component: Home,
            }]   
        },
        
]})