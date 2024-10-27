import {get, post} from '/@/utils/http/axios';

enum URL {
    loginLogList = '/hotel/admin/loginLog/list',
    opLogList = '/hotel/admin/opLog/list',
    errorLogList = '/hotel/admin/errorLog/list',
}

const listLoginLogApi = async (params: any) =>
    get<any>({url: URL.loginLogList, params: params, data: {}, headers: {}});
const listOpLogListApi = async (params: any) =>
    get<any>({url: URL.opLogList, params: params, data: {}, headers: {}});
const listErrorLogListApi = async (params: any) =>
    get<any>({url: URL.errorLogList, params: params, data: {}, headers: {}});

export {listLoginLogApi, listOpLogListApi, listErrorLogListApi};
