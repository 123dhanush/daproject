df1=read.csv("notesapp_studentstats.csv",header = FALSE,sep=",")

colnames(df1)=c("id","username","filename","count","courseid")
df1

df2=read.csv("notesapp_filedb.csv",header = FALSE,sep=",")
colnames(df2)=c("fileid","filename","fileurl","filecount","courseid","filecontent")
df2


barplot(as.numeric(df1$count),
        main = "count vs files",
        xlab = "files",
        ylab = "count",
        names.arg = df1$filename,
        col = rainbow(5),
        horiz = FALSE,
        las=2,
        cex.names = 0.5,
        cex.axis = 0.5)


barplot(as.numeric(df2$filecount),
        main = "count vs files",
        xlab = "files",
        ylab = "count",
        names.arg = df2$filename,
        col = rainbow(5),
        horiz = FALSE,
        las=2,
        cex.names = 0.5,
        cex.axis = 0.5)


barplot(as.numeric(df1$count),
        main = "count vs files",
        xlab = "count",
        ylab = "files",
        names.arg = df1$username,
        col = "darkred",
        horiz = FALSE,
        las=2,
        cex.names = 0.5,
        cex.axis = 0.5)
library(dplyr)



byusername=group_by(df1,username)

#summarize(data,userfilecount=sum(count))
# user activity

summarize(byusername,userfilecount=sum(count))

summarize(byusername,userfilecount=sum(count))[[2]]


plot(summarize(byusername,userfilecount=sum(count))[[1]],summarize(byusername,userfilecount=sum(count))[[2]],main="username vs filecount",type="p",col=rainbow(5),xlab="username",ylab="filecount")


bycourse =group_by(df2,courseid)

summarize(bycourse,userfilecount=sum(filecount))

summarize(bycourse,userfilecount=sum(filecount))[[2]]


plot(summarize(bycourse,userfilecount=sum(filecount))[[1]],summarize(bycourse,userfilecount=sum(filecount))[[2]],main="couseid vs filecount",type="p",col=rainbow(5),xlab="course",ylab="filecount")


