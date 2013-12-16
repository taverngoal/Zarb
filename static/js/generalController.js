/**
 * Created by tavern on 13-12-4.
 */
var generalModule = angular.module("blog.general", [])
    .directive("postPagination", function ($http, $location) {
        return {
            link: function (scope, ele, attrs) {
                $http.get("/post/count", {}).success(function (content) {
                    // 创建分页
                    $(".pagination").pagination(content.count, {
                        num_edge_entries: 1, //边缘页数
                        num_display_entries: 4, //主体页数
                        url: attrs.url,
                        callback: function (page_index, jq) {
                        },
                        items_per_page: 1 //每页显示1项
                    });
                });
            }
        }
    });