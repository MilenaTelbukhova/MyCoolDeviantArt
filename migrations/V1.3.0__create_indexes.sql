CREATE INDEX IF NOT EXISTS "User_UserName"
ON "User"("Username");

CREATE INDEX IF NOT EXISTS "Message_isdeleted"
ON "Message"("IsDeleted");

CREATE INDEX IF NOT EXISTS "Group_groupname"
ON "Group"("GroupName");

CREATE INDEX IF NOT EXISTS "Subscriber_endofsubscribe"
ON "Subscriber"("EndOfSubscribe");

CREATE INDEX IF NOT EXISTS "Subscribe_price"
ON "Subscribe"("Price");