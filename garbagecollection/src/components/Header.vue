<script lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { userStore } from "../stores/counter";
import screenfull from "screenfull";

export default {
  setup() {
    // 获取store
    const store = userStore();
    const router = useRouter();
    let isCollapsed = computed(() => store.meunIsCollapsed);

    const collapsedSider = () => {
      store.setMeunIsCollapsed(!isCollapsed.value);
    }

    let rotateIcon = computed(() => {
      return [
        'menu-icon',
        isCollapsed.value ? 'rotate-icon' : ''
      ];
    })

    const signOut = () => {
      store.setLoginUser("");
      sessionStorage.removeItem('token');
      router.push("/login");
    }


    const messageBaseList = [
      {
        icon: 'md-mail',
        iconColor: '#3391e5',
        title: '蒂姆·库克回复了你的邮件',
        read: 1,
        time: 1557297198
      },
      {
        icon: 'md-home',
        iconColor: '#87d068',
        title: '乔纳森·伊夫邀请你参加会议',
        read: 0,
        time: 1557297198
      },
      {
        icon: 'md-information',
        iconColor: '#fe5c57',
        title: '斯蒂夫·沃兹尼亚克已批准了你的休假申请',
        read: 1,
        time: 1557297198
      },
      {
        icon: 'md-star',
        iconColor: '#ff9900',
        title: '史蒂夫·乔布斯收藏了你的文章',
        read: 1,
        time: 1557297198
      },
      {
        icon: 'md-people',
        iconColor: '#f06292',
        title: '比尔·费尔南德斯通过了你的好友申请',
        read: 1,
        time: 1557297198
      }
    ]
    let messageList = ref(messageBaseList);
    let messageLoading = ref(false)

    let unreadMessage = computed(() => {
      let unread = 0;
      messageList.value.forEach(item => {
        if (item.read == 0) unread++;
      });
      return unread;
    })

    const handleLoadMore = () => {
      if (messageLoading.value) return;
      messageLoading.value = true;
      setTimeout(() => {
        messageList.value = messageList.value.concat([...messageBaseList]);
        messageLoading.value = false;
      }, 1000);

    }

    const handleClear = () => {
      messageList.value = messageList.value.map(item => {
        item.read = 1;
        return item;
      });
    }

    onMounted(() => {
      messageList.value = [...messageBaseList];
    })

    const toggleFullscreen = () => {
      //判断是否支持全屏
      if (screenfull.isEnabled) {
        screenfull.toggle()
      }
    }

    return {
      rotateIcon,
      collapsedSider,
      signOut,
      messageList,
      messageLoading,
      unreadMessage,
      handleLoadMore,
      handleClear,
      toggleFullscreen
    };
  },
};
</script>
<template>
  <Header class="header">
    <Row>
      <Col span="6" class="header-title">
      <Icon @click="collapsedSider" :class="rotateIcon" type="md-menu" size="30">
      </Icon>
      <div class="header-logo">后台管理系统</div>
      </Col>

      <Col span="18" class="header-menu">
      <Icon class="hearder-full" type="ios-expand" @click="toggleFullscreen" size="24" />

      <div class="header-notification">
        <Notification auto-count @on-load-more="handleLoadMore" @on-clear="handleClear">
          <NotificationTab title="通知" name="message" :count="unreadMessage" :loading="messageLoading">
            <NotificationItem v-for="(item, index) in messageList" :key="index" :title="item.title" :icon="item.icon"
              :icon-color="item.iconColor" :time="item.time" :read="item.read" />
          </NotificationTab>
        </Notification>
      </div>

      <div class="header-user">
        <img class="header-photo" src="../images/tx.jpg">
        <Dropdown>
          <a href="javascript:void(0)">
            admin
            <Icon type="md-arrow-dropdown" size="20" />
          </a>
          <template #list>
            <DropdownMenu>
              <DropdownItem>修改密码</DropdownItem>
              <DropdownItem @click="signOut">退出</DropdownItem>
            </DropdownMenu>
          </template>
        </Dropdown>
      </div>
      </Col>
    </Row>
  </Header>
</template>

<style lang="less" scoped>
.header {
  padding: 0;
}

.header-logo {
  border-radius: 3px;
  font-size: 22px;
}

.header-title {
  color: #fff;
  display: flex;
  line-height: 60px;

  :deep(i) {
    margin: 15px 20px;
  }
}

.header-menu {
  display: flex;
  justify-content: right;
  color: #fff;
  align-items: center;
  line-height: 24px;

  > .hearder-full {
    margin: 0 10px;
    cursor: pointer;
  }

  > .header-notification {
    margin: 0 10px;
    width: 24px;
    height: 24px;
  }

  > .header-user {
    margin: 0 10px;
    height: 60px;
    display: flex;
    align-items: center;
    > img {
      margin-right: 10px;
    }
    :deep(i) {
      margin: 0;
    }
  }
}

.header-photo {
  width: 50px;
  height: 50px;
  border-radius: 25px;
}

.menu-icon {
  transition: all 0.3s;
}

.rotate-icon {
  transform: rotate(-90deg);
}
</style>
