# ApplicationServiceBinaryClient - класс
Сервис для инициализации приложения с передачей приложению всех данных,
требуемых для его работы. Использует бинарную сериализацию.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationServiceBinaryClient : IApplicationService
VB __Копировать
     Public NotInheritable Class ApplicationServiceBinaryClient
    	Implements IApplicationService
C++ __Копировать
     public ref class ApplicationServiceBinaryClient sealed : IApplicationService
F# __Копировать
     [<SealedAttribute>]
    type ApplicationServiceBinaryClient = 
        class
            interface IApplicationService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationServiceBinaryClient
Implements
    [IApplicationService](T_Tessa_Applications_Services_TessaServer_IApplicationService.htm)
##  __Конструкторы
[ApplicationServiceBinaryClient](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[DownloadAsync](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_DownloadAsync.htm)|
Операция скачивания приложения.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetApplicationsAsync](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_GetApplicationsAsync.htm)|
Возвращает список всех приложений, доступных пользователю.  
[GetDownloadReaderFlags](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_GetDownloadReaderFlags.htm)|
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetApplicationIdAsync](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_TryGetApplicationIdAsync.htm)|
Осуществляет попытку получения идентификатора приложения по его алиасу.  
[TryGetFaultedResultAsync](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_TryGetFaultedResultAsync.htm)|
Возвращает ошибки при скачивании приложения как объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) или null,
если информация недоступна: ошибок не было или пользователь не имеет доступа к
этой записи в истории.  
[TryGetModifiedAsync](M_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient_TryGetModifiedAsync.htm)|
Возвращает дату изменения приложения и признак того, что приложение является
64-битным.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
