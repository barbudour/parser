# IPipeHandler - интерфейс
Объект, выполняющий обработку сообщений, полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeHandler
VB __Копировать
     Public Interface IPipeHandler
C++ __Копировать
     public interface class IPipeHandler
F# __Копировать
     type IPipeHandler = interface end
##  __Методы
[TryHandleAsync](M_Tessa_Platform_Pipes_IPipeHandler_TryHandleAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
