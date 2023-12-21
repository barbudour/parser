# Utf8StringWriter - класс
Объект
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter),
выполняющий запись в кодировке UTF-8.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Utf8StringWriter : StringWriter
VB __Копировать
     Public NotInheritable Class Utf8StringWriter
    	Inherits StringWriter
C++ __Копировать
     public ref class Utf8StringWriter sealed : public StringWriter
F# __Копировать
     [<SealedAttribute>]
    type Utf8StringWriter = 
        class
            inherit StringWriter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject) __[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) __[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter) __ Utf8StringWriter
##  __Конструкторы
[Utf8StringWriter()](M_Tessa_Platform_IO_Utf8StringWriter__ctor.htm)|
Инициализирует новый экземпляр класса Utf8StringWriter.  
---|---  
[Utf8StringWriter(IFormatProvider)](M_Tessa_Platform_IO_Utf8StringWriter__ctor_1.htm)|
Инициализирует новый экземпляр класса Utf8StringWriter с указанным форматом
объекта.  
[Utf8StringWriter(StringBuilder)](M_Tessa_Platform_IO_Utf8StringWriter__ctor_2.htm)|
Инициализирует новый экземпляр класса Utf8StringWriter, с помощью которого
осуществляется запись в указанный класс
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder).  
[Utf8StringWriter(StringBuilder,
IFormatProvider)](M_Tessa_Platform_IO_Utf8StringWriter__ctor_3.htm)|
Инициализирует новый экземпляр класса Utf8StringWriter, с помощью которого
осуществляется запись в указанный класс
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
и который имеет указанный формат поставщика.  
## __Свойства
[Encoding](P_Tessa_Platform_IO_Utf8StringWriter_Encoding.htm)|  Получает
кодировку
[Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding), в
которой осуществляется запись выходных данных.  
(Переопределяет
[StringWriter.Encoding](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.encoding#system-
io-stringwriter-encoding))  
---|---  
[FormatProvider](https://learn.microsoft.com/dotnet/api/system.io.textwriter.formatprovider#system-
io-textwriter-formatprovider)| Gets an object that controls formatting.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[NewLine](https://learn.microsoft.com/dotnet/api/system.io.textwriter.newline#system-
io-textwriter-newline)| Gets or sets the line terminator string used by the
current TextWriter.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
##  __Методы
[Close](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.close#system-
io-stringwriter-close)| Closes the current
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter)
and the underlying stream.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
---|---  
[Dispose()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.dispose#system-
io-textwriter-dispose)| Releases all resources used by the
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
object.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.dispose#system-
io-stringwriter-dispose\(system-boolean\))| Releases the unmanaged resources
used by the
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter)
and optionally releases the managed resources.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.io.textwriter.disposeasync#system-
io-textwriter-disposeasync)| Asynchronously releases all resources used by the
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
object.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
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
[Flush](https://learn.microsoft.com/dotnet/api/system.io.textwriter.flush#system-
io-textwriter-flush)| Clears all buffers for the current writer and causes any
buffered data to be written to the underlying device.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[FlushAsync](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.flushasync#system-
io-stringwriter-flushasync)| Asynchronously clears all buffers for the current
writer and causes any buffered data to be written to the underlying device.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLifetimeService](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject.getlifetimeservice#system-
marshalbyrefobject-getlifetimeservice)| Retrieves the current lifetime service
object that controls the lifetime policy for this instance.  
(Унаследован от
[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject))  
[GetStringBuilder](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.getstringbuilder#system-
io-stringwriter-getstringbuilder)| Returns the underlying
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder).  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.tostring#system-
io-stringwriter-tostring)| Returns a string containing the characters written
to the current StringWriter so far.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[Write(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-boolean\))| Writes the text representation of a
Boolean value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Char)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.write#system-
io-stringwriter-write\(system-char\))| Writes a character to the string.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[Write(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-char\(\)\))| Writes a character array to the text
stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
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
[Write(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.write#system-
io-stringwriter-write\(system-readonlyspan\(\(system-char\)\)\))| Writes the
string representation of a span of chars to the current string.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[Write(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-single\))| Writes the text representation of a
4-byte floating-point value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(String)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.write#system-
io-stringwriter-write\(system-string\))| Writes a string to the current
string.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
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
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.write#system-
io-stringwriter-write\(system-char\(\)-system-int32-system-int32\))| Writes a
subarray of characters to the string.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
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
[WriteAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writeasync#system-
io-stringwriter-writeasync\(system-char\))| Writes a character to the string
asynchronously.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-char\(\)\))| Writes a character array to the
text stream asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writeasync#system-
io-stringwriter-writeasync\(system-string\))| Writes a string to the current
string asynchronously.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writeasync#system-
io-stringwriter-writeasync\(system-readonlymemory\(\(system-char\)\)-system-
threading-cancellationtoken\))| Asynchronously writes a memory region of
characters to the string.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writeasync#system-
io-stringwriter-writeasync\(system-char\(\)-system-int32-system-int32\))|
Writes a subarray of characters to the string asynchronously.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
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
[WriteLine(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writeline#system-
io-stringwriter-writeline\(system-readonlyspan\(\(system-char\)\)\))| Writes
the text representation a span of characters to the string, followed by a line
terminator.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteLine(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-single\))| Writes the text representation of a
4-byte floating-point value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string\))| Writes a string to the text stream,
followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
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
[WriteLineAsync()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync)| Asynchronously writes a line terminator to the
text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writelineasync#system-
io-stringwriter-writelineasync\(system-char\))| Asynchronously writes a
character to the string, followed by a line terminator.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteLineAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-char\(\)\))| Asynchronously writes an
array of characters to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writelineasync#system-
io-stringwriter-writelineasync\(system-string\))| Asynchronously writes a
string to the current string, followed by a line terminator.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteLineAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writelineasync#system-
io-stringwriter-writelineasync\(system-readonlymemory\(\(system-
char\)\)-system-threading-cancellationtoken\))| Asynchronously writes the
string representation of the memory region of characters to the current
string, followed by a line terminator.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
[WriteLineAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.stringwriter.writelineasync#system-
io-stringwriter-writelineasync\(system-char\(\)-system-int32-system-int32\))|
asynchronously writes a subarray of characters to the string, followed by a
line terminator.  
(Унаследован от
[StringWriter](https://learn.microsoft.com/dotnet/api/system.io.stringwriter))  
##  __Поля
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
