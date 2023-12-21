# FileConverterAnyOutputFormatPolicy - класс
Политика, определяющая допустимость любого выходного формата по конвертации
файлов для выполнения методов расширения. Может быть использована для
замещения другой политики
[IFileConverterOutputFormatPolicy](T_Tessa_FileConverters_IFileConverterOutputFormatPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverterAnyOutputFormatPolicy : IFileConverterOutputFormatPolicy, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class FileConverterAnyOutputFormatPolicy
    	Implements IFileConverterOutputFormatPolicy, IExtensionPolicy
C++ __Копировать
     public ref class FileConverterAnyOutputFormatPolicy sealed : IFileConverterOutputFormatPolicy, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type FileConverterAnyOutputFormatPolicy = 
        class
            interface IFileConverterOutputFormatPolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterAnyOutputFormatPolicy
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFileConverterOutputFormatPolicy](T_Tessa_FileConverters_IFileConverterOutputFormatPolicy.htm)
##  __Заметки
Для использования этой политики требуется зарегистрировать политику
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm).
## __Конструкторы
[FileConverterAnyOutputFormatPolicy](M_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterAnyOutputFormatPolicy  
---|---  
##  __Свойства
[Instance](P_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy_Instance.htm)|
Экземпляр класса.  
---|---  
[IsAllowAny](P_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые выходные форматы файлов, в том
числе неизвестные на момент фильтрации.  
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
[IsAllowed](M_Tessa_FileConverters_FileConverterAnyOutputFormatPolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного выходного формата по конвертации файлов.  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)