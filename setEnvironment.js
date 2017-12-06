postman.setEnvironmentVariable("uri","http://yltest.xylpay.com");
postman.setEnvironmentVariable("appId","test001");
postman.setEnvironmentVariable("idCardNo", ("34112619770921"+(parseInt(Math.random()*1000))+"6"));
postman.setEnvironmentVariable("mobile", ("130000"+(parseInt(Math.random()*100000))));
postman.setEnvironmentVariable("userName", ("automationTest"+("000000" + (Math.random()*Math.pow(36,6) << 0).toString(36)).slice(-6)));
postman.setEnvironmentVariable("verifyCode","");
var smsArr=["register","bankcard"];
var index = Math.floor((Math.random()*smsArr.length));   
postman.setEnvironmentVariable("type",smsArr[index]);
postman.setEnvironmentVariable("bankCardNo", ("62252203"+(parseInt(Math.random()*10000000))+"0"));
postman.setEnvironmentVariable("userId","");
postman.setEnvironmentVariable("storeName", ("automationTest"+("000000" + (Math.random()*Math.pow(36,6) << 0).toString(36)).slice(-6)));
postman.setEnvironmentVariable("address","automationTest");
postman.setEnvironmentVariable("industryMcc","5699");
postman.setEnvironmentVariable("provinceCode","926");
postman.setEnvironmentVariable("cityCode","941");
postman.setEnvironmentVariable("areaCode","944");
postman.setEnvironmentVariable("bizLicence", ("001300"+(parseInt(Math.random()*1000000))));
postman.setEnvironmentVariable("licence","");

postman.setEnvironmentVariable("tradeNo","111");
postman.setEnvironmentVariable("key","gEV9GhV413vDlDtc");
postman.setEnvironmentVariable("PicBase64","eee");

var array=[
    {name:"tradeNo",value:environment.tradeNo},
    {name:"key",value:environment.key}
    ];
var str = [];
array.forEach(function (n, i) {
        if(n.value === ''){
                return;
        }
        str.push(n.name + '=' + n.value);
    });

str=str.join('&');
postman.setEnvironmentVariable("str",str);
var sign = CryptoJS.MD5(str).toString().toUpperCase();
postman.setEnvironmentVariable('sign', sign);