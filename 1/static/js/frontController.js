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
            .when('/', {
                controller: 'postListCTRL',
                templateUrl: '/static/templates/post/front_list.html'
            });
    }]);


var post = angular.module('blog.post', [])
    .factory('postService', function ($resource) {
        return $resource('/post/:id', {'id': '@id'}, {
            getlist: { method: 'get', isArray: false, url: '/post'}
        });
    })
    .controller('postListCTRL', ['$scope', 'postService', function ($scope, postService) {
        postService.getlist(function (content) {
            $scope.posts = content.posts
        });
    }])
    .controller('postViewCTRL', ['$scope', 'postService', '$route', function ($scope, postService, $route) {
        $scope.post = postService.get({id: $route.current.params.id});

    }]);

var comment = angular.module('blog.comment', [])
    .directive('commentList', function (commentService, $route) {
        return {
            replace: true,
            controller: 'commentCTRL',
            templateUrl: '/static/templates/comment/list.html'
        }
    })
    .directive('addComment', function (commentService, $route) {
        return {
            link: function (scope, ele, attrs) {
                ele.bind('click', function () {
                    scope.comment.postid = $route.current.params.id;
                    commentService.addComment(scope.comment, function (content) {
                        if (content.success) {
                            scope.comments = commentService.comments($route.current.params.id);
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