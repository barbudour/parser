# BusinessProcessCardStoreExtension.BeforeRequest - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeRequest(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeRequest ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardStoreExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeRequest : 
            context : ICardStoreExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeRequest.htm)  
##  __См. также
#### Ссылки
[BusinessProcessCardStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
