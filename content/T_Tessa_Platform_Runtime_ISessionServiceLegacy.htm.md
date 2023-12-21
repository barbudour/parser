# ISessionServiceLegacy - интерфейс
Сервис, управляющий открытыми сессиями.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [ServiceContractAttribute(Name = "ISessionService")]
    [SessionServiceAttribute("tessa/SessionService.svc", TransferMode.Buffered)]
    public interface ISessionServiceLegacy
VB __Копировать
    <ServiceContractAttribute(Name := "ISessionService")>
    <SessionServiceAttribute("tessa/SessionService.svc", TransferMode.Buffered)>
    Public Interface ISessionServiceLegacy
C++ __Копировать
    [ServiceContractAttribute(Name = L"ISessionService")]
    [SessionServiceAttribute(L"tessa/SessionService.svc", TransferMode::Buffered)]
    public interface class ISessionServiceLegacy
F# __Копировать
     [<ServiceContractAttribute(Name = "ISessionService")>]
    [<SessionServiceAttribute("tessa/SessionService.svc", TransferMode.Buffered)>]
    type ISessionServiceLegacy = interface end
##  __Методы
[CloseSession](M_Tessa_Platform_Runtime_ISessionServiceLegacy_CloseSession.htm)|
Закрывает текущую сессию. Закрытие сессии удаляет её, а также может
дополнительно добавить запись в логах аудита или выполнить другие действия.
Возвращает признак того, что сессия ещё была открыта на момент вызова метода.  
---|---  
[CloseSessionAsAdmin](M_Tessa_Platform_Runtime_ISessionServiceLegacy_CloseSessionAsAdmin.htm)|
Закрывает сессию с заданным идентификатором от имени администратора. Закрытие
сессии удаляет её, а также может дополнительно добавить запись в логах аудита
или выполнить другие действия. Возвращает признак того, что сессия ещё была
открыта на момент вызова метода.  
[CloseSessionWithToken](M_Tessa_Platform_Runtime_ISessionServiceLegacy_CloseSessionWithToken.htm)|
Закрывает текущую сессию, причём сессия определяется по токену, передаваемому
в параметре. Закрытие сессии удаляет её, а также может дополнительно добавить
запись в логах аудита или выполнить другие действия. Возвращает признак того,
что сессия ещё была открыта на момент вызова метода.  
[IncrementConfigurationVersion](M_Tessa_Platform_Runtime_ISessionServiceLegacy_IncrementConfigurationVersion.htm)|
Увеличивает версию конфигурации без внесения в неё фактических изменений, а
также обновляет информацию по текущей версии платформы. Может использоваться,
например, для сброса клиентского кэша. Метод доступен только администраторам.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
