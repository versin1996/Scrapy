# -*- coding: utf-8 -*-


class TransCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def getCookie(self):
        itemDict = {}
        items = [item.strip() for item in self.cookie.split(';')]
        for item in items:
            key, value = item.split('=')
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'UserIC=182%2E142%2E35%2E172%2D20200708110033; UM_distinctid=1732c5e1f91827-0f5fdf5a784653-4353761-144000-1732c5e1f92c6b; utype=%C6%E4%CB%FB; username=versin; password=0761c8bb76093e45; iReadArtID=%2D27%2D; vipnum=0; yname=%CD%FE%C9%AD; RememberMe=ok; UserEduType=; IfZhuanye=; company=; IfLockGb=; ifpartner=; enddate=; ifvip=; ASPSESSIONIDSQETSRDD=CONAHDNDCKAKFMDEPPAHPKPH; CNZZDATA2878103=cnzz_eid%3D282836955-1594176557-%26ntime%3D1594367720; CNZZDATA1274624805=1020660856-1594175226-%7C1594367737; lastIP=182%2E142%2E35%2E172; ComTitle=; ifpass=0; bname=versin; UID=C20200710277680988; lastlogin=2020%2F7%2F10+17%3A00%3A32; lastlogintime=2020%2F7%2F10+17%3A00%3A32; UserID=100981; face=%2Fimg%5Fuserface%2Fdefault%2Dboy%2Fboy6%2Epng; LoginOK=1bianju%2Ecom; loginnum=6; ifpass%5Femail=1; CurrentBannerNo=2; ComeUrl=http%3A%2F%2Fwww%2E1bianju%2Ecom%3A443%2FArt%5Flist%2Easp%3Fid%3D27%26CType%3Dcontent; BannerOrderID%5FLast=1%2E5; ReadADID=5; ReadADID2=5; ViewPages=28'
    trans = TransCookie(cookie)
    print(trans.getCookie())