# AdSyncCardStoreExtension.AfterBeginTransaction - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterBeginTransaction(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterBeginTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterBeginTransaction(
    	ICardStoreExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterBeginTransaction : 
            context : ICardStoreExtensionContext -> Task 
    override AfterBeginTransaction : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardStoreExtension.AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterBeginTransaction.htm)  
##  __См. также
#### Ссылки
[AdSyncCardStoreExtension -
](T_Tessa_Extensions_Platform_Server_AdSync_AdSyncCardStoreExtension.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
