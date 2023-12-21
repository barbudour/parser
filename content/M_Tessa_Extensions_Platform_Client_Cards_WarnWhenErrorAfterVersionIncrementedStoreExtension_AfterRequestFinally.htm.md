# WarnWhenErrorAfterVersionIncrementedStoreExtension.AfterRequestFinally -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequestFinally(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequestFinally ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardStoreExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardStoreExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardStoreExtension.AfterRequestFinally(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterRequestFinally.htm)  
##  __См. также
#### Ссылки
[WarnWhenErrorAfterVersionIncrementedStoreExtension -
](T_Tessa_Extensions_Platform_Client_Cards_WarnWhenErrorAfterVersionIncrementedStoreExtension.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
