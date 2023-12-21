# ApplicationHostConnectionInfo - свойства
##  __Свойства
[BaseAddress](P_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo_BaseAddress.htm)|
Базовый адрес для подключения.  
---|---  
[ConnectTimeout](P_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo_ConnectTimeout.htm)|
Таймаут подключения к сервису или null, если используются текущие таймауты в
настройках. Применяется для указания всех таймаутов: открытие соединения,
отправка запроса, закрытие соединения.  
[InstanceName](P_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo_InstanceName.htm)|
Имя экземпляра сервера для подключения. Если равно null или пустой строке, то
используется текущее имя экземпляра в настройках. Укажите
[DefaultLegacyInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultLegacyInstanceName.htm)
для подключения к серверам 2.x.  
[TokenString](P_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo_TokenString.htm)|
Сериализованный в XML токен
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) или null/пустая
строка, если токен не задан.  
## __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
