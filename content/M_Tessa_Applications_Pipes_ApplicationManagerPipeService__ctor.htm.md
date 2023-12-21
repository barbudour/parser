# ApplicationManagerPipeService - конструктор
Инициализирует новый экземпляр класса
[ApplicationManagerPipeService](T_Tessa_Applications_Pipes_ApplicationManagerPipeService.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationManagerPipeService(
    	IApplicationManagerMessageBus messageBus,
    	ILinkParser linkParser,
    	ILogger logger,
    	Func<Task<IApplicationCatalogRegistry>> getCatalogsFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	messageBus As IApplicationManagerMessageBus,
    	linkParser As ILinkParser,
    	logger As ILogger,
    	getCatalogsFuncAsync As Func(Of Task(Of IApplicationCatalogRegistry))
    )
C++ __Копировать
     public:
    ApplicationManagerPipeService(
    	IApplicationManagerMessageBus^ messageBus, 
    	ILinkParser^ linkParser, 
    	ILogger^ logger, 
    	Func<Task<IApplicationCatalogRegistry^>^>^ getCatalogsFuncAsync
    )
F# __Копировать
     new : 
            messageBus : IApplicationManagerMessageBus * 
            linkParser : ILinkParser * 
            logger : ILogger * 
            getCatalogsFuncAsync : Func<Task<IApplicationCatalogRegistry>> -> ApplicationManagerPipeService
#### Параметры
messageBus
[IApplicationManagerMessageBus](T_Tessa_Applications_Messages_IApplicationManagerMessageBus.htm)
linkParser [ILinkParser](T_Tessa_Platform_Links_ILinkParser.htm)
logger ILogger
getCatalogsFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IApplicationCatalogRegistry](T_Tessa_Applications_IApplicationCatalogRegistry.htm)>>
## __См. также
#### Ссылки
[ApplicationManagerPipeService -
](T_Tessa_Applications_Pipes_ApplicationManagerPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
