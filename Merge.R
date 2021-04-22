#Summarize kaiju2table outputs from multiple samples

rm(list=ls())
setwd("C:/Users/pengxi/Desktop/New Folder/species")
filename_list = c("1B","1C","1D","1E","2A","2B","2C","2D","2E","3A","3B","3C","3D","3E","4A","4B","4C","4D","4E","5A","5B","5C","5D","5E","6A","6B","6C","6D","6E","7A","7B","7C","7D","7E","8A","8B","8C","8D","8E")
filename=paste('1A','.kaiju.species.txt',sep='')
x <- read.table(filename,sep= '\t',header=T)
for (f in filename_list){
  filenamey=paste(f,'.kaiju.species.txt',sep='')
  y <- read.table(filenamey,sep= '\t', header=T)
  xy <- merge(x,y, by="taxon_name", all = T)
  xy[is.na(xy)] = 0
  x <- xy
  }
write.table(xy, file='output.txt',sep='\t')
