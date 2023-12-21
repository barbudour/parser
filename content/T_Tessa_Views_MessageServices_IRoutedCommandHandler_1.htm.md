# IRoutedCommandHandler<TCommand> \- интерфейс
Описание интерфейса типизированного обработчика команды
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRoutedCommandHandler<in TCommand> : IRoutedCommandHandler
    where TCommand : IRoutedCommand
VB __Копировать
     Public Interface IRoutedCommandHandler(Of In TCommand As IRoutedCommand)
    	Inherits IRoutedCommandHandler
C++ __Копировать
    generic<typename TCommand>
    where TCommand : IRoutedCommand
    public interface class IRoutedCommandHandler : IRoutedCommandHandler
F# __Копировать
     type IRoutedCommandHandler<'TCommand when 'TCommand : IRoutedCommand> = 
        interface
            interface IRoutedCommandHandler
        end
Implements
    [IRoutedCommandHandler](T_Tessa_Views_MessageServices_IRoutedCommandHandler.htm)
#### Параметры типа
TCommand
     Тип команды 
## __Методы
[ExecuteAsync](M_Tessa_Views_MessageServices_IRoutedCommandHandler_1_ExecuteAsync.htm)|
Осуществляет исполнение команды command  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
