# IPipeSerializer - интерфейс
Объект, выполняющий сериализацию и десериализацию текстовых сообщений по
каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeSerializer
VB __Копировать
     Public Interface IPipeSerializer
C++ __Копировать
     public interface class IPipeSerializer
F# __Копировать
     type IPipeSerializer = interface end
##  __Методы
[ReadBytesAsync](M_Tessa_Platform_Pipes_IPipeSerializer_ReadBytesAsync.htm)|
Выполняет чтение сообщения как массива байт, переданного по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
Если возвращённое значение равно null или пустому массиву, то считается, что
канал был закрыт.  
---|---  
[ReadStringAsync](M_Tessa_Platform_Pipes_IPipeSerializer_ReadStringAsync.htm)|
Выполняет чтение сообщения как строки текста, переданной по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).
Если возвращённое значение равно null или пустой строке, то считается, что
канал был закрыт.  
[WriteBytesAsync](M_Tessa_Platform_Pipes_IPipeSerializer_WriteBytesAsync.htm)|
Отправляет массив байт как сообщение по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
[WriteStringAsync](M_Tessa_Platform_Pipes_IPipeSerializer_WriteStringAsync.htm)|
Отправляет строку текста как сообщение по заданному каналу
[PipeStream](https://learn.microsoft.com/dotnet/api/system.io.pipes.pipestream).  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
