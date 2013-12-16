/**
 * Created by tavern on 13-11-30.
 */

var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource', 'ngSanitize', 'ngAnimate', 'blog.comment', 'blog.general'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {

    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/:id', {
                controller: 'postViewCTRL',
                templateUrl: '/static/templates/post/front_view.html'
            })
            .when('/posts', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            })
            .when('/posts/:size/:page', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            })
            .when('/tag/:tag/postlist', {
                controller: 'tagPostListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            })
            .when('/tag/:tag/postlist/:size/:page', {
                controller: 'tagPostListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            })
            .when('/', {
                controller: 'postHomeListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            });
    }]);


var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post/:size/:page'},
            getlistByTag: { method: 'get', isArray: false, url: '/tag/:tag/postlist/:size/:page' }
        });
    })
    .controller('postHomeListCTRL', ['$scope', 'postService', '$rootScope', function ($scope, postService, $rootScope) {
        $scope.posts = postService.getlist({ size: 10, page: 0});
        $rootScope.module = 'home'
    }])
    .controller('postListCTRL', ['$scope', 'postService', '$http', '$rootScope', function ($scope, postService, $http, $rootScope) {
        var size = 10;
        $rootScope.module = 'postlist';
        $scope.showPagination = true;
        $http.get("/post/count", {}).success(function (content) {
            $(".pagination").pagination(content.count, {
                num_edge_entries: 1, //边缘页数
                num_display_entries: 4, //主体页数
                callback: function (page_index, jq) {
                    $scope.posts = postService.getlist({ size: size, page: page_index});
                },
                items_per_page: size //每页显示1项
            });
        });
    }])
    .controller('postViewCTRL', ['$scope', 'postService', '$route', function ($scope, postService, $route) {
        $scope.post = postService.get({id: $route.current.params.id, size: 0, page: 0});

    }])
    .controller('tagPostListCTRL', ['$scope', 'postService', '$route', '$http', '$rootScope', function ($scope, postService, $route, $http, $rootScope) {
        var size = 10;
        var tag = $route.current.params.tag;
        $http.get("/tag/" + tag + "/name").success(function (content) {
            $rootScope.tag_name = content;
        });
        $rootScope.module = 'tag';
        $scope.showPagination = true;
        $http.get("/tag/" + tag + "/postlist/count", {}).success(function (content) {
            $(".pagination").pagination(content.count, {
                num_edge_entries: 1, //边缘页数
                num_display_entries: 4, //主体页数
                callback: function (page_index, jq) {
                    $scope.posts = postService.getlistByTag({tag: tag, size: size, page: page_index});
                },
                items_per_page: size //每页显示1项
            });
        });

    }]);

var comment = angular.module('blog.comment', [])
    .directive('commentList', function () {
        return {
            replace: true,
            controller: 'commentCTRL',
            templateUrl: '/static/templates/comment/list.html'
        }
    })
    .directive('addComment', function (commentService, $route) {
        return {
            link: function (scope, ele) {
                ele.bind('click', function () {
                    scope.comment.postid = $route.current.params.id;
                    commentService.addComment(scope.comment, function (content) {
                        if (content.success) {
                            scope.comments = commentService.comments($route.current.params.id);
                            $('form')[0].reset();
                            $(ele).popover('show');
                            setTimeout(function () {
                                $(ele).popover('hide');
                            }, 3000)
                        }
                    });
                });
            }
        };
    })
    .service('commentService', function ($resource) {
        var source = $resource('/comment/:postid/:size/:page', {});
        return {
            comments: function (postid, size, page) {
                return  source.get({postid: postid, size: size, page: page})
            },
            addComment: function (comment, func) {
                source.save(comment, func);
            }
        }
    })
    .controller('commentCTRL', ['$scope', 'commentService', '$route', '$http', function ($scope, commentService, $route, $http) {
        var postid = $route.current.params.id;
        var size = 5;
        $http.get("/comment/count/" + postid).success(function (content) {
            $(".pagination").pagination(content.count, {
                num_edge_entries: 1, //边缘页数
                num_display_entries: 4, //主体页数
                callback: function (page_index, jq) {
                    $scope.comments = commentService.comments(postid, size, page_index);
                },
                items_per_page: size //每页显示1项
            });
        });

    }]);