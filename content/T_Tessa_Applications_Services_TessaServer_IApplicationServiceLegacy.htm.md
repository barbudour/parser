# IApplicationServiceLegacy - интерфейс
Сервис для инициализации приложения с передачей приложению всех данных,
требуемых для его работы.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [ServiceContractAttribute(Name = "IApplicationService")]
    [SessionServiceAttribute("tessa/ApplicationService.svc", TransferMode.Streamed)]
    public interface IApplicationServiceLegacy
VB __Копировать
    <ServiceContractAttribute(Name := "IApplicationService")>
    <SessionServiceAttribute("tessa/ApplicationService.svc", TransferMode.Streamed)>
    Public Interface IApplicationServiceLegacy
C++ __Копировать
    [ServiceContractAttribute(Name = L"IApplicationService")]
    [SessionServiceAttribute(L"tessa/ApplicationService.svc", TransferMode::Streamed)]
    public interface class IApplicationServiceLegacy
F# __Копировать
     [<ServiceContractAttribute(Name = "IApplicationService")>]
    [<SessionServiceAttribute("tessa/ApplicationService.svc", TransferMode.Streamed)>]
    type IApplicationServiceLegacy = interface end
##  __Методы
[Download](M_Tessa_Applications_Services_TessaServer_IApplicationServiceLegacy_Download.htm)|
Операция скачивания приложения.  
---|---  
[ResolveFailResult](M_Tessa_Applications_Services_TessaServer_IApplicationServiceLegacy_ResolveFailResult.htm)|
Возвращает ошибки при скачивании приложения как объект [!:ValidationResult],
сериализованный в виде массива байт, или null, либо пустой массив, если
информация недоступна: ошибок не было или пользователь не имеет доступа к этой
записи в истории.  
## __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
