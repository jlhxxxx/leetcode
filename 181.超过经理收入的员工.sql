--
-- @lc app=leetcode.cn id=181 lang=mysql
--
-- [181] 超过经理收入的员工
--
# Write your MySQL query statement below

select a.name Employee from Employee a,Employee b where a.ManagerId=b.id and a.salary > b.salary

