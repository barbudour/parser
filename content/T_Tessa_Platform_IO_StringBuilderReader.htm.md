# StringBuilderReader - класс
##  __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StringBuilderReader : TextReader
VB __Копировать
     Public NotInheritable Class StringBuilderReader
    	Inherits TextReader
C++ __Копировать
     public ref class StringBuilderReader sealed : public TextReader
F# __Копировать
     [<SealedAttribute>]
    type StringBuilderReader = 
        class
            inherit TextReader
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject) __[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader) __ StringBuilderReader
##  __Конструкторы
[StringBuilderReader](M_Tessa_Platform_IO_StringBuilderReader__ctor.htm)|
Инициализирует новый экземпляр класса StringBuilderReader  
---|---  
##  __Методы
[Close](M_Tessa_Platform_IO_StringBuilderReader_Close.htm)|  
(Переопределяет
[TextReader.Close()](https://learn.microsoft.com/dotnet/api/system.io.textreader.close#system-
io-textreader-close))  
---|---  
[Dispose()](https://learn.microsoft.com/dotnet/api/system.io.textreader.dispose#system-
io-textreader-dispose)| Releases all resources used by the
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader)
object.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[Dispose(Boolean)](M_Tessa_Platform_IO_StringBuilderReader_Dispose.htm)|
Освобождает неуправляемые ресурсы, используемые объектом StringBuilderReader,
а при необходимости освобождает также управляемые ресурсы  
(Переопределяет
[TextReader.Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textreader.dispose#system-
io-textreader-dispose\(system-boolean\)))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLifetimeService](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject.getlifetimeservice#system-
marshalbyrefobject-getlifetimeservice)| Retrieves the current lifetime service
object that controls the lifetime policy for this instance.  
(Унаследован от
[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeLifetimeService](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject.initializelifetimeservice#system-
marshalbyrefobject-initializelifetimeservice)| Obtains a lifetime service
object to control the lifetime policy for this instance.  
(Унаследован от
[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject))  
[MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone(Boolean)](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject.memberwiseclone#system-
marshalbyrefobject-memberwiseclone\(system-boolean\))| Creates a shallow copy
of the current
[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject)
object.  
(Унаследован от
[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject))  
[Peek](M_Tessa_Platform_IO_StringBuilderReader_Peek.htm)|  
(Переопределяет
[TextReader.Peek()](https://learn.microsoft.com/dotnet/api/system.io.textreader.peek#system-
io-textreader-peek))  
[Read()](M_Tessa_Platform_IO_StringBuilderReader_Read.htm)|  
(Переопределяет
[TextReader.Read()](https://learn.microsoft.com/dotnet/api/system.io.textreader.read#system-
io-textreader-read))  
[Read(Span<Char>)](https://learn.microsoft.com/dotnet/api/system.io.textreader.read#system-
io-textreader-read\(system-span\(\(system-char\)\)\))|  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[Read(Char[], Int32,
Int32)](M_Tessa_Platform_IO_StringBuilderReader_Read_1.htm)|  
(Переопределяет [TextReader.Read(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textreader.read#system-
io-textreader-read\(system-char\(\)-system-int32-system-int32\)))  
[ReadAsync(Memory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readasync#system-
io-textreader-readasync\(system-memory\(\(system-char\)\)-system-threading-
cancellationtoken\))|  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readasync#system-
io-textreader-readasync\(system-char\(\)-system-int32-system-int32\))| Reads a
specified maximum number of characters from the current text reader
asynchronously and writes the data to a buffer, beginning at the specified
index.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadBlock(Span<Char>)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readblock#system-
io-textreader-readblock\(system-span\(\(system-char\)\)\))|  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadBlock(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readblock#system-
io-textreader-readblock\(system-char\(\)-system-int32-system-int32\))| Reads a
specified maximum number of characters from the current text reader and writes
the data to a buffer, beginning at the specified index.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadBlockAsync(Memory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readblockasync#system-
io-textreader-readblockasync\(system-memory\(\(system-char\)\)-system-
threading-cancellationtoken\))|  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadBlockAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textreader.readblockasync#system-
io-textreader-readblockasync\(system-char\(\)-system-int32-system-int32\))|
Reads a specified maximum number of characters from the current text reader
asynchronously and writes the data to a buffer, beginning at the specified
index.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadLine](M_Tessa_Platform_IO_StringBuilderReader_ReadLine.htm)|  
(Переопределяет
[TextReader.ReadLine()](https://learn.microsoft.com/dotnet/api/system.io.textreader.readline#system-
io-textreader-readline))  
[ReadLineAsync](https://learn.microsoft.com/dotnet/api/system.io.textreader.readlineasync#system-
io-textreader-readlineasync)| Reads a line of characters asynchronously and
returns the data as a string.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ReadToEnd](M_Tessa_Platform_IO_StringBuilderReader_ReadToEnd.htm)|  
(Переопределяет
[TextReader.ReadToEnd()](https://learn.microsoft.com/dotnet/api/system.io.textreader.readtoend#system-
io-textreader-readtoend))  
[ReadToEndAsync](https://learn.microsoft.com/dotnet/api/system.io.textreader.readtoendasync#system-
io-textreader-readtoendasync)| Reads all characters from the current position
to the end of the text reader asynchronously and returns them as one string.  
(Унаследован от
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[DrainAsync](M_Chronos_Platform_IOExtensions_DrainAsync.htm)|  Выполняет
асинхронное чтение всех данных, содержащихся для заданного объекта
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader), но
не использует эти данные, и возвращает асинхронную задачу по окончанию чтения.  
(Определяется [IOExtensions](T_Chronos_Platform_IOExtensions.htm))  
---|---  
[DrainAsync](M_Tessa_Platform_IO_IOExtensions_DrainAsync.htm)|  Выполняет
асинхронное чтение всех данных, содержащихся для заданного объекта
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader), но
не использует эти данные, и возвращает асинхронную задачу по окончанию чтения.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ReadToEndAsync](M_Tessa_Platform_IO_IOExtensions_ReadToEndAsync.htm)|
Выполняет асинхронное чтение строки для заданного объекта
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader) с
указанием токена отмены операции
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken).
Метод без указания токена отмены
[ReadToEndAsync()](https://learn.microsoft.com/dotnet/api/system.io.textreader.readtoendasync#system-
io-textreader-readtoendasync) доступен в классе
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader), но
он не позволяет прервать чтение.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
