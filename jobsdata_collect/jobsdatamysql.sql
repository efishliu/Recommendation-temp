USE zhaopin;

CREATE TABLE jobsdata(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
workcity VARCHAR(50) NOT NULL,
job_name VARCHAR(100) NOT NULL,
job_inwhichcompany VARCHAR(100) NOT NULL,
min_salary VARCHAR(20) NOT NULL,
max_salary VARCHAR(20) NOT NULL,
salary VARCHAR(20) NOT NULL,
job_category VARCHAR(20) NOT NULL,
workplace VARCHAR(100) NOT NULL,
zhaopin_numbers VARCHAR(20) NOT NULL,
job_welfare VARCHAR(100) NOT NULL,
education_background VARCHAR(20) NOT NULL,
min_workexperience VARCHAR(20) NOT NULL,
job_form VARCHAR(20) NOT NULL,
job_releasetime VARCHAR(20) NOT NULL,
job_require TEXT NOT NULL,
company_name VARCHAR(100) NOT NULL,
company_form VARCHAR(20) NOT NULL,
company_industry VARCHAR(100) NOT NULL,
company_scale VARCHAR(30) NOT NULL,
company_web TEXT NOT NULL,
company_introduce TEXT NOT NULL,
company_address VARCHAR(100) NOT NULL,
data_addtime VARCHAR(20) NOT NULL,
data_sourceweb TEXT NOT NULL,
PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
;