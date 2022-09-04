
<style lang="less" scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  min-height: 100%;

  .ivu-layout-has-sider {
    background: red;
  }
}
</style>
<template>
  <Layout class="layout">
    <my-header></my-header>
    <Layout class="ivu-layout-has-sider" :style="{padding: '0'}">
      <my-menu></my-menu>
      <Layout :style="{padding: '0'}">
        <my-tags></my-tags>
        <div :style="{padding: '0 24px 24px'}">
          <Breadcrumb :style="{margin: '0 0 10px 0'}">
            <BreadcrumbItem v-for="item in tagsName" :key="item">{{item}}</BreadcrumbItem>
          </Breadcrumb>
          <Content :style="{padding: '24px', minHeight: '280px', background: '#fff'}">
            <router-view v-slot="{ Component }">
              <transition name="move" mode="out-in">
                <keep-alive :include="tagsList">
                  <component :is="Component" />
                </keep-alive>
              </transition>
            </router-view>
          </Content>
        </div>
      </Layout>
    </Layout>
  </Layout>
</template>

<script lang="ts">
import myHeader from "../components/Header.vue";
import myMenu from "../components/SiderMenu.vue";
import myTags from "../components/Tags.vue";
import { computed } from "vue";
import { userStore } from "../stores/counter";
import { useRoute, useRouter } from "vue-router";

export default {
  name: "MainPage",
  components: {
    myHeader,
    myMenu,
    myTags,
  },
  setup() {
    const route = useRoute();
    const store = userStore();
    const tagsList = computed(() =>
      store.tagsList.map((item) => item.name)
    );
    const tagsName = computed(() =>
      route.meta.tags
    );
    return {
      tagsList,
      tagsName
    }
  },
};
</script>
