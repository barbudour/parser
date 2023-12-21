# StreamSynchronizationSource - конструктор
Initializes a new instance of the
[StreamSynchronizationSource](T_Tessa_Applications_Synchronization_StreamSynchronizationSource.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public StreamSynchronizationSource(
    	[NotNullAttribute] Func<IApplicationService> applicationServiceFunc,
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] ILogger logger
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> applicationServiceFunc As Func(Of IApplicationService),
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> logger As ILogger
    )
C++ __Копировать
     public:
    StreamSynchronizationSource(
    	[NotNullAttribute] Func<IApplicationService^>^ applicationServiceFunc, 
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] ILogger^ logger
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] applicationServiceFunc : Func<IApplicationService> * 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] logger : ILogger -> StreamSynchronizationSource
#### Параметры
applicationServiceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IApplicationService](T_Tessa_Applications_Services_TessaServer_IApplicationService.htm)>
     Функция получения прокси-клиента для сервиса приложений 
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Контроллер управления сессиями 
logger ILogger
     Логгер событий приложения 
## __См. также
#### Ссылки
[StreamSynchronizationSource -
](T_Tessa_Applications_Synchronization_StreamSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
