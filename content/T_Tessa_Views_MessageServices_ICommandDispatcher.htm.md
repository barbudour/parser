# ICommandDispatcher - интерфейс
Описание интерфейса диспетчера команд
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICommandDispatcher
VB __Копировать
     Public Interface ICommandDispatcher
C++ __Копировать
     public interface class ICommandDispatcher
F# __Копировать
     type ICommandDispatcher = interface end
##  __Методы
[Deregister<TCommand>](M_Tessa_Views_MessageServices_ICommandDispatcher_Deregister__1.htm)|
Осуществляет удаление регистрации обработчика команды  
---|---  
[ExecuteAsync](M_Tessa_Views_MessageServices_ICommandDispatcher_ExecuteAsync.htm)|
Вызывает исполнение команды  
[IsRegistered<TCommand>](M_Tessa_Views_MessageServices_ICommandDispatcher_IsRegistered__1.htm)|
Осуществляет проверку наличия обработчика для команды  
[Register](M_Tessa_Views_MessageServices_ICommandDispatcher_Register.htm)|
Осуществляет регистрацию обработчика команды  
[TryGetHandler<TCommand>](M_Tessa_Views_MessageServices_ICommandDispatcher_TryGetHandler__1.htm)|
Осуществляет попытку получения обработчика для команды TCommand  
##  __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
