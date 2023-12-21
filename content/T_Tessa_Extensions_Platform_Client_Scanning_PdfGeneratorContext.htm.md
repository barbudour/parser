# PdfGeneratorContext - класс
Контекст операции по генерации PDF из изображений со страницами. Используется
совместно с
[IPdfGenerator](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PdfGeneratorContext : IPdfGeneratorContext
VB __Копировать
     Public NotInheritable Class PdfGeneratorContext
    	Implements IPdfGeneratorContext
C++ __Копировать
     public ref class PdfGeneratorContext sealed : IPdfGeneratorContext
F# __Копировать
     [<SealedAttribute>]
    type PdfGeneratorContext = 
        class
            interface IPdfGeneratorContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PdfGeneratorContext
Implements
    [IPdfGeneratorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext.htm)
##  __Конструкторы
[PdfGeneratorContext](M_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств и методов.  
---|---  
## __Свойства
[AddStamp](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_AddStamp.htm)|
Признак того, что для документа требуется вывести штамп. При этом формирование
штампа обычно выполняется посредством расширений.  
---|---  
[ExternalContext](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_ExternalContext.htm)|
Контекст, в пределах которого выполняется формирование PDF. Например, может
быть контекстом
[IFileControlExtensionContext](T_Tessa_UI_Files_IFileControlExtensionContext.htm)
или null, если контекст неизвестен.  
[GeneratorInfo](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_GeneratorInfo.htm)|
Информация для расширений, заданная в генераторе, обычно это объект
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm).
Информация недоступна для изменений.  
[Info](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_Info.htm)|
Информация для расширений, существующая в рамках запроса по генерации.  
[PngPageFiles](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_PngPageFiles.htm)|
Файлы изображений в формате PNG со страницами в порядке их добавления. В одном
файле содержится изображение для одной страницы.  
[TemporaryFiles](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_TemporaryFiles.htm)|
Список временных файлов, которые будут гарантированно удалены после завершения
метода.  
[TemporaryFolders](P_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_TemporaryFolders.htm)|
Список временных папок, которые будут гарантированно удалены после завершения
метода.  
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
[ReportProgressAsync](M_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext_ReportProgressAsync.htm)|
Отображает пользователю текущий прогресс операции.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
