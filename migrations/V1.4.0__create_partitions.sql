CREATE TABLE IF NOT EXISTS "tmp_user"
 (
  "UserID" BIGINT PRIMARY KEY,
  "Username" varchar(30),
  "E_mail" varchar(100),
  "Password" varchar(100),
  "Status" varchar(255),
  "AvatarImage" varchar(255)
) PARTITION BY RANGE ("UserID");

CREATE TABLE IF NOT EXISTS "user_1" PARTITION OF "tmp_user"
FOR VALUES FROM (1) TO (200000);

CREATE TABLE IF NOT EXISTS "user_2" PARTITION OF "tmp_user"
FOR VALUES FROM (200000) TO (400000);

CREATE TABLE IF NOT EXISTS "user_3" PARTITION OF "tmp_user"
FOR VALUES FROM (400000) TO (600000);

CREATE TABLE IF NOT EXISTS "user_4" PARTITION OF "tmp_user"
FOR VALUES FROM (600000) TO (800000);

CREATE TABLE IF NOT EXISTS "user_5" PARTITION OF "tmp_user"
FOR VALUES FROM (800000) TO (10000000);

CREATE INDEX IF NOT EXISTS "user_userID_1" ON "user_1"("UserID");
CREATE INDEX IF NOT EXISTS "user_userID_2" ON "user_2"("UserID");
CREATE INDEX IF NOT EXISTS "user_userID_3" ON "user_3"("UserID");
CREATE INDEX IF NOT EXISTS "user_userID_4" ON "user_4"("UserID");
CREATE INDEX IF NOT EXISTS "user_userID_5" ON "user_5"("UserID");


INSERT INTO "tmp_user" OVERRIDING SYSTEM VALUE SELECT * FROM "User";
ALTER TABLE "tmp_user" ALTER COLUMN "UserID" ADD generated always as IDENTITY;

ALTER TABLE "User" RENAME TO "old_User";
ALTER TABLE "tmp_user" RENAME TO "User";



CREATE TABLE IF NOT EXISTS "tmp_dialog" (
  "DialogID" BIGINT PRIMARY KEY,
  "DialogName" varchar(100),
  "Logo" varchar(255)
) PARTITION BY RANGE ("DialogID") ;

CREATE TABLE IF NOT EXISTS "dialog_1" PARTITION OF "tmp_dialog"
FOR VALUES FROM (1) TO (200000) ;

CREATE TABLE IF NOT EXISTS "dialog_2" PARTITION OF "tmp_dialog"
FOR VALUES FROM (200000) TO (400000);

CREATE TABLE IF NOT EXISTS "dialog_3" PARTITION OF "tmp_dialog"
FOR VALUES FROM (400000) TO (600000);

CREATE TABLE IF NOT EXISTS "dialog_4" PARTITION OF "tmp_dialog"
FOR VALUES FROM (600000) TO (800000);

CREATE TABLE IF NOT EXISTS "dialog_5" PARTITION OF "tmp_dialog"
FOR VALUES FROM (800000) TO (10000000);

CREATE INDEX IF NOT EXISTS "dialog_dialogID_1" ON "dialog_1"("DialogID");
CREATE INDEX IF NOT EXISTS "dialog_dialogID_2" ON "dialog_2"("DialogID");
CREATE INDEX IF NOT EXISTS "dialog_dialogID_3" ON "dialog_3"("DialogID");
CREATE INDEX IF NOT EXISTS "dialog_dialogID_4" ON "dialog_4"("DialogID");
CREATE INDEX IF NOT EXISTS "dialog_dialogID_5" ON "dialog_5"("DialogID");

INSERT INTO "tmp_dialog" OVERRIDING SYSTEM VALUE SELECT * FROM "Dialog";
ALTER TABLE "tmp_dialog" ALTER COLUMN "DialogID" ADD generated always as IDENTITY;

ALTER TABLE "Dialog" RENAME TO "old_Dialog";
ALTER TABLE "tmp_dialog" RENAME TO "Dialog";

