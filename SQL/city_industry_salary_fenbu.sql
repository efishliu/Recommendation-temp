USE zhaopin;

CREATE TABLE industry_edu_counts(
edu VARCHAR(20) NOT NULL,
industry VARCHAR(100) NOT NULL,
onep VARCHAR(20) NOT NULL,
threep VARCHAR(20) NOT NULL,
fivep VARCHAR(20) NOT NULL,
sevenp VARCHAR(20) NOT NULL,
ninep VARCHAR(20) NOT NULL,
PRIMARY KEY(city,industry)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
;