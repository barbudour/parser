# ErrorFile - класс
Файл, связанный с ошибкой.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ErrorFile : IErrorFile
VB __Копировать
     Public NotInheritable Class ErrorFile
    	Implements IErrorFile
C++ __Копировать
     public ref class ErrorFile sealed : IErrorFile
F# __Копировать
     [<SealedAttribute>]
    type ErrorFile = 
        class
            interface IErrorFile
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ErrorFile
Implements
    [IErrorFile](T_Tessa_Platform_Runtime_IErrorFile.htm)
##  __Конструкторы
[ErrorFile(String, Byte[],
Nullable<Guid>)](M_Tessa_Platform_Runtime_ErrorFile__ctor.htm)|  Создаёт
экземпляр класса с указанием контента в виде массива байт.  
---|---  
[ErrorFile(String, Int64, Func<CancellationToken, ValueTask<Stream>>,
Nullable<Guid>)](M_Tessa_Platform_Runtime_ErrorFile__ctor_1.htm)|  Создаёт
экземпляр класса с указанием функции, которая возвращает контент файла.  
[ErrorFile(String, String, Encoding,
Nullable<Guid>)](M_Tessa_Platform_Runtime_ErrorFile__ctor_2.htm)|  Создаёт
экземпляр класса с указанием контента в виде текста в заданной кодировке.  
## __Свойства
[ID](P_Tessa_Platform_Runtime_ErrorFile_ID.htm)| Идентификатор файла.  
---|---  
[Name](P_Tessa_Platform_Runtime_ErrorFile_Name.htm)| Имя файла с расширением.  
[Size](P_Tessa_Platform_Runtime_ErrorFile_Size.htm)| Размер контента файла в
байтах.  
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
[GetStreamAsync](M_Tessa_Platform_Runtime_ErrorFile_GetStreamAsync.htm)|
Возвращает поток с контентом файла. Не возвращает null.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
