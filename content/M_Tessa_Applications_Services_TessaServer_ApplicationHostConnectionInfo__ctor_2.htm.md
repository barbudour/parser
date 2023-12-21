# ApplicationHostConnectionInfo(IConnectionSettings, ISessionToken) -
конструктор
Создаёт экземпляр класса, копируя в него свойства из заданных объектов.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationHostConnectionInfo(
    	IConnectionSettings connectionSettings,
    	ISessionToken token = null
    )
VB __Копировать
     Public Sub New ( 
    	connectionSettings As IConnectionSettings,
    	Optional token As ISessionToken = Nothing
    )
C++ __Копировать
     public:
    ApplicationHostConnectionInfo(
    	IConnectionSettings^ connectionSettings, 
    	ISessionToken^ token = nullptr
    )
F# __Копировать
     new : 
            connectionSettings : IConnectionSettings * 
            ?token : ISessionToken 
    (* Defaults:
            let _token = defaultArg token null
    *)
    -> ApplicationHostConnectionInfo
#### Параметры
connectionSettings
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
    Объект, из которого копируются свойства настроек подключения. Не должен быть равен null.
token [ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) (Optional)
    Токен, сериализуемый для аутентификации. Может быть равен null.
##  __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[ApplicationHostConnectionInfo -
перегрузка](Overload_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo__ctor.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
