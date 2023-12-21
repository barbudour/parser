# PdfScanDocumentGenerator - класс
Объект, управляющий генерацией документов PDF.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class PdfScanDocumentGenerator : ScanDocumentGenerator
VB __Копировать
     Public Class PdfScanDocumentGenerator
    	Inherits ScanDocumentGenerator
C++ __Копировать
     public ref class PdfScanDocumentGenerator : public ScanDocumentGenerator
F# __Копировать
     type PdfScanDocumentGenerator = 
        class
            inherit ScanDocumentGenerator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm) __ PdfScanDocumentGenerator
##  __Конструкторы
[PdfScanDocumentGenerator](M_Tessa_Extensions_Platform_Client_Scanning_PdfScanDocumentGenerator__ctor.htm)|
Создаёт экземпляр класса с указанием дополнительных параметров, связанных с
генерацией документов.  
---|---  
## __Свойства
[AddStamp](P_Tessa_Extensions_Platform_Client_Scanning_PdfScanDocumentGenerator_AddStamp.htm)|
Признак того, что при генерации документа должен быть добавлен штамп.  
---|---  
[Info](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator_Info.htm)|
Дополнительные параметры, связанные с генерацией документов, могут
использоваться в расширениях. Объект защищён от изменений, его свойства нельзя
изменять динамически.  
(Унаследован от
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm))  
[UnityContainer](P_Tessa_Extensions_Platform_Client_Scanning_PdfScanDocumentGenerator_UnityContainer.htm)|
Контейнер Unity, содержащий зависимости для обработки PDF.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[TryGenerateAsync](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator_TryGenerateAsync.htm)|  
(Унаследован от
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm))  
[TryGenerateCoreAsync](M_Tessa_Extensions_Platform_Client_Scanning_PdfScanDocumentGenerator_TryGenerateCoreAsync.htm)|  
(Переопределяет [ScanDocumentGenerator.TryGenerateCoreAsync(ITempFile[],
List<ITempFile>, List<ITempFolder>, Func<Double, CancellationToken, Task>,
Object, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator_TryGenerateCoreAsync.htm))  
##  __Методы расширения
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
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
