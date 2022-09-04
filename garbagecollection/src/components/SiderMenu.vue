
<script lang="ts">
import { ref, computed, watch} from "vue";
import { userStore } from "../stores/counter";
import { useRoute, useRouter } from "vue-router";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    // 获取store
    const store = userStore();
    let menu = computed(() => store.menuList);
    let isCollapsed = computed(() => store.meunIsCollapsed);
    let sideMenu = ref();
    let fullPath = computed(() => route.fullPath);

    const menuitemClasses = computed(() => {
      return [
        'menu-item',
        isCollapsed.value ? 'collapsed-menu' : ''
      ]
    })
    const goPage = (path: string) => {
      router.push(path);
    }

    watch(isCollapsed, () => {
      if (sideMenu) {
        sideMenu.value.toggleCollapse();
      }
    });
    return {
      isCollapsed,
      menuitemClasses,
      sideMenu,
      goPage,
      menu,
      fullPath
    };
  },
};
</script>

<template>
  <Sider ref="sideMenu" hide-trigger collapsible :collapsed-width="78" :width="220" v-model="isCollapsed" class="sider">

    <Menu :theme="menuTheme" width="auto" :class="menuitemClasses" accordion>
      <template v-for="item in menu">
        <!-- 有二级子菜单 -->
        <Submenu v-if="item.children && item.children.length" :key="'1_' + item.id" :name="item.id">
          <template #title>
            <Icon :type="item.icon" />
            <span>{{ item.title }}</span>

            <!-- 菜单栏收起时，二级子菜单渲染 -->
            <Dropdown v-if="isCollapsed" placement="right-start" class="drop-down-menu">
              <div>&nbsp;</div>
              <template #list>
                <DropdownMenu>
                  <!-- 展开二级子菜单 -->
                  <template v-for="item2 in item.children">
                    <!-- 展开并且有三级子菜单 -->
                    <Dropdown v-if="item2.children && item2.children.length" :key="item2.id" placement="right-start">
                      <DropdownItem>
                        <div class="ivu-menu-item">
                          {{item2.title}}
                          <Icon type="ios-arrow-forward"></Icon>
                        </div>
                      </DropdownItem>
                      <template #list>
                        <DropdownMenu>
                          <DropdownItem v-for="(item3, index3) in item2.children" :key="index3">
                            <MenuItem :name="item3.id" :to="item3.path">{{ item3.title }}</MenuItem>
                          </DropdownItem>
                        </DropdownMenu>
                      </template>
                    </Dropdown>

                    <!-- 无三级子菜单 -->
                    <DropdownItem v-else :key="item2.id">
                      <MenuItem :name="item2.id" :to="item2.path">{{ item2.title }}</MenuItem>
                    </DropdownItem>
                  </template>
                </DropdownMenu>
              </template>
            </Dropdown>
          </template>

          <!-- 菜单栏展开时，二级子菜单渲染 -->
          <div v-if="!isCollapsed">
            <!-- 二级子菜单渲染 -->
            <template v-for="item2 in item.children">
              <!-- 有三级子菜单 -->
              <Submenu v-if="item2.children && item2.children.length" :key="item2.id" :name="item2.id">
                <template #title>
                  <span>{{ item2.title }}</span>
                </template>
                <MenuItem v-for="(item3, index3) in item2.children" :key="index3" :name="item2.path" :to="item3.path">
                <span>{{ item3.title }}</span>
                </MenuItem>
              </Submenu>

              <!-- 无三级子菜单 -->
              <MenuItem v-else :key="item2.id" :name="item2.path" :to="item2.path">
              <span>{{ item2.title }}</span>
              </MenuItem>
            </template>
          </div>
        </Submenu>

        <!-- 没有子菜单 -->
        <MenuItem v-else :name="item.id" :to="item.path" :key="'2_'+ item.id">
        <Icon :type="item.icon" />
        <span>{{ item.title }}</span>
        <Tooltip v-if="isCollapsed" :content="item.title" placement="right">
          <span></span>
        </Tooltip>
        </MenuItem>

      </template>
    </Menu>

  </Sider>
</template>

<style lang="less" scoped>
.sider {
  background-color: #fff;
}

.ivu-tooltip {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

 :deep(.ivu-tooltip-rel) {
    width: 100%;
    height: 100%;
  }
}

.drop-down-menu {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

  :deep(.ivu-select-dropdown) {
    width: auto;
  }

  :deep(.ivu-dropdown-rel) {
    width: 100%;
    height: 100%;
  }
}
.menu-item {
  height: 100%;

  span {
    display: inline-block;
    overflow: hidden;
    width: 100px;
    text-overflow: ellipsis;
    white-space: nowrap;
    vertical-align: bottom;
    transition: width 0.2s ease 0.2s;
  }
  i {
    transform: translateX(0px);
    transition: font-size 0.2s ease, transform 0.2s ease;
    vertical-align: middle;
    font-size: 16px;
  }
}

.collapsed-menu {
  :deep(.ivu-menu-submenu-title) {
    .ivu-menu-submenu-title-icon {
      display: none;
    }
  }

  span {
    width: 0px;
    transition: width 0.2s ease;
  }
  i {
    transform: translateX(5px);
    transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
    vertical-align: middle;
    font-size: 22px;
  }

  :deep(.ivu-select-dropdown) {
    margin: 0 0 0 5px;
  }

  :deep(.ivu-dropdown-item) {
    padding: 0;
  }
}
</style>