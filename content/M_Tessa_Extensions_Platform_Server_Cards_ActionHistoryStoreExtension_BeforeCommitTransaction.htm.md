# ActionHistoryStoreExtension.BeforeCommitTransaction - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeCommitTransaction(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeCommitTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeCommitTransaction(
    	ICardStoreExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeCommitTransaction : 
            context : ICardStoreExtensionContext -> Task 
    override BeforeCommitTransaction : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm)  
##  __См. также
#### Ссылки
[ActionHistoryStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
