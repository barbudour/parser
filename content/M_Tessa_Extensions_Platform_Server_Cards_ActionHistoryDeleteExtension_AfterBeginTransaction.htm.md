# ActionHistoryDeleteExtension.AfterBeginTransaction - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterBeginTransaction(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterBeginTransaction ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterBeginTransaction(
    	ICardDeleteExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterBeginTransaction : 
            context : ICardDeleteExtensionContext -> Task 
    override AfterBeginTransaction : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardDeleteExtension.AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)  
##  __См. также
#### Ссылки
[ActionHistoryDeleteExtension -
](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
