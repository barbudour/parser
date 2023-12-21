# ApplicationServiceBinaryClient.GetDownloadReaderFlags - метод
Возвращает флаги, которые необходимо добавить при чтении пакета посредством
[ApplicationPackageReader](T_Tessa_Applications_Synchronization_ApplicationPackageReader.htm)
из потока, полученного в результате десериализации
[DownloadAsync(ApplicationDownloadRequest, ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm).
Обычно это флаг
[PackageBinarySerialization](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
при подключении к веб-сервису предыдущей версии платформы. Со стороны сервера
всегда возвращает
[None](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationDownloadFlags GetDownloadReaderFlags()
VB __Копировать
     Public Function GetDownloadReaderFlags As ApplicationDownloadFlags
C++ __Копировать
     public:
    virtual ApplicationDownloadFlags GetDownloadReaderFlags() sealed
F# __Копировать
     abstract GetDownloadReaderFlags : unit -> ApplicationDownloadFlags 
    override GetDownloadReaderFlags : unit -> ApplicationDownloadFlags 
#### Возвращаемое значение
[ApplicationDownloadFlags](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)  
Флаги для чтения из потока, возвращённого в
[DownloadAsync(ApplicationDownloadRequest, ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm).
#### Реализации
[IApplicationService.GetDownloadReaderFlags()](M_Tessa_Applications_Services_TessaServer_IApplicationService_GetDownloadReaderFlags.htm)  
##  __См. также
#### Ссылки
[ApplicationServiceBinaryClient -
](T_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
