# VirtualFile - класс
Виртуальный файл, указываемый при добавлении.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class VirtualFile
VB __Копировать
     Public NotInheritable Class VirtualFile
C++ __Копировать
     public ref class VirtualFile sealed
F# __Копировать
     [<SealedAttribute>]
    type VirtualFile = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ VirtualFile
##  __Конструкторы
[VirtualFile(String, String, Func<IFileCreationToken, CancellationToken,
ValueTask>, Dictionary<String,
Object>)](M_Tessa_Files_VirtualFile__ctor_1.htm)|  Создаёт экземпляр класса с
указанием значений его свойств и методов. Идентификатор файла генерируется.  
---|---  
[VirtualFile(String, Guid, String, Func<IFileCreationToken, CancellationToken,
ValueTask>, Dictionary<String, Object>)](M_Tessa_Files_VirtualFile__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств и методов.  
## __Свойства
[ID](P_Tessa_Files_VirtualFile_ID.htm)|  Идентификатор файла.  
---|---  
[Name](P_Tessa_Files_VirtualFile_Name.htm)|  Имя файла (указывается вместе с
расширением).  
[RequestInfo](P_Tessa_Files_VirtualFile_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы на загрузку содержимого
версий этого файла, на загрузку списка версий и на загрузку списка подписей
для версий этого файла.  
[TypeName](P_Tessa_Files_VirtualFile_TypeName.htm)|  Имя виртуального типа
файла. На каждый виртуальный файл рекомендуется указывать уникальную строку с
именем типом.  
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
[ModifyAsync](M_Tessa_Files_VirtualFile_ModifyAsync.htm)|  Изменяет токен
создаваемого файла в соответствии с настройками текущего объекта.  
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
