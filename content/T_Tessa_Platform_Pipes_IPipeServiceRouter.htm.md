# IPipeServiceRouter - интерфейс
Объект, выполняющий маршрутизацию сообщений, полученных по каналу.
Предоставляет метод регистрации обработчика по типу сервиса.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeServiceRouter : IPipeRouter
VB __Копировать
     Public Interface IPipeServiceRouter
    	Inherits IPipeRouter
C++ __Копировать
     public interface class IPipeServiceRouter : IPipeRouter
F# __Копировать
     type IPipeServiceRouter = 
        interface
            interface IPipeRouter
        end
Implements
    [IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm)
##  __Методы
[Register](M_Tessa_Platform_Pipes_IPipeServiceRouter_Register.htm)|  Выполняет
регистрацию обработчика по типу сервиса.  
---|---  
[RemoveRegistration](M_Tessa_Platform_Pipes_IPipeServiceRouter_RemoveRegistration.htm)|
Удаляет регистрацию обработчика для заданного сервиса.  
[TryGetHandlerAsync](M_Tessa_Platform_Pipes_IPipeRouter_TryGetHandlerAsync.htm)|
Возвращает объект, выполняющий обработку запроса в канале, или null, если
подходящий объект не зарегистрирован.  
(Унаследован от [IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm))  
##  __Методы расширения
[HandleAsync](M_Tessa_Platform_Pipes_PipesExtensions_HandleAsync.htm)|
Выполняет обработку сообщения по каналу и возвращает ответ на запрос,
отправленный по каналу. Не возвращает null, в случае невозможности обработки
выбрасывается исключение
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
[Register](M_Tessa_Platform_Pipes_PipesExtensions_Register.htm)|  Выполняет
регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_2.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_3.htm)|
Выполняет регистрацию обработчика по типу сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
[RemoveRegistration<T>](M_Tessa_Platform_Pipes_PipesExtensions_RemoveRegistration__1.htm)|
Удаляет регистрацию обработчика для заданного сервиса.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
