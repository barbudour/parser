# NumberEventContainer<T>.NumberEventFuncAsync - метод
Выполняет функцию, переданную в конструкторе, и возвращает признак того, что
функция успешно выполнена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> NumberEventFuncAsync(
    	INumberContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NumberEventFuncAsync ( 
    	context As INumberContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    Task<bool>^ NumberEventFuncAsync(
    	INumberContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member NumberEventFuncAsync : 
            context : INumberContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером, передаваемый в параметр выполняемой функции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие с номером успешно выполнено; false, если при выполнении
действия возникли ошибки.
## __См. также
#### Ссылки
[NumberEventContainer<T> \-
](T_Tessa_Cards_Numbers_NumberEventContainer_1.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
