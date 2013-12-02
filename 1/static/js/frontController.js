/**
 * Created by tavern on 13-11-30.
 */

var app = angular.module('blog', ['ngRoute', 'blog.post', 'ngResource', 'ngSanitize', 'ngAnimate', 'blog.comment'])
    .controller('generalCTRL', ['$scope', '$location', function ($scope, $location) {

    }])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/post/:id', {
                controller: 'postViewCTRL',
                templateUrl: '/static/templates/post/front_view.html'
            })
            .when('/posts', {
                controller: 'postHomeListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            })
            .when('/', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            });
    }]);


var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post/:size/:page'}
        });
    })
    .controller('postHomeListCTRL', ['$scope', 'postService', function ($scope, postService) {
        postService.getlist({ size: 10, page: 0}, function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postListCTRL', ['$scope', 'postService', function ($scope, postService) {
        postService.getlist({ size: 0, page: 0}, function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postViewCTRL', ['$scope', 'postService', '$route', function ($scope, postService, $route) {
        $scope.post = postService.get({id: $route.current.params.id, size: 0, page: 0});

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
        }
    })
    .service('commentService', function ($resource) {
        var source = $resource('/comment/:postid', {});
        return {
            comments: function (postid) {
                return  source.get({postid: postid})
            },
            addComment: function (comment, func) {
                source.save(comment, func);
            }
        }
    })
    .controller('commentCTRL', ['$scope', 'commentService', '$route', function ($scope, commentService, $route) {
        $scope.comments = commentService.comments($route.current.params.id);
    }]);