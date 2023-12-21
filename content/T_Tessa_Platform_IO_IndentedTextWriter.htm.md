# IndentedTextWriter - класс
##  __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class IndentedTextWriter : TextWriter
VB __Копировать
     Public Class IndentedTextWriter
    	Inherits TextWriter
C++ __Копировать
     public ref class IndentedTextWriter : public TextWriter
F# __Копировать
     type IndentedTextWriter = 
        class
            inherit TextWriter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarshalByRefObject](https://learn.microsoft.com/dotnet/api/system.marshalbyrefobject) __[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) __ IndentedTextWriter
##  __Конструкторы
[IndentedTextWriter(TextWriter)](M_Tessa_Platform_IO_IndentedTextWriter__ctor.htm)|
Инициализирует новый экземпляр класса IndentedTextWriter  
---|---  
[IndentedTextWriter(TextWriter,
String)](M_Tessa_Platform_IO_IndentedTextWriter__ctor_1.htm)| Инициализирует
новый экземпляр класса IndentedTextWriter  
##  __Свойства
[Encoding](P_Tessa_Platform_IO_IndentedTextWriter_Encoding.htm)|  
(Переопределяет
[TextWriter.Encoding](https://learn.microsoft.com/dotnet/api/system.io.textwriter.encoding#system-
io-textwriter-encoding))  
---|---  
[FormatProvider](https://learn.microsoft.com/dotnet/api/system.io.textwriter.formatprovider#system-
io-textwriter-formatprovider)| Gets an object that controls formatting.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[IndentLevel](P_Tessa_Platform_IO_IndentedTextWriter_IndentLevel.htm)|  
[IndentString](P_Tessa_Platform_IO_IndentedTextWriter_IndentString.htm)|  
[NewLine](P_Tessa_Platform_IO_IndentedTextWriter_NewLine.htm)|  
(Переопределяет
[TextWriter.NewLine](https://learn.microsoft.com/dotnet/api/system.io.textwriter.newline#system-
io-textwriter-newline))  
##  __Методы
[Close](M_Tessa_Platform_IO_IndentedTextWriter_Close.htm)|  
(Переопределяет
[TextWriter.Close()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.close#system-
io-textwriter-close))  
---|---  
[Dispose()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.dispose#system-
io-textwriter-dispose)| Releases all resources used by the
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
object.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Dispose(Boolean)](M_Tessa_Platform_IO_IndentedTextWriter_Dispose.htm)|
Освобождает неуправляемые ресурсы, используемые объектом IndentedTextWriter, а
при необходимости освобождает также управляемые ресурсы  
(Переопределяет
[TextWriter.Dispose(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.dispose#system-
io-textwriter-dispose\(system-boolean\)))  
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
[Flush](M_Tessa_Platform_IO_IndentedTextWriter_Flush.htm)|  
(Переопределяет
[TextWriter.Flush()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.flush#system-
io-textwriter-flush))  
[FlushAsync](https://learn.microsoft.com/dotnet/api/system.io.textwriter.flushasync#system-
io-textwriter-flushasync)| Asynchronously clears all buffers for the current
writer and causes any buffered data to be written to the underlying device.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
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
[Indent](M_Tessa_Platform_IO_IndentedTextWriter_Indent.htm)|  
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
[Unindent](M_Tessa_Platform_IO_IndentedTextWriter_Unindent.htm)|  
[Write(Boolean)](M_Tessa_Platform_IO_IndentedTextWriter_Write.htm)|  
(Переопределяет
[TextWriter.Write(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-boolean\)))  
[Write(Char)](M_Tessa_Platform_IO_IndentedTextWriter_Write_1.htm)|  
(Переопределяет
[TextWriter.Write(Char)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-char\)))  
[Write(Char[])](M_Tessa_Platform_IO_IndentedTextWriter_Write_2.htm)|  
(Переопределяет
[TextWriter.Write(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-char\(\)\)))  
[Write(Decimal)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-decimal\))| Writes the text representation of a
decimal value to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Double)](M_Tessa_Platform_IO_IndentedTextWriter_Write_4.htm)|  
(Переопределяет
[TextWriter.Write(Double)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-double\)))  
[Write(Int32)](M_Tessa_Platform_IO_IndentedTextWriter_Write_5.htm)|  
(Переопределяет
[TextWriter.Write(Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-int32\)))  
[Write(Int64)](M_Tessa_Platform_IO_IndentedTextWriter_Write_6.htm)|  
(Переопределяет
[TextWriter.Write(Int64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-int64\)))  
[Write(Object)](M_Tessa_Platform_IO_IndentedTextWriter_Write_7.htm)|  
(Переопределяет
[TextWriter.Write(Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-object\)))  
[Write(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-readonlyspan\(\(system-char\)\)\))| Writes a
character span to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[Write(Single)](M_Tessa_Platform_IO_IndentedTextWriter_Write_8.htm)|  
(Переопределяет
[TextWriter.Write(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-single\)))  
[Write(String)](M_Tessa_Platform_IO_IndentedTextWriter_Write_9.htm)|  
(Переопределяет
[TextWriter.Write(String)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string\)))  
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
[Write(String, Object)](M_Tessa_Platform_IO_IndentedTextWriter_Write_10.htm)|  
(Переопределяет [TextWriter.Write(String,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object\)))  
[Write(String,
Object[])](M_Tessa_Platform_IO_IndentedTextWriter_Write_12.htm)|  
(Переопределяет [TextWriter.Write(String,
Object[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object\(\)\)))  
[Write(Char[], Int32,
Int32)](M_Tessa_Platform_IO_IndentedTextWriter_Write_3.htm)|  
(Переопределяет [TextWriter.Write(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-char\(\)-system-int32-system-int32\)))  
[Write(String, Object,
Object)](M_Tessa_Platform_IO_IndentedTextWriter_Write_11.htm)|  
(Переопределяет [TextWriter.Write(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.write#system-
io-textwriter-write\(system-string-system-object-system-object\)))  
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
[WriteAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-char\))| Writes a character to the text
stream asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-char\(\)\))| Writes a character array to the
text stream asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-string\))| Writes a string to the text stream
asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-readonlymemory\(\(system-char\)\)-system-
threading-cancellationtoken\))| Asynchronously writes a character memory
region to the text stream.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeasync#system-
io-textwriter-writeasync\(system-char\(\)-system-int32-system-int32\))| Writes
a subarray of characters to the text stream asynchronously.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteIndent](M_Tessa_Platform_IO_IndentedTextWriter_WriteIndent.htm)|  
[WriteLine()](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine.htm)|  
(Переопределяет
[TextWriter.WriteLine()](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline))  
[WriteLine(Boolean)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_1.htm)|  
(Переопределяет
[TextWriter.WriteLine(Boolean)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-boolean\)))  
[WriteLine(Char)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_2.htm)|  
(Переопределяет
[TextWriter.WriteLine(Char)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\)))  
[WriteLine(Char[])](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_3.htm)|  
(Переопределяет
[TextWriter.WriteLine(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\(\)\)))  
[WriteLine(Decimal)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-decimal\))| Writes the text representation of
a decimal value to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Double)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_5.htm)|  
(Переопределяет
[TextWriter.WriteLine(Double)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-double\)))  
[WriteLine(Int32)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_6.htm)|  
(Переопределяет
[TextWriter.WriteLine(Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-int32\)))  
[WriteLine(Int64)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_7.htm)|  
(Переопределяет
[TextWriter.WriteLine(Int64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-int64\)))  
[WriteLine(Object)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_8.htm)|  
(Переопределяет
[TextWriter.WriteLine(Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-object\)))  
[WriteLine(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-readonlyspan\(\(system-char\)\)\))| Writes the
text representation of a character span to the text stream, followed by a line
terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(Single)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_9.htm)|  
(Переопределяет
[TextWriter.WriteLine(Single)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-single\)))  
[WriteLine(String)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_10.htm)|  
(Переопределяет
[TextWriter.WriteLine(String)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string\)))  
[WriteLine(UInt32)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_14.htm)|  
(Переопределяет
[TextWriter.WriteLine(UInt32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-uint32\)))  
[WriteLine(UInt64)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-uint64\))| Writes the text representation of
an 8-byte unsigned integer to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLine(String,
Object)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_11.htm)|  
(Переопределяет [TextWriter.WriteLine(String,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object\)))  
[WriteLine(String,
Object[])](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_13.htm)|  
(Переопределяет [TextWriter.WriteLine(String,
Object[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object\(\)\)))  
[WriteLine(Char[], Int32,
Int32)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_4.htm)|  
(Переопределяет [TextWriter.WriteLine(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-char\(\)-system-int32-system-int32\)))  
[WriteLine(String, Object,
Object)](M_Tessa_Platform_IO_IndentedTextWriter_WriteLine_12.htm)|  
(Переопределяет [TextWriter.WriteLine(String, Object,
Object)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writeline#system-
io-textwriter-writeline\(system-string-system-object-system-object\)))  
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
[WriteLineAsync(Char)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-char\))| Asynchronously writes a
character to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(Char[])](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-char\(\)\))| Asynchronously writes an
array of characters to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(String)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-string\))| Asynchronously writes a string
to the text stream, followed by a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(ReadOnlyMemory<Char>,
CancellationToken)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-readonlymemory\(\(system-char\)\)-system-
threading-cancellationtoken\))| Asynchronously writes the text representation
of a character memory region to the text stream, followed by a line
terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
[WriteLineAsync(Char[], Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.io.textwriter.writelineasync#system-
io-textwriter-writelineasync\(system-char\(\)-system-int32-system-int32\))|
Asynchronously writes a subarray of characters to the text stream, followed by
a line terminator.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
##  __Поля
[CoreNewLine](https://learn.microsoft.com/dotnet/api/system.io.textwriter.corenewline)|
Stores the newline characters used for this TextWriter.  
(Унаследован от
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter))  
---|---  
[DefaultIndentString](F_Tessa_Platform_IO_IndentedTextWriter_DefaultIndentString.htm)|  
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
