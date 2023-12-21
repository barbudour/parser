# DefaultPdfGenerator - класс
Объект, выполняющий формирование файла PDF из страниц с изображениями PNG. По
умолчанию используется библиотека PdfSharp.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Pdf](N_Tessa_Extensions_Default_Client_Pdf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultPdfGenerator : IPdfGenerator
VB __Копировать
     Public Class DefaultPdfGenerator
    	Implements IPdfGenerator
C++ __Копировать
     public ref class DefaultPdfGenerator : IPdfGenerator
F# __Копировать
     type DefaultPdfGenerator = 
        class
            interface IPdfGenerator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultPdfGenerator
Implements
    [IPdfGenerator](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm)
##  __Конструкторы
[DefaultPdfGenerator](M_Tessa_Extensions_Default_Client_Pdf_DefaultPdfGenerator__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей из Unity.  
---|---  
## __Методы
[CreateStampWriterAsync](M_Tessa_Extensions_Default_Client_Pdf_DefaultPdfGenerator_CreateStampWriterAsync.htm)|
Создаёт объект
[PdfStampWriter](T_Tessa_Extensions_Default_Client_Pdf_PdfStampWriter.htm),
используемый для наложения штампа.  
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
[TryGenerateAsync](M_Tessa_Extensions_Default_Client_Pdf_DefaultPdfGenerator_TryGenerateAsync.htm)|
Формирует документ PDF в виде
[ScanDocument](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocument.htm).
Возвращает null, если формирование документа не удалось.  
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
[Tessa.Extensions.Default.Client.Pdf - пространство
имён](N_Tessa_Extensions_Default_Client_Pdf.htm)
