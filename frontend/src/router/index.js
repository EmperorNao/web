import Vue from 'vue'
import VueRouter from 'vue-router'
import ServicesView from '@/views/ServicesView'
import DemoView from "@/views/DemoView";
import ReviewsView from "@/views/ReviewsView";
import ContactsView from "@/views/ContactsView";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: ServicesView
  },
  {
    path: '/demo',
    name: 'demo',
    component: DemoView
  },
  {
    path: '/reviews',
    name: 'reviews',
    component: ReviewsView
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactsView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
