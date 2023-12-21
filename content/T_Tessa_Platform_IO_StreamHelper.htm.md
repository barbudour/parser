# StreamHelper - класс
Вспомогательные методы и константы для организации работы с потоками ввода /
вывода.
## __Definition
 **Пространство имён:** [Tessa.Platform.IO](N_Tessa_Platform_IO.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class StreamHelper
VB __Копировать
     Public NotInheritable Class StreamHelper
C++ __Копировать
     public ref class StreamHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type StreamHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StreamHelper
##  __Методы
[AcquireMemoryStream](M_Tessa_Platform_IO_StreamHelper_AcquireMemoryStream.htm)|
Возвращает объект
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream),
который можно повторно использовать в текущем потоке. Вызов метода
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) может вызвать возврат объекта в кэш, который повторно
используется при вызове этого метода из того же потока.  
---|---  
[CreateStream](M_Tessa_Platform_IO_StreamHelper_CreateStream.htm)|  Создаёт
поток в памяти, над которым выполняется заданный метод. Если при выполнении
метода происходит исключение, то поток корректно закрывается.  
[CreateStreamAsync](M_Tessa_Platform_IO_StreamHelper_CreateStreamAsync.htm)|
Создаёт поток в памяти, над которым выполняется заданный метод. Если при
выполнении метода происходит исключение, то поток корректно закрывается.  
[CreateUtf8BinaryWriter](M_Tessa_Platform_IO_StreamHelper_CreateUtf8BinaryWriter.htm)|
Создаёт объект
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
с кодировкой UTF-8. Поток остаётся открытым после закрытия
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter).  
## __Поля
[MaxCachedSize](F_Tessa_Platform_IO_StreamHelper_MaxCachedSize.htm)|
Максимальный размер кэшируемого потока
[MemoryStream](https://learn.microsoft.com/dotnet/api/system.io.memorystream).
Если не ограничивать размер, то в кэше могут оказаться очень большие блоки
памяти, которые не используются и не достижимы для сборщика мусора.  
---|---  
[SeekBufferSize](F_Tessa_Platform_IO_StreamHelper_SeekBufferSize.htm)|  Размер
буфера в байтах, который может использоваться для операций поиска в потоках
ввода / вывода.  
[WriteBufferSize](F_Tessa_Platform_IO_StreamHelper_WriteBufferSize.htm)|
Размер буфера в байтах, который может использоваться для операций записи в
потоки ввода / вывода.  
## __См. также
#### Ссылки
[Tessa.Platform.IO - пространство имён](N_Tessa_Platform_IO.htm)
