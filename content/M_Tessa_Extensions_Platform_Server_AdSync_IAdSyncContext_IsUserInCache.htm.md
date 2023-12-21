# IAdSyncContext.IsUserInCache - метод
Проверяет был ли уже обновлен указанный пользователь.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsUserInCache(
    	Guid objectId
    )
VB __Копировать
     Function IsUserInCache ( 
    	objectId As Guid
    ) As Boolean
C++ __Копировать
     bool IsUserInCache(
    	Guid objectId
    )
F# __Копировать
     abstract IsUserInCache : 
            objectId : Guid -> bool 
#### Параметры
objectId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор пользователя. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Обновлен ли пользователь.
##  __См. также
#### Ссылки
[IAdSyncContext -
](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
