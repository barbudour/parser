# BusinessProcessSetIsDefaultRequestExtension.BeforeRequest - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Workflow](N_Tessa_Extensions_Platform_Server_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeRequest(
    	ICardRequestExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeRequest ( 
    	context As ICardRequestExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardRequestExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeRequest : 
            context : ICardRequestExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardRequestExtensionContext -> Task 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardRequestExtension.BeforeRequest(ICardRequestExtensionContext)](M_Tessa_Cards_Extensions_ICardRequestExtension_BeforeRequest.htm)  
##  __См. также
#### Ссылки
[BusinessProcessSetIsDefaultRequestExtension -
](T_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessSetIsDefaultRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Server_Workflow.htm)
