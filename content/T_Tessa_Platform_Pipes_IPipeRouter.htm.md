# IPipeRouter - интерфейс
Объект, выполняющий маршрутизацию сообщений, полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeRouter
VB __Копировать
     Public Interface IPipeRouter
C++ __Копировать
     public interface class IPipeRouter
F# __Копировать
     type IPipeRouter = interface end
##  __Методы
[TryGetHandlerAsync](M_Tessa_Platform_Pipes_IPipeRouter_TryGetHandlerAsync.htm)|
Возвращает объект, выполняющий обработку запроса в канале, или null, если
подходящий объект не зарегистрирован.  
---|---  
## __Методы расширения
[HandleAsync](M_Tessa_Platform_Pipes_PipesExtensions_HandleAsync.htm)|
Выполняет обработку сообщения по каналу и возвращает ответ на запрос,
отправленный по каналу. Не возвращает null, в случае невозможности обработки
выбрасывается исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
