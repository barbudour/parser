# INumberBuilder.GetAsync<T> \- метод
Возвращает типизированные данные для контекста события, происходящего с
номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<T> GetAsync<T>(
    	INumberContext context,
    	Object parameter = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAsync(Of T) ( 
    	context As INumberContext,
    	Optional parameter As Object = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     generic<typename T>
    ValueTask<T> GetAsync(
    	INumberContext^ context, 
    	Object^ parameter = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAsync : 
            context : INumberContext * 
            ?parameter : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parameter = defaultArg parameter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
parameter [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
    Необязательный параметр, определяющий запрашиваемые данные.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
    Тип запрашиваемых данных.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<T>  
Запрошенные типизированные данные для контекста события, происходящего с
номером, или null, если получить такие данные не удалось.
## __См. также
#### Ссылки
[INumberBuilder - ](T_Tessa_Cards_Numbers_INumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
