

<style lang="less" scoped>

</style>
<template>
    <div>
        <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="100">
            <Row>
                <Col span="5">
                <FormItem label="处理吨数" prop="ability">
                    <Input type="text" v-model="formInline.ability" placeholder="165-210"> </Input>
                </FormItem>
                </Col>
                <Col span="6">
                <FormItem>
                    <Button type="primary" @click="handleSearch()">搜索</Button>
                </FormItem>
                </Col>
            </Row>
        </Form>
        <Tabs value="name1">
            <TabPane :label="label" name="baseInfo">
                <div id="printMe" class="print-area">
                    <Table striped border ref="selection" :columns="columns" :data="v1">
                    </Table>
                </div>
            </TabPane>
            <TabPane label="性价比最佳报告" name="name3">
                <div id="printMe" class="print-area">
                    <Table striped border ref="selection" :columns="columns" :data="v2">
                    </Table>
                </div>
            </TabPane>
            <TabPane label="性能最好报告" name="fajiao">
                <div id="printMe" class="print-area">
                    <Table striped border ref="selection" :columns="columns" :data="v3">
                    </Table>
                </div>
            </TabPane>

        </Tabs>
    </div>
</template>

<script lang="ts">
import { resolveComponent, reactive, ref } from 'vue';
import axios from 'axios'

export default {
    name: "DemoTabs",
    setup() {
        const columns = [
            {
                title: '装置',
                key: '装置'
            },
            {
                title: '参数',
                key: '参数'
            },
            {
                title: '材质',
                key: '材质'
            },
            {
                title: '价格（万元）',
                key: '价格（万元）'
            },
            {
                title: '数量',
                key: '数量',
            },
            {
                title: '得分',
                key: '得分',
            },
            {
                title: '总价',
                key: '总价',
            },
            {
                title: '总能力',
                key: '总能力',
            },

            {
                title: '厂家',
                key: '厂家',
                width: 250,
            }];
        let formInline = reactive({
            ability: '',
            budget: ''
        })
        let v1 = ref()
        let v2 = ref()
        let v3 = ref()
        const ruleInline = {
            budget: [
                { message: '请输入预算', trigger: 'blur' }
            ],
            ability: [
                { message: '请输入处理量', trigger: 'blur' },
                // { type: 'number', max: 3, message: '年龄必须是数字', trigger: 'blur' }
            ]
        }

        const handleSearch = () => {
            console.log("ability:" + formInline.ability)
            let ability= formInline.ability==''?"210":formInline.ability
            var url1 = `/api/score/${ability}/`
            axios.get(url1)
                .then(response => {
                    //   this. = response.data;
                    v1.value = response.data;
                    console.log(v1.value);
                })
                .catch(error => {
                    console.log(error);
                });
            var url2 = `/api/badget/${ability}/`
            axios.get(url2)
                .then(response => {
                    //   this. = response.data;
                    v2.value = response.data;
                    console.log(v1.value);
                })
                .catch(error => {
                    console.log(error);
                });
            var url3 = `/api/ability/${ability}/`
            axios.get(url3)
                .then(response => {
                    //   this. = response.data;
                    v3.value = response.data;
                    console.log(v1.value);
                })
                .catch(error => {
                    console.log(error);
                });
        }

        const label = (h: any) => {
            return h('div', [
                h('span', '综合评分最高报告'),
                h(resolveComponent('Badge'), {
                    count: 1
                })
            ])
        }
        return {
            label,
            formInline,
            handleSearch,
            columns,
            v1,
            v2,
            v3
        }
    },
};
</script>
