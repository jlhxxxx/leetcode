--
-- @lc app=leetcode.cn id=176 lang=mysql
--
-- [176] 第二高的薪水
--
# Write your MySQL query statement below
select (select distinct Salary from Employee order by salary desc limit 1,1) SecondHighestSalary;

