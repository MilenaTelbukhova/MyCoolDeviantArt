CREATE TABLE IF NOT EXISTS "User" (
  "UserID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "Username" varchar(30),
  "E_mail" varchar(100),
  "Password" varchar(100),
  "Status" varchar(255),
  "AvatarImage" varchar(255)
);

CREATE TABLE IF NOT EXISTS "Post" (
  "PostID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "GroupID" BIGINT,
  "AuthorID" BIGINT,
  "Picture" varchar(255),
  "Description" varchar(1500),
  "TimePosted" date,
  "IsDeleted" bool
);

CREATE TABLE IF NOT EXISTS "Like" (
  "PostID" BIGINT,
  "UserID" BIGINT,
  PRIMARY KEY ("PostID", "UserID")
);

CREATE TABLE IF NOT EXISTS "Comment" (
  "CommentID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "PostID" BIGINT,
  "UserID" BIGINT,
  "Comment" varchar(1000),
  "TimePosted" date
);

CREATE TABLE IF NOT EXISTS "Dialog" (
  "DialogID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "DialogName" varchar(100),
  "Logo" varchar(255)
);

CREATE TABLE IF NOT EXISTS "Message" (
  "MessageID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "Text" varchar(1500),
  "AuthorID" BIGINT,
  "TimeSent" date,
  "IsDeleted" bool,
  "Read" bool
);

CREATE TABLE IF NOT EXISTS "Subscriber" (
  "SubscriberID" BIGINT,
  "SubscribeID" BIGINT,
  "EndOfSubscribe" date,
  PRIMARY KEY ("SubscriberID", "SubscribeID")
);

CREATE TABLE IF NOT EXISTS "Subscribe" (
  "SubscribeID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "Price" money,
  "SubscribeName" varchar(40),
  "SubscribedUserID" BIGINT,
  "SubscribedGroupID" BIGINT
);

CREATE TABLE IF NOT EXISTS "Group" (
  "GroupID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "GroupName" varchar(30),
  "GroupLogo" varchar(255)
);

CREATE TABLE IF NOT EXISTS "Role" (
  "RoleID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "RoleName" varchar(30)
);

CREATE TABLE IF NOT EXISTS "ThemeOfADay" (
  "ThemeID" BIGINT PRIMARY KEY generated always as IDENTITY,
  "Date" date,
  "ThemeName" varchar(30)
);

