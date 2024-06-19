CREATE TABLE IF NOT EXISTS "DialogUser" (
  "DialogID" BIGINT,
  "UserID" BIGINT,
  PRIMARY KEY ("DialogID", "UserID")
);

CREATE TABLE IF NOT EXISTS "DialogMessage" (
  "DialogID" BIGINT,
  "MessageID" BIGINT,
  PRIMARY KEY ("DialogID", "MessageID")
);

CREATE TABLE IF NOT EXISTS "GroupUserRole" (
  "GroupID" BIGINT,
  "UserID" BIGINT,
  "UserRoleID" BIGINT,
  PRIMARY KEY ("GroupID", "UserID", "UserRoleID")
);

