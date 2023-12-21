# ScanDocumentType - класс
Тип формируемого документа в окне сканирования/редактирования документов.
Описывает способ генерации объекта
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm)
и внешний вид в выпадающем списке.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScanDocumentType
VB __Копировать
     Public NotInheritable Class ScanDocumentType
C++ __Копировать
     public ref class ScanDocumentType sealed
F# __Копировать
     [<SealedAttribute>]
    type ScanDocumentType = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScanDocumentType
##  __Конструкторы
[ScanDocumentType](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Caption](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Caption.htm)|
Заголовок типа документа. Если не равен null или пустой строке, то он
используется вместо описания имени типа
[Name](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Name.htm)
и тега
[Tag](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Tag.htm).  
---|---  
[DefaultTypes](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_DefaultTypes.htm)|
Типы, используемые в диалоге сканирования/редактирования документов по
умолчанию.  
[Name](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Name.htm)|
Имя формата файла, например, "PDF" или "TIFF". Отображается пользователю, если
заголовок
[Caption](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Caption.htm)
равен null или пустой строке.  
[Pdf](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Pdf.htm)|
Документ PDF без штампа.  
[Tag](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Tag.htm)|
Информация, описывающая тип генерируемого документа и выводимая рядом с именем
документа. Актуальна, если заголовок
[Caption](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Caption.htm)
равен null или пустой строке.  
[Tiff](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_Tiff.htm)|
Документ TIFF.  
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
[GetGenerator](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_GetGenerator.htm)|  
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
