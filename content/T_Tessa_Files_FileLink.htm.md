# FileLink - класс
Ссылка на файл.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileLink : IFileLink, 
    	IEquatable<IFileLink>
VB __Копировать
     Public NotInheritable Class FileLink
    	Implements IFileLink, IEquatable(Of IFileLink)
C++ __Копировать
     public ref class FileLink sealed : IFileLink, 
    	IEquatable<IFileLink^>
F# __Копировать
     [<SealedAttribute>]
    type FileLink = 
        class
            interface IFileLink
            interface IEquatable<IFileLink>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileLink
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileLink](T_Tessa_Files_IFileLink.htm)>, [IFileLink](T_Tessa_Files_IFileLink.htm)
##  __Конструкторы
[FileLink](M_Tessa_Files_FileLink__ctor.htm)|  Создаёт экземпляр класса с
указанием его свойств.  
---|---  
## __Свойства
[FileID](P_Tessa_Files_FileLink_FileID.htm)| Идентификатор файла, на который
делается ссылка.  
---|---  
[Uri](P_Tessa_Files_FileLink_Uri.htm)| Ссылка, используемая для открытия
файла.  
##  __Методы
[Equals(IFileLink)](M_Tessa_Files_FileLink_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Files_FileLink_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileLink_GetHashCode.htm)| Возвращает хеш-код
объекта.  
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
[ToString](M_Tessa_Files_FileLink_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(FileLink, IFileLink)](M_Tessa_Files_FileLink_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Inequality(FileLink, IFileLink)](M_Tessa_Files_FileLink_op_Inequality.htm)|
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
