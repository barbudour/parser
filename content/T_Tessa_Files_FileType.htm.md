# FileType - класс
Тип файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileType : IFileType, IEquatable<IFileType>
VB __Копировать
     Public Class FileType
    	Implements IFileType, IEquatable(Of IFileType)
C++ __Копировать
     public ref class FileType : IFileType, 
    	IEquatable<IFileType^>
F# __Копировать
     type FileType = 
        class
            interface IFileType
            interface IEquatable<IFileType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileType
Derived
[Tessa.Cards.CardFileType](T_Tessa_Cards_CardFileType.htm)
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileType](T_Tessa_Files_IFileType.htm)>, [IFileType](T_Tessa_Files_IFileType.htm)
##  __Заметки
Наследники класса могут определять дополнительные свойства, специфичные для
типа файла, который относится к определённой подсистеме, такой как карточки.
## __Конструкторы
[FileType](M_Tessa_Files_FileType__ctor.htm)|  Создаёт экземпляр класса с
указанием значений его свойств.  
---|---  
## __Свойства
[Caption](P_Tessa_Files_FileType_Caption.htm)|  Отображаемое имя типа файла,
которое видит пользователь. Не может быть равно null, пустой строке или
строке, состоящей из пробелов.  
---|---  
[ID](P_Tessa_Files_FileType_ID.htm)| Уникальный идентификатор типа файла.  
##  __Методы
[Equals(IFileType)](M_Tessa_Files_FileType_Equals_1.htm)| Сравнивает текущий
объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Files_FileType_Equals.htm)| Сравнивает текущий объект
с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileType_GetHashCode.htm)| Возвращает хеш-код
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
[ToString](M_Tessa_Files_FileType_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(FileType, IFileType)](M_Tessa_Files_FileType_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Inequality(FileType, IFileType)](M_Tessa_Files_FileType_op_Inequality.htm)|
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
