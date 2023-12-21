# IAdSyncContext.GetCachedGroup - метод
Получает состав закэшированной группы или null если группа не найдена
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     List<Guid> GetCachedGroup(
    	Guid groupId
    )
VB __Копировать
     Function GetCachedGroup ( 
    	groupId As Guid
    ) As List(Of Guid)
C++ __Копировать
    List<Guid>^ GetCachedGroup(
    	Guid groupId
    )
F# __Копировать
     abstract GetCachedGroup : 
            groupId : Guid -> List<Guid> 
#### Параметры
groupId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор группы. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Состав группы или null если группа не найдена.
##  __См. также
#### Ссылки
[IAdSyncContext -
](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
