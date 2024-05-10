
#打开邮箱
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#访问outlook的收件箱
inbox = outlook.GetDefaultFolder(6)
#访问outlook的发件箱
outbox= outlook.GetDefaultFolder(5)
#统计收件箱中邮件的数量
messages = inbox.Items



# outlook.GetDefaultFolder()方法中各类数字对应的邮件文件夹
# olFolderInbox: 6 - 收件箱
# olFolderCalendar: 9 - 日历
# olFolderContacts: 10 - 联系人
# olFolderNotes: 11 - 笔记
# olFolderTasks: 13 - 任务
# olFolderDrafts: 16 - 草稿箱
# olFolderSentMail: 5 - 已发送邮件
# olFolderDeletedItems: 3 - 已删除邮件
# olFolderOutbox: 4 - 发件箱
# olFolderJournal: 12 - 日志
# olFolderConflicts: 2 - 冲突项
# olFolderSyncIssues: 14 - 同步问题
# olPublicFoldersRoot: 18 - 公共文件夹根目录
# olFolderRssFeeds: 25 - RSS 源
