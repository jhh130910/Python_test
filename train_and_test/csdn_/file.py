import  os
import  re


class FilterNumber:
    def filefilter(self):
        dir_path = '/data/tools/csdn/demo'
        ndir_path = '/data/tools/csdn/worker'
        list = os.listdir(dir_path)
        first =[]
        ffile = []
        for i in range(0,len(list)):
            path = os.path.join(dir_path,list[i])
            first.append(path)
            ffile.append(list[i])
            fopen = open(path, 'r')
            fwrite = open(ndir_path + "/" + ffile[i],'w')
            for eachline in fopen:
                    nline =re.sub('\d+','',eachline)
                    print(eachline)
                    fwrite.write(nline)

            print('write success')
            fopen.close()
            fwrite.close()


if __name__ == '__main__':
    f = FilterNumber()
    f.filefilter()
