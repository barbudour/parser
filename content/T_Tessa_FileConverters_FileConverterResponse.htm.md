# FileConverterResponse - класс
Результат конвертации файла с возможностью получить доступ к его контенту.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileConverterResponse : IFileConverterResponse
VB __Копировать
     Public NotInheritable Class FileConverterResponse
    	Implements IFileConverterResponse
C++ __Копировать
     public ref class FileConverterResponse sealed : IFileConverterResponse
F# __Копировать
     [<SealedAttribute>]
    type FileConverterResponse = 
        class
            interface IFileConverterResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterResponse
Implements
    [IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm)
##  __Конструкторы
[FileConverterResponse(Func<CancellationToken, ValueTask<Stream>>, Int64,
Boolean, Boolean, Dictionary<String,
Object>)](M_Tessa_FileConverters_FileConverterResponse__ctor.htm)|  Создаёт
экземпляр класса с указанием функции на получение контента файла. Результат
выполнения операции не будет содержать сообщений.  
---|---  
[FileConverterResponse(ValidationResult, Func<CancellationToken,
ValueTask<Stream>>, Int64, Boolean, Boolean, Dictionary<String,
Object>)](M_Tessa_FileConverters_FileConverterResponse__ctor_1.htm)|  Создаёт
экземпляр класса с указанием значений его свойств и методов.  
## __Свойства
[HasAwaitedResult](P_Tessa_FileConverters_FileConverterResponse_HasAwaitedResult.htm)|
Признак того, что ожидание результата было выполнено и результат был получен
(успешный или с ошибками). Если значение равно false, то метод получения
содержимого файла
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.  
---|---  
[Info](P_Tessa_FileConverters_FileConverterResponse_Info.htm)| Дополнительная
информация, полученная из результатов операции конвертации.  
[IsAcquiredFromCache](P_Tessa_FileConverters_FileConverterResponse_IsAcquiredFromCache.htm)|
Признак того, что результат конвертации был получен из кэша.  
[Size](P_Tessa_FileConverters_FileConverterResponse_Size.htm)|  Размер
содержимого [Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] в
байтах или -1, если содержимое отсутствует или размер неизвестен.  
[ValidationResult](P_Tessa_FileConverters_FileConverterResponse_ValidationResult.htm)|
Результат выполнения операции. Если он содержит ошибки, то метод
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.  
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
[GetStreamOrThrowAsync](M_Tessa_FileConverters_FileConverterResponse_GetStreamOrThrowAsync.htm)|
Возвращает поток с содержимым файла. Возвращённое значение потока не равно
null. В случае ошибок в
[Tessa.FileConverters.IFileConverterResponse.ValidationResult] или в случае,
если ожидание результата не было завершено, т.е.
[Tessa.FileConverters.IFileConverterResponse.HasAwaitedResult] равен false,
выбрасывается исключение.  
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
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
