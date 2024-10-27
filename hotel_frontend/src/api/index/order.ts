import {get, post} from '/@/utils/http/axios';

enum URL {
    create='/hotel/index/order/create',
    cancelUserOrder = '/hotel/index/order/cancel_order',
    payUserOrder = 'hotel/index/order/pay_order',
    userOrderList = '/hotel/index/order/list',
}

const createApi = async (data: any) =>
    post<any>({url: URL.create, data: data, headers: {}});

const userOrderListApi = async (params: any) =>
    get<any>({url: URL.userOrderList, params: params, data: {}, headers: {}});

const cancelUserOrderApi = async (params: any) =>
    post<any>({url: URL.cancelUserOrder, params: params, headers: {}});

const payUserOrderApi = async (params: any) =>
    post<any>({url: URL.payUserOrder, params: params, headers: {}});

export {createApi, userOrderListApi, cancelUserOrderApi, payUserOrderApi};
