# Write your MySQL query statement below
select P.firstName,P.lastName,A.city,A.state from person P LEFT join address A ON P.personId=A.personId;