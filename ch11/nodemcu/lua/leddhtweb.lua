led = 2
dht22 = 4

gpio.mode(led,gpio.OUTPUT)

rnrn=0
Status = 0
DataToGet = 0
method=""
url=""
vars=""
--t=0
--h=0
srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
    conn:on("receive",function(conn,payload)

        if Status==0 then
            _,_,method,url,vars = string.find(payload, "([A-Z]+) /([^?]*)%??(.*) HTTP")
            print(":",method,url,vars)

        end

        if method=="GET" then
            if url=="events" then
                s,t,h,td,hd=dht.read(dht22)
                conn:send("HTTP/1.1 200 OK\r\n\r\n")
                if h ~= nil then
                    local json = "{".."\"temperature\": \""..(t).."\", "
                    json = json.."\"humidity\": \""..(h).."\" }"
                    conn:send(json)
                else
                    conn:send("")
                end
                return
            end
        end

        if method=="POST" then
          if url=="led" then
            if Status==0 then
                --print("status", Status)
                _,_,DataToGet, payload = string.find(payload, "Content%-Length: (%d+)(.+)")
                if DataToGet~=nil then
                    DataToGet = tonumber(DataToGet)
                    --print(DataToGet)
                    rnrn=1
                    Status = 1
                else
                    print("Can't get length")
                end
            end

            -- find /r/n/r/n
            if Status==1 then
                --print("status", Status)
                local payloadlen = string.len(payload)
                local mark = "\r\n\r\n"
                local i
                for i=1, payloadlen do
                    if string.byte(mark, rnrn) == string.byte(payload, i) then
                        rnrn=rnrn+1
                        if rnrn==5 then
                            payload = string.sub(payload, i+1,payloadlen)
                            Status=2
                            break
                        end
                    else
                        rnrn=1
                    end
                end
                if Status==1 then
                    return
                end
            end

            if Status==2 then
                --print("status", Status)
                if payload~=nil then
                    DataToGet=DataToGet-string.len(payload)
                    --print("DataToGet:", DataToGet, "payload len:", string.len(payload))
                else
                    conn:send("HTTP/1.1 200 OK\r\n\r\nERROR")
                    Status=0
                end

                if DataToGet==0 then
                    conn:send("HTTP/1.1 200 OK\r\n\r\nOK")

                    if payload=="on" then
                        gpio.write(led, gpio.HIGH)
                        conn:send("<br>Result:<verbatim>on</verbatim>")
                    else
                        gpio.write(led, gpio.LOW)
                        conn:send("<br>Result:<verbatim>off</verbatim>")
                    end
                    Status=0
                end
            end
          end

          return
        end

        if url == "favicon.ico" then
            conn:send("HTTP/1.1 404 file not found")
            return
        end

        conn:send("HTTP/1.1 200 OK\r\n\r\n<html><body>")
        conn:send("<h1>NodeMCU IDE</h1>")

        if url=="" then
            local l = file.list();
            for k,v in pairs(l) do
                conn:send("<a href='"..k.."'>"..k.."</a>, size:"..v.."<br>")
            end
        end

        conn:send("</body></html>")

    end)
    conn:on("sent",function(conn) conn:close() end)
end)
