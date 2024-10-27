// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
    list = '/hotel/index/thing/list',
    detail = '/hotel/index/thing/detail',
    addWishUser = '/hotel/index/thing/addWishUser',
    addCollectUser = '/hotel/index/thing/addCollectUser',
    getCollectThingList = '/hotel/index/thing/getCollectThingList',
    getWishThingList = '/hotel/index/thing/getWishThingList',
    removeCollectUser = '/hotel/index/thing/removeCollectUser',
    removeWishUser = '/hotel/index/thing/removeWishUser'
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const detailApi = async (params: any) => get<any>({ url: URL.detail, params: params, headers: {} });
const addWishUserApi = async (params: any) => post<any>({ url: URL.addWishUser, params: params, headers: {} });
const addCollectUserApi = async (params: any) => post<any>({ url: URL.addCollectUser, params: params, headers: {} });
const getCollectThingListApi = async (params: any) => get<any>({ url: URL.getCollectThingList, params: params, headers: {} });
const getWishThingListApi = async (params: any) => get<any>({ url: URL.getWishThingList, params: params, headers: {} });

const removeCollectUserApi = async (params: any) => post<any>({ url: URL.removeCollectUser, params: params, headers: {} });
const removeWishUserApi = async (params: any) => post<any>({ url: URL.removeWishUser, params: params, headers: {} });


export { listApi, detailApi, addWishUserApi,addCollectUserApi, getCollectThingListApi,
    getWishThingListApi, removeCollectUserApi, removeWishUserApi };
