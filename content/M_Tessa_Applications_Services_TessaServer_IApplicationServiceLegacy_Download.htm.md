# IApplicationServiceLegacy.Download - метод
Операция скачивания приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    [OperationContractAttribute]
    Stream Download(
    	[NotNullAttribute] ApplicationDownloadRequest request
    )
VB __Копировать
    <NotNullAttribute>
    <OperationContractAttribute>
    Function Download ( 
    	<NotNullAttribute> request As ApplicationDownloadRequest
    ) As Stream
C++ __Копировать
    [NotNullAttribute]
    [OperationContractAttribute]
    Stream^ Download(
    	[NotNullAttribute] ApplicationDownloadRequest^ request
    )
F# __Копировать
     [<NotNullAttribute>]
    [<OperationContractAttribute>]
    abstract Download : 
            [<NotNullAttribute>] request : ApplicationDownloadRequest -> Stream 
#### Параметры
request
[ApplicationDownloadRequest](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadRequest.htm)
     Запрос к сервису содержащий параметры приложения запрашиваемого к загрузке на клиента. 
#### Возвращаемое значение
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)  
Поток содержащий результаты обработки запроса request
##  __См. также
#### Ссылки
[IApplicationServiceLegacy -
](T_Tessa_Applications_Services_TessaServer_IApplicationServiceLegacy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
