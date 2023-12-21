# IApplicationDownloader - интерфейс
Объект, обеспечивающий скачивание приложений.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationDownloader
VB __Копировать
     Public Interface IApplicationDownloader
C++ __Копировать
     public interface class IApplicationDownloader
F# __Копировать
     type IApplicationDownloader = interface end
##  __Методы
[GetApplicationStreamAsync](M_Tessa_Applications_Services_TessaServer_IApplicationDownloader_GetApplicationStreamAsync.htm)|
Создает и возвращает поток содержащий неизменные файлы приложения  
---|---  
[TryGetFaultedResultAsync](M_Tessa_Applications_Services_TessaServer_IApplicationDownloader_TryGetFaultedResultAsync.htm)|
Возвращает ошибки при скачивании приложения как объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), или
null, если информация недоступна: ошибок не было или пользователь не имеет
доступа к этой записи в истории.  
## __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
