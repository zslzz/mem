<style lang="less" scoped>
</style>
<template>
  <div>
    <Row>
      <Col v-padding="20" :span="12">
      <Card style="width:100%">
        <template #title>
          <Icon type="ios-film-outline"></Icon>
          报告推荐
        </template>
        <template #extra>
          <a href="#" @click.prevent="changeLimit">
            <Icon type="ios-loop-strong"></Icon>
            换一换
          </a>
        </template>
        <p class="rate-demo" v-for="(item, index) in randomMovieList" :key="index">
          <router-link :to="item.url">{{ item.name }}</router-link>
          <span>
            <Rate disabled v-model="item.rate" />{{ item.rate }}
          </span>
        </p>
      </Card>
      </Col>

      <Col v-padding="20" :span="6">
      <Circle :size="250" :trail-width="4" :stroke-width="5" :percent="75" stroke-linecap="square"
        stroke-color="#43a3fb">
        <div class="demo-Circle-custom">
          <h1>4,00</h1>
          <p>下载人数</p>
          <span>
            占总浏览人数
            <i>75%</i>
          </span>
        </div>
      </Circle>
      </Col>

      <Col v-padding="20" :span="6">
      <Timeline>
        <TimelineItem color="green">发布0.1版本</TimelineItem>
        <TimelineItem color="green">发布0.2版本</TimelineItem>
        <TimelineItem color="red">正式上线啦 1.0版本</TimelineItem>
        <TimelineItem color="blue">100设备导入</TimelineItem>
        <TimelineItem color="blue">10人浏览</TimelineItem>
        <TimelineItem color="blue">10人下载</TimelineItem>
      </Timeline>
      </Col>
    </Row>

    <!-- <Row>
      <Col v-padding="20" :span="24">
      <Calendar :cell-height="50" />
      </Col>
    </Row> -->

  </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue';
interface Movie {
  name?: string,
  url?: string,
  rate?: number
}
export default {
  name: "DemoHome",
  setup() {
    let movieList: Array<Movie> = [
      {
        name: '最佳性价比',
        url: '/deviceReport1',
        rate: 9.6
      },
      {
        name: '最经济',
        url: 'deviceReport2',
        rate: 9.4
      },
      {
        name: '最稳定',
        url: 'deviceReport3',
        rate: 9.5
      },
      {
        name: '最人气',
        url: 'deviceReport1',
        rate: 9.4
      },
      {
        name: '当前选择最多',
        url: 'deviceReport1',
        rate: 9.5
      },
      {
        name: '查看最多',
        url: 'deviceReport1',
        rate: 9.2
      },
      {
        name: '下载最多',
        url: 'deviceReport1',
        rate: 9.4
      },
      {
        name: '历史最佳',
        url: 'deviceReport1',
        rate: 9.2
      }
    ]

    let randomMovieList = ref(movieList);

    const getArrayItems = (arr: Array<Movie>, num: number) => {
      const temp_array = [];
      for (let index in arr) {
        temp_array.push(arr[index]);
      }
      const return_array = [];
      for (let i = 0; i < num; i++) {
        if (temp_array.length > 0) {
          const arrIndex = Math.floor(Math.random() * temp_array.length);
          return_array[i] = temp_array[arrIndex];
          temp_array.splice(arrIndex, 1);
        } else {
          break;
        }
      }
      return return_array;
    }
    const changeLimit = () => {
      randomMovieList.value = getArrayItems(movieList, 5);
    }

    onMounted(() => {
      changeLimit();
    })

    return {
      randomMovieList,
      changeLimit
    }
  },
};
</script>
