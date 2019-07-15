--
-- @lc app=leetcode.cn id=183 lang=mysql
--
-- [183] 从不订购的客户
--
# Write your MySQL query statement below

select name Customers from Customers where id not in(select distinct CustomerId from orders)
