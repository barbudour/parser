# ApplicationHostConnectionInfo.SetToken - метод
Устанавливает заданный токен в свойстве
[TokenString](P_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo_TokenString.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void SetToken(
    	ISessionToken token
    )
VB __Копировать
     Public Sub SetToken ( 
    	token As ISessionToken
    )
C++ __Копировать
     public:
    void SetToken(
    	ISessionToken^ token
    )
F# __Копировать
     member SetToken : 
            token : ISessionToken -> unit 
#### Параметры
token [ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm)
    Устанавливаемый токен. Может быть равен null, если считается, что он не был задан.
##  __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
