# FileContentResponse - класс
Ответ на запрос на получение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileContentResponse : IFileContentResponse
VB __Копировать
     Public NotInheritable Class FileContentResponse
    	Implements IFileContentResponse
C++ __Копировать
     public ref class FileContentResponse sealed : IFileContentResponse
F# __Копировать
     [<SealedAttribute>]
    type FileContentResponse = 
        class
            interface IFileContentResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileContentResponse
Implements
    [IFileContentResponse](T_Tessa_Files_IFileContentResponse.htm)
##  __Конструкторы
[FileContentResponse](M_Tessa_Files_FileContentResponse__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Info](P_Tessa_Files_FileContentResponse_Info.htm)|  Информация для
расширений. Информация может быть не сериализуемой. В стандартной реализации
[IFileSource] информация не используется.  
---|---  
[ResponseInfo](P_Tessa_Files_FileContentResponse_ResponseInfo.htm)|  Данные,
которые были записаны из ответа на запрос response.Info, который получен от
сервера (в типовом сценарии).  
[SuggestedFileName](P_Tessa_Files_FileContentResponse_SuggestedFileName.htm)|
Предпочитаемое название загруженного файла или null, если название не
изменяется относительно заданного в версии.  
[ValidationResult](P_Tessa_Files_FileContentResponse_ValidationResult.htm)|
Результат валидации, отражающий произошедшие события и ошибки в процессе
выполнения запроса.  
[Version](P_Tessa_Files_FileContentResponse_Version.htm)| Версия файла, для
которой был выполнен запрос.  
##  __Методы
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
