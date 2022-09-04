<style lang="less" scoped>
</style>
<template>
  <div>
    <Row>
      <Col v-padding="20" :span="12">
      <Card style="width:100%">
        <template #title>
          <Icon type="ios-film-outline"></Icon>
          Classic film
        </template>
        <template #extra>
          <a href="#" @click.prevent="changeLimit">
            <Icon type="ios-loop-strong"></Icon>
            Change
          </a>
        </template>
        <p class="rate-demo" v-for="(item, index) in randomMovieList" :key="index">
          <a :href="item.url" target="_blank">{{ item.name }}</a>
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
          <h1>4,000</h1>
          <p>下载人数</p>
          <span>
            占总人数
            <i>75%</i>
          </span>
        </div>
      </Circle>
      </Col>

      <Col v-padding="20" :span="6">
      <Timeline>
        <TimelineItem color="green">发布1.0版本</TimelineItem>
        <TimelineItem color="green">发布2.0版本</TimelineItem>
        <TimelineItem color="red">严重故障</TimelineItem>
        <TimelineItem color="blue">发布3.0版本</TimelineItem>
        <TimelineItem color="blue">发布4.0版本</TimelineItem>
        <TimelineItem color="blue">发布5.0版本</TimelineItem>
      </Timeline>
      </Col>
    </Row>

    <Row>
      <Col v-padding="20" :span="24">
      <Calendar :cell-height="50" />
      </Col>
    </Row>

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
        name: 'The Shawshank Redemption',
        url: 'https://movie.douban.com/subject/1292052/',
        rate: 9.6
      },
      {
        name: 'Leon:The Professional',
        url: 'https://movie.douban.com/subject/1295644/',
        rate: 9.4
      },
      {
        name: 'Farewell to My Concubine',
        url: 'https://movie.douban.com/subject/1291546/',
        rate: 9.5
      },
      {
        name: 'Forrest Gump',
        url: 'https://movie.douban.com/subject/1292720/',
        rate: 9.4
      },
      {
        name: 'Life Is Beautiful',
        url: 'https://movie.douban.com/subject/1292063/',
        rate: 9.5
      },
      {
        name: 'Spirited Away',
        url: 'https://movie.douban.com/subject/1291561/',
        rate: 9.2
      },
      {
        name: 'Schindler\'s List',
        url: 'https://movie.douban.com/subject/1295124/',
        rate: 9.4
      },
      {
        name: 'The Legend of 1900',
        url: 'https://movie.douban.com/subject/1292001/',
        rate: 9.2
      },
      {
        name: 'WALL·E',
        url: 'https://movie.douban.com/subject/2131459/',
        rate: 9.3
      },
      {
        name: 'Inception',
        url: 'https://movie.douban.com/subject/3541415/',
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
