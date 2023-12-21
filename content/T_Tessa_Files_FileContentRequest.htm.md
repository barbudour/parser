# FileContentRequest - класс
Запрос на загрузку содержимого файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileContentRequest : IFileContentRequest
VB __Копировать
     Public Class FileContentRequest
    	Implements IFileContentRequest
C++ __Копировать
     public ref class FileContentRequest : IFileContentRequest
F# __Копировать
     type FileContentRequest = 
        class
            interface IFileContentRequest
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileContentRequest
Implements
    [IFileContentRequest](T_Tessa_Files_IFileContentRequest.htm)
##  __Конструкторы
[FileContentRequest](M_Tessa_Files_FileContentRequest__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Info](P_Tessa_Files_FileContentRequest_Info.htm)|  Информация для расширений.
Информация может быть не сериализуемой. В стандартной реализации [IFileSource]
информация не используется.  
---|---  
[ProcessContentActionAsync](P_Tessa_Files_FileContentRequest_ProcessContentActionAsync.htm)|
Метод, которому передаётся полученный из внешней подсистемы контент и который
должен его обработать, например, записать в локальный кэш. Если при загрузке
происходит ошибка, то метод может быть ни разу не вызван. Делегат может быть
равен null.  
[RequestInfo](P_Tessa_Files_FileContentRequest_RequestInfo.htm)|
Сериализуемые данные, которые будут записаны в объект запроса request.Info,
отправляемый к серверу (в типовом сценарии). Такие данные могут перезаписать
данные из [IFileObject.RequestInfo].  
[Version](P_Tessa_Files_FileContentRequest_Version.htm)| Версия файла, для
которой требуется получить контент.  
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
