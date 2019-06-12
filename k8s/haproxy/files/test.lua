json = loadfile("/etc/haproxy/json.lua")()                
core.register_fetches("get_username", function(txn)     
local payload = txn.req:dup()                             
local request_json = json.decode(string.sub(payload,string.find(payload,"\r\n\r\n")+4))
print ( request_json )
return request_json.username
end)
