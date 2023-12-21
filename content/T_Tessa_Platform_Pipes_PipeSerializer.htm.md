# PipeSerializer - класс
Объект, выполняющий сериализацию и десериализацию текстовых сообщений по
каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PipeSerializer : IPipeSerializer
VB __Копировать
     Public NotInheritable Class PipeSerializer
    	Implements IPipeSerializer
C++ __Копировать
     public ref class PipeSerializer sealed : IPipeSerializer
F# __Копировать
     [<SealedAttribute>]
    type PipeSerializer = 
        class
            interface IPipeSerializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeSerializer
Implements
    [IPipeSerializer](T_Tessa_Platform_Pipes_IPipeSerializer.htm)
##  __Конструкторы
[PipeSerializer](M_Tessa_Platform_Pipes_PipeSerializer__ctor.htm)|
Инициализирует новый экземпляр класса PipeSerializer  
---|---  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReadBytesAsync](M_Tessa_Platform_Pipes_PipeSerializer_ReadBytesAsync.htm)|
Выполняет чтение сообщения как массива байт, переданного по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
Если возвращённое значение равно null или пустому массиву, то считается, что
канал был закрыт.  
[ReadStringAsync](M_Tessa_Platform_Pipes_PipeSerializer_ReadStringAsync.htm)|
Выполняет чтение сообщения как строки текста, переданной по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
Если возвращённое значение равно null или пустой строке, то считается, что
канал был закрыт.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteBytesAsync](M_Tessa_Platform_Pipes_PipeSerializer_WriteBytesAsync.htm)|
Отправляет массив байт как сообщение по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
[WriteStringAsync](M_Tessa_Platform_Pipes_PipeSerializer_WriteStringAsync.htm)|
Отправляет строку текста как сообщение по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
