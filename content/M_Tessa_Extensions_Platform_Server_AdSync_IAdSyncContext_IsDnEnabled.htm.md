# IAdSyncContext.IsDnEnabled - метод
Проверяет необходимо ли синхронизировать указанный DN.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsDnEnabled(
    	string dn
    )
VB __Копировать
     Function IsDnEnabled ( 
    	dn As String
    ) As Boolean
C++ __Копировать
     bool IsDnEnabled(
    	String^ dn
    )
F# __Копировать
     abstract IsDnEnabled : 
            dn : string -> bool 
#### Параметры
dn [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ветвь OU. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Нужно ли синхронизировать объект.
##  __См. также
#### Ссылки
[IAdSyncContext -
](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
