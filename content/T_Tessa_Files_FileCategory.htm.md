# FileCategory - класс
Категория файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileCategory : IFileCategory, 
    	IEquatable<IFileCategory>
VB __Копировать
     Public Class FileCategory
    	Implements IFileCategory, IEquatable(Of IFileCategory)
C++ __Копировать
     public ref class FileCategory : IFileCategory, 
    	IEquatable<IFileCategory^>
F# __Копировать
     type FileCategory = 
        class
            interface IFileCategory
            interface IEquatable<IFileCategory>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileCategory
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileCategory](T_Tessa_Files_IFileCategory.htm)>, [IFileCategory](T_Tessa_Files_IFileCategory.htm)
##  __Заметки
Наследники класса могут определять дополнительные свойства, специфичные для
категории файла, которая относится к определённой подсистеме, такой как
карточки.
## __Конструкторы
[FileCategory](M_Tessa_Files_FileCategory__ctor.htm)|  Создаёт экземпляр
класса с указанием значений его свойств.  
---|---  
## __Свойства
[Caption](P_Tessa_Files_FileCategory_Caption.htm)|  Отображаемое имя типа
файла, которое видит пользователь. Не может быть равно null, пустой строке или
строке, состоящей из пробелов.  
---|---  
[ID](P_Tessa_Files_FileCategory_ID.htm)| Уникальный идентификатор типа файла.  
##  __Методы
[Equals(IFileCategory)](M_Tessa_Files_FileCategory_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Files_FileCategory_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileCategory_GetHashCode.htm)| Возвращает хеш-код
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
[ToString](M_Tessa_Files_FileCategory_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(FileCategory,
IFileCategory)](M_Tessa_Files_FileCategory_op_Equality.htm)| Сравнивает
заданные значения на равенство.  
---|---  
[Inequality(FileCategory,
IFileCategory)](M_Tessa_Files_FileCategory_op_Inequality.htm)| Сравнивает
заданные значения на неравенство.  
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
