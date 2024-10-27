import {get, post} from '/@/utils/http/axios';

enum URL {
    create = '/hotel/index/comment/create',
    listThingComments = '/hotel/index/comment/list',
    listUserComments = '/hotel/index/comment/listMyComments',
    like = '/hotel/index/comment/like'
}

const createApi = async (data: any) => post<any>({
    url: URL.create,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});
const listThingCommentsApi = async (params: any) => get<any>({url: URL.listThingComments, params: params, data: {}, headers: {}});
const listUserCommentsApi = async (params: any) => get<any>({url: URL.listUserComments, params: params, data: {}, headers: {}});
const likeApi = async (params: any) => post<any>({url: URL.like, params: params, headers: {}});

export {createApi, listThingCommentsApi,listUserCommentsApi, likeApi};
