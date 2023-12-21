# PdfPageExtractorContext - класс
Контекст операции по разбору файла PDF на страницы. Используется совместно с
[IPdfPageExtractor](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PdfPageExtractorContext : IPdfPageExtractorContext
VB __Копировать
     Public NotInheritable Class PdfPageExtractorContext
    	Implements IPdfPageExtractorContext
C++ __Копировать
     public ref class PdfPageExtractorContext sealed : IPdfPageExtractorContext
F# __Копировать
     [<SealedAttribute>]
    type PdfPageExtractorContext = 
        class
            interface IPdfPageExtractorContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PdfPageExtractorContext
Implements
    [IPdfPageExtractorContext](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext.htm)
##  __Конструкторы
[PdfPageExtractorContext](M_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств и методов.  
---|---  
## __Свойства
[PdfFilePath](P_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext_PdfFilePath.htm)|
Полный путь к файлу PDF.  
---|---  
[PngPageFiles](P_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext_PngPageFiles.htm)|
Массив объектов, которые описывают все извлечённые страницы в виде изображений
PNG.  
[Settings](P_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext_Settings.htm)|
Настройки диалога сканирования, для которых вызывается извлечение страниц.
Может быть равны null, если настройки неизвестны.  
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
[ReportProgressAsync](M_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext_ReportProgressAsync.htm)|
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
