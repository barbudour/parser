# CsvWriter - класс
Объект осуществляющий запись в csv
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CsvWriter : StreamWriter, 
    	IEscapeableStreamWriter, ICsvItemSeparator
VB __Копировать
     Public NotInheritable Class CsvWriter
    	Inherits StreamWriter
    	Implements IEscapeableStreamWriter, ICsvItemSeparator
C++ __Копировать
     public ref class CsvWriter sealed : public StreamWriter, 
    	IEscapeableStreamWriter, ICsvItemSeparator
F# __Копировать
     [<SealedAttribute>]
    type CsvWriter = 
        class
            inherit StreamWriter
            interface IEscapeableStreamWriter
            interface ICsvItemSeparator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject) __[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) __[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter) __ CsvWriter
Implements
    [ICsvItemSeparator](T_Tessa_Platform_IO_ICsvItemSeparator.htm), [IEscapeableStreamWriter](T_Tessa_Platform_IO_IEscapeableStreamWriter.htm)
##  __Конструкторы
[CsvWriter(Stream)](M_Tessa_Platform_IO_CsvWriter__ctor.htm)|  Initializes a
new instance of the CsvWriter class. Инициализирует новый экземпляр
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного потока, используя кодировку UTF-8 и размер буфера по умолчанию.  
---|---  
[CsvWriter(String)](M_Tessa_Platform_IO_CsvWriter__ctor_4.htm)|  Initializes a
new instance of the CsvWriter class. Инициализирует новый экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного файла по заданному пути, используя кодировку и размер буфера по
умолчанию.  
[CsvWriter(Stream, Encoding)](M_Tessa_Platform_IO_CsvWriter__ctor_1.htm)|
Initializes a new instance of the CsvWriter class. Инициализирует новый
экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного потока, используя заданную кодировку и размер буфера по
умолчанию.  
[CsvWriter(String, Boolean)](M_Tessa_Platform_IO_CsvWriter__ctor_5.htm)|
Initializes a new instance of the CsvWriter class. Инициализирует новый
экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного файла по заданному пути, используя кодировку и размер буфера по
умолчанию.Если файл существует, он может быть либо перезаписан, либо в него
могут быть добавлены данные.Если файл не существует, конструктор создает новый
файл.  
[CsvWriter(Stream, Encoding,
Int32)](M_Tessa_Platform_IO_CsvWriter__ctor_2.htm)|  Initializes a new
instance of the CsvWriter class. Инициализирует новый экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного потока, используя заданную кодировку и размер буфера.  
[CsvWriter(String, Boolean,
Encoding)](M_Tessa_Platform_IO_CsvWriter__ctor_6.htm)|  Initializes a new
instance of the CsvWriter class. Инициализирует новый экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного файла по заданному пути, используя заданную кодировку и размер
буфера по умолчанию.Если файл существует, он может быть либо перезаписан, либо
в него могут быть добавлены данные.Если файл не существует, конструктор
создает новый файл.  
[CsvWriter(Stream, Encoding, Int32,
Boolean)](M_Tessa_Platform_IO_CsvWriter__ctor_3.htm)| Initializes a new
instance of the
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
class for the specified stream by using the specified encoding and buffer
size, and optionally leaves the stream open.  
[CsvWriter(String, Boolean, Encoding,
Int32)](M_Tessa_Platform_IO_CsvWriter__ctor_7.htm)|  Initializes a new
instance of the CsvWriter class. Инициализирует новый экземпляр класса
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
для указанного файла по заданному пути, используя заданную кодировку и размер
буфера.Если файл существует, он может быть либо перезаписан, либо в него могут
быть добавлены данные.Если файл не существует, конструктор создает новый файл.  
## __Свойства
[AutoFlush](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.autoflush#system-
io-streamwriter-autoflush)| Gets or sets a value indicating whether the
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter)
will flush its buffer to the underlying stream after every call to
[Write(Char)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-char\)).  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
---|---  
[BaseStream](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.basestream#system-
io-streamwriter-basestream)| Gets the underlying stream that interfaces with a
backing store.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[Encoding](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.encoding#system-
io-streamwriter-encoding)| Gets the
[Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding) in
which the output is written.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[ForceEscaping](P_Tessa_Platform_IO_CsvWriter_ForceEscaping.htm)|  Признак
того, что требуется включить принудительный режим экранирования выводимых
строк, даже если он не требуется по правилами используемых настроек
форматирования.  
[FormatProvider](P_Tessa_Platform_IO_CsvWriter_FormatProvider.htm)|  Получает
объект, управляющий форматированием.  
(Переопределяет
[TextWriter.FormatProvider](https://learn.microsoft.com/dotnet/api/system.io.textwriter.formatprovider#system-
io-textwriter-formatprovider))  
[NewLine](https://learn.microsoft.com/dotnet/api/system.io.textwriter.newline#system-
io-textwriter-newline)| Gets or sets the line terminator string used by the
current TextWriter.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Separator](P_Tessa_Platform_IO_CsvWriter_Separator.htm)|  Gets or sets
Разделитель полей  
## __Методы
[Close](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.close#system-
io-streamwriter-close)| Closes the current StreamWriter object and the
underlying stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
---|---  
[Dispose()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.dispose#system-
io-textwriter-dispose)| Releases all resources used by the
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
object.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.dispose#system-
io-streamwriter-dispose\(system-boolean\))| Causes any buffered data to be
written to the underlying stream, releases the unmanaged resources used by the
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter),
and optionally the managed resources.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.disposeasync#system-
io-streamwriter-disposeasync)| Asynchronously writes any buffered data to the
underlying stream and releases the unmanaged resources used by the
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter).  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
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
[Flush](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.flush#system-
io-streamwriter-flush)| Clears all buffers for the current writer and causes
any buffered data to be written to the underlying stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[FlushAsync](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.flushasync#system-
io-streamwriter-flushasync)| Clears all buffers for this stream asynchronously
and causes any buffered data to be written to the underlying device.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Write(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-boolean\))| Writes the text representation of a
Boolean value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Char)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-char\))| Writes a character to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[Write(Char[])](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-char\(\)\))| Writes a character array to the
stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[Write(Decimal)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-decimal\))| Writes the text representation of a
decimal value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Double)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-double\))| Writes the text representation of an
8-byte floating-point value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-int32\))| Writes the text representation of a
4-byte signed integer to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Int64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-int64\))| Writes the text representation of an
8-byte signed integer to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-object\))| Writes the text representation of an
object to the text stream by calling the ToString method on that object.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-readonlyspan\(\(system-char\)\)\))| Writes a
character span to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[Write(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-single\))| Writes the text representation of a
4-byte floating-point value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(String)](M_Tessa_Platform_IO_CsvWriter_Write.htm)|  Записывает в поток
строку.  
(Переопределяет
[StreamWriter.Write(String)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-string\)))  
[Write(UInt32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-uint32\))| Writes the text representation of a
4-byte unsigned integer to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(UInt64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-uint64\))| Writes the text representation of an
8-byte unsigned integer to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(String,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object\))| Writes a formatted string
to the text stream, using the same semantics as the [Format(String,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\)) method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(String,
Object[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object\(\)\))| Writes a formatted
string to the text stream, using the same semantics as the [Format(String,
Object[])](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\(\)\)) method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.write#system-
io-streamwriter-write\(system-char\(\)-system-int32-system-int32\))| Writes a
subarray of characters to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[Write(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object-system-object\))| Writes a
formatted string to the text stream using the same semantics as the
[Format(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object-system-object\)) method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(String, Object, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object-system-object-system-
object\))| Writes a formatted string to the text stream, using the same
semantics as the [Format(String, Object, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object-system-object-system-object\))
method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeasync#system-
io-streamwriter-writeasync\(system-char\))| Asynchronously writes a character
to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-char\(\)\))| Writes a character array to the
text stream asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(String)](M_Tessa_Platform_IO_CsvWriter_WriteAsync.htm)|
Asynchronously writes a string to the stream.  
(Переопределяет
[StreamWriter.WriteAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeasync#system-
io-streamwriter-writeasync\(system-string\)))  
[WriteAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeasync#system-
io-streamwriter-writeasync\(system-readonlymemory\(\(system-char\)\)-system-
threading-cancellationtoken\))| Asynchronously writes a character memory
region to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeasync#system-
io-streamwriter-writeasync\(system-char\(\)-system-int32-system-int32\))|
Asynchronously writes a subarray of characters to the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLine()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline)| Writes a line terminator to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-boolean\))| Writes the text representation of
a Boolean value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Char)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\))| Writes a character to the text
stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\(\)\))| Writes an array of characters to
the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Decimal)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-decimal\))| Writes the text representation of
a decimal value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Double)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-double\))| Writes the text representation of a
8-byte floating-point value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-int32\))| Writes the text representation of a
4-byte signed integer to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Int64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-int64\))| Writes the text representation of an
8-byte signed integer to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-object\))| Writes the text representation of
an object to the text stream, by calling the ToString method on that object,
followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeline#system-
io-streamwriter-writeline\(system-readonlyspan\(\(system-char\)\)\))| Writes
the text representation of a character span to the stream, followed by a line
terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLine(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-single\))| Writes the text representation of a
4-byte floating-point value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writeline#system-
io-streamwriter-writeline\(system-string\))| Writes a string to the stream,
followed by a line terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLine(UInt32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-uint32\))| Writes the text representation of a
4-byte unsigned integer to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(UInt64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-uint64\))| Writes the text representation of
an 8-byte unsigned integer to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object\))| Writes a formatted
string and a new line to the text stream, using the same semantics as the
[Format(String,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\)) method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String,
Object[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object\(\)\))| Writes out a
formatted string and a new line to the text stream, using the same semantics
as [Format(String,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\)).  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\(\)-system-int32-system-int32\))| Writes
a subarray of characters to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object-system-object\))| Writes
a formatted string and a new line to the text stream, using the same semantics
as the [Format(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object-system-object\)) method.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String, Object, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object-system-object-system-
object\))| Writes out a formatted string and a new line to the text stream,
using the same semantics as [Format(String,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\)).  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync()](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writelineasync#system-
io-streamwriter-writelineasync)| Asynchronously writes a line terminator to
the stream.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLineAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writelineasync#system-
io-streamwriter-writelineasync\(system-char\))| Asynchronously writes a
character to the stream, followed by a line terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLineAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-char\(\)\))| Asynchronously writes an
array of characters to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writelineasync#system-
io-streamwriter-writelineasync\(system-string\))| Asynchronously writes a
string to the stream, followed by a line terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLineAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writelineasync#system-
io-streamwriter-writelineasync\(system-readonlymemory\(\(system-
char\)\)-system-threading-cancellationtoken\))| Asynchronously writes the text
representation of a character memory region to the stream, followed by a line
terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteLineAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.streamwriter.writelineasync#system-
io-streamwriter-writelineasync\(system-char\(\)-system-int32-system-int32\))|
Asynchronously writes a subarray of characters to the stream, followed by a
line terminator.  
(Унаследован от
[StreamWriter](https://learn.microsoft.com/dotnet/api/system.io.streamwriter))  
[WriteSeparatorAsync](M_Tessa_Platform_IO_CsvWriter_WriteSeparatorAsync.htm)|
Осуществляет запись разделителя  
## __Поля
[CoreNewLine](https://learn.microsoft.com/dotnet/api/system.io.textwriter.corenewline)|
Stores the newline characters used for this TextWriter.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
---|---  
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
[WriteIndent](M_Tessa_Platform_CommandLine_CommandLineIOExtensions_WriteIndent.htm)|  
(Определяется
[CommandLineIOExtensions](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm))  
[WriteIndented](M_Tessa_Platform_CommandLine_CommandLineIOExtensions_WriteIndented.htm)|
Writes a string to the text string or stream with indentation of every line of
the string.  
(Определяется
[CommandLineIOExtensions](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm))  
[WriteIndented](M_Tessa_Platform_CommandLine_CommandLineIOExtensions_WriteIndented_1.htm)|
Writes a string to the text string or stream with indentation of every line of
the string.  
(Определяется
[CommandLineIOExtensions](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm))  
[WriteLogo](M_Tessa_Platform_CommandLine_CommandLineIOExtensions_WriteLogo.htm)|
Writes a logo to the specified output stream.  
(Определяется
[CommandLineIOExtensions](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
