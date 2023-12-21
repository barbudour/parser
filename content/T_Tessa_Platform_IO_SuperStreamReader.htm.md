# SuperStreamReader - класс
Обеспечивает чтение данных из суперпотока.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SuperStreamReader
VB __Копировать
     Public NotInheritable Class SuperStreamReader
C++ __Копировать
     public ref class SuperStreamReader sealed
F# __Копировать
     [<SealedAttribute>]
    type SuperStreamReader = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SuperStreamReader
##  __Конструкторы
[SuperStreamReader](M_Tessa_Platform_IO_SuperStreamReader__ctor.htm)|  Создаёт
экземпляр класса с указанием суперпотока, для которого необходимо обеспечить
чтение данных.  
---|---  
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
[ReadBytes](M_Tessa_Platform_IO_SuperStreamReader_ReadBytes.htm)|  Выполняет
чтение данных из суперпотока, ограниченных заданным максимальным размером байт
length, и возвращает их в виде массива байт действительного размера.  
[ReadBytesAsync](M_Tessa_Platform_IO_SuperStreamReader_ReadBytesAsync.htm)|
Выполняет чтение данных из суперпотока, ограниченных заданным максимальным
размером байт length, и возвращает их в виде массива байт действительного
размера.  
[ReadBytesExact](M_Tessa_Platform_IO_SuperStreamReader_ReadBytesExact.htm)|
Выполняет чтение заданного числа байт length из суперпотока, и возвращает их в
виде массива байт.  
[ReadBytesExactAsync](M_Tessa_Platform_IO_SuperStreamReader_ReadBytesExactAsync.htm)|
Выполняет чтение заданного числа байт length из суперпотока, и возвращает их в
виде массива байт.  
[ReadInt32](M_Tessa_Platform_IO_SuperStreamReader_ReadInt32.htm)|  Выполняет
чтение из суперпотока целочисленного значения
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[ReadInt32Async](M_Tessa_Platform_IO_SuperStreamReader_ReadInt32Async.htm)|
Выполняет чтение из суперпотока целочисленного значения
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[ReadStream](M_Tessa_Platform_IO_SuperStreamReader_ReadStream.htm)|
Возвращает поток, обеспечивающий чтение данных из суперпотока, причём
количество байт, которые можно прочитать, ограничено заданным числом length.  
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
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
