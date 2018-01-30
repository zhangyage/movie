/*
Navicat MySQL Data Transfer

Source Server         : mytest
Source Server Version : 50634
Source Host           : 47.94.188.237:3306
Source Database       : movie

Target Server Type    : MYSQL
Target Server Version : 50634
File Encoding         : 65001

Date: 2018-01-29 16:42:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `is_super` smallint(6) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `role_id` (`role_id`),
  KEY `ix_admin_addtime` (`addtime`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'zhangyage', 'pbkdf2:sha256:50000$d4LpM5zg$5664c005e7f72e2ed6820c9956689a339e1922f47def42ea7922a865b8874508', '0', '2', '2017-10-25 10:38:31');
INSERT INTO `admin` VALUES ('2', 'mingtian', 'pbkdf2:sha256:50000$hToneIBI$c6fa3013169a13477aa4d809328d363ec35cb9c62c45880d8ab5e7990486215b', null, '2', '2017-11-01 09:09:48');
INSERT INTO `admin` VALUES ('3', 'xiaoming', 'pbkdf2:sha256:50000$2hLGxTpO$52dd366f63efe6ed02ca9f7886b8bd2d518c2bbb47386f8f96bdfa2894529acc', '1', '2', '2017-11-01 09:13:24');
INSERT INTO `admin` VALUES ('5', 'panyuanqing', 'pbkdf2:sha256:50000$jT1eQ8zc$00ec9917edc4dfb0785426254a4fbfb444fa9eed2a9fbf33518f393b49d5c030', '1', '2', '2017-11-01 15:58:01');

-- ----------------------------
-- Table structure for adminlog
-- ----------------------------
DROP TABLE IF EXISTS `adminlog`;
CREATE TABLE `adminlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_adminlog_addtime` (`addtime`),
  CONSTRAINT `adminlog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of adminlog
-- ----------------------------
INSERT INTO `adminlog` VALUES ('1', '1', '127.0.0.1', '2017-11-01 10:39:13');
INSERT INTO `adminlog` VALUES ('2', '1', '127.0.0.1', '2017-11-01 11:08:43');
INSERT INTO `adminlog` VALUES ('3', '5', '127.0.0.1', '2017-11-01 16:00:45');
INSERT INTO `adminlog` VALUES ('4', '1', '127.0.0.1', '2017-11-01 16:00:50');
INSERT INTO `adminlog` VALUES ('5', '1', '127.0.0.1', '2017-11-01 20:52:40');
INSERT INTO `adminlog` VALUES ('6', '1', '127.0.0.1', '2017-11-02 10:56:02');
INSERT INTO `adminlog` VALUES ('7', '1', '127.0.0.1', '2017-11-02 16:36:44');
INSERT INTO `adminlog` VALUES ('8', '1', '127.0.0.1', '2017-11-03 11:17:52');
INSERT INTO `adminlog` VALUES ('9', '1', '127.0.0.1', '2017-11-03 11:34:00');
INSERT INTO `adminlog` VALUES ('10', '1', '20.20.20.217', '2017-11-03 15:13:42');

-- ----------------------------
-- Table structure for auth
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `ix_auth_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth
-- ----------------------------
INSERT INTO `auth` VALUES ('3', '修改密码', '/admin/pwd/', '2017-10-31 11:32:04');
INSERT INTO `auth` VALUES ('4', '添加标签', '/admin/tag/add/', '2017-10-31 11:32:35');
INSERT INTO `auth` VALUES ('5', '标签列表', '/admin/tag/list/<int:page>/', '2017-10-31 11:32:52');
INSERT INTO `auth` VALUES ('6', '删除标签', '/admin/tag/del/<int:id>/', '2017-10-31 11:33:08');
INSERT INTO `auth` VALUES ('7', '修改标签', '/admin/tag/update/<int:id>/', '2017-10-31 11:33:44');
INSERT INTO `auth` VALUES ('8', '添加电影', '/admin/movie/add/', '2017-10-31 11:34:00');
INSERT INTO `auth` VALUES ('9', '电影列表', '/admin/movie/list/<int:page>', '2017-10-31 11:34:16');
INSERT INTO `auth` VALUES ('10', '删除电影', '/admin/movie/del/<int:id>/', '2017-10-31 11:34:42');
INSERT INTO `auth` VALUES ('11', '修改电影', '/admin/movie/update/<int:id>/', '2017-10-31 11:35:02');
INSERT INTO `auth` VALUES ('12', '预告添加', '/admin/preview/add/', '2017-10-31 11:35:20');
INSERT INTO `auth` VALUES ('13', '预告列表', '/admin/preview/list/<int:page>/', '2017-10-31 11:35:36');
INSERT INTO `auth` VALUES ('14', '删除预告', '/admin/preview/del/<int:id>/', '2017-10-31 11:35:52');
INSERT INTO `auth` VALUES ('15', '修改预告', '/admin/preview/update/<int:id>/', '2017-10-31 11:36:13');
INSERT INTO `auth` VALUES ('16', '会员列表', '/admin/user/list/<int:page>/', '2017-11-01 14:18:51');
INSERT INTO `auth` VALUES ('17', '会员查看', '/admin/user/view/<int:id>/', '2017-11-01 14:19:14');
INSERT INTO `auth` VALUES ('18', '删除会员', '/admin/user/del/<int:id>/', '2017-11-01 14:19:35');
INSERT INTO `auth` VALUES ('19', '评论列表', '/admin/comment/list/<int:page>/', '2017-11-01 14:19:57');
INSERT INTO `auth` VALUES ('20', '删除评论', '/admin/comment/del/<int:id>/', '2017-11-01 14:20:18');
INSERT INTO `auth` VALUES ('21', '电影收藏列表', '/admin/moviecol/list/<int:page>/', '2017-11-01 14:20:37');
INSERT INTO `auth` VALUES ('22', '删除电影收藏', '/admin/moviecol/del/<int:id>/', '2017-11-01 14:20:51');
INSERT INTO `auth` VALUES ('23', '管理员登录日志', '/admin/adminloginlog/list/<int:page>/', '2017-11-01 14:21:38');
INSERT INTO `auth` VALUES ('24', '用户登录日志', '/admin/userloginlog/list/<int:page>/', '2017-11-01 14:22:21');
INSERT INTO `auth` VALUES ('25', '权限添加', '/admin/auth/add/', '2017-11-01 14:22:38');
INSERT INTO `auth` VALUES ('26', '权限列表', '/admin/auth/list/<int:page>/', '2017-11-01 14:22:54');
INSERT INTO `auth` VALUES ('27', '删除权限', '/admin/auth/del/<int:id>/', '2017-11-01 14:23:10');
INSERT INTO `auth` VALUES ('28', '修改权限', '/admin/auth/update/<int:id>/', '2017-11-01 14:23:23');
INSERT INTO `auth` VALUES ('29', '角色添加', '/admin/role/add/', '2017-11-01 14:23:37');
INSERT INTO `auth` VALUES ('30', '角色列表', '/admin/role/list/<int:page>/', '2017-11-01 14:23:59');
INSERT INTO `auth` VALUES ('31', '删除角色', '/admin/role/del/<int:id>/', '2017-11-01 14:24:11');
INSERT INTO `auth` VALUES ('32', '修改角色', '/admin/role/update/<int:id>/', '2017-11-01 14:24:23');
INSERT INTO `auth` VALUES ('33', '添加管理员', '/admin/admin/add/', '2017-11-01 14:24:36');
INSERT INTO `auth` VALUES ('34', '管理员列表', '/admin/admin/list/<int:page>/', '2017-11-01 14:24:48');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_comment_addtime` (`addtime`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', '无聊', '27', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('2', '有意思', '27', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('3', '好的', '29', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('4', '你可以', '30', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('5', '精彩极了！', '32', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('6', '完美', '28', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('7', '这是什么东西啊', '31', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('8', '垃圾', '30', '21', '2017-10-30 15:43:30');
INSERT INTO `comment` VALUES ('9', '有没有其他的', '17', '21', '2017-10-30 15:43:31');
INSERT INTO `comment` VALUES ('13', '<p>这是一条测试评论！</p>', '27', '21', '2017-11-06 11:07:35');
INSERT INTO `comment` VALUES ('14', '<p>这是一条测试评论！</p>', '27', '21', '2017-11-06 11:08:26');
INSERT INTO `comment` VALUES ('15', '<p>期待di6bu</p>', '16', '21', '2017-11-06 11:11:33');
INSERT INTO `comment` VALUES ('16', '<p>世界之外</p>', '29', '21', '2017-11-06 14:01:21');
INSERT INTO `comment` VALUES ('17', '<p>dsdasda</p>', '16', '21', '2017-11-06 14:15:06');
INSERT INTO `comment` VALUES ('18', '<p>dsdasda</p>', '16', '21', '2017-11-06 14:15:06');

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `info` text,
  `logo` varchar(255) DEFAULT NULL,
  `star` smallint(6) DEFAULT NULL,
  `playnum` bigint(20) DEFAULT NULL,
  `commentnum` bigint(20) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `release_time` date DEFAULT NULL,
  `length` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `logo` (`logo`),
  KEY `tag_id` (`tag_id`),
  KEY `ix_movie_addtime` (`addtime`),
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of movie
-- ----------------------------
INSERT INTO `movie` VALUES ('16', '变形金刚5', '2017110311212600d1290ea7c2400abfd4dd67a063cfb4.mp4', '变形金刚5--最后的骑士', '20171103112126adbbbf8e7209423283ff015b5e568e29.png', '3', '16', '3', '13', '美国', '2016-10-01', '3分钟', '2017-11-03 11:21:26');
INSERT INTO `movie` VALUES ('17', '密战', '2017110311371051c487823e4143a09805bbbb298019cd.mp4', '密战—-谍战电影', '2017110311371010204aa54ac841418c858486ccb958f7.jpg', '2', '3', '0', '18', '中国', '2017-11-18', '3分钟', '2017-11-03 11:37:11');
INSERT INTO `movie` VALUES ('26', '火力全开', '20171103140408db374958d6884b93a7d9d946e9d00d3f.mp4', '火力全开', '2017110314040859700b55b44b427095f60e270f00fcca.jpg', '2', '1', '0', '29', '中国', '2017-11-01', '3分钟', '2017-11-03 14:04:08');
INSERT INTO `movie` VALUES ('27', '降魔转', '20171103140615684b177368ae42ee8ede2dd019a26445.mp4', '降魔转', '2017110314061504162bbd820c4241b3bf7a8bb3d46a9b.jpg', '5', '10', '2', '27', '中国', '2017-11-02', '5分钟', '2017-11-03 14:06:15');
INSERT INTO `movie` VALUES ('28', '情遇曼哈顿', '20171103140702a63c4c1239644a818d5543a5706cdc8f.mp4', '情遇曼哈顿', '20171103140702029e718e502b4fb598a20729becafcbc.jpg', '2', '3', '0', '15', '中国', '2017-11-04', '4分钟', '2017-11-03 14:07:03');
INSERT INTO `movie` VALUES ('29', '识色，幸也', '201711031407489f0538e7a5ea4ac6a63abd83098b156f.mp4', '识色，幸也', '201711031407484a30a35709fd4316a022ac8fadbeb417.jpg', '2', '10', '1', '14', '中国', '2017-11-07', '4分钟', '2017-11-03 14:07:49');
INSERT INTO `movie` VALUES ('30', '兄弟，别闹', '201711031408307a895d67fd4c4c53a9247a3f221205c1.mp4', '兄弟，别闹', '20171103140830fac9e12b405049fea07b2e64fb003b17.jpg', '4', '1', '0', '16', '中国', '2017-11-08', '3分钟', '2017-11-03 14:08:30');
INSERT INTO `movie` VALUES ('31', '怨灵', '2017110314090620b4df8a6e2346b5967a35ca4f94cf04.mp4', '怨灵', '2017110314090602ba0aed53d14e4f85c1e6e0980d3056.jpg', '4', '1', '0', '21', '中国', '2017-11-17', '15分钟', '2017-11-03 14:09:07');
INSERT INTO `movie` VALUES ('32', '正义联盟', '201711031409485fd480741d2e4d688c0b8f7f4ce81966.mp4', '正义联盟', '201711031409480de24f164c0e4a3183b43f0469de939c.jpg', '5', '2', '0', '13', '美国', '2017-07-06', '13分钟', '2017-11-03 14:09:49');

-- ----------------------------
-- Table structure for moviecol
-- ----------------------------
DROP TABLE IF EXISTS `moviecol`;
CREATE TABLE `moviecol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_moviecol_addtime` (`addtime`),
  CONSTRAINT `moviecol_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `moviecol_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of moviecol
-- ----------------------------
INSERT INTO `moviecol` VALUES ('1', null, '21', '2017-10-30 16:33:41');
INSERT INTO `moviecol` VALUES ('2', null, '21', '2017-10-30 16:33:41');
INSERT INTO `moviecol` VALUES ('4', null, null, '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('5', null, '4', '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('6', null, '12', '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('7', null, '5', '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('8', null, null, '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('9', null, '21', '2017-10-30 16:34:18');
INSERT INTO `moviecol` VALUES ('11', null, '5', '2017-10-30 16:35:09');
INSERT INTO `moviecol` VALUES ('14', null, '10', '2017-10-30 16:35:09');
INSERT INTO `moviecol` VALUES ('15', null, '21', '2017-10-30 16:35:09');
INSERT INTO `moviecol` VALUES ('16', '29', '21', '2017-11-06 11:53:00');
INSERT INTO `moviecol` VALUES ('17', '26', '21', '2017-11-06 11:55:12');

-- ----------------------------
-- Table structure for oplog
-- ----------------------------
DROP TABLE IF EXISTS `oplog`;
CREATE TABLE `oplog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `reason` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_oplog_addtime` (`addtime`),
  CONSTRAINT `oplog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oplog
-- ----------------------------
INSERT INTO `oplog` VALUES ('1', '1', '127.0.0.1', 'xxxx', '2017-11-01 11:44:05');
INSERT INTO `oplog` VALUES ('2', '1', '127.0.0.1', 'xxxx', '2017-11-01 11:44:09');
INSERT INTO `oplog` VALUES ('3', '1', '127.0.0.1', '/admin/tag/add/', '2017-11-01 11:46:10');
INSERT INTO `oplog` VALUES ('4', '1', '127.0.0.1', '/admin/tag/add/', '2017-11-01 11:46:45');
INSERT INTO `oplog` VALUES ('5', '1', '127.0.0.1', '/admin/logout/', '2017-11-01 15:58:15');
INSERT INTO `oplog` VALUES ('6', '5', '127.0.0.1', '/admin/logout/', '2017-11-01 16:00:49');
INSERT INTO `oplog` VALUES ('7', '1', '127.0.0.1', '/admin/user/view/<int:id>/', '2017-11-01 20:52:58');
INSERT INTO `oplog` VALUES ('8', '1', '127.0.0.1', '/admin/preview/del/<int:id>/', '2017-11-02 16:36:52');
INSERT INTO `oplog` VALUES ('9', '1', '127.0.0.1', '/admin/preview/del/<int:id>/', '2017-11-02 16:36:53');
INSERT INTO `oplog` VALUES ('10', '1', '127.0.0.1', '/admin/preview/del/<int:id>/', '2017-11-02 16:36:55');
INSERT INTO `oplog` VALUES ('11', '1', '127.0.0.1', '/admin/preview/del/<int:id>/', '2017-11-02 16:36:56');
INSERT INTO `oplog` VALUES ('12', '1', '127.0.0.1', '/admin/preview/del/<int:id>/', '2017-11-02 16:36:57');
INSERT INTO `oplog` VALUES ('13', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:37:21');
INSERT INTO `oplog` VALUES ('14', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:05');
INSERT INTO `oplog` VALUES ('15', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:06');
INSERT INTO `oplog` VALUES ('16', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:27');
INSERT INTO `oplog` VALUES ('17', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:27');
INSERT INTO `oplog` VALUES ('18', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:49');
INSERT INTO `oplog` VALUES ('19', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:41:49');
INSERT INTO `oplog` VALUES ('20', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:42:05');
INSERT INTO `oplog` VALUES ('21', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:42:20');
INSERT INTO `oplog` VALUES ('22', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:42:20');
INSERT INTO `oplog` VALUES ('23', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:42:29');
INSERT INTO `oplog` VALUES ('24', '1', '127.0.0.1', '/admin/preview/add/', '2017-11-02 16:42:29');
INSERT INTO `oplog` VALUES ('25', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-02 17:12:06');
INSERT INTO `oplog` VALUES ('26', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-02 17:13:13');
INSERT INTO `oplog` VALUES ('27', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-02 17:14:19');
INSERT INTO `oplog` VALUES ('28', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-02 17:14:21');
INSERT INTO `oplog` VALUES ('29', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-02 17:14:22');
INSERT INTO `oplog` VALUES ('30', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:17:56');
INSERT INTO `oplog` VALUES ('31', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:20:01');
INSERT INTO `oplog` VALUES ('32', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:21:03');
INSERT INTO `oplog` VALUES ('33', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:21:25');
INSERT INTO `oplog` VALUES ('34', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:21:26');
INSERT INTO `oplog` VALUES ('35', '1', '127.0.0.1', '/admin/movie/update/<int:id>/', '2017-11-03 11:23:20');
INSERT INTO `oplog` VALUES ('36', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:34:04');
INSERT INTO `oplog` VALUES ('37', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:37:10');
INSERT INTO `oplog` VALUES ('38', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 11:37:11');
INSERT INTO `oplog` VALUES ('39', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:11:01');
INSERT INTO `oplog` VALUES ('40', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:14:58');
INSERT INTO `oplog` VALUES ('41', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:14:59');
INSERT INTO `oplog` VALUES ('42', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:15:39');
INSERT INTO `oplog` VALUES ('43', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:15:40');
INSERT INTO `oplog` VALUES ('44', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:16:20');
INSERT INTO `oplog` VALUES ('45', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:16:21');
INSERT INTO `oplog` VALUES ('46', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:16:57');
INSERT INTO `oplog` VALUES ('47', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:16:57');
INSERT INTO `oplog` VALUES ('48', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:17:35');
INSERT INTO `oplog` VALUES ('49', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:17:36');
INSERT INTO `oplog` VALUES ('50', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:18:11');
INSERT INTO `oplog` VALUES ('51', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:18:12');
INSERT INTO `oplog` VALUES ('52', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:18:42');
INSERT INTO `oplog` VALUES ('53', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 12:18:43');
INSERT INTO `oplog` VALUES ('54', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:00:11');
INSERT INTO `oplog` VALUES ('55', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:00:11');
INSERT INTO `oplog` VALUES ('56', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:16');
INSERT INTO `oplog` VALUES ('57', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:19');
INSERT INTO `oplog` VALUES ('58', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:20');
INSERT INTO `oplog` VALUES ('59', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:20');
INSERT INTO `oplog` VALUES ('60', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:21');
INSERT INTO `oplog` VALUES ('61', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:22');
INSERT INTO `oplog` VALUES ('62', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:00:22');
INSERT INTO `oplog` VALUES ('63', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:00:27');
INSERT INTO `oplog` VALUES ('64', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:01:34');
INSERT INTO `oplog` VALUES ('65', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:01:34');
INSERT INTO `oplog` VALUES ('66', '1', '127.0.0.1', '/admin/movie/del/<int:id>/', '2017-11-03 14:02:33');
INSERT INTO `oplog` VALUES ('67', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:03:44');
INSERT INTO `oplog` VALUES ('68', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:04:08');
INSERT INTO `oplog` VALUES ('69', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:04:09');
INSERT INTO `oplog` VALUES ('70', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:06:15');
INSERT INTO `oplog` VALUES ('71', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:06:15');
INSERT INTO `oplog` VALUES ('72', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:07:02');
INSERT INTO `oplog` VALUES ('73', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:07:03');
INSERT INTO `oplog` VALUES ('74', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:07:49');
INSERT INTO `oplog` VALUES ('75', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:07:49');
INSERT INTO `oplog` VALUES ('76', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:08:30');
INSERT INTO `oplog` VALUES ('77', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:08:30');
INSERT INTO `oplog` VALUES ('78', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:09:07');
INSERT INTO `oplog` VALUES ('79', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:09:07');
INSERT INTO `oplog` VALUES ('80', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:09:48');
INSERT INTO `oplog` VALUES ('81', '1', '127.0.0.1', '/admin/movie/add/', '2017-11-03 14:09:49');

-- ----------------------------
-- Table structure for preview
-- ----------------------------
DROP TABLE IF EXISTS `preview`;
CREATE TABLE `preview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `logo` (`logo`),
  KEY `ix_preview_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of preview
-- ----------------------------
INSERT INTO `preview` VALUES ('8', '变形金刚', '201711021641050b0db350dacb471eaa8ed80bff4c5caf.png', '2017-11-02 16:41:06');
INSERT INTO `preview` VALUES ('9', '死神来了', '201711021641266504483ba9984f9c993ab8ffbe943e31.png', '2017-11-02 16:41:27');
INSERT INTO `preview` VALUES ('10', '黑客帝国', '20171102164149d4b105d9a94f4cd7ba9ba80eb41c0626.png', '2017-11-02 16:41:49');
INSERT INTO `preview` VALUES ('11', '疯狂麦克斯', '201711021642192f70bc4499184c108dd11fabb211bace.png', '2017-11-02 16:42:20');
INSERT INTO `preview` VALUES ('12', '范海辛', '20171102164229c3fdbc1a6d8447f4bb93c3f8c2ad8bac.png', '2017-11-02 16:42:29');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `auths` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_role_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('2', '管理员', '3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34', '2017-10-31 14:31:37');
INSERT INTO `role` VALUES ('3', '超级管理员', '3', '2017-10-31 15:23:56');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_tag_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('13', '科幻', '2017-10-27 17:25:22');
INSERT INTO `tag` VALUES ('14', '动作', '2017-10-27 17:25:28');
INSERT INTO `tag` VALUES ('15', '爱情', '2017-10-27 17:25:34');
INSERT INTO `tag` VALUES ('16', '剧情', '2017-10-27 17:25:44');
INSERT INTO `tag` VALUES ('18', '战争', '2017-10-27 17:26:45');
INSERT INTO `tag` VALUES ('21', '惊悚', '2017-10-27 17:27:15');
INSERT INTO `tag` VALUES ('27', '历史', '2017-10-30 21:02:00');
INSERT INTO `tag` VALUES ('29', '记录片', '2017-11-01 11:46:45');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `info` text,
  `face` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `face` (`face`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2', '鼠', '1235', '1235@qq.com', '12355678945', '鼠', '1.png', '2017-10-30 14:53:41', 'adhagdasd5645d4f5wef4fvdsdf465f4s65f4s');
INSERT INTO `user` VALUES ('4', '虎', '1231', '1231@qq.com', '12344678945', '虎', '3.png', '2017-10-30 14:53:41', '1231gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('5', '兔', '1232', '1232@qq.com', '12325678945', '兔', '4.png', '2017-10-30 14:53:41', '1232gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('6', '龙', '1233', '1233@qq.com', '12335678945', '龙', '5.png', '2017-10-30 14:53:41', '1233gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('10', '蛇', '1244', '1244@qq.com', '12355648945', '蛇', '6.png', '2017-10-30 14:55:06', '1234gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('12', '马', '1236', '1236@qq.com', '12349678945', '马', '7.png', '2017-10-30 14:55:23', '1236gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('13', '羊', '1237', '1237@qq.com', '12375678945', '羊', '8.png', '2017-10-30 14:55:23', '1237gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('15', '鸡', '1239', '1239@qq.com', '12395678945', '鸡', '10.png', '2017-10-30 14:55:23', '1239gdasd5645d4f5wef4fvds5f465f4s65f4s');
INSERT INTO `user` VALUES ('21', 'zhangyage', 'pbkdf2:sha256:50000$idobdeQQ$c3f39bd5983117435a8ef5b01913dc98e309ac157da9a56d1ab07247ba535fe9', 'zhangyage2015@163.com', '15510367325', 'sdsdsds', '201711021031391c9463d93aff4ca2a44f76a0166c8947.png', '2017-11-01 14:48:30', '814c7012f2944e888ab26e91d3c2f54b');
INSERT INTO `user` VALUES ('22', 'zhangyage2', 'pbkdf2:sha256:50000$YSvnGabz$dc7c2f0f46f807a971e2d28f6e81c2b38f7862aff11128f33cae8dd56211b858', 'zhangyage3015@163.com', '15510369325', null, '5c16cc1700c747388b3e55674cf28cb5.png', '2017-11-01 15:03:50', '3b774acdcc5344db84ccc0c2f588d937');

-- ----------------------------
-- Table structure for userlog
-- ----------------------------
DROP TABLE IF EXISTS `userlog`;
CREATE TABLE `userlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `ip_addr` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_userlog_addtime` (`addtime`),
  CONSTRAINT `userlog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userlog
-- ----------------------------
INSERT INTO `userlog` VALUES ('12', '21', '127.0.0.1', '内网IP==内网IP', '2017-11-02 13:44:28');
INSERT INTO `userlog` VALUES ('13', '21', '127.0.0.1', '内网IP==内网IP', '2017-11-02 17:28:01');
INSERT INTO `userlog` VALUES ('14', '21', '127.0.0.1', '内网IP==内网IP', '2017-11-03 12:43:05');
INSERT INTO `userlog` VALUES ('15', '21', '20.20.20.217', '==', '2017-11-03 15:11:36');
INSERT INTO `userlog` VALUES ('16', '21', '192.168.10.251', '内网IP==内网IP', '2017-11-03 15:13:12');
INSERT INTO `userlog` VALUES ('17', '21', '218.244.52.150', '北京市==联通', '2017-11-03 16:00:56');
INSERT INTO `userlog` VALUES ('18', '21', '124.65.164.54', '北京市==联通', '2017-11-03 16:02:49');
INSERT INTO `userlog` VALUES ('19', '21', '218.244.52.150', '北京市==联通', '2017-11-03 16:04:03');
INSERT INTO `userlog` VALUES ('20', '21', '127.0.0.1', '内网IP==内网IP', '2017-11-06 11:07:13');
INSERT INTO `userlog` VALUES ('21', '21', '127.0.0.1', '内网IP==内网IP', '2017-11-06 14:30:16');
