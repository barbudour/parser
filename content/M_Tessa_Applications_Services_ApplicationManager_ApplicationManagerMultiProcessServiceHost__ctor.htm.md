# ApplicationManagerMultiProcessServiceHost - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationManagerMultiProcessServiceHost(
    	ILogger logger,
    	params IApplicationManagerServiceHost[] serviceHosts
    )
VB __Копировать
     Public Sub New ( 
    	logger As ILogger,
    	ParamArray serviceHosts As IApplicationManagerServiceHost()
    )
C++ __Копировать
     public:
    ApplicationManagerMultiProcessServiceHost(
    	ILogger^ logger, 
    	... array<IApplicationManagerServiceHost^>^ serviceHosts
    )
F# __Копировать
     new : 
            logger : ILogger * 
            serviceHosts : IApplicationManagerServiceHost[] -> ApplicationManagerMultiProcessServiceHost
#### Параметры
logger ILogger
    Объект, выполняющий логирование.
serviceHosts
[IApplicationManagerServiceHost](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm)[]
    Список объектов, которые последовательно вызываются данным объектом.
##  __См. также
#### Ссылки
[ApplicationManagerMultiProcessServiceHost -
](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
