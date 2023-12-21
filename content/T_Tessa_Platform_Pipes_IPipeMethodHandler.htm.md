# IPipeMethodHandler - интерфейс
Объект, выполняющий обработку сообщений, полученных по каналу. Предоставляет
метод регистрации обработчика по имени метода.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeMethodHandler : IPipeHandler
VB __Копировать
     Public Interface IPipeMethodHandler
    	Inherits IPipeHandler
C++ __Копировать
     public interface class IPipeMethodHandler : IPipeHandler
F# __Копировать
     type IPipeMethodHandler = 
        interface
            interface IPipeHandler
        end
Implements
    [IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm)
##  __Методы
[Register](M_Tessa_Platform_Pipes_IPipeMethodHandler_Register.htm)|  Выполняет
регистрацию метода обработки по имени.  
---|---  
[TryHandleAsync](M_Tessa_Platform_Pipes_IPipeHandler_TryHandleAsync.htm)|
Выполняет обработку сообщения, полученного по каналу. Возвращает null, если
обработка не выполнена, например, если подходящий метод не был
зарегистрирован.  
(Унаследован от [IPipeHandler](T_Tessa_Platform_Pipes_IPipeHandler.htm))  
##  __Методы расширения
[Register<T>](M_Tessa_Platform_Pipes_PipesExtensions_Register__1_1.htm)|
Выполняет регистрацию метода обработки по имени, в который передаётся
экземпляр объекта T, время жизни которого контролируется объектом
instanceResolver. Используйте объект
[PipeContextualInstanceResolver](T_Tessa_Platform_Pipes_PipeContextualInstanceResolver.htm)
(container.[GetContextualInstanceResolver(IUnityContainer)](M_Tessa_Platform_Pipes_PipesExtensions_GetContextualInstanceResolver.htm)),
чтобы время жизни экземпляра объекта, передаваемого в метод обработки
сообщения handleAsync, определялось временем жизни соединения сервера с
клиентом.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
