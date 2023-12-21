# IRoutedQueryHandler<TQuery, TResult> \- интерфейс
Описание интерфейса обработчика перенаправляемого запроса
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRoutedQueryHandler<in TQuery, out TResult> : IRoutedQueryHandler
    where TQuery : Object, IRoutedQuery<TResult>
VB __Копировать
     Public Interface IRoutedQueryHandler(Of In TQuery As {Object, IRoutedQuery(Of TResult)}, Out TResult)
    	Inherits IRoutedQueryHandler
C++ __Копировать
    generic<typename TQuery, typename TResult>
    where TQuery : Object, IRoutedQuery<TResult>
    public interface class IRoutedQueryHandler : IRoutedQueryHandler
F# __Копировать
     type IRoutedQueryHandler<'TQuery, 'TResult when 'TQuery : Object and IRoutedQuery<'TResult>> = 
        interface
            interface IRoutedQueryHandler
        end
Implements
    [IRoutedQueryHandler](T_Tessa_Views_MessageServices_IRoutedQueryHandler.htm)
#### Параметры типа
TQuery
     Тип запроса 
TResult
     Тип результат выполнения запроса 
## __Методы
[Handle](M_Tessa_Views_MessageServices_IRoutedQueryHandler_2_Handle.htm)|
Осуществляет выполнение запроса query  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
