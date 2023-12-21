# IQueryDispatcher - интерфейс
Описание интерфейса диспетчера запросов
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IQueryDispatcher
VB __Копировать
     Public Interface IQueryDispatcher
C++ __Копировать
     public interface class IQueryDispatcher
F# __Копировать
     type IQueryDispatcher = interface end
##  __Методы
[Execute<TResult>](M_Tessa_Views_MessageServices_IQueryDispatcher_Execute__1.htm)|
Осуществляет попытку выполнения запроса  
---|---  
[IsRegistered<TQuery>](M_Tessa_Views_MessageServices_IQueryDispatcher_IsRegistered__1.htm)|
Осуществляет проверку наличия обработчика для запросаа  
[Register](M_Tessa_Views_MessageServices_IQueryDispatcher_Register.htm)|
Осуществляет регистрацию обработчика запроса  
[TryGetHandler<TQuery,
TResult>](M_Tessa_Views_MessageServices_IQueryDispatcher_TryGetHandler__2.htm)|
Осуществляет попытку получения обработчика для запроса TQuery с результатом
выполнения TResult  
[UnRegister<TQuery>](M_Tessa_Views_MessageServices_IQueryDispatcher_UnRegister__1.htm)|
Осуществляет удаление регистрации обработчика запроса  
## __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
