# FileConverterFormat - структура
Формат файла, в который выполняется конвертация.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct FileConverterFormat : IEquatable<FileConverterFormat>
VB __Копировать
     Public Structure FileConverterFormat
    	Implements IEquatable(Of FileConverterFormat)
C++ __Копировать
     public value class FileConverterFormat : IEquatable<FileConverterFormat>
F# __Копировать
     [<SealedAttribute>]
    type FileConverterFormat = 
        struct
            inherit ValueType
            interface IEquatable<FileConverterFormat>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ FileConverterFormat
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<FileConverterFormat>
##  __Заметки
При создании формата файла зарегистрируйте его расширения посредством методов
[RegisterExtensions(FileConverterFormat, String, IEnumerable<String>,
IEnumerable<String>)](M_Tessa_FileConverters_FileConverterFormat_RegisterExtensions.htm).
Рекомендуется это сделать статическом конструкторе класса, в котором объявлено
поле с форматом файла.
## __Конструкторы
[FileConverterFormat](M_Tessa_FileConverters_FileConverterFormat__ctor.htm)|
Создаёт экземпляр структуры для формата файла.  
---|---  
## __Свойства
[ID](P_Tessa_FileConverters_FileConverterFormat_ID.htm)|  Идентификатор
формата файла.  
---|---  
[ResolveKey](P_Tessa_FileConverters_FileConverterFormat_ResolveKey.htm)|  Ключ
для использования в регистрациях контейнера IUnityContainer.  
## __Методы
[Equals(FileConverterFormat)](M_Tessa_FileConverters_FileConverterFormat_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_FileConverters_FileConverterFormat_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAdditionalInputFormats](M_Tessa_FileConverters_FileConverterFormat_GetAdditionalInputFormats.htm)|
Возвращает дополнительные поддерживаемые типы файлов для конвертации, из
которых может быть выполнена конвертация в заданный формат. Не рекомендуется
выполнять конвертацию с использованием этого формата, но конвертация возможна,
если возникла необходимость.  
[GetExtension](M_Tessa_FileConverters_FileConverterFormat_GetExtension.htm)|
Возвращает расширение файла без точки или пустую строку, если для формата не
зарегистрировано расширение посредством метода
[RegisterExtensions(FileConverterFormat, String, IEnumerable<String>,
IEnumerable<String>)](M_Tessa_FileConverters_FileConverterFormat_RegisterExtensions.htm).  
[GetHashCode](M_Tessa_FileConverters_FileConverterFormat_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
[GetRecommendedInputFormats](M_Tessa_FileConverters_FileConverterFormat_GetRecommendedInputFormats.htm)|
Возвращает список рекомендуемых поддерживаемых форматов, из которых может быть
выполнена конвертация в заданный формат.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsSupportedConversion](M_Tessa_FileConverters_FileConverterFormat_IsSupportedConversion.htm)|
Возвращает признак того, что конвертация допустима для заданных форматов.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterExtensions](M_Tessa_FileConverters_FileConverterFormat_RegisterExtensions.htm)|
Регистрирует информацию по входным расширениям для заданного формата выходного
файла. Если заданы null или пустые массивы для обоих параметров, то
конвертация будет допустима для любых входных файлов.  
[ToString](M_Tessa_FileConverters_FileConverterFormat_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(FileConverterFormat,
FileConverterFormat)](M_Tessa_FileConverters_FileConverterFormat_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Explicit(FileConverterFormat to
Guid)](M_Tessa_FileConverters_FileConverterFormat_op_Explicit_1.htm)|  
[Explicit(Guid to
FileConverterFormat)](M_Tessa_FileConverters_FileConverterFormat_op_Explicit.htm)|  
[Inequality(FileConverterFormat,
FileConverterFormat)](M_Tessa_FileConverters_FileConverterFormat_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
##  __Поля
[Pdf](F_Tessa_FileConverters_FileConverterFormat_Pdf.htm)|  Формат файла PDF.  
---|---  
[Unknown](F_Tessa_FileConverters_FileConverterFormat_Unknown.htm)|  Не
заданный формат файла. При попытке выполнить его конвертацию будет ошибка.  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
