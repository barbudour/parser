# IOExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.IO.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class IOExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class IOExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class IOExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type IOExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ IOExtensions
##  __Методы
[AsMemoryStreamAsync](M_Tessa_Platform_IO_IOExtensions_AsMemoryStreamAsync.htm)|
Возвращает поток stream, преобразованный к типу
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream).
Если его тип отличается от
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
то его содержимое будет скопировано в созданный объект
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
после чего исходный stream будет освобождён, но только если параметр
disposeNonMemoryStream равен true.  
---|---  
[CalculateStreamLengthAsync](M_Tessa_Platform_IO_IOExtensions_CalculateStreamLengthAsync.htm)|
Вычисляет длину потока посредством его чтения, но отбрасывая сам контент.  
[DrainAsync](M_Tessa_Platform_IO_IOExtensions_DrainAsync.htm)|  Выполняет
асинхронное чтение всех данных, содержащихся для заданного объекта
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader), но
не использует эти данные, и возвращает асинхронную задачу по окончанию чтения.  
[DrainOutputAndErrorAsync](M_Tessa_Platform_IO_IOExtensions_DrainOutputAndErrorAsync.htm)|
Выполняет чтение стандартного вывода
[StandardOutput](https://learn.microsoft.com/dotnet/api/system.diagnostics.process.standardoutput#system-
diagnostics-process-standardoutput) и ошибок
[StandardError](https://learn.microsoft.com/dotnet/api/system.diagnostics.process.standarderror#system-
diagnostics-process-standarderror) процесса process до их завершения (закрытия
дескрипторов, что обычно происходит перед завершением процесса). Не возвращает
прочитанные значения.
Используйте, чтобы не происходило переполнение буфера при выполнении процесса,
вывод которого перенаправлен. Чтение гарантированно выполняется в другом
потоке на пуле.  
[ReadAllBytes](M_Tessa_Platform_IO_IOExtensions_ReadAllBytes.htm)|  Выполняет
синхронное чтение всех данных потока в виде одного массива байт. Чтение
выполняется до того момента, как поток перестанет возвращать данные, при этом
метод не использует свойство
[Length](https://learn.microsoft.com/dotnet/api/system.io.stream.length#system-
io-stream-length) для определения количества считываемых данных.  
[ReadAllBytesAsync](M_Tessa_Platform_IO_IOExtensions_ReadAllBytesAsync.htm)|
Выполняет асинхронное чтение всех данных потока в виде одного массива байт.
Чтение выполняется до того момента, как поток перестанет возвращать данные,
при этом метод не использует свойство
[Length](https://learn.microsoft.com/dotnet/api/system.io.stream.length#system-
io-stream-length) для определения количества считываемых данных.  
[ReadByteAsync](M_Tessa_Platform_IO_IOExtensions_ReadByteAsync.htm)|
Выполняет асинхронное чтение целочисленного значения Byte из потока.  
[ReadBytes](M_Tessa_Platform_IO_IOExtensions_ReadBytes.htm)|  Выполняет чтение
данных из потока stream и записывает их в возвращаемый массив байт, который
имеет максимальный размер length байт.  
[ReadBytesAsync](M_Tessa_Platform_IO_IOExtensions_ReadBytesAsync.htm)|
Выполняет чтение данных из потока stream и записывает их в возвращаемый массив
байт, который имеет максимальный размер length байт.  
[ReadBytesExact](M_Tessa_Platform_IO_IOExtensions_ReadBytesExact.htm)|
Выполняет чтение данных из потока stream и записывает их в возвращаемый массив
байт, который имеет заданный размер length байт.  
[ReadBytesExactAsync](M_Tessa_Platform_IO_IOExtensions_ReadBytesExactAsync.htm)|
Выполняет асинхронное чтение данных из потока stream и записывает их в
возвращаемый массив байт, который имеет заданный размер length байт.  
[ReadDateTime](M_Tessa_Platform_IO_IOExtensions_ReadDateTime.htm)|  Читает из
байтового потока
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime).  
[ReadExact](M_Tessa_Platform_IO_IOExtensions_ReadExact.htm)|  Выполняет чтение
указанного количества байт из потока в буфер. Возвращает количество
действительно прочитанных байт, которое может быть меньше указанного
количества только в том случае, если поток завершился.  
[ReadExactAsync](M_Tessa_Platform_IO_IOExtensions_ReadExactAsync.htm)|
Выполняет асинхронное чтение указанного количества байт из потока в буфер.
Возвращает количество действительно прочитанных байт, которое может быть
меньше указанного количества только в том случае, если поток завершился.  
[ReadGuid(BinaryReader)](M_Tessa_Platform_IO_IOExtensions_ReadGuid.htm)|
Читает из байтового потока
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[ReadGuid(Stream)](M_Tessa_Platform_IO_IOExtensions_ReadGuid_1.htm)|
Выполняет чтение значения Guid из потока.  
[ReadGuidAsync](M_Tessa_Platform_IO_IOExtensions_ReadGuidAsync.htm)|
Выполняет асинхронное чтение значения Guid из потока.  
[ReadInt16Async](M_Tessa_Platform_IO_IOExtensions_ReadInt16Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int16 из потока.  
[ReadInt32](M_Tessa_Platform_IO_IOExtensions_ReadInt32.htm)|  Выполняет чтение
целочисленного значения Int32 из потока.  
[ReadInt32Async](M_Tessa_Platform_IO_IOExtensions_ReadInt32Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int32 из потока.  
[ReadInt64](M_Tessa_Platform_IO_IOExtensions_ReadInt64.htm)|  Выполняет чтение
целочисленного значения Int32 из потока.  
[ReadInt64Async](M_Tessa_Platform_IO_IOExtensions_ReadInt64Async.htm)|
Выполняет асинхронное чтение целочисленного значения Int32 из потока.  
[ReadNullableBoolean](M_Tessa_Platform_IO_IOExtensions_ReadNullableBoolean.htm)|
Читает из байтового потока значение bool, которое может быть равно null.  
[ReadNullableBytes](M_Tessa_Platform_IO_IOExtensions_ReadNullableBytes.htm)|
Читает из байтового потока массив байт, который может быть равен null.  
[ReadNullableDateTime](M_Tessa_Platform_IO_IOExtensions_ReadNullableDateTime.htm)|
Читает из байтового потока
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime), который
может быть равен null.  
[ReadNullableDouble](M_Tessa_Platform_IO_IOExtensions_ReadNullableDouble.htm)|
Читает из байтового потока вещественное число double, которое может быть равно
null.  
[ReadNullableGuid](M_Tessa_Platform_IO_IOExtensions_ReadNullableGuid.htm)|
Читает из байтового потока
[Guid](https://learn.microsoft.com/dotnet/api/system.guid), который может быть
равен null.  
[ReadNullableInt32](M_Tessa_Platform_IO_IOExtensions_ReadNullableInt32.htm)|
Читает из байтового потока целое число int, которое может быть равно null.  
[ReadNullableInt64](M_Tessa_Platform_IO_IOExtensions_ReadNullableInt64.htm)|
Читает из байтового потока целое число long, которое может быть равно null.  
[ReadNullableString](M_Tessa_Platform_IO_IOExtensions_ReadNullableString.htm)|
Читает из байтового потока строку, которая может быть равна null.  
[ReadOutputAndErrorToEndAsync](M_Tessa_Platform_IO_IOExtensions_ReadOutputAndErrorToEndAsync.htm)|
Выполняет чтение стандартного вывода
[StandardOutput](https://learn.microsoft.com/dotnet/api/system.diagnostics.process.standardoutput#system-
diagnostics-process-standardoutput) и ошибок
[StandardError](https://learn.microsoft.com/dotnet/api/system.diagnostics.process.standarderror#system-
diagnostics-process-standarderror) процесса process до их завершения (закрытия
дескрипторов, что обычно происходит перед завершением процесса). Возвращает
прочитанные значения.
Используйте, чтобы не происходило переполнение буфера при выполнении процесса,
вывод которого перенаправлен. Чтение гарантированно выполняется в другом
потоке на пуле.  
[ReadString](M_Tessa_Platform_IO_IOExtensions_ReadString.htm)|  Выполняет
чтение значения string из потока.  
[ReadStringAsync](M_Tessa_Platform_IO_IOExtensions_ReadStringAsync.htm)|
Выполняет асинхронное чтение значения string из потока.  
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
[TryReadPrimitiveType](M_Tessa_Platform_IO_IOExtensions_TryReadPrimitiveType.htm)|
Выполняет чтение объекта примитивного типа из потока. Возвращает значение
объекта или признак того, что тип объекта type является примитивным, и объект
был прочитан из потока.  
[TryReadPrimitiveTypeAsync](M_Tessa_Platform_IO_IOExtensions_TryReadPrimitiveTypeAsync.htm)|
Выполняет асинхронное чтение объекта примитивного типа из потока. Возвращает
значение объекта или признак того, что тип объекта type является примитивным,
и объект был прочитан из потока.  
[TryWritePrimitiveType](M_Tessa_Platform_IO_IOExtensions_TryWritePrimitiveType.htm)|
Выполняет запись объекта примитивного типа в поток. Возвращает признак того,
что тип объекта obj является примитивным, и объект был записан в поток.  
[TryWritePrimitiveTypeAsync](M_Tessa_Platform_IO_IOExtensions_TryWritePrimitiveTypeAsync.htm)|
Выполняет асинхронную запись объекта примитивного типа в поток. Возвращает
признак того, что тип объекта obj является примитивным, и объект был записан в
поток.  
[Write(BinaryWriter, DateTime)](M_Tessa_Platform_IO_IOExtensions_Write.htm)|
Записывает в байтовый поток
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime).  
[Write(BinaryWriter, Guid)](M_Tessa_Platform_IO_IOExtensions_Write_1.htm)|
Записывает в байтовый поток
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[Write(Stream, Byte)](M_Tessa_Platform_IO_IOExtensions_Write_2.htm)|
Выполняет запись целочисленного значения Byte в поток.  
[Write(Stream, Guid)](M_Tessa_Platform_IO_IOExtensions_Write_3.htm)|
Выполняет запись значения Guid в поток.  
[Write(Stream, Int16)](M_Tessa_Platform_IO_IOExtensions_Write_4.htm)|
Выполняет запись целочисленного значения Int16 в поток.  
[Write(Stream, Int32)](M_Tessa_Platform_IO_IOExtensions_Write_5.htm)|
Выполняет запись целочисленного значения Int32 в поток.  
[Write(Stream, Int64)](M_Tessa_Platform_IO_IOExtensions_Write_6.htm)|
Выполняет запись целочисленного значения Int32 в поток.  
[Write(Stream, String,
Encoding)](M_Tessa_Platform_IO_IOExtensions_Write_7.htm)|  Выполняет запись
значения string в поток.  
[WriteAsync(Stream, Byte,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync.htm)|
Выполняет асинхронную запись целочисленного значения Byte в поток.  
[WriteAsync(Stream, Guid,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync_1.htm)|
Выполняет запись значения Guid в поток.  
[WriteAsync(Stream, Int16,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync_2.htm)|
Выполняет асинхронную запись целочисленного значения Int16 в поток.  
[WriteAsync(Stream, Int32,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync_3.htm)|
Выполняет асинхронную запись целочисленного значения Int32 в поток.  
[WriteAsync(Stream, Int64,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync_4.htm)|
Выполняет асинхронную запись целочисленного значения Int32 в поток.  
[WriteAsync(Stream, String, Encoding,
CancellationToken)](M_Tessa_Platform_IO_IOExtensions_WriteAsync_5.htm)|
Выполняет асинхронную запись значения string в поток.  
[WriteNullable(BinaryWriter,
Byte[])](M_Tessa_Platform_IO_IOExtensions_WriteNullable.htm)|  Записывает в
байтовый поток массив байт, который может быть равен null.  
[WriteNullable(BinaryWriter,
Nullable<Boolean>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_1.htm)|
Записывает в байтовый поток значение bool, которое может быть равно null.  
[WriteNullable(BinaryWriter,
Nullable<DateTime>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_2.htm)|
Записывает в байтовый поток
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime), который
может быть равен null.  
[WriteNullable(BinaryWriter,
Nullable<Double>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_3.htm)|
Записывает в байтовый поток вещественное число double, которое может быть
равно null.  
[WriteNullable(BinaryWriter,
Nullable<Guid>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_4.htm)|
Записывает в байтовый поток
[Guid](https://learn.microsoft.com/dotnet/api/system.guid), который может быть
равен null.  
[WriteNullable(BinaryWriter,
Nullable<Int32>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_5.htm)|
Записывает в байтовый поток целое число int, которое может быть равно null.  
[WriteNullable(BinaryWriter,
Nullable<Int64>)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_6.htm)|
Записывает в байтовый поток целое число long, которое может быть равно null.  
[WriteNullable(BinaryWriter,
String)](M_Tessa_Platform_IO_IOExtensions_WriteNullable_7.htm)|  Записывает в
байтовый поток строку, которая может быть равна null.  
[WriteStream](M_Tessa_Platform_IO_IOExtensions_WriteStream.htm)|  Записывает
все данные из потока source в поток target.  
[WriteStreamAsync](M_Tessa_Platform_IO_IOExtensions_WriteStreamAsync.htm)|
Записывает все данные из потока source в поток target.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
