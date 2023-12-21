# ClientApplicationExtension.Initialize - метод
Метод, выполняемый при инициализации приложения, когда основные подсистемы уже
инициализированы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task Initialize(
    	IApplicationExtensionContext context
    )
VB __Копировать
     Public Overrides Function Initialize ( 
    	context As IApplicationExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ Initialize(
    	IApplicationExtensionContext^ context
    ) override
F# __Копировать
     abstract Initialize : 
            context : IApplicationExtensionContext -> Task 
    override Initialize : 
            context : IApplicationExtensionContext -> Task 
#### Параметры
context
[IApplicationExtensionContext](T_Tessa_Platform_Runtime_IApplicationExtensionContext.htm)
    Контекст расширения.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationExtension.Initialize(IApplicationExtensionContext)](M_Tessa_Platform_Runtime_IApplicationExtension_Initialize.htm)  
##  __См. также
#### Ссылки
[ClientApplicationExtension -
](T_Tessa_Extensions_Platform_Client_Application_ClientApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)
