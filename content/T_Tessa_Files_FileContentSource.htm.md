# FileContentSource - структура
Местоположение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct FileContentSource : IEquatable<FileContentSource>
VB __Копировать
     Public Structure FileContentSource
    	Implements IEquatable(Of FileContentSource)
C++ __Копировать
     public value class FileContentSource : IEquatable<FileContentSource>
F# __Копировать
     [<SealedAttribute>]
    type FileContentSource = 
        struct
            inherit ValueType
            interface IEquatable<FileContentSource>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ FileContentSource
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<FileContentSource>
##  __Конструкторы
[FileContentSource](M_Tessa_Files_FileContentSource__ctor.htm)|  Создаёт
структуру с указанием источника контента.  
---|---  
## __Свойства
[ID](P_Tessa_Files_FileContentSource_ID.htm)|  Идентификатор источника
контента.  
---|---  
[Name](P_Tessa_Files_FileContentSource_Name.htm)|  Имя для источника контента.  
## __Методы
[Equals(FileContentSource)](M_Tessa_Files_FileContentSource_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Files_FileContentSource_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromCardFileSource](M_Tessa_Files_FileContentSource_FromCardFileSource.htm)|
Создаёт и возвращает объект FileContentSource, полученный для заданного
объекта настроек [ICardFileSource](T_Tessa_Cards_ICardFileSource.htm).  
[GetHashCode](M_Tessa_Files_FileContentSource_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
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
[ToString](M_Tessa_Files_FileContentSource_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(FileContentSource,
FileContentSource)](M_Tessa_Files_FileContentSource_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Inequality(FileContentSource,
FileContentSource)](M_Tessa_Files_FileContentSource_op_Inequality.htm)|
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
