# ApplicationMessageBus - конструктор
Initializes a new instance of the
[ApplicationMessageBus](T_Tessa_Applications_Messages_ApplicationMessageBus.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationMessageBus(
    	[NotNullAttribute] ILogger logger,
    	[NotNullAttribute] ApplicationManagerServiceProxyFactoryDelegate proxyFactory,
    	[NotNullAttribute] ITessaApplicationServiceHost applicationServiceHost,
    	[NotNullAttribute] IMessageProvider messageProvider,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> logger As ILogger,
    	<NotNullAttribute> proxyFactory As ApplicationManagerServiceProxyFactoryDelegate,
    	<NotNullAttribute> applicationServiceHost As ITessaApplicationServiceHost,
    	<NotNullAttribute> messageProvider As IMessageProvider,
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    ApplicationMessageBus(
    	[NotNullAttribute] ILogger^ logger, 
    	[NotNullAttribute] ApplicationManagerServiceProxyFactoryDelegate^ proxyFactory, 
    	[NotNullAttribute] ITessaApplicationServiceHost^ applicationServiceHost, 
    	[NotNullAttribute] IMessageProvider^ messageProvider, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] logger : ILogger * 
            [<NotNullAttribute>] proxyFactory : ApplicationManagerServiceProxyFactoryDelegate * 
            [<NotNullAttribute>] applicationServiceHost : ITessaApplicationServiceHost * 
            [<NotNullAttribute>] messageProvider : IMessageProvider * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> ApplicationMessageBus
#### Параметры
logger ILogger
     Логгер 
proxyFactory
[ApplicationManagerServiceProxyFactoryDelegate](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerServiceProxyFactoryDelegate.htm)
     Фабрика создания прокси-клиента для WCF-сервиса предоставляемого диспетчером приложений 
applicationServiceHost
[ITessaApplicationServiceHost](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost.htm)
     Управление WCF-сервисом приложения. 
messageProvider
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
     Сервис диалоговых окон. 
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
##  __См. также
#### Ссылки
[ApplicationMessageBus -
](T_Tessa_Applications_Messages_ApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
