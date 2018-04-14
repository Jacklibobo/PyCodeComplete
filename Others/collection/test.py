#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    data_dict = {"symbols":[{"id":"6","short_name":"USD","name":"    USD ","date_update":"131673151560000000","sell_rate":"50598","buy_rate":"49718","sell_tradable":1,"buy_tradable":1},{"id":"7","short_name":"EUR","name":"    EUR ","date_update":"131673154350000000","sell_rate":"62623","buy_rate":"61241","sell_tradable":1,"buy_tradable":1},{"id":"22","short_name":"AED","name":"    AED","date_update":"131673151560000000","sell_rate":"13730","buy_rate":"13560","sell_tradable":1,"buy_tradable":1},{"id":"24","short_name":"TRY","name":"        TRY ","date_update":"131673154340000000","sell_rate":"12800","buy_rate":"12241","sell_tradable":1,"buy_tradable":1},{"id":"25","short_name":"CNY","name":"    CNY ","date_update":"131673152430000000","sell_rate":"7976","buy_rate":"7864","sell_tradable":1,"buy_tradable":1},{"id":"26","short_name":"GBP","name":"    GBP","date_update":"131673151560000000","sell_rate":"71338","buy_rate":"69117","sell_tradable":1,"buy_tradable":1},{"id":"27","short_name":"CAD","name":"      CAD ","date_update":"131673154340000000","sell_rate":"41237","buy_rate":"39188","sell_tradable":1,"buy_tradable":1},{"id":"92","short_name":"GOLD24","name":"1          24     ","date_update":"131667786420000000","sell_rate":"2144174","buy_rate":"2144174","sell_tradable":1,"buy_tradable":1},{"id":"93","short_name":"GOLD18","name":"1          18     ","date_update":"131673154320000000","sell_rate":"1637507","buy_rate":"1637507","sell_tradable":1,"buy_tradable":1},{"id":"94","short_name":"COIN1","name":"         (         )","date_update":"131667786420000000","sell_rate":"15688924","buy_rate":"15688924","sell_tradable":1,"buy_tradable":1},{"id":"95","short_name":"XAU1OUNCE","name":"1          24     ","date_update":"131673030700000000","sell_rate":"67465881","buy_rate":"67465881","sell_tradable":1,"buy_tradable":1}]}
    for data in data_dict["symbols"]:
        if data["short_name"] in ["USD", "CNY"]:
            print("{0}:sall_rate is {1}, buy_rate is {2}".format(data["short_name"], data["sell_rate"], data["buy_rate"]))