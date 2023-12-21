# ApplicationModel - конструктор
Initializes a new instance of the
[ApplicationModel](T_Tessa_Applications_ApplicationModel.htm) class.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationModel(
    	[NotNullAttribute] IApplicationCatalog applicationCatalog,
    	[NotNullAttribute] ApplicationPackage applicationPackage,
    	[NotNullAttribute] LaunchStrategyFactoryDelegate launchStrategyFactory,
    	[NotNullAttribute] IApplicationManagerMessageBus messageBus,
    	[NotNullAttribute] TessaApplicationServiceProxyFactoryDelegate tessaApplicationServiceProxyFactory,
    	[NotNullAttribute] IMessageProvider messageProvider,
    	[NotNullAttribute] ISessionController sessionController
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> applicationCatalog As IApplicationCatalog,
    	<NotNullAttribute> applicationPackage As ApplicationPackage,
    	<NotNullAttribute> launchStrategyFactory As LaunchStrategyFactoryDelegate,
    	<NotNullAttribute> messageBus As IApplicationManagerMessageBus,
    	<NotNullAttribute> tessaApplicationServiceProxyFactory As TessaApplicationServiceProxyFactoryDelegate,
    	<NotNullAttribute> messageProvider As IMessageProvider,
    	<NotNullAttribute> sessionController As ISessionController
    )
C++ __Копировать
     public:
    ApplicationModel(
    	[NotNullAttribute] IApplicationCatalog^ applicationCatalog, 
    	[NotNullAttribute] ApplicationPackage^ applicationPackage, 
    	[NotNullAttribute] LaunchStrategyFactoryDelegate^ launchStrategyFactory, 
    	[NotNullAttribute] IApplicationManagerMessageBus^ messageBus, 
    	[NotNullAttribute] TessaApplicationServiceProxyFactoryDelegate^ tessaApplicationServiceProxyFactory, 
    	[NotNullAttribute] IMessageProvider^ messageProvider, 
    	[NotNullAttribute] ISessionController^ sessionController
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] applicationCatalog : IApplicationCatalog * 
            [<NotNullAttribute>] applicationPackage : ApplicationPackage * 
            [<NotNullAttribute>] launchStrategyFactory : LaunchStrategyFactoryDelegate * 
            [<NotNullAttribute>] messageBus : IApplicationManagerMessageBus * 
            [<NotNullAttribute>] tessaApplicationServiceProxyFactory : TessaApplicationServiceProxyFactoryDelegate * 
            [<NotNullAttribute>] messageProvider : IMessageProvider * 
            [<NotNullAttribute>] sessionController : ISessionController -> ApplicationModel
#### Параметры
applicationCatalog
[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Каталог приложений 
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
launchStrategyFactory
[LaunchStrategyFactoryDelegate](T_Tessa_Applications_LaunchStrategyFactoryDelegate.htm)
     Стратегия запуска приложения 
messageBus
[IApplicationManagerMessageBus](T_Tessa_Applications_Messages_IApplicationManagerMessageBus.htm)
     Шина сообщений 
tessaApplicationServiceProxyFactory
[TessaApplicationServiceProxyFactoryDelegate](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationServiceProxyFactoryDelegate.htm)
     Фабрика создания клиента для подключения к сервису приложений 
messageProvider
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
     Вывод сообщений 
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Управление пользовательской сессией 
## __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
