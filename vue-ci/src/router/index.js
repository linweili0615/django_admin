import Vue from 'vue'
import Router from 'vue-router'
import joblist from '@/components/joblist'
import test from '@/components/test'

Vue.use(Router)

//f
export default new Router({
  routes: [
    {
      path: '/',
      name: 'joblist',
      component: joblist
    }
  ]
})
