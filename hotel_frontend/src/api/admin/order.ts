import {get, post} from '/@/utils/http/axios';

enum URL {
    list = '/hotel/admin/order/list',
    create = '/hotel/admin/order/create',
    update = '/hotel/admin/order/update',
    delete = '/hotel/admin/order/delete',
    cancel = '/hotel/admin/order/cancel_order',
    ok = '/hotel/admin/order/ok_order',
    cancelUserOrder = '/api/order/cancelUserOrder',
    userOrderList = '/api/order/userOrderList',
}

const listApi = async (params: any) =>
    get<any>({url: URL.list, params: params, data: {}, headers: {}});
    
const userOrderListApi = async (params: any) =>
    get<any>({url: URL.userOrderList, params: params, data: {}, headers: {}});

const createApi = async (data: any) =>
    post<any>({
        url: URL.create,
        params: {},
        data: data,
        headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
    });
const updateApi = async (params: any, data: any) =>
    post<any>({
        url: URL.update,
        params: params,
        data: data,
        headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
    });
const deleteApi = async (params: any) =>
    post<any>({url: URL.delete, params: params, headers: {}});

const cancelApi = async (params: any) =>
    post<any>({url: URL.cancel, params: params, headers: {}});

const okApi = async (params: any) =>
    post<any>({url: URL.ok, params: params, headers: {}});

const cancelUserOrderApi = async (params: any) =>
    post<any>({url: URL.cancelUserOrder, params: params, headers: {}});

export {listApi, userOrderListApi, createApi, updateApi, deleteApi, cancelApi, okApi, cancelUserOrderApi};
