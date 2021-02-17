-- Schema design made on dbdiagram.io --

CREATE TABLE "user" (
  "id" int PRIMARY KEY NOT NULL,
  "username" text,
  "password" text,
  "display_name" text
);

CREATE TABLE "post" (
  "id" int PRIMARY KEY NOT NULL,
  "location" location,
  "pictures" text,
  "desc" text
);

CREATE TABLE "user_post" (
  "id" int PRIMARY KEY NOT NULL,
  "user_id" int,
  "post" int
);

CREATE TABLE "tag" (
  "id" int PRIMARY KEY NOT NULL,
  "tag_name" text
);

CREATE TABLE "Post_tag" (
  "id" int PRIMARY KEY NOT NULL,
  "tag_id" int,
  "post_id" int
);

ALTER TABLE "user_post" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "user_post" ADD FOREIGN KEY ("post") REFERENCES "post" ("id");

ALTER TABLE "Post_tag" ADD FOREIGN KEY ("tag_id") REFERENCES "tag" ("id");

ALTER TABLE "Post_tag" ADD FOREIGN KEY ("post_id") REFERENCES "post" ("id");
