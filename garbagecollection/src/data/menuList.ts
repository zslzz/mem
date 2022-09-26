export declare interface Menu {
    id: string,
    icon?: string,
    path?: string,
    name?: string,
    componentPath?: string,
    title: string,
    children?: Array<Menu>,
}

export const menuList1 = [
    {
        id: "M0001",
        icon: "md-home",
        path: "/home",
        name: "DemoHome",
        componentPath: "home.vue",
        title: "系统首页",
    },
    {
        id: "M0020",
        icon: "md-git-compare",
        path: "/bpmn",
        name: "DemoBpmn",
        componentPath: "bpmn.vue",
        title: "系统介绍",
    },
    {
        id: "M0003",
        icon: "md-bookmark",
        path: "/tabs",
        name: "DemoTabs",
        componentPath: "tabs.vue",
        title: "资料卡片",
    },
    {
        id: "M0022",
        icon: "md-paw",
        path: "/personal",
        name: "personResult",
        componentPath: "personResult.vue",
        title: "个人定制",
    },
    {
        id: "M0021",
        icon: "md-book",
        path: "/devices",
        name: "DeviceList",
        componentPath: "deviceList.vue",
        title: "所有设备",
    },
    {
        id: "M0002",
        icon: "md-grid",
        //path: "/table",
        //name: "DemoTable",
        //componentPath: "table.vue",
        title: "专家推荐",
        children: [
            {
                id: "M0005",
                icon: "md-grid",
                path: "/table",
                name: "报告总览",
                componentPath: "table.vue",
                title: "报告总览",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport1",
                name: "最佳性价比报告",
                componentPath: 'result/deviceReport1.vue',
                title: "最佳性价比报告",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport2",
                name: "最经济报告",
                componentPath: 'result/deviceReport2.vue',
                title: "最经济报告",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport3",
                name: "最稳定报告",
                componentPath: 'result/deviceReport3.vue',
                title: "最稳定报告",
            },
        ],
    },   
    {
        id: "M0010",
        icon: "ios-speedometer",
        path: "/charts",
        name: "DemoEharts",
        componentPath: "charts.vue",
        title: "数据分析",
    },
    {
        id: "M0011",
        icon: "md-bookmark",
        path: "/attachment",
        name: "attachment",
        componentPath: "attachment.vue",
        title: "附录清单",
    },
    {
        id: "M0012",
        icon: "md-warning",
        title: "权限处理",
        children: [
            {
                id: "M0013",
                path: "/permission",
                name: "DemoPermission",
                componentPath: "permission.vue",
                title: "权限测试",
            },
            {
                id: "M0014",
                path: "/404",
                name: "DemoError404",
                componentPath: "error404.vue",
                title: "404页面",
            },
        ],
    },
    {
        id: "M0015",
        icon: "md-body",
        path: "/contactus",
        name: "ContactUs",
        componentPath: "contactUs.vue",
        title: "联系我们",
    },
];

export const menuList2 = [
    {
        id: "M0001",
        icon: "md-home",
        path: "/home",
        name: "DemoHome",
        componentPath: "home.vue",
        title: "系统首页",
    },
    {
        id: "M0012",
        icon: "md-warning",
        title: "权限处理",
        children: [
            {
                id: "M0013",
                path: "/permission",
                name: "DemoPermission",
                componentPath: "permission.vue",
                title: "权限测试",
            },
            {
                id: "M0014",
                path: "/404",
                name: "DemoError404",
                componentPath: "error404.vue",
                title: "404页面",
            },
        ],
    },
    {
        id: "M0015",
        icon: "md-body",
        path: "/contactus",
        name: "ContactUs",
        componentPath: "contactUs.vue",
        title: "联系我们",
    },
];

export const menuList3 = [
    {
        id: "M0001",
        icon: "md-home",
        path: "/home",
        name: "DemoHome",
        componentPath: "home.vue",
        title: "系统首页",
    },
    {
        id: "M0020",
        icon: "md-git-compare",
        path: "/bpmn",
        name: "DemoBpmn",
        componentPath: "bpmn.vue",
        title: "系统介绍",
    },
    {
        id: "M0003",
        icon: "md-bookmark",
        path: "/tabs",
        name: "DemoTabs",
        componentPath: "tabs.vue",
        title: "资料卡片",
    },
    {
        id: "M0021",
        icon: "md-bookmark",
        path: "/devices",
        name: "DeviceList",
        componentPath: "deviceList.vue",
        title: "所有设备",
    },
    {
        id: "M0002",
        icon: "md-grid",
        //path: "/table",
        //name: "DemoTable",
        //componentPath: "table.vue",
        title: "专家推荐",
        children: [
            {
                id: "M0005",
                icon: "md-grid",
                path: "/table",
                name: "报告总览",
                componentPath: "table.vue",
                title: "报告总览",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport1",
                name: "最佳性价比报告",
                componentPath: 'result/deviceReport1.vue',
                title: "最佳性价比报告",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport2",
                name: "最经济报告",
                componentPath: 'result/deviceReport2.vue',
                title: "最经济报告",
            },
            {
                id: "M0005",
                icon: "md-grid",
                path: "/deviceReport3",
                name: "最稳定报告",
                componentPath: 'result/deviceReport3.vue',
                title: "最稳定报告",
            },
        ],
    },   
    {
        id: "M0004",
        icon: "ios-list-box",
        title: "设备信息导入",
        children: [
            {
                id: "M0005",
                path: "/form",
                name: "DemoForm",
                componentPath: "form.vue",
                title: "手动输入",
            },
            {
                id: "M0006",
                path: "/upload",
                name: "DemoUpload",
                componentPath: "upload.vue",
                title: "文件导入",
            },
            // {
            //     id: "M0025",
            //     path: "/print",
            //     name: "DemoPrint",
            //     componentPath: "print.vue",
            //     title: "打印",
            // },
        ],
    },    
    {
        id: "M0010",
        icon: "ios-speedometer",
        path: "/charts",
        name: "DemoEharts",
        componentPath: "charts.vue",
        title: "数据分析",
    },
    {
        id: "M0012",
        icon: "md-warning",
        title: "权限处理",
        children: [
            {
                id: "M0013",
                path: "/permission",
                name: "DemoPermission",
                componentPath: "permission.vue",
                title: "权限测试",
            },
            {
                id: "M0014",
                path: "/404",
                name: "DemoError404",
                componentPath: "error404.vue",
                title: "404页面",
            },
        ],
    },
    {
        id: "M0015",
        icon: "md-body",
        path: "/contactus",
        name: "ContactUs",
        componentPath: "contactUs.vue",
        title: "联系我们",
    },
];