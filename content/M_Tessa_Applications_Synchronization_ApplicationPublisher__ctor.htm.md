# ApplicationPublisher - конструктор
Initializes a new instance of the
[ApplicationPublisher](T_Tessa_Applications_Synchronization_ApplicationPublisher.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPublisher(
    	[NotNullAttribute] IApplicationDescriptor applicationDescriptor,
    	[NotNullAttribute] IApplicationSynchronizer applicationSynchronizer,
    	[NotNullAttribute] Func<IAssemblySynchronizationSource> sourceFactory,
    	[NotNullAttribute] Func<ICardSynchronizationTarget> targetFactory,
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] IMessageProvider messageProvider
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> applicationDescriptor As IApplicationDescriptor,
    	<NotNullAttribute> applicationSynchronizer As IApplicationSynchronizer,
    	<NotNullAttribute> sourceFactory As Func(Of IAssemblySynchronizationSource),
    	<NotNullAttribute> targetFactory As Func(Of ICardSynchronizationTarget),
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> messageProvider As IMessageProvider
    )
C++ __Копировать
     public:
    ApplicationPublisher(
    	[NotNullAttribute] IApplicationDescriptor^ applicationDescriptor, 
    	[NotNullAttribute] IApplicationSynchronizer^ applicationSynchronizer, 
    	[NotNullAttribute] Func<IAssemblySynchronizationSource^>^ sourceFactory, 
    	[NotNullAttribute] Func<ICardSynchronizationTarget^>^ targetFactory, 
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] IMessageProvider^ messageProvider
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] applicationDescriptor : IApplicationDescriptor * 
            [<NotNullAttribute>] applicationSynchronizer : IApplicationSynchronizer * 
            [<NotNullAttribute>] sourceFactory : Func<IAssemblySynchronizationSource> * 
            [<NotNullAttribute>] targetFactory : Func<ICardSynchronizationTarget> * 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] messageProvider : IMessageProvider -> ApplicationPublisher
#### Параметры
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
     Описатель приложения 
applicationSynchronizer
[IApplicationSynchronizer](T_Tessa_Applications_Synchronization_IApplicationSynchronizer.htm)
     Синхронизатор приложения 
sourceFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IAssemblySynchronizationSource](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)>
     Фабрика получения источника синхронизации 
targetFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardSynchronizationTarget](T_Tessa_Applications_Synchronization_ICardSynchronizationTarget.htm)>
     Фабрика получения целевого объекта синхронизации 
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Контроллер управляющий сессией приложения 
messageProvider
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
     Объект, обеспечивающий вывод сообщений 
## __См. также
#### Ссылки
[ApplicationPublisher -
](T_Tessa_Applications_Synchronization_ApplicationPublisher.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
