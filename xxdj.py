#   --------------------------------注释区--------------------------------
#   入口:http://xingxing.cpjla.com/pages/register/index.html?invite_code=362064 走个头谢谢
#   记得绑定支付宝 不然无法自动提现
#   变量:yuanshen_xxdj 多号 [ @ 或 换行 或 新建同名变量 ]
#   抓取api.xx.xingdouduanju.com请求头中Authorization的值和X-Device-ID的填入
#   格式Authorization#X-Device-ID
#   corn: 8小时一次 一天两次
#
#   金币换牛子 牛子产红包 记得把新手的1w金币买牛子
#   够1w金币自己换牛子吧 懒得写了 一头现金牛子0.04r/h 一天0.96
#   加上红包任务一天大概1r吧 每日自己提现0.3（自动提现貌似有bug暂时不更新了）
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   验签异常是正常的不用鸟 脚本会自动处理 觉得不顺眼的不跑即可
#   除非跑了几小时都是验签异常再来联系我处理
#   --------------------------------一般不动区--------------------------------
# cron 22 20 */8 * * *
# const $ = new Env('星星短剧');
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))
