# KrClientAndConsoleInitializationExtension.AfterRequest - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Initialization](N_Tessa_Extensions_Default_Shared_Initialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	IClientInitializationExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As IClientInitializationExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	IClientInitializationExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : IClientInitializationExtensionContext -> Task 
    override AfterRequest : 
            context : IClientInitializationExtensionContext -> Task 
#### Параметры
context
[IClientInitializationExtensionContext](T_Tessa_Platform_Initialization_IClientInitializationExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[IClientInitializationExtension.AfterRequest(IClientInitializationExtensionContext)](M_Tessa_Platform_Initialization_IClientInitializationExtension_AfterRequest.htm)  
##  __См. также
#### Ссылки
[KrClientAndConsoleInitializationExtension -
](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm)
[Tessa.Extensions.Default.Shared.Initialization - пространство
имён](N_Tessa_Extensions_Default_Shared_Initialization.htm)
