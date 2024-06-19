ALTER TABLE "Post" ADD FOREIGN KEY ("GroupID") REFERENCES "Group" ("GroupID");

ALTER TABLE "Post" ADD FOREIGN KEY ("AuthorID") REFERENCES "User" ("UserID");

ALTER TABLE "Like" ADD FOREIGN KEY ("PostID") REFERENCES "Post" ("PostID");

ALTER TABLE "Like" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "Comment" ADD FOREIGN KEY ("PostID") REFERENCES "Post" ("PostID");

ALTER TABLE "Comment" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "Message" ADD FOREIGN KEY ("AuthorID") REFERENCES "User" ("UserID");

ALTER TABLE "DialogUser" ADD FOREIGN KEY ("DialogID") REFERENCES "Dialog" ("DialogID");

ALTER TABLE "DialogUser" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "DialogMessage" ADD FOREIGN KEY ("DialogID") REFERENCES "Dialog" ("DialogID");

ALTER TABLE "DialogMessage" ADD FOREIGN KEY ("MessageID") REFERENCES "Message" ("MessageID");

ALTER TABLE "Subscriber" ADD FOREIGN KEY ("SubscriberID") REFERENCES "User" ("UserID");

ALTER TABLE "Subscriber" ADD FOREIGN KEY ("SubscribeID") REFERENCES "Subscribe" ("SubscribeID");

ALTER TABLE "Subscribe" ADD FOREIGN KEY ("SubscribedUserID") REFERENCES "User" ("UserID");

ALTER TABLE "Subscribe" ADD FOREIGN KEY ("SubscribedGroupID") REFERENCES "Group" ("GroupID");

ALTER TABLE "GroupUserRole" ADD FOREIGN KEY ("GroupID") REFERENCES "Group" ("GroupID");

ALTER TABLE "GroupUserRole" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "GroupUserRole" ADD FOREIGN KEY ("UserRoleID") REFERENCES "Role" ("RoleID");