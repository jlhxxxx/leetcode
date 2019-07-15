--
-- @lc app=leetcode.cn id=182 lang=mysql
--
-- [182] 查找重复的电子邮箱
--
# Write your MySQL query statement below

--select a.email email from person a,person b where a.email=b.email and a.id!=b.id
select distinct email from person group by email having count(email)>1
