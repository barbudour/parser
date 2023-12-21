# FileVersionLink - класс
Ссылка на версию файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileVersionLink : IFileVersionLink, 
    	IEquatable<IFileVersionLink>
VB __Копировать
     Public NotInheritable Class FileVersionLink
    	Implements IFileVersionLink, IEquatable(Of IFileVersionLink)
C++ __Копировать
     public ref class FileVersionLink sealed : IFileVersionLink, 
    	IEquatable<IFileVersionLink^>
F# __Копировать
     [<SealedAttribute>]
    type FileVersionLink = 
        class
            interface IFileVersionLink
            interface IEquatable<IFileVersionLink>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileVersionLink
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileVersionLink](T_Tessa_Files_IFileVersionLink.htm)>, [IFileVersionLink](T_Tessa_Files_IFileVersionLink.htm)
##  __Конструкторы
[FileVersionLink](M_Tessa_Files_FileVersionLink__ctor.htm)|  Создаёт экземпляр
класса с указанием его свойств.  
---|---  
## __Свойства
[FileID](P_Tessa_Files_FileVersionLink_FileID.htm)| Идентификатор файла, на
версию которого делается ссылка.  
---|---  
[Uri](P_Tessa_Files_FileVersionLink_Uri.htm)| Ссылка, используемая для
открытия версии файла.  
[VersionID](P_Tessa_Files_FileVersionLink_VersionID.htm)| Идентификатор версии
файла, на которую делается ссылка.  
##  __Методы
[Equals(IFileVersionLink)](M_Tessa_Files_FileVersionLink_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Files_FileVersionLink_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileVersionLink_GetHashCode.htm)| Возвращает хеш-
код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](M_Tessa_Files_FileVersionLink_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(FileVersionLink,
IFileVersionLink)](M_Tessa_Files_FileVersionLink_op_Equality.htm)| Сравнивает
заданные значения на равенство.  
---|---  
[Inequality(FileVersionLink,
IFileVersionLink)](M_Tessa_Files_FileVersionLink_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
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
