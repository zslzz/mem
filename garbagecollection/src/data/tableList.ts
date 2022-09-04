export declare interface TableData {
    name?: string,
    age?: string,
    address?: string,
    date?: string
}

export declare interface DeviceResultData {
    device?: string,
    measure?: string,
    count?: string,
    value?: string,
    totalValue?:string
}

//50t
export const deviceResult1: Array<DeviceResultData> =[{
    device: '预处理系统',
    totalValue: '701.75'
  }, {
    device: '接收系统',
    totalValue: '135.6'
  },{
    device: '接收装置',
    measure: '套',
    count: '1',
    value: '105',
    totalValue: '105'
  },{
    device: '固液分离装置',
    measure: '套',
    count: '1',
    value: '18.6',
    totalValue: '18.6'
  },{
    device: '沥液装置',
    measure: '套',
    count: '2',
    value: '6',
    totalValue: '12'
  },{
    device: '分选制浆系统',
    totalValue: '293'
  },{
    device: '分拣装置',
    measure: '套',
    count: '1',
    value: '125',
    totalValue: '125'
  },{
    device: '液压站',
    measure: '台',
    count: '1',
    value: '12',
    totalValue: '12'
  },{
    device: '筛下物料输送装置',
    measure: '套',
    count: '1',
    value: '26',
    totalValue: '26'
  },{
    device: '浆料输送装置',
    measure: '套',
    count: '1',
    value: '10',
    totalValue: '10'
  },{
    device: '除杂系统',
    totalValue: '131.4'
  },{
    device: '浆料沥液混合装置',
    measure: '套',
    count: '1',
    value: '2.25',
    totalValue: '2.25'
  },{
    device: '沉砂装置',
    measure: '套',
    count: '1',
    value: '36',
    totalValue: '39.75'
  },{
    device: '除杂装置',
    measure: '套',
    count: '1',
    value: '47.4',
    totalValue: '47.4'
  },{
    device: '杂质输送系统',
    measure: '套',
    count: '1',
    value: '7.5',
    totalValue: '39'
  },{
    device: '油脂分离系统',
    totalValue: '141.75'
  },{
    device: '油水混合装置',
    measure: '套',
    count: '1',
    value: '3.75',
    totalValue: '48.75'
  },{
    device: '三相分离装置',
    measure: '套',
    count: '2',
    value: '3',
    totalValue: '57'
  },{
    device: '固相沉降罐',
    measure: '套',
    count: '1',
    value: '2.25',
    totalValue: '2.25'
  },{
    device: '废水罐及输送装置',
    measure: '套',
    count: '1',
    value: '4.5',
    totalValue: '12'
  },{
    device: '毛油收集及输送装置',
    measure: '套',
    count: '1',
    value: '0.75',
    totalValue: '21.75'
  },{
    device: '固渣输送装置',
  },{
    device: '厌氧发酵系统',
    measure: '套',
    totalValue: '360'
  },{
    device: '污泥脱水系统',
    totalValue: '90'
  },{
    device: '污水处理系统',
    totalValue: '0'
  },{
    device: '沼气收集及处理系统',
    totalValue: '182'
  },{
    device: '除臭系统',
    totalValue: '235'
  },{
    device: '沼渣处理系统',
  },{
    device: '合计',
    totalValue: '1568.75'
  }];
export const tableDataList: Array<TableData> = [
    {
        name: '张三',
        age: '18',
        address: '东大街',
        date: '2016-10-03'
    },
    {
        name: '李四',
        age: '24',
        address: '春熙路',
        date: '2016-10-01'
    },
    {
        name: '王五',
        age: '30',
        address: '二仙桥',
        date: '2016-10-02'
    },
    {
        name: '黄六',
        age: '26',
        address: '天府一街',
        date: '2016-10-04'
    }
];