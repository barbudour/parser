# IAdExtension.SyncStaticRole - метод
Выполняет синхронизацию статической роли (группы).
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SyncStaticRole(
    	IAdExtensionContext context
    )
VB __Копировать
     Function SyncStaticRole ( 
    	context As IAdExtensionContext
    ) As Task
C++ __Копировать
    Task^ SyncStaticRole(
    	IAdExtensionContext^ context
    )
F# __Копировать
     abstract SyncStaticRole : 
            context : IAdExtensionContext -> Task 
#### Параметры
context
[IAdExtensionContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext.htm)
    Контекст операции по синхронизации. Содержит токен отмены операции.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IAdExtension - ](T_Tessa_Extensions_Platform_Server_AdSync_IAdExtension.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
