# FileFinalizationApplicationExtension.Shutdown - метод
Метод, выполняемый при завершении работы приложения.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task Shutdown(
    	IApplicationExtensionContext context
    )
VB __Копировать
     Public Overrides Function Shutdown ( 
    	context As IApplicationExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ Shutdown(
    	IApplicationExtensionContext^ context
    ) override
F# __Копировать
     abstract Shutdown : 
            context : IApplicationExtensionContext -> Task 
    override Shutdown : 
            context : IApplicationExtensionContext -> Task 
#### Параметры
context
[IApplicationExtensionContext](T_Tessa_Platform_Runtime_IApplicationExtensionContext.htm)
    Контекст расширения.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationExtension.Shutdown(IApplicationExtensionContext)](M_Tessa_Platform_Runtime_IApplicationExtension_Shutdown.htm)  
##  __См. также
#### Ссылки
[FileFinalizationApplicationExtension -
](T_Tessa_Extensions_Platform_Client_Application_FileFinalizationApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)
