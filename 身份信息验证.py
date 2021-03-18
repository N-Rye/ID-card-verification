import re
def checkIdcard(idcard):
    # 各个地区的身份证前两位
    area={"11":"北京","12":"天津","13":"河北","14":"山西",
          "15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江",
          "31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建",
          "36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南",
          "44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川",
          "52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃",
          "63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港",
          "82":"澳门","91":"国外"}
    #各个市区的身份证前四位
    city = {
	'420500': ['湖北省', '宜昌市'],
	'231200': ['黑龙江省', '绥化市'],
	'420900': ['湖北省', '孝感市'],
	'230400': ['黑龙江省', '鹤岗市'],
	'150500': ['内蒙古自治区', '通辽市'],
	'150300': ['内蒙古自治区', '乌海市'],
	'150400': ['内蒙古自治区', '赤峰市'],
	'140500': ['山西省', '晋城市'],
	'620100': ['甘肃省', '兰州市'],
	'152900': ['内蒙古自治区', '阿拉善盟'],
	'511000': ['四川省', '内江市'],
	'140200': ['山西省', '大同市'],
	'131000': ['河北省', '廊坊市'],
	'430100': ['湖南省', '长沙市'],
	'511100': ['四川省', '乐山市'],
	'440400': ['广东省', '珠海市'],
	'445300': ['广东省', '云浮市'],
	'530600': ['云南省', '昭通市'],
	'440500': ['广东省', '汕头市'],
	'411600': ['河南省', '周口市'],
	'513400': ['四川省', '凉山彝族自治州'],
	'340700': ['安徽省', '铜陵市'],
	'411500': ['河南省', '信阳市'],
	'211200': ['辽宁省', '铁岭市'],
	'330100': ['浙江省', '杭州市'],
	'371700': ['山东省', '菏泽市'],
	'130400': ['河北省', '邯郸市'],
	'411200': ['河南省', '三门峡市'],
	'130300': ['河北省', '秦皇岛市'],
	'441900': ['广东省', '东莞市'],
	'611000': ['陕西省', '商洛市'],
	'530500': ['云南省', '保山市'],
	'510800': ['四川省', '广元市'],
	'652700': ['新疆维吾尔自治区', '博尔塔拉蒙古自治州'],
	'632600': ['青海省', '果洛藏族自治州'],
	'640400': ['宁夏回族自治区', '固原市'],
	'510700': ['四川省', '绵阳市'],
	'421000': ['湖北省', '荆州市'],
	'411400': ['河南省', '商丘市'],
	'120000': ['天津市', '天津市'],
	'650200': ['新疆维吾尔自治区', '克拉玛依市'],
	'210600': ['辽宁省', '丹东市'],
	'370600': ['山东省', '烟台市'],
	'370300': ['山东省', '淄博市'],
	'430200': ['湖南省', '株洲市'],
	'231000': ['黑龙江省', '牡丹江市'],
	'340400': ['安徽省', '淮南市'],
	'510400': ['四川省', '攀枝花市'],
	'370500': ['山东省', '东营市'],
	'511400': ['四川省', '眉山市'],
	'340800': ['安徽省', '安庆市'],
	'411300': ['河南省', '南阳市'],
	'140900': ['山西省', '忻州市'],
	'371200': ['山东省', '莱芜市'],
	'130800': ['河北省', '承德市'],
	'431000': ['湖南省', '郴州市'],
	'360700': ['江西省', '赣州市'],
	'422800': ['湖北省', '恩施土家族苗族自治州'],
	'520200': ['贵州省', '六盘水市'],
	'650100': ['新疆维吾尔自治区', '乌鲁木齐市'],
	'371100': ['山东省', '日照市'],
	'331100': ['浙江省', '丽水市'],
	'430800': ['湖南省', '张家界市'],
	'610300': ['陕西省', '宝鸡市'],
	'210100': ['辽宁省', '沈阳市'],
	'340100': ['安徽省', '合肥市'],
	'350100': ['福建省', '福州市'],
	'130500': ['河北省', '邢台市'],
	'640100': ['宁夏回族自治区', '银川市'],
	'533400': ['云南省', '迪庆藏族自治州'],
	'450200': ['广西壮族自治区', '柳州市'],
	'522300': ['贵州省', '黔西南布依族苗族自治州'],
	'433100': ['湖南省', '湘西土家族苗族自治州'],
	'320800': ['江苏省', '淮安市'],
	'350900': ['福建省', '宁德市'],
	'420300': ['湖北省', '十堰市'],
	'440300': ['广东省', '深圳市'],
	'320600': ['江苏省', '南通市'],
	'520500': ['贵州省', '毕节市'],
	'130600': ['河北省', '保定市'],
	'450100': ['广西壮族自治区', '南宁市'],
	'441200': ['广东省', '肇庆市'],
	'511600': ['四川省', '广安市'],
	'140400': ['山西省', '长治市'],
	'450600': ['广西壮族自治区', '防城港市'],
	'150700': ['内蒙古自治区', '呼伦贝尔市'],
	'430500': ['湖南省', '邵阳市'],
	'421300': ['湖北省', '随州市'],
	'330800': ['浙江省', '衢州市'],
	'420700': ['湖北省', '鄂州市'],
	'210300': ['辽宁省', '鞍山市'],
	'331000': ['浙江省', '台州市'],
	'370200': ['山东省', '青岛市'],
	'131100': ['河北省', '衡水市'],
	'654000': ['新疆维吾尔自治区', '伊犁哈萨克自治州'],
	'610800': ['陕西省', '榆林市'],
	'230900': ['黑龙江省', '七台河市'],
	'211400': ['辽宁省', '葫芦岛市'],
	'441800': ['广东省', '清远市'],
	'620600': ['甘肃省', '武威市'],
	'230200': ['黑龙江省', '齐齐哈尔市'],
	'431200': ['湖南省', '怀化市'],
	'620200': ['甘肃省', '嘉峪关市'],
	'350800': ['福建省', '龙岩市'],
	'511900': ['四川省', '巴中市'],
	'450800': ['广西壮族自治区', '贵港市'],
	'110000': ['北京市', '北京市'],
	'140800': ['山西省', '运城市'],
	'630100': ['青海省', '西宁市'],
	'440900': ['广东省', '茂名市'],
	'350500': ['福建省', '泉州市'],
	'460200': ['海南省', '三亚市'],
	'341800': ['安徽省', '宣城市'],
	'632200': ['青海省', '海北藏族自治州'],
	'320500': ['江苏省', '苏州市'],
	'410400': ['河南省', '平顶山市'],
	'140700': ['山西省', '晋中市'],
	'542500': ['西藏自治区', '阿里地区'],
	'140300': ['山西省', '阳泉市'],
	'640200': ['宁夏回族自治区', '石嘴山市'],
	'710000': ['台湾省', '台湾省'],
	'410300': ['河南省', '洛阳市'],
	'210400': ['辽宁省', '抚顺市'],
	'653100': ['新疆维吾尔自治区', '喀什地区'],
	'654300': ['新疆维吾尔自治区', '阿勒泰地区'],
	'530100': ['云南省', '昆明市'],
	'321200': ['江苏省', '泰州市'],
	'441700': ['广东省', '阳江市'],
	'410500': ['河南省', '安阳市'],
	'152500': ['内蒙古自治区', '锡林郭勒盟'],
	'370400': ['山东省', '枣庄市'],
	'330600': ['浙江省', '绍兴市'],
	'632300': ['青海省', '黄南藏族自治州'],
	'620700': ['甘肃省', '张掖市'],
	'320300': ['江苏省', '徐州市'],
	'370800': ['山东省', '济宁市'],
	'410700': ['河南省', '新乡市'],
	'360500': ['江西省', '新余市'],
	'440800': ['广东省', '湛江市'],
	'460300': ['海南省', '三沙市'],
	'445200': ['广东省', '揭阳市'],
	'620400': ['甘肃省', '白银市'],
	'520600': ['贵州省', '铜仁市'],
	'210200': ['辽宁省', '大连市'],
	'511700': ['四川省', '达州市'],
	'530700': ['云南省', '丽江市'],
	'220500': ['吉林省', '通化市'],
	'532500': ['云南省', '红河哈尼族彝族自治州'],
	'431100': ['湖南省', '永州市'],
	'350200': ['福建省', '厦门市'],
	'540200': ['西藏自治区', '日喀则市'],
	'450700': ['广西壮族自治区', '钦州市'],
	'371000': ['山东省', '威海市'],
	'230300': ['黑龙江省', '鸡西市'],
	'341700': ['安徽省', '池州'],
	'650400': ['新疆维吾尔自治区', '吐鲁番市'],
	'420200': ['湖北省', '黄石市'],
	'431300': ['湖南省', '娄底市'],
	'220400': ['吉林省', '辽源市'],
	'340300': ['安徽省', '蚌埠市'],
	'330200': ['浙江省', '宁波市'],
	'330300': ['浙江省', '温州市'],
	'532600': ['云南省', '文山壮族苗族自治州'],
	'150800': ['内蒙古自治区', '巴彦淖尔市'],
	'620800': ['甘肃省', '平凉市'],
	'650500': ['新疆维吾尔自治区', '哈密市'],
	'622900': ['甘肃省', '临夏回族自治州'],
	'220800': ['吉林省', '白城市'],
	'220200': ['吉林省', '吉林市'],
	'210500': ['辽宁省', '本溪市'],
	'330400': ['浙江省', '嘉兴市'],
	'441400': ['广东省', '梅州市'],
	'440100': ['广东省', '广州市'],
	'360200': ['江西省', '景德镇市'],
	'532800': ['云南省', '西双版纳傣族自治州'],
	'371300': ['山东省', '临沂市'],
	'230600': ['黑龙江省', '大庆市'],
	'341100': ['安徽省', '滁州市'],
	'440200': ['广东省', '韶关市'],
	'513300': ['四川省', '甘孜藏族自治州'],
	'530300': ['云南省', '曲靖市'],
	'632500': ['青海省', '海南藏族自治州'],
	'450300': ['广西壮族自治区', '桂林市'],
	'410900': ['河南省', '濮阳市'],
	'150100': ['内蒙古自治区', '呼和浩特市'],
	'340600': ['安徽省', '淮北市'],
	'361100': ['江西省', '上饶市'],
	'451300': ['广西壮族自治区', '来宾市'],
	'360100': ['江西省', '南昌市'],
	'341500': ['安徽省', '六安市'],
	'130200': ['河北省', '唐山市'],
	'520100': ['贵州省', '贵阳市'],
	'320200': ['江苏省', '无锡市'],
	'530400': ['云南省', '玉溪市'],
	'512000': ['四川省', '资阳市'],
	'410100': ['河南省', '郑州市'],
	'220600': ['吉林省', '白山市'],
	'520300': ['贵州省', '遵义市'],
	'451400': ['广西壮族自治区', '崇左市'],
	'321100': ['江苏省', '镇江市'],
	'222400': ['吉林省', '延边朝鲜族自治州'],
	'511800': ['四川省', '雅安市'],
	'321300': ['江苏省', '宿迁市'],
	'430600': ['湖南省', '岳阳市'],
	'230100': ['黑龙江省', '哈尔滨市'],
	'421100': ['湖北省', '黄冈市'],
	'511300': ['四川省', '南充市'],
	'320400': ['江苏省', '常州市'],
	'540300': ['西藏自治区', '昌都市'],
	'210800': ['辽宁省', '营口市'],
	'360600': ['江西省', '鹰潭市'],
	'152200': ['内蒙古自治区', '兴安盟'],
	'370100': ['山东省', '济南市'],
	'360300': ['江西省', '萍乡市'],
	'341200': ['安徽省', '阜阳市'],
	'360400': ['江西省', '九江市'],
	'130900': ['河北省', '沧州市'],
	'210700': ['辽宁省', '锦州市'],
	'340200': ['安徽省', '芜湖市'],
	'220700': ['吉林省', '松原市'],
	'522700': ['贵州省', '黔南布依族苗族自治州'],
	'150900': ['内蒙古自治区', '乌兰察布市'],
	'150200': ['内蒙古自治区', '包头市'],
	'620300': ['甘肃省', '金昌市'],
	'211300': ['辽宁省', '朝阳市'],
	'440700': ['广东省', '江门市'],
	'141000': ['山西省', '临汾市'],
	'610600': ['陕西省', '延安市'],
	'451200': ['广西壮族自治区', '河池市'],
	'442000': ['广东省', '中山市'],
	'441500': ['广东省', '汕尾市'],
	'220100': ['吉林省', '长春市'],
	'621100': ['甘肃省', '定西市'],
	'500000': ['重庆市', '重庆市'],
	'820000': ['澳门特别行政区', '澳门特别行政区'],
	'652800': ['新疆维吾尔自治区', '巴音郭楞蒙古自治州'],
	'150600': ['内蒙古自治区', '鄂尔多斯市'],
	'510500': ['四川省', '泸州市'],
	'652900': ['新疆维吾尔自治区', '阿克苏地区'],
	'451000': ['广西壮族自治区', '百色市'],
	'621000': ['甘肃省', '庆阳市'],
	'430900': ['湖南省', '益阳市'],
	'510900': ['四川省', '遂宁市'],
	'520400': ['贵州省', '安顺市'],
	'510600': ['四川省', '德阳市'],
	'321000': ['江苏省', '扬州市'],
	'460400': ['海南省', '儋州市'],
	'232700': ['黑龙江省', '大兴安岭地区'],
	'411100': ['河南省', '漯河市'],
	'621200': ['甘肃省', '陇南市'],
	'130100': ['河北省', '石家庄市'],
	'451100': ['广西壮族自治区', '贺州市'],
	'441300': ['广东省', '惠州市'],
	'340500': ['安徽省', '马鞍山市'],
	'370700': ['山东省', '潍坊市'],
	'230800': ['黑龙江省', '佳木斯市'],
	'341000': ['安徽省', '黄山市'],
	'210900': ['辽宁省', '阜新市'],
	'530800': ['云南省', '普洱市'],
	'511500': ['四川省', '宜宾市'],
	'220300': ['吉林省', '四平市'],
	'540100': ['西藏自治区', '拉萨市'],
	'513200': ['四川省', '阿坝藏族羌族自治州'],
	'411700': ['河南省', '驻马店市'],
	'370900': ['山东省', '泰安市'],
	'350600': ['福建省', '漳州市'],
	'410600': ['河南省', '鹤壁市'],
	'360800': ['江西省', '吉安市'],
	'360900': ['江西省', '宜春市'],
	'640500': ['宁夏回族自治区', '中卫市'],
	'610500': ['陕西省', '渭南市'],
	'653200': ['新疆维吾尔自治区', '和田地区'],
	'632700': ['青海省', '玉树藏族自治州'],
	'522600': ['贵州省', '黔东南苗族侗族自治州'],
	'540600': ['西藏自治区', '那曲市'],
	'510300': ['四川省', '自贡市'],
	'330900': ['浙江省', '舟山市'],
	'330700': ['浙江省', '金华市'],
	'630200': ['青海省', '海东市'],
	'610400': ['陕西省', '咸阳市'],
	'130700': ['河北省', '张家口市'],
	'410800': ['河南省', '焦作市'],
	'140100': ['山西省', '太原市'],
	'460100': ['海南省', '海口市'],
	'141100': ['山西省', '吕梁市'],
	'419001': ['河南省', '济源市'],
	'320700': ['江苏省', '连云港市'],
	'510100': ['四川省', '成都市'],
	'430300': ['湖南省', '湘潭市'],
	'652300': ['新疆维吾尔自治区', '昌吉回族自治州'],
	'230700': ['黑龙江省', '伊春市'],
	'610100': ['陕西省', '西安市'],
	'231100': ['黑龙江省', '黑河市'],
	'230500': ['黑龙江省', '双鸭山市'],
	'610700': ['陕西省', '汉中市'],
	'341300': ['安徽省', '宿州市'],
	'623000': ['甘肃省', '甘南藏族自治州'],
	'540500': ['西藏自治区', '山南市'],
	'371500': ['山东省', '聊城市'],
	'610900': ['陕西省', '安康市'],
	'640300': ['宁夏回族自治区', '吴忠市'],
	'430700': ['湖南省', '常德市'],
	'653000': ['新疆维吾尔自治区', '克孜勒苏柯尔克孜自治州'],
	'810000': ['香港特别行政区', '香港特别行政区'],
	'450500': ['广西壮族自治区', '北海市'],
	'533100': ['云南省', '德宏傣族景颇族自治州'],
	'211000': ['辽宁省', '辽阳市'],
	'532300': ['云南省', '楚雄彝族自治州'],
	'411000': ['河南省', '许昌市'],
	'330500': ['浙江省', '湖州市'],
	'320900': ['江苏省', '盐城市'],
	'420100': ['湖北省', '武汉市'],
	'620500': ['甘肃省', '天水市'],
	'420600': ['湖北省', '襄阳市'],
	'532900': ['云南省', '大理白族自治州'],
	'371600': ['山东省', '滨州市'],
	'310000': ['上海市', '上海市'],
	'632800': ['青海省', '海西蒙古族藏族自治州'],
	'420800': ['湖北省', '荆门市'],
	'341600': ['安徽省', '豪州市'],
	'410200': ['河南省', '开封市'],
	'350700': ['福建省', '南平市'],
	'441600': ['广东省', '河源市'],
	'350300': ['福建省', '莆田市'],
	'371400': ['山东省', '德州市'],
	'533300': ['云南省', '怒江傈僳族自治州'],
	'654200': ['新疆维吾尔自治区', '塔城地区'],
	'350400': ['福建省', '三明市'],
	'140600': ['山西省', '朔州市'],
	'421200': ['湖北省', '咸宁市'],
	'530900': ['云南省', '临沧市'],
	'620900': ['甘肃省', '酒泉市'],
	'440600': ['广东省', '佛山市'],
	'540400': ['西藏自治区', '林芝市'],
	'361000': ['江西省', '抚州市'],
	'610200': ['陕西省', '铜川市'],
	'211100': ['辽宁省', '盘锦市'],
	'445100': ['广东省', '潮州市'],
	'430400': ['湖南省', '衡阳市'],
	'450400': ['广西壮族自治区', '梧州市'],
	'450900': ['广西壮族自治区', '玉林市'],
	'320100': ['江苏省', '南京市']}
    idcard=str(idcard)  # 将idcard转为string类型
    idcard=idcard.strip()  # 默认删除空白符
    idcard_list=list(idcard)  # 将idcard 放入列表中
    idcard_brith = idcard[6:14]# 生日字段
    idcard_sex = idcard[14:17]  # 性别字段
    year = idcard_brith[0:4]  # 年
    month = idcard_brith[4:6]  # 月
    day = idcard_brith[6:8]  # 日
    #地区校验，验证输入的前两位
    if(not area[(idcard)[0:2]]):
        print('身份证地区非法!')
    #18位身份号码检测
    elif(len(idcard)==18):
        #出生日期的合法性检查
        if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
            # 闰年出生日期的合法性正则表达式(闰年2月有29天，年份前两位只能是19，或者20，前两位是20的话，后两位最大到21。1,3,4,7,8,10,12月一个月可以有31天，4,6,9,11只能到30天)
            ereg=re.compile('(19[0-9]{2})|(20[0-2][0-9])((01|03|05|07|08|10|12)([0-2][0-9]|3[0-1])|((04|06|09|11)([0-2][0-9]|30))|((02)([0-2][0-9])))')
        else:
            # 平年出生日期的合法性正则表达式(平年2月有28天，年份前两位只能是19，或者20，前两位是20的话，后两位最大到21。1,3,4,7,8,10,12月一个月可以有31天，4,6,9,11只能到30天)
            ereg=re.compile('(19[0-9]{2})|(20[0-2][0-9])((01|03|05|07|08|10|12)([0-2][0-9]|3[0-1])|((04|06|09|11)([0-2][0-9]|30))|((02)([0-2][0-8])))')
        #测试出生日期的合法性
        if(re.match(ereg,idcard_brith)):
            #计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + \
                (int(idcard_list[1]) + int(idcard_list[11])) * 9 + \
                (int(idcard_list[2]) + int(idcard_list[12])) * 10 + \
                (int(idcard_list[3]) + int(idcard_list[13])) * 5 + \
                (int(idcard_list[4]) + int(idcard_list[14])) * 8 + \
                (int(idcard_list[5]) + int(idcard_list[15])) * 4 + \
                (int(idcard_list[6]) + int(idcard_list[16])) * 2 + \
                int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + \
                int(idcard_list[9]) * 3
            Y = S % 11 # 求余
            JYM = "10X98765432"
            M = JYM[Y]#判断校验位
            if(M == idcard_list[17]):#检测ID的校验位
                print ('验证通过!')
                B=idcard[0:2]
                print("省份:"+area[idcard[0:2]])
                print("市区:"+city[idcard[0:4]+"00"][1])
                print ('生日:'+year+'年'+ month +'月'+day+'日')
                if int(idcard_sex)%2 == 0:
                    print ('性别：女')
                else:
                    print ('性别：男')
            else:
                print ('身份证号码校验错误!')
        else:
            print ('身份证号码出生日期超出范围!')
    else:
        print ('身份证号码位数不对!')
if __name__ == '__main__':
    while True:           #在输入时判断是否为18位，否则重新输入
        idcard =input('请输入身份证号码：')
        if len(idcard)==18:
            break
        else:
            print("~~~~~~~~~~身份证号码位数不对,请重新输入~~~~~~~~~~~")
    checkIdcard(idcard)