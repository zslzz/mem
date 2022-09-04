
import { createI18n } from 'vue-i18n';
import zh from './lang/zh-CN';
import en from './lang/en-US';
// @ts-ignore
import viewUIzh from 'view-ui-plus/dist/locale/zh-CN';
// @ts-ignore
import viewUIen from 'view-ui-plus/dist/locale/en-US';

const i18n = createI18n({
    allowComposition: true,
    globalInjection: true,
    legacy: false,
    locale: 'zh-CN',
    messages: {
        'zh-CN': { ...zh, ...viewUIzh },
        'en-US': { ...en, ...viewUIen }
    }
});

export {
    i18n
};