create database reddit DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
use reddit;
create table comments_test(
    body text,
    score_hidden boolean,
    archived boolean,
    name varchar(255),
    author varchar(255),
    author_flair_text varchar(255),
    downs int,
    created_utc int,
    subreddit_id varchar(255),
    link_id varchar(255),
    parent_id varchar(255),
    score int,
    retrieved_on int,
    controversiality int,
    gilded int,
    id varchar(255),
    subreddit varchar(255),
    ups int,
    distinguished varchar(255),
    author_flair_css_class varchar(255),
  PRIMARY KEY (id));
ALTER TABLE reddit.comments_test ADD INDEX (id);

