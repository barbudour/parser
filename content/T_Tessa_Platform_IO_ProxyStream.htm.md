# ProxyStream - класс
Поток, который оборачивает заданный оригинальный поток. Используется для
случаев, когда API некорректно обрабатывает оригинальный поток.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ProxyStream : Stream
VB __Копировать
     Public Class ProxyStream
    	Inherits Stream
C++ __Копировать
     public ref class ProxyStream : public Stream
F# __Копировать
     type ProxyStream = 
        class
            inherit Stream
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject) __[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream) __ ProxyStream
##  __Конструкторы
[ProxyStream](M_Tessa_Platform_IO_ProxyStream__ctor.htm)|  Создаёт экземпляр
класса с указанием оригинального потока.  
---|---  
## __Свойства
[CanRead](P_Tessa_Platform_IO_ProxyStream_CanRead.htm)| When overridden in a
derived class, gets a value indicating whether the current stream supports
reading.  
(Переопределяет
[Stream.CanRead](https://learn.microsoft.com/dotnet/api/system.io.stream.canread#system-
io-stream-canread))  
---|---  
[CanSeek](P_Tessa_Platform_IO_ProxyStream_CanSeek.htm)| When overridden in a
derived class, gets a value indicating whether the current stream supports
seeking.  
(Переопределяет
[Stream.CanSeek](https://learn.microsoft.com/dotnet/api/system.io.stream.canseek#system-
io-stream-canseek))  
[CanTimeout](P_Tessa_Platform_IO_ProxyStream_CanTimeout.htm)| Gets a value
that determines whether the current stream can time out.  
(Переопределяет
[Stream.CanTimeout](https://learn.microsoft.com/dotnet/api/system.io.stream.cantimeout#system-
io-stream-cantimeout))  
[CanWrite](P_Tessa_Platform_IO_ProxyStream_CanWrite.htm)| When overridden in a
derived class, gets a value indicating whether the current stream supports
writing.  
(Переопределяет
[Stream.CanWrite](https://learn.microsoft.com/dotnet/api/system.io.stream.canwrite#system-
io-stream-canwrite))  
[Length](P_Tessa_Platform_IO_ProxyStream_Length.htm)| When overridden in a
derived class, gets the length in bytes of the stream.  
(Переопределяет
[Stream.Length](https://learn.microsoft.com/dotnet/api/system.io.stream.length#system-
io-stream-length))  
[Position](P_Tessa_Platform_IO_ProxyStream_Position.htm)| When overridden in a
derived class, gets or sets the position within the current stream.  
(Переопределяет
[Stream.Position](https://learn.microsoft.com/dotnet/api/system.io.stream.position#system-
io-stream-position))  
[ReadTimeout](P_Tessa_Platform_IO_ProxyStream_ReadTimeout.htm)| Gets or sets a
value, in milliseconds, that determines how long the stream will attempt to
read before timing out.  
(Переопределяет
[Stream.ReadTimeout](https://learn.microsoft.com/dotnet/api/system.io.stream.readtimeout#system-
io-stream-readtimeout))  
[WriteTimeout](P_Tessa_Platform_IO_ProxyStream_WriteTimeout.htm)| Gets or sets
a value, in milliseconds, that determines how long the stream will attempt to
write before timing out.  
(Переопределяет
[Stream.WriteTimeout](https://learn.microsoft.com/dotnet/api/system.io.stream.writetimeout#system-
io-stream-writetimeout))  
##  __Методы
[BeginRead](M_Tessa_Platform_IO_ProxyStream_BeginRead.htm)| Begins an
asynchronous read operation. (Consider using [ReadAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.readasync#system-
io-stream-readasync\(system-byte\(\)-system-int32-system-int32\)) instead.)  
(Переопределяет [Stream.BeginRead(Byte[], Int32, Int32, AsyncCallback,
Object)](https://learn.microsoft.com/dotnet/api/system.io.stream.beginread#system-
io-stream-beginread\(system-byte\(\)-system-int32-system-int32-system-
asynccallback-system-object\)))  
---|---  
[BeginWrite](M_Tessa_Platform_IO_ProxyStream_BeginWrite.htm)| Begins an
asynchronous write operation. (Consider using [WriteAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.writeasync#system-
io-stream-writeasync\(system-byte\(\)-system-int32-system-int32\)) instead.)  
(Переопределяет [Stream.BeginWrite(Byte[], Int32, Int32, AsyncCallback,
Object)](https://learn.microsoft.com/dotnet/api/system.io.stream.beginwrite#system-
io-stream-beginwrite\(system-byte\(\)-system-int32-system-int32-system-
asynccallback-system-object\)))  
[Close](M_Tessa_Platform_IO_ProxyStream_Close.htm)| Closes the current stream
and releases any resources (such as sockets and file handles) associated with
the current stream. Instead of calling this method, ensure that the stream is
properly disposed.  
(Переопределяет
[Stream.Close()](https://learn.microsoft.com/dotnet/api/system.io.stream.close#system-
io-stream-close))  
[CopyTo(Stream)](https://learn.microsoft.com/dotnet/api/system.io.stream.copyto#system-
io-stream-copyto\(system-io-stream\))| Reads the bytes from the current stream
and writes them to another stream.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[CopyTo(Stream, Int32)](M_Tessa_Platform_IO_ProxyStream_CopyTo.htm)| Reads the
bytes from the current stream and writes them to another stream, using a
specified buffer size.  
(Переопределяет [Stream.CopyTo(Stream,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.copyto#system-
io-stream-copyto\(system-io-stream-system-int32\)))  
[CopyToAsync(Stream)](https://learn.microsoft.com/dotnet/api/system.io.stream.copytoasync#system-
io-stream-copytoasync\(system-io-stream\))| Asynchronously reads the bytes
from the current stream and writes them to another stream.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[CopyToAsync(Stream,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.copytoasync#system-
io-stream-copytoasync\(system-io-stream-system-int32\))| Asynchronously reads
the bytes from the current stream and writes them to another stream, using a
specified buffer size.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[CopyToAsync(Stream,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.copytoasync#system-
io-stream-copytoasync\(system-io-stream-system-threading-cancellationtoken\))|
Asynchronously reads the bytes from the current stream and writes them to
another stream, using a specified cancellation token.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[CopyToAsync(Stream, Int32,
CancellationToken)](M_Tessa_Platform_IO_ProxyStream_CopyToAsync.htm)|
Asynchronously reads the bytes from the current stream and writes them to
another stream, using a specified buffer size and cancellation token.  
(Переопределяет [Stream.CopyToAsync(Stream, Int32,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.copytoasync#system-
io-stream-copytoasync\(system-io-stream-system-int32-system-threading-
cancellationtoken\)))  
[CreateWaitHandle](https://learn.microsoft.com/dotnet/api/system.io.stream.createwaithandle#system-
io-stream-createwaithandle)| Allocates a
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
object.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
Устарело.  
[Dispose()](https://learn.microsoft.com/dotnet/api/system.io.stream.dispose#system-
io-stream-dispose)| Releases all resources used by the
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[Dispose(Boolean)](M_Tessa_Platform_IO_ProxyStream_Dispose.htm)| Releases the
unmanaged resources used by the
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream) and
optionally releases the managed resources.  
(Переопределяет
[Stream.Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.stream.dispose#system-
io-stream-dispose\(system-boolean\)))  
[DisposeAsync](M_Tessa_Platform_IO_ProxyStream_DisposeAsync.htm)|
Asynchronously releases the unmanaged resources used by the
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
(Переопределяет
[Stream.DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.io.stream.disposeasync#system-
io-stream-disposeasync))  
[EndRead](M_Tessa_Platform_IO_ProxyStream_EndRead.htm)| Waits for the pending
asynchronous read to complete. (Consider using [ReadAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.readasync#system-
io-stream-readasync\(system-byte\(\)-system-int32-system-int32\)) instead.)  
(Переопределяет
[Stream.EndRead(IAsyncResult)](https://learn.microsoft.com/dotnet/api/system.io.stream.endread#system-
io-stream-endread\(system-iasyncresult\)))  
[EndWrite](M_Tessa_Platform_IO_ProxyStream_EndWrite.htm)| Ends an asynchronous
write operation. (Consider using [WriteAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.writeasync#system-
io-stream-writeasync\(system-byte\(\)-system-int32-system-int32\)) instead.)  
(Переопределяет
[Stream.EndWrite(IAsyncResult)](https://learn.microsoft.com/dotnet/api/system.io.stream.endwrite#system-
io-stream-endwrite\(system-iasyncresult\)))  
[Equals](M_Tessa_Platform_IO_ProxyStream_Equals.htm)| Determines whether the
specified object is equal to the current object.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Flush](M_Tessa_Platform_IO_ProxyStream_Flush.htm)| When overridden in a
derived class, clears all buffers for this stream and causes any buffered data
to be written to the underlying device.  
(Переопределяет
[Stream.Flush()](https://learn.microsoft.com/dotnet/api/system.io.stream.flush#system-
io-stream-flush))  
[FlushAsync()](https://learn.microsoft.com/dotnet/api/system.io.stream.flushasync#system-
io-stream-flushasync)| Asynchronously clears all buffers for this stream and
causes any buffered data to be written to the underlying device.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[FlushAsync(CancellationToken)](M_Tessa_Platform_IO_ProxyStream_FlushAsync.htm)|
Asynchronously clears all buffers for this stream, causes any buffered data to
be written to the underlying device, and monitors cancellation requests.  
(Переопределяет
[Stream.FlushAsync(CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.flushasync#system-
io-stream-flushasync\(system-threading-cancellationtoken\)))  
[GetHashCode](M_Tessa_Platform_IO_ProxyStream_GetHashCode.htm)| Serves as the
default hash function.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ObjectInvariant](https://learn.microsoft.com/dotnet/api/system.io.stream.objectinvariant#system-
io-stream-objectinvariant)| Provides support for a
[Contract](https://learn.microsoft.com/dotnet/api/system.diagnostics.contracts.contract).  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
Устарело.  
[Read(Span<Byte>)](M_Tessa_Platform_IO_ProxyStream_Read_1.htm)| When
overridden in a derived class, reads a sequence of bytes from the current
stream and advances the position within the stream by the number of bytes
read.  
(Переопределяет
[Stream.Read(Span<Byte>)](https://learn.microsoft.com/dotnet/api/system.io.stream.read#system-
io-stream-read\(system-span\(\(system-byte\)\)\)))  
[Read(Byte[], Int32, Int32)](M_Tessa_Platform_IO_ProxyStream_Read.htm)| When
overridden in a derived class, reads a sequence of bytes from the current
stream and advances the position within the stream by the number of bytes
read.  
(Переопределяет [Stream.Read(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.read#system-
io-stream-read\(system-byte\(\)-system-int32-system-int32\)))  
[ReadAsync(Memory<Byte>,
CancellationToken)](M_Tessa_Platform_IO_ProxyStream_ReadAsync_1.htm)|
Asynchronously reads a sequence of bytes from the current stream, advances the
position within the stream by the number of bytes read, and monitors
cancellation requests.  
(Переопределяет [Stream.ReadAsync(Memory<Byte>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.readasync#system-
io-stream-readasync\(system-memory\(\(system-byte\)\)-system-threading-
cancellationtoken\)))  
[ReadAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.readasync#system-
io-stream-readasync\(system-byte\(\)-system-int32-system-int32\))|
Asynchronously reads a sequence of bytes from the current stream and advances
the position within the stream by the number of bytes read.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[ReadAsync(Byte[], Int32, Int32,
CancellationToken)](M_Tessa_Platform_IO_ProxyStream_ReadAsync.htm)|
Asynchronously reads a sequence of bytes from the current stream, advances the
position within the stream by the number of bytes read, and monitors
cancellation requests.  
(Переопределяет [Stream.ReadAsync(Byte[], Int32, Int32,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.readasync#system-
io-stream-readasync\(system-byte\(\)-system-int32-system-int32-system-
threading-cancellationtoken\)))  
[ReadByte](M_Tessa_Platform_IO_ProxyStream_ReadByte.htm)| Reads a byte from
the stream and advances the position within the stream by one byte, or returns
-1 if at the end of the stream.  
(Переопределяет
[Stream.ReadByte()](https://learn.microsoft.com/dotnet/api/system.io.stream.readbyte#system-
io-stream-readbyte))  
[Seek](M_Tessa_Platform_IO_ProxyStream_Seek.htm)| When overridden in a derived
class, sets the position within the current stream.  
(Переопределяет [Stream.Seek(Int64,
SeekOrigin)](https://learn.microsoft.com/dotnet/api/system.io.stream.seek#system-
io-stream-seek\(system-int64-system-io-seekorigin\)))  
[SetLength](M_Tessa_Platform_IO_ProxyStream_SetLength.htm)| When overridden in
a derived class, sets the length of the current stream.  
(Переопределяет
[Stream.SetLength(Int64)](https://learn.microsoft.com/dotnet/api/system.io.stream.setlength#system-
io-stream-setlength\(system-int64\)))  
[ToString](M_Tessa_Platform_IO_ProxyStream_ToString.htm)| Returns a string
that represents the current object.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[Write(ReadOnlySpan<Byte>)](M_Tessa_Platform_IO_ProxyStream_Write_1.htm)| When
overridden in a derived class, writes a sequence of bytes to the current
stream and advances the current position within this stream by the number of
bytes written.  
(Переопределяет
[Stream.Write(ReadOnlySpan<Byte>)](https://learn.microsoft.com/dotnet/api/system.io.stream.write#system-
io-stream-write\(system-readonlyspan\(\(system-byte\)\)\)))  
[Write(Byte[], Int32, Int32)](M_Tessa_Platform_IO_ProxyStream_Write.htm)| When
overridden in a derived class, writes a sequence of bytes to the current
stream and advances the current position within this stream by the number of
bytes written.  
(Переопределяет [Stream.Write(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.write#system-
io-stream-write\(system-byte\(\)-system-int32-system-int32\)))  
[WriteAsync(ReadOnlyMemory<Byte>,
CancellationToken)](M_Tessa_Platform_IO_ProxyStream_WriteAsync_1.htm)|
Asynchronously writes a sequence of bytes to the current stream, advances the
current position within this stream by the number of bytes written, and
monitors cancellation requests.  
(Переопределяет [Stream.WriteAsync(ReadOnlyMemory<Byte>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.writeasync#system-
io-stream-writeasync\(system-readonlymemory\(\(system-byte\)\)-system-
threading-cancellationtoken\)))  
[WriteAsync(Byte[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stream.writeasync#system-
io-stream-writeasync\(system-byte\(\)-system-int32-system-int32\))|
Asynchronously writes a sequence of bytes to the current stream and advances
the current position within this stream by the number of bytes written.  
(Унаследован от
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream))  
[WriteAsync(Byte[], Int32, Int32,
CancellationToken)](M_Tessa_Platform_IO_ProxyStream_WriteAsync.htm)|
Asynchronously writes a sequence of bytes to the current stream, advances the
current position within this stream by the number of bytes written, and
monitors cancellation requests.  
(Переопределяет [Stream.WriteAsync(Byte[], Int32, Int32,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stream.writeasync#system-
io-stream-writeasync\(system-byte\(\)-system-int32-system-int32-system-
threading-cancellationtoken\)))  
[WriteByte](M_Tessa_Platform_IO_ProxyStream_WriteByte.htm)| Writes a byte to
the current position in the stream and advances the position within the stream
by one byte.  
(Переопределяет
[Stream.WriteByte(Byte)](https://learn.microsoft.com/dotnet/api/system.io.stream.writebyte#system-
io-stream-writebyte\(system-byte\)))  
##  __Методы расширения
[AsMemoryStreamAsync](M_Tessa_Platform_IO_IOExtensions_AsMemoryStreamAsync.htm)|
Возвращает поток stream, преобразованный к типу
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream).
Если его тип отличается от
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
то его содержимое будет скопировано в созданный объект
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
после чего исходный stream будет освобождён, но только если параметр
disposeNonMemoryStream равен true.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
---|---  
[CalculateStreamLengthAsync](M_Tessa_Platform_IO_IOExtensions_CalculateStreamLengthAsync.htm)|
Вычисляет длину потока посредством его чтения, но отбрасывая сам контент.  
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
[ReadAllBytes](M_Tessa_Platform_IO_IOExtensions_ReadAllBytes.htm)|  Выполняет
синхронное чтение всех данных потока в виде одного массива байт. Чтение
выполняется до того момента, как поток перестанет возвращать данные, при этом
метод не использует свойство
[Length](https://learn.microsoft.com/dotnet/api/system.io.stream.length#system-
io-stream-length) для определения количества считываемых данных.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadAllBytesAsync](M_Tessa_Platform_IO_IOExtensions_ReadAllBytesAsync.htm)|
Выполняет асинхронное чтение всех данных потока в виде одного массива байт.
Чтение выполняется до того момента, как поток перестанет возвращать данные,
при этом метод не использует свойство
[Length](https://learn.microsoft.com/dotnet/api/system.io.stream.length#system-
io-stream-length) для определения количества считываемых данных.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadByteAsync](M_Tessa_Platform_IO_IOExtensions_ReadByteAsync.htm)|
Выполняет асинхронное чтение целочисленного значения Byte из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadBytes](M_Tessa_Platform_IO_IOExtensions_ReadBytes.htm)|  Выполняет чтение
данных из потока stream и записывает их в возвращаемый массив байт, который
имеет максимальный размер length байт.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadBytesAsync](M_Tessa_Platform_IO_IOExtensions_ReadBytesAsync.htm)|
Выполняет чтение данных из потока stream и записывает их в возвращаемый массив
байт, который имеет максимальный размер length байт.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadBytesExact](M_Tessa_Platform_IO_IOExtensions_ReadBytesExact.htm)|
Выполняет чтение данных из потока stream и записывает их в возвращаемый массив
байт, который имеет заданный размер length байт.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadBytesExactAsync](M_Tessa_Platform_IO_IOExtensions_ReadBytesExactAsync.htm)|
Выполняет асинхронное чтение данных из потока stream и записывает их в
возвращаемый массив байт, который имеет заданный размер length байт.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadExact](M_Tessa_Platform_IO_IOExtensions_ReadExact.htm)|  Выполняет чтение
указанного количества байт из потока в буфер. Возвращает количество
действительно прочитанных байт, которое может быть меньше указанного
количества только в том случае, если поток завершился.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadExactAsync](M_Tessa_Platform_IO_IOExtensions_ReadExactAsync.htm)|
Выполняет асинхронное чтение указанного количества байт из потока в буфер.
Возвращает количество действительно прочитанных байт, которое может быть
меньше указанного количества только в том случае, если поток завершился.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadGuid](M_Tessa_Platform_IO_IOExtensions_ReadGuid_1.htm)|  Выполняет чтение
значения Guid из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadGuidAsync](M_Tessa_Platform_IO_IOExtensions_ReadGuidAsync.htm)|
Выполняет асинхронное чтение значения Guid из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadInt16Async](M_Tessa_Platform_IO_IOExtensions_ReadInt16Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int16 из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadInt32](M_Tessa_Platform_IO_IOExtensions_ReadInt32.htm)|  Выполняет чтение
целочисленного значения Int32 из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadInt32Async](M_Tessa_Platform_IO_IOExtensions_ReadInt32Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int32 из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadInt64](M_Tessa_Platform_IO_IOExtensions_ReadInt64.htm)|  Выполняет чтение
целочисленного значения Int32 из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadInt64Async](M_Tessa_Platform_IO_IOExtensions_ReadInt64Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int32 из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadString](M_Tessa_Platform_IO_IOExtensions_ReadString.htm)|  Выполняет
чтение значения string из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[ReadStringAsync](M_Tessa_Platform_IO_IOExtensions_ReadStringAsync.htm)|
Выполняет асинхронное чтение значения string из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryReadPrimitiveType](M_Tessa_Platform_IO_IOExtensions_TryReadPrimitiveType.htm)|
Выполняет чтение объекта примитивного типа из потока. Возвращает значение
объекта или признак того, что тип объекта type является примитивным, и объект
был прочитан из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[TryReadPrimitiveTypeAsync](M_Tessa_Platform_IO_IOExtensions_TryReadPrimitiveTypeAsync.htm)|
Выполняет асинхронное чтение объекта примитивного типа из потока. Возвращает
значение объекта или признак того, что тип объекта type является примитивным,
и объект был прочитан из потока.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[TryWritePrimitiveType](M_Tessa_Platform_IO_IOExtensions_TryWritePrimitiveType.htm)|
Выполняет запись объекта примитивного типа в поток. Возвращает признак того,
что тип объекта obj является примитивным, и объект был записан в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[TryWritePrimitiveTypeAsync](M_Tessa_Platform_IO_IOExtensions_TryWritePrimitiveTypeAsync.htm)|
Выполняет асинхронную запись объекта примитивного типа в поток. Возвращает
признак того, что тип объекта obj является примитивным, и объект был записан в
поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_2.htm)|  Выполняет запись
целочисленного значения Byte в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_3.htm)|  Выполняет запись
значения Guid в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_4.htm)|  Выполняет запись
целочисленного значения Int16 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_5.htm)|  Выполняет запись
целочисленного значения Int32 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_6.htm)|  Выполняет запись
целочисленного значения Int32 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[Write](M_Tessa_Platform_IO_IOExtensions_Write_7.htm)|  Выполняет запись
значения string в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync.htm)|  Выполняет
асинхронную запись целочисленного значения Byte в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync_1.htm)|  Выполняет
запись значения Guid в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync_2.htm)|  Выполняет
асинхронную запись целочисленного значения Int16 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync_3.htm)|  Выполняет
асинхронную запись целочисленного значения Int32 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync_4.htm)|  Выполняет
асинхронную запись целочисленного значения Int32 в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteAsync](M_Tessa_Platform_IO_IOExtensions_WriteAsync_5.htm)|  Выполняет
асинхронную запись значения string в поток.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteStream](M_Tessa_Platform_IO_IOExtensions_WriteStream.htm)|  Записывает
все данные из потока source в поток target.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
[WriteStreamAsync](M_Tessa_Platform_IO_IOExtensions_WriteStreamAsync.htm)|
Записывает все данные из потока source в поток target.  
(Определяется [IOExtensions](T_Tessa_Platform_IO_IOExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
